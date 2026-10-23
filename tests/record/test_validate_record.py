"""Optional YAML-record tests; run with the validator's PyYAML/jsonschema dependencies."""
from __future__ import annotations

import contextlib
import copy
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))
import validate_record as validator

FIXTURE = """\
record_format: ai-use-record/0.1
artefact: {title: Test record, kind: repository}
narrative: AI_USE.md
record:
  prepared_by: [ai]
  prepared_on: 2026-10-23
  human_review: {status: pending}
participants:
  systems:
    - id: ai
      product: Test tool
      provider: Test provider
      model: Test model
      model_source: exposed-by-tool
      period: {from: 2026-10, to: ongoing}
      interaction_record: contemporaneous-summary
relationship: {predominant_mode: ai-assistance, summary: Test fixture only.}
records:
  clean_release: {status: absent}
  development_history: {status: absent}
  deliberative_record: {status: absent}
claims:
  - id: C1
    statement: Test claim.
    produced_by: [ai]
    produced_through: Test fixture only.
    failure_modes: [Test failure.]
    checks:
      - id: C1.a
        method: model-self-review
        description: Test check.
        performed_by: [ai]
        target: Test failure.
        oracle: Test oracle.
        evidence_source: Test fixture only.
        shares: [model]
        outcome: passed
        observed: Test outcome only.
        residual: Test fixture only.
        preserved_at: [{note: Test fixture only.}]
    limits: Test fixture only.
"""


class RecordValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.record = validator.yaml.load(FIXTURE, Loader=validator.TextDateLoader)

    def write(self, text, name='record.yaml'):
        path = self.root / name
        path.write_text(text, encoding='utf-8')
        return path

    def errors(self, data):
        return validator.validate(self.write(validator.yaml.safe_dump(data)))

    def test_conflicting_duplicate_outcome_is_rejected(self):
        text = FIXTURE.replace('outcome: passed', 'outcome: failed\n        outcome: passed')
        errors = validator.validate(self.write(text))
        self.assertTrue(any("duplicate mapping key 'outcome'" in error for error in errors))

    def test_merge_collision_is_rejected(self):
        text = FIXTURE.replace('outcome: passed', '<<: {outcome: failed}\n        outcome: passed')
        errors = validator.validate(self.write(text))
        self.assertTrue(any("duplicate mapping key 'outcome'" in error for error in errors))

    def test_merge_without_collision_preserves_outcome(self):
        text = FIXTURE.replace('outcome: passed', '<<: {outcome: passed}')
        self.assertEqual(validator.validate(self.write(text)), [])

    def test_invalid_utf8_does_not_abort_remaining_records(self):
        bad = self.root / 'bad.yaml'
        bad.write_bytes(b'\xff\n')
        good = self.write(FIXTURE)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = validator.main([str(bad), str(good)])
        self.assertEqual(status, 1)
        self.assertIn(f'FAIL: {bad}', output.getvalue())
        self.assertIn(f'PASS: {good}', output.getvalue())

    def test_impossible_calendar_dates_in_each_date_field(self):
        cases = [
            (('record', 'prepared_on'), '2026-02-30'),
            (('record', 'human_review', 'reviewed_on'), '2026-13'),
            (('participants', 'systems', 0, 'period', 'from'), '0000'),
            (('participants', 'systems', 0, 'period', 'to'), '2026-04-31'),
            (('claims', 0, 'checks', 0, 'date'), '2026-99-99'),
        ]
        for path, value in cases:
            with self.subTest(path=path, value=value):
                record = copy.deepcopy(self.record)
                node = record
                for key in path[:-1]:
                    node = node[key]
                node[path[-1]] = value
                self.assertTrue(any('invalid calendar date' in error for error in self.errors(record)))

    def test_leap_day_and_partial_dates_remain_valid(self):
        for value in ['2024-02-29', '2026', '2026-10', '9999-12-31']:
            with self.subTest(value=value):
                self.record['record']['prepared_on'] = value
                self.assertEqual(self.errors(self.record), [])

    def test_provably_reversed_periods_are_rejected(self):
        for start, end in [('2026-10-23', '2026-10-22'), ('2026-02', '2026-01'), ('2026', '2025')]:
            with self.subTest(start=start, end=end):
                self.record['participants']['systems'][0]['period'] = {'from': start, 'to': end}
                self.assertTrue(any('from is later than to' in error for error in self.errors(self.record)))

    def test_overlapping_partial_and_unknown_periods_remain_valid(self):
        cases = [
            ('2026', '2026-01'), ('2026-10-23', '2026'), ('2026-10', '2026-10-01'),
            ('2026', 'ongoing'), ('not recorded', '2026-10'), ('not recorded', 'not recorded'),
        ]
        for start, end in cases:
            with self.subTest(start=start, end=end):
                self.record['participants']['systems'][0]['period'] = {'from': start, 'to': end}
                self.assertEqual(self.errors(self.record), [])

    def test_honest_claim_without_checks_is_valid(self):
        self.record['claims'][0]['checks'] = []
        self.assertEqual(self.errors(self.record), [])

    def test_contributors_need_not_be_reconstructed(self):
        del self.record['claims'][0]['produced_by']
        self.assertEqual(self.errors(self.record), [])

    def test_later_contribution_by_reviewer_does_not_invalidate_its_review(self):
        self.record['participants']['systems'].append(
            dict(self.record['participants']['systems'][0], id='other', provider='Other provider'))
        check = self.record['claims'][0]['checks'][0]
        check.update(method='cross-provider-review', performed_by=['other'])
        self.record['claims'][0]['produced_by'] = ['ai', 'other']
        self.assertEqual(self.errors(self.record), [])

    def test_completed_check_requires_observed_and_residual(self):
        check = self.record['claims'][0]['checks'][0]
        del check['observed'], check['residual']
        errors = self.errors(self.record)
        self.assertTrue(any("'observed' is a required property" in error for error in errors))
        self.assertTrue(any("'residual' is a required property" in error for error in errors))

    def test_not_run_check_needs_no_invented_observation(self):
        check = self.record['claims'][0]['checks'][0]
        del check['observed'], check['residual']
        check['outcome'] = 'not-run'
        self.assertEqual(self.errors(self.record), [])

    def test_human_review_label_must_name_people(self):
        self.record['claims'][0]['checks'][0]['method'] = 'human-primary-review'
        self.assertTrue(any('must be performed by people only' in error for error in self.errors(self.record)))

    def test_model_review_labels_must_name_systems(self):
        self.record['participants']['people'] = [{'id': 'researcher', 'name': 'Test researcher'}]
        check = self.record['claims'][0]['checks'][0]
        check['performed_by'] = ['researcher']
        for method in ['model-self-review', 'same-provider-review', 'cross-provider-review']:
            with self.subTest(method=method):
                check['method'] = method
                self.assertTrue(any('must be performed by systems only' in error for error in self.errors(self.record)))

    def test_human_can_review_their_own_contribution(self):
        self.record['participants']['people'] = [{'id': 'researcher', 'name': 'Test researcher'}]
        self.record['claims'][0]['produced_by'] = ['researcher', 'ai']
        self.record['claims'][0]['checks'][0].update(
            method='human-primary-review', performed_by=['researcher'],
            description='The researcher checked their own derivation against the source data.')
        self.assertEqual(self.errors(self.record), [])


if __name__ == '__main__':
    unittest.main()
