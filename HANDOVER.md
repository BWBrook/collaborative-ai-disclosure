# Development handover

## Project in one paragraph

Build an open, contributable framework for truthful declarations of human–AI collaborative research. The intended default is narrative, workflow-level description rather than artificial task ownership. Preserve usable categories, responsibility and evidential detail without implying that the human must personally perform most execution or originate every word and idea. The framework must accommodate bounded assistance and more deeply integrated relationships, and must not misrepresent actual practice to satisfy a journal form.

## What has been established

The founding discussion supports workflow-level disclosure with optional finer provenance; accurate collaboration language; governance distinct from labour share; four overlapping modes with a predominant descriptor; and narrative-first contribution accounts with optional role vocabulary. Read [principles](docs/principles.md), [the decision log](provenance/decision-log.md) and [the founding synthesis](provenance/founding-discussion.md).

Do not infer a fixed twelve-principle structure from the earlier “about twelve” discussion sequence. Do not resurrect a 50% cutoff or make contributor-role checklists the default.

## Adoption boundary

The founding discussion stopped at the sixth question: verification, and how a candidate contribution becomes part of the accepted scientific account. On 2026-10-23 Barry adopted Claude's proposed answer: "origin tells you which checks a contribution needs; warrant decides whether it stands" ([D010](provenance/decision-log.md)).

The operational account of checks in [warrant and independence](docs/warrant-and-independence.md), together with the templates, policy records and implementation details, remains **draft proposals for review**. None of it is an authorised extension of Barry's philosophy until he adopts it.

## Development on 2026-10-23

The ChatGPT scaffold was imported unchanged as `e721a3d`. Claude's [first-pass review](provenance/reviews/2026-10-23-claude-first-pass.md) led to P06 and an operational warrant draft. Codex's [review](provenance/reviews/2026-10-23-codex-warrant-review.md) raised eight findings about that draft. Claude addressed them in `467f2d5` and `dbd299a`, and Codex checked the substantive repairs. D016 remains a proposal. Correspondence threads 92 (division of work), 93 (warrant review) and 94 (structured record) hold the current coordination and disagreements. The board is private; these notes are a selective account, not its transcript.

The [positioning discussion](docs/positioning.md) compares six requested disclosure works using full main-text readings with separately recorded supplement/tool limits. Existing frameworks already address workflow, collaboration and checks. Neither conceptual novelty nor improved disclosure quality has been established for this project's proposed combination.

The ZIP packager and extraction guide have been retired. The [bootstrap report](provenance/bootstrap-report.md) remains a historical record; the ignored `MANIFEST.sha256` remains the original import receipt. It is not a checksum of current files. Core maintenance checks now scan configured working-tree files, including new files before staging, and retain source/status consistency checks.

Topic 6 is resolved. Further conceptual discussion should follow Barry's priorities or the [roadmap](ROADMAP.md). His earlier preference was one compact proposition at a time; do not ask him to re-answer settled topics or respond to a large questionnaire. He has now moved the project into a development workflow, so do not assume continued serial questioning is the only acceptable mode of progress.

## Use Codex and Claude without inventing independence

Either system can implement changes and either can critique them. Announce file ownership on the board before editing the shared checkout, check the working tree, and stage only owned paths. Use a separate worktree when a clean committed snapshot is needed. Preserve disagreements and their evidence. A second model's agreement does not establish independent confirmation.

Update [AI_USE.md](AI_USE.md) with actual systems, observable periods and material contributions. Distinguish the original ChatGPT archive from subsequent Claude and Codex work. Record only model identifiers exposed by the relevant environment.

## Before the first public push

Review the name and project description; the scoped licensing defaults; the proposed initial maintainer arrangement; the `CITATION.cff` attribution; all public provenance notes; and any source summary likely to be read as policy advice. Check current files and whatever Git history is being published for sensitive material. No raw transcript is included in this scaffold.

This local repository has no remote. Barry's current instruction requires permission for creating a public remote, publication or contact outside the collaboration. After an authorised remote exists, add its verified URL to `CITATION.cff` and appropriate documentation. Do not invent identifiers, endorsements or release dates.

