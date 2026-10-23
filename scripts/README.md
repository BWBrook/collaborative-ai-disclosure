# Optional maintenance tools

The core maintenance tools use Python 3.10+ and the standard library. They check local files without fetching policies or calling an AI model.

| Command | What it does |
| --- | --- |
| `python3 scripts/check_repo.py` | Checks expected public files, text format, simple inline relative links and source/policy JSON consistency. |
| `python3 scripts/policy_age.py` | Reports stale, incomplete, future-dated or human-unreviewed policy records. |
| `python3 -m unittest discover -s tests -v` | Exercises the maintenance tools against local fixtures. |

Both command-line tools accept `--help` and `--root` for an explicit project directory. `check_repo.py` returns 0 for a pass and 1 for a structural failure. The age report normally returns 0 while printing reminders; `--fail-on-due` returns 2 when attention is needed. Invalid data returns 1.

## Scope

`repo_config.json` defines the roots and required files to check. Checks use current working-tree files, including new files before staging; they do not select files for publication. Files outside those roots and common local/private paths are skipped. Symlinks are rejected to prevent reading outside the project. Schema files and machine-readable examples receive text checks; the separate record validator handles their content.

The Markdown checker handles simple inline relative links, without checking heading anchors or external URLs. JSON checks cover syntax, status/date consistency, review metadata and source references. They do not establish source truth, journal compliance, scientific validity or absence of secrets. Review staged files and relevant history before publication.

The optional GitHub Actions workflow runs these local checks; it does not monitor policy changes. Its initial build history is recorded in the [bootstrap report](../provenance/bootstrap-report.md).

## Optional structured-record validation

`uv run scripts/validate_record.py AI_USE.yaml examples/embedded-collaboration.yaml` checks the two populated records against the proposed schema and cross-reference rules. This separate tool uses Python 3.11+, PyYAML and jsonschema, declared inline and managed by `uv`. The blank template contains placeholders and is not a populated test record. See the [proposed specification](../docs/structured-record.md) for scope; structural validity does not establish factual truth or adequate checks.

Run the optional validator regressions with `uv run --with pyyaml --with jsonschema python -m unittest discover -s tests/record -v`. These tests exercise duplicate-key rejection, calendar/date precision and continuation after a per-file read failure. They are separate from the standard-library maintenance suite.
