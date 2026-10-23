# The structured AI-use record

**Status.** This is Claude's proposal ([D017](../provenance/decision-log.md)), drafted on 2026-10-23, and it has not been adopted. It implements adopted principle P06 together with the operational account in [warrant and independence](warrant-and-independence.md) (D016), which is also a proposal. Before the first commit it was revised in response to Codex's review in board threads 93 and 94.

## Purpose

The narrative stays primary ([P05](principles.md)). The record carries the facts that a reader or a tool should be able to query and a reviewer should be able to falsify:

- which systems took part, when, and how their identities are known;
- the relationship between the people and the systems;
- which records of the work exist; and
- for each consequential claim, which checks were made and with what result.

This is what formalisation means in this framework: **formalise facts and links to evidence, never shares of labour.** A sentence such as "The authors reviewed all outputs and take full responsibility" cannot be falsified. The record replaces it with statements that can be checked one by one.

## What a record never contains

- **No shares of labour, time or output.** It holds no percentages, no grids of contributor roles, and no attribution sentence by sentence or line by line. The schema rejects any field it does not define, so these cannot be added informally. `produced_by` lists everyone involved in a claim, unordered and without shares.
- **No verdict on sufficiency.** A record that passes validation certifies nothing about whether the evidence is enough to support a claim. That remains a judgement for authors, reviewers and readers ([warrant and independence, section 5](warrant-and-independence.md)).
- **No selective omission.** Material adverse checks stay in the record, with their disposition shown in `outcome` (`failed` or `issues-fixed`) and `observed`. A record that lists only favourable checks can be literally true and still mislead.
- **No guesses.** "not recorded" and "not assessed" are valid values and are expected where they are true. A model identifier is never inferred from a product name or a date.

## File, format and validation

- **Location.** The record lives in `AI_USE.yaml`, beside the narrative in `AI_USE.md`. A blank template is at [templates/AI_USE.yaml](../templates/AI_USE.yaml).
- **Why YAML.** Researchers already write it for Quarto, R Markdown and `CITATION.cff`, and it allows comments.
- **Schema.** The structure is defined by a JSON Schema (draft 2020-12) at [schema/ai-use.schema.json](../schema/ai-use.schema.json), so any language can validate a record. R has `jsonvalidate`; Python has `jsonschema`.
- **Two YAML pitfalls.**
  - Many YAML parsers turn an unquoted `2026-10-23` into a date object. Either quote dates or tell the parser to keep them as strings, as the validator does.
  - Under YAML 1.1 the keys `on`, `yes` and `no` parse as booleans. That is why the review fields are named `reviewed_by` and `reviewed_on`.
- **The validator.** Run `uv run scripts/validate_record.py AI_USE.yaml`. It needs PyYAML and jsonschema, which the script declares inline and `uv` installs on demand. The repository's core checks stay standard-library-only, and validating YAML is the demonstrated need that AGENTS.md asks for before a dependency is added.

## Sections

| Section | Content |
| --- | --- |
| `artefact` | What the record describes: title, kind, and optionally an identifier and version. |
| `narrative` | The path or URL of the narrative account. |
| `record` | Who prepared the record, including any AI system that drafted it; the date; and whether a human has reviewed it. |
| `participants.people` | Identifiers for people, needed when they perform checks. |
| `participants.systems` | One entry per product, provider and model combination. Each entry records the model identifier and **how it is known** (`exposed-by-tool`, `provider-record`, `contemporaneous-note`, `recollection` or `not-recorded`); the period; the kind of interaction record (`original`, `partial-original`, `contemporaneous-summary`, `later-reconstruction`, `none` or `not-recorded`, following [provenance and preservation](provenance-and-preservation.md)); and optionally a `configuration` such as reasoning effort or delegation. |
| `relationship` | The predominant mode, using the adopted names from [D006](interaction-modes.md) (or `mixed`), any secondary modes by phase, and a one-sentence summary. |
| `records` | The clean release, development history and deliberative record ([D003](../provenance/decision-log.md)), each with a status, access level and location. |
| `claims` | The consequential claims that the AI-involved work bears on. This is usually a handful, not every output, and it can be omitted when bounded assistance touched no claim. Each claim lists who was involved, how it was produced, its failure modes, its checks and its limits. |
| `checks` | For each check, the elements set out in [warrant and independence, section 3](warrant-and-independence.md): `target`, `oracle`, `evidence_source`, `performed_by`, `outcome` and `observed`, `shares` and `residual`, plus `preserved_at` for where the record of the check is kept. |
| `gaps` | Missing records, unknown identifiers and checks not yet run. |

## Method labels

`method` is a descriptive label: `self-review`, `same-provider-review`, `cross-provider-review`, `generator-written-tests`, `reproduction`, `independent-reimplementation`, `human-summary-review`, `human-primary-review`, `known-answer-test`, `external-evidence` or `other`. **A label sets no default strength.** The fictional example shows a known-answer test that shares code with the fit, an external benchmark that may sit in the training data, and a test the generator wrote for itself that caught a real error.

The validator checks only that a label is literally true of the participants:

- a `self-review` is performed by participants among the claim's producers;
- a `same-provider-review` is performed by systems whose provider is among the producers' providers;
- a `cross-provider-review` is performed by systems that share no provider with the producers;
- a provider recorded as `not recorded` is left out of these comparisons, so that an unknown stays unknown rather than failing a claim the record never made; and
- the `human-*` methods are performed by people.

These rules test whether a label is accurate, not whether a check is strong.

## Validator scope

| The validator checks | The validator does not check |
| --- | --- |
| Structure against the schema | Whether the recorded facts are true |
| That identifiers are unique and resolve to participants | Whether a check could detect what its `target` names |
| That `preserved_at` paths exist | Whether the checks suffice for the claim |
| That method labels are literally consistent with the participants | Whether the narrative and the record agree |

## Worked records

- **[AI_USE.yaml](../AI_USE.yaml)** is real: it describes this repository. It records two errors in Claude's drafting that Codex caught by reading the primary sources (claims C4 and C5), and two human checks that are still pending (C1.b and C2.b).
- **[examples/embedded-collaboration.yaml](../examples/embedded-collaboration.yaml)** is fictional. It pairs with the prose example of the same name and carries the four counterexamples from Codex's review.

## Testing against real statements

Barry supplied two unpublished AI-use statements: one submitted with a review paper, and a draft for a data and analysis paper. They are not reproduced here. Encoding the draft exposed two gaps, both now fixed:

- there was nowhere to record reasoning effort or delegation between systems, which `configuration` now covers; and
- there was no label for one system reproducing another's analyses from the same specification, which `independent-reimplementation` now covers.

## Relation to the paper-level declaration

Write the narrative first, then the record, then derive the short declaration from both. Every sentence about checking in a declaration should trace to a check in the record. The declaration can point to the record and to the deposit holding the deliberative record.

## Open questions

- Should `claims` be able to point to an existing claim-to-evidence register instead of duplicating it? Barry's analysis projects already maintain such registers.
- Should the record map onto W3C PROV or PROV-AGENT for interoperability, and if so, when?
- Should the method list stay controlled, or become free text?
- How finely should delegate systems be listed: one entry per model, or one per role?
- Records will often be drafted by an AI and reviewed by a human. Is `prepared_by` together with `human_review` enough to make that visible?
