# Instructions for agents and coding assistants

Applies throughout this repository. Read `README.md`, `HANDOVER.md`, `docs/principles.md`, `provenance/decision-log.md` and `provenance/founding-discussion.md` before substantive changes.

## Preserve the project brief

- Narrative and workflow are the default. Do not impose a role-assignment matrix, numerical contribution score, token count, labour percentage or a human-only drafting requirement.
- Retain the four interaction modes as descriptive and overlapping, not a quality ladder. Propose definition changes explicitly.
- Treat collaboration as a functional description. Do not imply AI consciousness, legal personhood, formal scientific authorship or accountability.
- Keep the distinction between clean results, development history and deliberative records. Do not promise complete historical logs or access to model-internal reasoning.
- The verification question was unanswered. Label new assurance criteria as proposals until explicitly adopted. Do not convert an assistant suggestion into a founder-endorsed principle.

## Evidence and honesty

Check current primary sources before asserting publisher requirements or recent findings. Cite the precise source and record what was actually inspected. A search snippet, abstract, policy section and full article are different evidence scopes. Failed retrieval must not receive an `inspected` status.

Do not fabricate dates, identifiers, citations, checks, human approval, endorsements or historical Git commits. Do not claim independent validation based only on another model agreeing. Cite external third-party materials appropriately even when discovered through AI.

Templates must never automatically assert that every source or output was checked. Document actual scope and limitations. Fictional examples must remain clearly labelled fictional.

## Working practice

Make coherent, reviewable changes. Update the decision log for conceptual changes and the changelog for material revisions. Run `python3 scripts/check_repo.py` and `python3 -m unittest discover -s tests -v`. Report failed or unrun tests accurately.

Keep Python maintenance code standard-library-only unless a demonstrated need justifies a dependency. The repository must remain useful as plain text. Do not introduce a website, API integration or elaborate form system by default.

Use ordinary, precise prose and Australian/British spelling in original explanatory text. Preserve titles and source wording accurately where quoted. Criticism is welcome; do not substitute agreement or advocacy for analysis.

## Publication and data boundaries

Never publish credentials, raw private transcripts, confidential manuscripts, sensitive data or private third-party communications. Review staged files and relevant history before a public push. Do not force-push, rewrite shared history, create a public remote or change licences without authorisation appropriate to the current task.

Do not add models to formal authorship metadata. Update the repository's AI-use account with actual work performed and identifiable systems when known. Do not infer the underlying model from a product label.

## Continuity

When handing over, record decisions, unresolved questions, sources checked and tests run. Do not present your handover as an exhaustive transcript or an independent scientific audit. Preserve the founder's preference for compact, single-topic discussion where further conceptual input is needed, without restarting topics already answered.