## Source-check limitations

Selected policy clauses and literature passages were inspected on 2026-09-08; the 2026-10-23 literature review extends that record without refreshing publisher policies. Some sources and supplements remain partially checked, and the earlier dedicated Wiley-guideline retrieval failed. The [source register](references/source-register.json) records current scopes and earlier inspection histories. Independent human source review is not recorded.

The source register is not an exhaustive review of journal policies or the literature. No policy watcher is running. The supplied script checks the age and review status of local records, not the content of external websites.

## Technical scope

The framework remains usable as plain text. The core repository checker and maintenance tests use Python's standard library. Claude's optional structured-record validator declares its separate dependencies in the script; it does not make a structured record compulsory or establish scientific warrant. See [maintenance tools](scripts/README.md) for commands and scope.

The checker and tests assess repository mechanics. They do not establish that the framework is ethically adequate, that a project's claims are valid, or that a journal will accept a declaration.

## Verification and remaining work

After integrating the source review and pruning, `python3 scripts/check_repo.py` passed on 76 configured text files and `python3 -m unittest discover -s tests -v` passed all 39 maintenance tests, with none skipped. `git diff --check` passed. The original 46-test baseline passed before changes; the smaller suite removes retired packaging behaviour and retains meaningful failure coverage.

`uv run scripts/validate_record.py AI_USE.yaml examples/embedded-collaboration.yaml` passed for both populated records after Codex updated its actual-work account. That run checked the records mechanically; the separate design review followed below.

Codex subsequently completed the separate [D017 design review](provenance/reviews/2026-10-23-codex-structured-record-review.md) against `6d25055`. Six findings are posted individually in thread 94 (2290–2295): whole-claim attribution misclassifies earlier reviews; empty checks are rejected; completed checks may omit observations and residuals; optional-record wording becomes compulsory; duplicate YAML keys silently overwrite evidence; and impossible dates pass. The diagnostic at `provenance/reviews/d017_adversarial_cases.py` reproduces the executable cases without modifying the record. Invalid UTF-8 also aborts batch validation.

Claude reproduced all twelve diagnostic cases against the unchanged validator, agreed all six findings in thread 94, and implemented them in `a2a53c2`. It applied the [F5/F6 patch](provenance/reviews/2026-10-23-d017-mechanical-proposal.patch) unchanged, which rejects duplicate keys and merge collisions, reports malformed UTF-8 per file, and validates calendar dates and provably reversed periods. The patch is retained as history and must not be reapplied. For F1–F4 it took Codex's proposed repairs:

- the validator no longer infers how a check relates to the work from a claim's contributor list, and checks only that human and model-review labels name people and systems;
- `produced_by` is optional;
- `checks: []` is valid, with the gap explained in `limits`;
- completed checks must state `observed` and `residual`; and
- the specification's workflow is conditional and optional, may link an existing claim register, and defers an external-register interface.

Claude added six regression tests, bringing `tests/record/` to 14. Codex then checked the implementation and source-scope additions, replayed the diagnostic, and clarified the retained model-specific label as `model-self-review`. Two further tests cover model-only review labels and a human reviewing their own contribution, bringing the optional suite to 16. A per-check `compared_with` relation remains deferred. Agreement and implementation are not adoption: D017 remains a proposal for Barry.

The current repository checker passes on 80 configured text files. All 39 maintenance tests and 16 optional record tests pass with none skipped; both populated records validate; and `git diff --check` passes. The twelve-case diagnostic now accepts the honest omissions and intertwined review history, rejects missing completed-check fields, duplicate keys and impossible dates, and reports invalid UTF-8 without a crash. Unknown-provider labels still pass structurally because provider relationships are explicitly outside the validator's scope. These checks do not establish factual truth or usability on real research records.

The positioning discussion proposes a comparison using the same documented episodes across frameworks. Private manuscript examples offered on the board require permission before inclusion in public-facing files. No existing operational proposal has been newly adopted.
