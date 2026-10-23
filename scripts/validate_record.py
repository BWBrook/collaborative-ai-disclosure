# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6", "jsonschema>=4.18"]
# ///
"""Validate AI-use records against schema/ai-use.schema.json and cross-reference rules.

Usage: uv run scripts/validate_record.py AI_USE.yaml [more records...]

Checks structure, calendar dates and period order, unique and resolvable identifiers,
preserved paths, and that a method label names the right kind of performer (people for
human reviews, systems for model reviews). It does not infer how a check relates to the
work it checks, says nothing about how strong a check is, and cannot check that the
recorded facts are true.
"""
from __future__ import annotations

import calendar
import datetime as dt
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / 'schema/ai-use.schema.json').read_text(encoding='utf-8'))
MACHINE_CLASSES = {'model-self-review', 'same-provider-review', 'cross-provider-review'}


class TextDateLoader(yaml.SafeLoader):
    """Keep dates as strings and reject duplicate keys, including merge collisions."""

    def construct_mapping(self, node, deep=False):
        self.flatten_mapping(node)
        seen = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                duplicate = key in seen
                seen.add(key)
            except TypeError as exc:
                raise yaml.constructor.ConstructorError(
                    'while constructing a mapping', node.start_mark,
                    'unhashable mapping key', key_node.start_mark,
                ) from exc
            if duplicate:
                raise yaml.constructor.ConstructorError(
                    'while constructing a mapping', node.start_mark,
                    f'duplicate mapping key {key!r}', key_node.start_mark,
                )
        return super().construct_mapping(node, deep=deep)


TextDateLoader.yaml_implicit_resolvers = {
    key: [r for r in resolvers if r[0] != 'tag:yaml.org,2002:timestamp']
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
HUMAN_CLASSES = {'human-summary-review', 'human-primary-review'}
UNKNOWN = 'not recorded'


def date_bounds(value: str) -> tuple[dt.date, dt.date] | None:
    """Calendar bounds for a schema-valid date of year, month or day precision."""
    if value in {UNKNOWN, 'ongoing'}:
        return None
    parts = [int(part) for part in value.split('-')]
    start = dt.date(*(parts + [1] * (3 - len(parts))))
    if len(parts) == 1:
        end = dt.date(parts[0], 12, 31)
    elif len(parts) == 2:
        end = dt.date(parts[0], parts[1], calendar.monthrange(*parts)[1])
    else:
        end = start
    return start, end


def date_errors(record: dict) -> list[str]:
    errors: list[str] = []

    def bounds(value: str, where: str):
        try:
            return date_bounds(value)
        except ValueError:
            errors.append(f'{where}: invalid calendar date {value!r}')
            return None

    bounds(record['record']['prepared_on'], 'record.prepared_on')
    review = record['record']['human_review']
    if 'reviewed_on' in review:
        bounds(review['reviewed_on'], 'record.human_review.reviewed_on')
    for system in record['participants']['systems']:
        where = f'participants.systems/{system["id"]}.period'
        start = bounds(system['period']['from'], f'{where}.from')
        end = bounds(system['period']['to'], f'{where}.to')
        # Reject only when every possible start is later than every possible end.
        if start is not None and end is not None and start[0] > end[1]:
            errors.append(f'{where}: from is later than to at the recorded precision')
    for claim in record.get('claims', []):
        for check in claim['checks']:
            if 'date' in check:
                bounds(check['date'], f'{claim["id"]}/{check["id"]}.date')
    return errors


def cross_reference_errors(record: dict, base: Path) -> list[str]:
    errors: list[str] = []
    participants = record['participants']
    people = {p['id'] for p in participants.get('people', [])}
    systems = {s['id']: s for s in participants['systems']}
    duplicated = people & systems.keys()
    if duplicated or len(people) != len(participants.get('people', [])) or len(systems) != len(participants['systems']):
        errors.append(f'participant ids must be unique: {sorted(duplicated) or "duplicate within a list"}')
    known = people | systems.keys()

    def unknown(ids: list[str], where: str) -> None:
        for missing in sorted(set(ids) - known):
            errors.append(f'{where}: unknown participant {missing!r}')

    unknown(record['record']['prepared_by'], 'record.prepared_by')
    unknown(record['record']['human_review'].get('reviewed_by', []), 'record.human_review.reviewed_by')
    if record['record']['human_review']['status'] == 'reviewed' and not set(record['record']['human_review']['reviewed_by']) <= people:
        errors.append('record.human_review.reviewed_by: a human review must name people, not systems')

    seen: set[str] = set()
    for claim in record.get('claims', []):
        cid = claim['id']
        if cid in seen:
            errors.append(f'duplicate claim or check id {cid!r}')
        seen.add(cid)
        unknown(claim.get('produced_by', []), f'{cid}.produced_by')
        for check in claim['checks']:
            where = f'{cid}/{check["id"]}'
            if check['id'] in seen:
                errors.append(f'duplicate claim or check id {check["id"]!r}')
            seen.add(check['id'])
            performers = set(check['performed_by'])
            unknown(sorted(performers), f'{where}.performed_by')
            kind = check['method']
            if kind in MACHINE_CLASSES and not performers <= systems.keys():
                errors.append(f'{where}: {kind} must be performed by systems only')
            if kind in HUMAN_CLASSES and not performers <= people:
                errors.append(f'{where}: {kind} must be performed by people only')
            for item in check['preserved_at']:
                if 'path' in item and not (base / item['path']).exists():
                    errors.append(f'{where}: preserved_at path not found: {item["path"]}')
    return errors


def validate(path: Path) -> list[str]:
    try:
        record = yaml.load(path.read_text(encoding='utf-8'), Loader=TextDateLoader)
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        return [f'cannot read: {exc}']
    schema_errors = sorted(Draft202012Validator(SCHEMA).iter_errors(record), key=lambda e: list(e.absolute_path))
    if schema_errors:
        return [f'{"/".join(map(str, e.absolute_path)) or "(root)"}: {e.message}' for e in schema_errors]
    return date_errors(record) + cross_reference_errors(record, path.resolve().parent)


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__.strip().splitlines()[2])
        return 2
    failed = False
    for name in argv:
        errors = validate(Path(name))
        failed |= bool(errors)
        print(f'{"FAIL" if errors else "PASS"}: {name}')
        for error in errors:
            print(f'  - {error}')
    print('Checked: structure, calendar dates and period order, identifiers, preserved paths and performer kinds. Not checked: how checks relate to the work, whether the recorded facts are true, or whether the checks are adequate.')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
