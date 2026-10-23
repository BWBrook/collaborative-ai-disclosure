"""Local consistency and policy-age tests. No network or Git required."""
from __future__ import annotations

import contextlib
import datetime as dt
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from check_repo import check_links, check_repository, valid_date, validate_records
from policy_age import assess, main as age_main
from repo_utils import collect_public_files, excluded, load_json, safe_relative


class Fixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / 'project'
        self.root.mkdir()
        self.write('README.md', '# Test project\n\n[Detail](docs/detail.md)\n')
        self.write('docs/detail.md', '# Detail\n')
        self.source = {
            'id': 'SRC-TEST', 'url': 'https://example.org/policy',
            'access_status': 'inspected', 'scope': 'Test fixture only',
            'last_attempted': '2026-09-08', 'last_inspected': '2026-09-08',
            'checked_by': 'test fixture', 'human_review': 'pending',
        }
        self.policy = {
            'id': 'POL-TEST', 'source_id': 'SRC-TEST', 'url': self.source['url'],
            'status': 'inspected', 'scope': 'Test fixture only',
            'last_attempted': '2026-09-08', 'last_inspected': '2026-09-08',
            'checked_by': 'test fixture', 'human_review': 'pending',
        }
        self.config = {
            'schema_version': 1, 'slug': 'test-project', 'version': 'draft',
            'public_roots': ['README.md', 'repo_config.json', 'docs', 'references', 'policies'],
            'required_files': ['README.md', 'docs/detail.md', 'references/source-register.json', 'policies/registry.json'],
        }
        self.write_json('repo_config.json', self.config)
        self.save_records()

    def write(self, path, text):
        dest = self.root / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding='utf-8', newline='\n')

    def write_json(self, path, data):
        self.write(path, json.dumps(data, ensure_ascii=False, indent=2) + '\n')

    def save_records(self):
        self.write_json('references/source-register.json', {'schema_version': 1, 'sources': [self.source]})
        self.write_json('policies/registry.json', {'schema_version': 1, 'review_interval_days': 90, 'policies': [self.policy]})

    def record_errors(self):
        return validate_records({'schema_version': 1, 'policies': [self.policy]}, 'policies', 'status')


