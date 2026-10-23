"""Check repository structure and local consistency, not scientific validity.

No network access. Markdown checks cover inline relative file links outside
code fences, not external URLs, heading anchors or all possible Markdown syntax.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from repo_utils import collect_public_files, load_json, safe_relative, valid_slug

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {'inspected', 'partial', 'unavailable'}


def valid_date(value: object) -> bool:
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        return False
    try:
        dt.date.fromisoformat(value)
        return True
    except ValueError:
        return False


def check_links(path: Path, root: Path, text: str) -> list[str]:
    errors: list[str] = []
    # The repository deliberately uses simple Markdown links, not a full parser.
    outside_code = re.sub(r'(?ms)^\s*(```|~~~).*?^\s*\1\s*$', '', text)
    for raw in re.findall(r'\]\(([^)]+)\)', outside_code):
        target = raw.strip().split()[0].strip('<>') if raw.strip() else ''
        if not target or '{{' in target or target.startswith('#'):
            continue
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        location = unquote(parsed.path)
        resolved = (path.parent / location).resolve()
        if not resolved.is_relative_to(root.resolve()):
            errors.append(f'{path.relative_to(root)}: link escapes project: {target}')
        elif not resolved.exists():
            errors.append(f'{path.relative_to(root)}: missing relative link target: {target}')
    return errors


def validate_records(data: dict, key: str, status_key: str) -> list[str]:
    errors: list[str] = []
    if data.get('schema_version') != 1:
        errors.append(f'{key}: unsupported schema_version')
    records = data.get(key)
    if not isinstance(records, list) or not records:
        return errors + [f'{key}: expected a non-empty record list']
    seen = set()
    for record in records:
        if not isinstance(record, dict):
            errors.append(f'{key}: record must be an object')
            continue
        identifier = record.get('id')
        if not isinstance(identifier, str) or not identifier:
            errors.append(f'{key}: missing string id')
            continue
        if identifier in seen:
            errors.append(f'{key}: duplicate id {identifier}')
        seen.add(identifier)
        label = f'{key}/{identifier}'
        status = record.get(status_key)
        if not isinstance(status, str) or status not in STATUSES:
            errors.append(f'{label}: invalid {status_key}')
        for date_key in ['last_attempted', 'last_inspected', 'policy_updated', 'human_reviewed_on']:
            value = record.get(date_key)
            if value is not None and not valid_date(value):
                errors.append(f'{label}: invalid {date_key}')
        if not valid_date(record.get('last_attempted')):
            errors.append(f'{label}: last_attempted is required')
        inspected = record.get('last_inspected')
        if status == 'inspected' and not valid_date(inspected):
            errors.append(f'{label}: inspected record needs last_inspected')
        attempted = record.get('last_attempted')
        if valid_date(inspected) and valid_date(attempted) and inspected > attempted:
            errors.append(f'{label}: last_inspected is later than last_attempted')
        if not isinstance(record.get('human_review'), str) or record.get('human_review') not in {'pending', 'reviewed'}:
            errors.append(f'{label}: human_review must be pending or reviewed')
        if record.get('human_review') == 'reviewed':
            if not record.get('human_reviewer') or not valid_date(record.get('human_reviewed_on')):
                errors.append(f'{label}: reviewed status needs human_reviewer and human_reviewed_on')
        url = record.get('url')
        try:
            url_ok = isinstance(url, str) and url.startswith('https://') and bool(urlsplit(url).netloc)
        except ValueError:
            url_ok = False
        if not url_ok:
            errors.append(f'{label}: valid primary HTTPS url required')
        for field in ['scope', 'checked_by']:
            if not isinstance(record.get(field), str) or not record[field].strip():
                errors.append(f'{label}: {field} required')
    return errors


def check_repository(root: Path) -> tuple[list[str], int, str]:
    root = root.resolve()
    errors: list[str] = []
    try:
        config = load_json(root / 'repo_config.json')
        files, mode = collect_public_files(root)
    except (ValueError, OSError) as exc:
        return [str(exc)], 0, 'unavailable'
    if config.get('schema_version') != 1 or not valid_slug(config.get('slug')):
        errors.append('repo_config.json: invalid schema_version or slug')
    if not isinstance(config.get('version'), str) or not config['version']:
        errors.append('repo_config.json: version required')
    required = config.get('required_files')
    if not isinstance(required, list) or not required:
        errors.append('repo_config.json: required_files must be a non-empty list')
        required = []
    selected = {p.relative_to(root).as_posix() for p in files}
    for name in required:
        if not isinstance(name, str) or not safe_relative(name):
            errors.append(f'Invalid required file name: {name!r}')
        elif name not in selected:
            errors.append(f'Required public file missing or untracked: {name}')
    for file in files:
        rel = file.relative_to(root).as_posix()
        try:
            raw = file.read_bytes()
            text = raw.decode('utf-8')
        except (UnicodeError, OSError) as exc:
            errors.append(f'{rel}: cannot read UTF-8: {exc}')
            continue
        if b'\r' in raw:
            errors.append(f'{rel}: CR/CRLF found; use LF line endings')
        if raw and not raw.endswith(b'\n'):
            errors.append(f'{rel}: final newline missing')
        if '\x00' in text:
            errors.append(f'{rel}: unexpected NUL byte')
        if file.suffix == '.md':
            errors.extend(check_links(file, root, text))
        if file.suffix == '.json':
            try:
                load_json(file)
            except ValueError as exc:
                errors.append(str(exc))
    try:
        sources = load_json(root / 'references/source-register.json')
        policies = load_json(root / 'policies/registry.json')
        errors.extend(validate_records(sources, 'sources', 'access_status'))
        errors.extend(validate_records(policies, 'policies', 'status'))
        source_rows = sources.get('sources') if isinstance(sources.get('sources'), list) else []
        policy_rows = policies.get('policies') if isinstance(policies.get('policies'), list) else []
        source_map = {s['id']: s for s in source_rows if isinstance(s, dict) and isinstance(s.get('id'), str)}
        for policy in policy_rows:
            if not isinstance(policy, dict):
                continue
            source_id = policy.get('source_id')
            source = source_map.get(source_id) if isinstance(source_id, str) else None
            if source is None:
                errors.append(f'{policy.get("id")}: unknown source_id')
            elif policy.get('url') != source.get('url'):
                errors.append(f'{policy.get("id")}: URL differs from referenced source')
        interval = policies.get('review_interval_days')
        if type(interval) is not int or interval < 1:
            errors.append('policies: review_interval_days must be a positive integer')
    except (ValueError, OSError) as exc:
        errors.append(str(exc))
    return errors, len(files), mode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    errors, count, mode = check_repository(args.root)
    if errors:
        for error in errors:
            print('ERROR:', error, file=sys.stderr)
        print(f'FAILED: {len(errors)} issue(s).', file=sys.stderr)
        return 1
    print(f'PASS: {count} public text files checked ({mode}).')
    print('Checked: required files, UTF-8/LF, inline relative links, JSON records and source references.')
    print('Not checked: external links, heading anchors, policy truth, scientific validity or all secrets.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
