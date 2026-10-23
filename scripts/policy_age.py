"""Report source-review age and incompleteness without fetching anything online."""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

from check_repo import validate_records
from repo_utils import load_json

ROOT = Path(__file__).resolve().parents[1]


def assess(record: dict, as_of: dt.date, max_age_days: int) -> tuple[int | None, list[str]]:
    reasons = []
    raw = record.get('last_inspected')
    age = None
    if raw is None:
        reasons.append('no substantive inspection date')
    else:
        age = (as_of - dt.date.fromisoformat(raw)).days
        if age < 0:
            reasons.append('inspection date is after report date')
        elif age >= max_age_days:
            reasons.append(f'inspection at least {max_age_days} days old')
    if dt.date.fromisoformat(record['last_attempted']) > as_of:
        reasons.append('attempt date is after report date')
    if record.get('status') != 'inspected':
        reasons.append(f'coverage {record.get("status", "unknown")}')
    if record.get('human_review') != 'reviewed':
        reasons.append('human review pending')
    return age, reasons


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--as-of', type=dt.date.fromisoformat, default=dt.date.today())
    parser.add_argument('--max-age-days', type=int)
    parser.add_argument('--fail-on-due', action='store_true')
    args = parser.parse_args(argv)
    try:
        data = load_json(args.root / 'policies/registry.json')
        errors = validate_records(data, 'policies', 'status')
        if errors:
            raise ValueError('; '.join(errors))
        interval = args.max_age_days if args.max_age_days is not None else data.get('review_interval_days', 90)
        if type(interval) is not int or interval < 1:
            raise ValueError('--max-age-days must be a positive integer')
        due = 0
        print(f'Policy review report as of {args.as_of} (age reminder: {interval} days)')
        for record in data['policies']:
            age, reasons = assess(record, args.as_of, interval)
            due += bool(reasons)
            age_text = 'no date' if age is None else f'{age} days'
            print(f'{record["id"]}: {age_text}; ' + ('REVIEW: ' + '; '.join(reasons) if reasons else 'no local reminder triggered'))
        print(f'{due}/{len(data["policies"])} records need attention. No policies fetched; no compliance certification.')
        return 2 if due and args.fail_on_due else 0
    except (OSError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