class StructureTests(Fixture):
    def test_valid_fixture(self):
        errors, count = check_repository(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(count, 5)

    def test_missing_required_file(self):
        (self.root / 'docs/detail.md').unlink()
        self.assertTrue(any('Required public file missing' in x for x in check_repository(self.root)[0]))

    def test_missing_link(self):
        self.assertTrue(check_links(self.root / 'README.md', self.root, '[x](missing.md)'))

    def test_outside_link(self):
        self.assertTrue(check_links(self.root / 'README.md', self.root, '[x](../outside.md)'))

    def test_external_and_anchor_links_ignored(self):
        self.assertEqual(check_links(self.root / 'README.md', self.root, '[x](https://example.org/a) [y](#somewhere)'), [])

    def test_code_fence_links_ignored(self):
        text = '```markdown\n[x](not-a-real-file.md)\n```\n'
        self.assertEqual(check_links(self.root / 'README.md', self.root, text), [])

    def test_relative_link_from_subdirectory(self):
        self.assertEqual(check_links(self.root / 'docs/detail.md', self.root, '[home](../README.md)'), [])

    def test_crlf_rejected(self):
        (self.root / 'README.md').write_bytes(b'# Test\r\n')
        self.assertTrue(any('CR/CRLF' in x for x in check_repository(self.root)[0]))

    def test_missing_final_newline(self):
        (self.root / 'README.md').write_bytes(b'# Test')
        self.assertTrue(any('final newline' in x for x in check_repository(self.root)[0]))

    def test_non_utf8_rejected(self):
        (self.root / 'README.md').write_bytes(b'\xff\n')
        self.assertTrue(any('UTF-8' in x for x in check_repository(self.root)[0]))

    def test_nul_rejected(self):
        (self.root / 'docs/detail.md').write_bytes(b'\x00\n')
        self.assertTrue(any('NUL byte' in x for x in check_repository(self.root)[0]))

    def test_bad_json_has_readable_error(self):
        self.write('policies/registry.json', '{oops}\n')
        self.assertTrue(check_repository(self.root)[0])

    def test_json_array_not_object(self):
        self.write('docs/array.json', '[]\n')
        with self.assertRaises(ValueError):
            load_json(self.root / 'docs/array.json')

    def test_unsafe_paths(self):
        for path in ['../outside', '/absolute', 'docs\\windows', 'a\nb', 'C:/path']:
            self.assertFalse(safe_relative(path), path)
        self.assertTrue(safe_relative('docs/a-file.md'))


class RegistryTests(Fixture):
    def test_wrong_status_types_report_errors(self):
        self.policy.update(status=[], human_review=[])
        self.assertTrue(self.record_errors())

    def test_malformed_url_reports_error(self):
        self.policy['url'] = 'https://['
        self.assertTrue(self.record_errors())

    def test_null_record_list_reports_error(self):
        self.write_json('policies/registry.json', {'schema_version': 1, 'policies': None})
        self.assertTrue(check_repository(self.root)[0])

    def test_invalid_source_id_type_reports_error(self):
        self.policy['source_id'] = []
        self.save_records()
        self.assertTrue(check_repository(self.root)[0])

    def test_invalid_calendar_date(self):
        self.assertFalse(valid_date('2026-02-30'))
        self.assertFalse(valid_date('20260908'))
        self.assertFalse(valid_date(None))
        self.assertTrue(valid_date('2026-09-08'))

    def test_duplicate_ids(self):
        data = {'schema_version': 1, 'policies': [self.policy, self.policy.copy()]}
        self.assertTrue(any('duplicate' in x for x in validate_records(data, 'policies', 'status')))

    def test_invalid_status(self):
        self.policy['status'] = 'probably-fine'
        self.assertTrue(self.record_errors())

    def test_inspected_requires_date(self):
        self.policy['last_inspected'] = None
        self.assertTrue(self.record_errors())

    def test_unavailable_honest_null_date(self):
        self.policy.update(status='unavailable', last_inspected=None)
        self.assertEqual(self.record_errors(), [])

    def test_inspection_after_attempt_invalid(self):
        self.policy['last_inspected'] = '2026-09-09'
        self.assertTrue(self.record_errors())

    def test_reviewed_requires_reviewer(self):
        self.policy['human_review'] = 'reviewed'
        self.assertTrue(self.record_errors())

    def test_reviewed_with_metadata_allowed(self):
        self.policy.update(human_review='reviewed', human_reviewer='Test reviewer', human_reviewed_on='2026-09-08')
        self.assertEqual(self.record_errors(), [])

    def test_unknown_source_id(self):
        self.policy['source_id'] = 'SRC-MISSING'
        self.save_records()
        self.assertTrue(any('unknown source_id' in x for x in check_repository(self.root)[0]))

    def test_source_url_mismatch(self):
        self.policy['url'] = 'https://example.org/another'
        self.save_records()
        self.assertTrue(any('URL differs' in x for x in check_repository(self.root)[0]))


class AgeTests(Fixture):
    def test_recent_but_unreviewed(self):
        age, reasons = assess(self.policy, dt.date(2026, 9, 8), 90)
        self.assertEqual(age, 0)
        self.assertIn('human review pending', reasons)

    def test_age_threshold_inclusive(self):
        self.policy.update(human_review='reviewed')
        _, reasons = assess(self.policy, dt.date(2026, 9, 8) + dt.timedelta(days=90), 90)
        self.assertTrue(any('90 days old' in x for x in reasons))

    def test_future_dates_flagged(self):
        _, reasons = assess(self.policy, dt.date(2026, 9, 7), 90)
        self.assertTrue(any('after report date' in x for x in reasons))

    def test_failed_retrieval_not_refreshed(self):
        self.policy.update(status='unavailable', last_inspected=None)
        age, reasons = assess(self.policy, dt.date(2026, 9, 8), 90)
        self.assertIsNone(age)
        self.assertIn('coverage unavailable', reasons)

    def test_complete_recent_review_no_reminder(self):
        self.policy.update(human_review='reviewed')
        self.assertEqual(assess(self.policy, dt.date(2026, 9, 8), 90)[1], [])

    def test_cli_reminders_and_exit_status(self):
        with contextlib.redirect_stdout(io.StringIO()):
            code = age_main(['--root', str(self.root), '--as-of', '2026-09-08'])
            strict = age_main(['--root', str(self.root), '--as-of', '2026-09-08', '--fail-on-due'])
        self.assertEqual(code, 0)
        self.assertEqual(strict, 2)

    def test_invalid_age_interval(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(age_main(['--root', str(self.root), '--max-age-days', '0']), 1)


class SelectionTests(Fixture):
    def test_private_and_unknown_files_excluded(self):
        self.write('private/session.md', 'private fixture\n')
        self.write('docs/.env', 'fixture\n')
        self.write('docs/raw-transcripts/chat.md', 'fixture\n')
        self.write('docs/credentials.json', '{}\n')
        self.write('unknown.md', 'unselected\n')
        paths = collect_public_files(self.root)
        self.assertEqual(len(paths), 5)
        for name in ['private/x.md', 'docs/.env', 'docs/raw-transcripts/x.md', 'docs/secret.key']:
            self.assertTrue(excluded(name))

    def test_symlink_file_refused(self):
        target = self.base / 'outside.md'
        target.write_text('private fixture\n')
        (self.root / 'docs/link.md').symlink_to(target)
        with self.assertRaises(ValueError):
            collect_public_files(self.root)

    def test_symlink_directory_refused(self):
        outside = self.base / 'outside'
        outside.mkdir()
        (self.root / 'docs/linked').symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            collect_public_files(self.root)

    def test_new_files_are_checked_before_staging(self):
        self.write('docs/new.md', '[broken](missing.md)\n')
        self.assertTrue(any('docs/new.md: missing relative link' in x for x in check_repository(self.root)[0]))


if __name__ == '__main__':
    unittest.main()
