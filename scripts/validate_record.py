# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6", "jsonschema>=4.18"]
# ///
"""Validate AI-use records against schema/ai-use.schema.json and cross-reference rules.

Usage: uv run scripts/validate_record.py AI_USE.yaml [more records...]

Checks structure, unique and resolvable identifiers, preserved paths, and that each
check's method label is literally true of who produced the claim and who performed
the check (for example, a cross-provider review must come from a different
provider). Labels say nothing about how strong a check is, and the validator cannot
check that the recorded facts are true.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / 'schema/ai-use.schema.json').read_text(encoding='utf-8'))
MACHINE_CLASSES = {'self-review', 'same-provider-review', 'cross-provider-review'}


class TextDateLoader(yaml.SafeLoader):
    """Keep unquoted dates such as 2026-10-23 as strings, as the schema expects."""


TextDateLoader.yaml_implicit_resolvers = {
    key: [r for r in resolvers if r[0] != 'tag:yaml.org,2002:timestamp']
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
HUMAN_CLASSES = {'human-summary-review', 'human-primary-review'}


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
        unknown(claim['produced_by'], f'{cid}.produced_by')
        producers = set(claim['produced_by'])
        producer_providers = {systems[p]['provider'] for p in producers if p in systems}
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
            performer_providers = {systems[p]['provider'] for p in performers if p in systems}
            if kind == 'self-review' and not performers <= producers:
                errors.append(f'{where}: self-review performers must be among the producers')
            if kind == 'same-provider-review' and not performer_providers <= producer_providers:
                errors.append(f'{where}: same-provider-review needs a provider shared with the producers')
            if kind == 'cross-provider-review' and performer_providers & producer_providers:
                errors.append(f'{where}: cross-provider-review shares a provider with the producers: {sorted(performer_providers & producer_providers)}')
            for item in check['preserved_at']:
                if 'path' in item and not (base / item['path']).exists():
                    errors.append(f'{where}: preserved_at path not found: {item["path"]}')
    return errors


def validate(path: Path) -> list[str]:
    try:
        record = yaml.load(path.read_text(encoding='utf-8'), Loader=TextDateLoader)
    except (OSError, yaml.YAMLError) as exc:
        return [f'cannot read: {exc}']
    schema_errors = sorted(Draft202012Validator(SCHEMA).iter_errors(record), key=lambda e: list(e.absolute_path))
    if schema_errors:
        return [f'{"/".join(map(str, e.absolute_path)) or "(root)"}: {e.message}' for e in schema_errors]
    return cross_reference_errors(record, path.resolve().parent)


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
    print('Checked: structure, identifiers, preserved paths and method-label consistency. Not checked: whether the recorded facts are true or the checks adequate.')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
