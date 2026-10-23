# Policy register: a dated starting point, not a compliance certificate

The [register](registry.json) records **six scoped checks attempted on 2026-09-08**. Four have inspected relevant guidance, one remains partial because detailed linked guidance is outstanding, and one dedicated page was unavailable. All require human review. “Inspected” refers to the specified section, not an exhaustive review of a publisher's rules.

| Record | Scope | Status |
| --- | --- | --- |
| POL-ELSEVIER | Publisher journal author guidance; individual titles still matter | Relevant sections inspected |
| POL-AJPS | Journal-specific guidance | Inspected |
| POL-CAMBRIDGE | Central AI authorship/contributorship subsection | Inspected |
| POL-NATURE-COMMSMAT | Journal-hosted core expectations and risk categories | Relevant sections inspected |
| POL-WILEY-ETHICS | General publishing-ethics page | Partial policy coverage |
| POL-WILEY-AI | Dedicated researcher guidelines | Unavailable |

Each record contains its primary URL, retrieval date, source identifier, interpretation, placement guidance and next check. The [source register](../references/source-register.json) separately records retrieval scope and uncertain applicability, including a legacy Cambridge-hosted journal page not treated as current universal policy.

## Applying this to a submission

Start with the actual target journal, submission date and manuscript workflow. Read the applicable primary pages. Identify what uses are permitted, prohibited or conditional; what detail is requested; and where the declaration must appear. Compare those requirements with the true project account. A different vocabulary must not conceal a prohibited use or invent oversight. See [policy adaptation](../docs/policy-adaptation.md) and the [project-specific policy-check template](../templates/policy-check.md).

No declaration here guarantees acceptance or policy compliance. A record can be recent yet incomplete, and a complete record can become stale. Applicable ethical, privacy or data constraints are not exhausted by an AI-disclosure policy.

## Maintaining the register

Keep `last_attempted` separate from `last_inspected`, and both separate from a publisher's stated `policy_updated` date. Use `null` for unknown dates. A failed retrieval does not renew the substantive inspection date. Record the precise scope of a check and leave `human_review` as `pending` until an identifiable human actually reviews it; changing that status requires a `human_reviewer` and `human_reviewed_on`.

```bash
python3 scripts/policy_age.py
python3 scripts/policy_age.py --as-of 2026-09-08 --max-age-days 90
```

This local report makes **no network requests**. Ninety days is an editable maintenance reminder, not a publisher requirement or a claim that policies remain valid for that period. `--fail-on-due` supplies a non-zero exit status for overdue, future-dated, incomplete or human-unreviewed records when maintainers intentionally want that behaviour. The normal repository check does not fail solely because a candidly documented source is unavailable.

Do not add automatic policy-rewriting or publishing tasks without explicit maintainer approval. A future monitoring process should create reviewable proposals, not silently reinterpret the framework.
