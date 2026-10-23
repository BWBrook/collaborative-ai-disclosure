# Adversarial review of D017 (Codex, 23 October 2026)

**Reviewed snapshot:** `6d25055`, including the specification, JSON Schema, validator, template, fictional example and repository record. **Reviewer:** Codex, described by its environment as GPT-6; no finer deployment identifier is exposed. A bounded delegate tested parser and date failures; the parent tested the design cases and assessed their implications. This is a separate review of Claude's implementation, not independent scientific validation.

**Recommendation:** revise before considering adoption. D017 remains unadopted. The distinction between structured reporting and sufficient evidence survives this review, but several implementation rules contradict it. Findings were posted separately in Correspondence thread 94, messages 2290–2295. The private manuscript statements supplied there are not reproduced or encoded here.

## Findings

### F1 — Major: a final claim's contributors do not identify the source of an earlier review

**Evidence:** `scripts/validate_record.py`, `cross_reference_errors`; the specification's method-label rules. Adding Claude to C1's `produced_by` makes its existing review fail the cross-provider rule. If Claude helped revise the claim after that review, the expanded list would be truthful. Conversely, changing all providers to `not recorded` leaves the cross-provider label valid. Unknown providers do not establish different providers.

The whole-claim contributor list lacks the particular input and time to which the review refers. Requiring every contributor also pressures researchers to reconstruct a division of work that may not be recoverable. An unordered list avoids percentages but can still impose artificial attribution.

**Proposed repair:** make `produced_by` optional descriptive provenance. Retain checks that any supplied identifiers resolve; remove deductions of self/same/cross-provider relations from that whole-claim list. Describe the contribution or system compared in the check's prose where that is known. Keep the controlled method vocabulary provisionally as a search aid, with `other` for overlapping or unlisted methods; it sets neither strength nor a single exclusive classification. The validator must not advertise proof of a relation it does not establish.

An alternative is a per-check `compared_with` relation to a particular earlier contribution. That would support a narrower mechanical comparison, but introduces more attribution machinery. Codex recommends testing whether readers need that machinery before adding it. This choice remains for discussion; removing the defective inference is not evidence that every descriptive label is true.

### F2 — Major: truthful absence of checks is rejected

**Evidence:** the claim's `checks` array has `minItems: 1`. Replacing C1's checks with `[]` fails validation. A record of a consequential but unchecked claim is therefore invalid unless its author invents or specifies a proposed check.

This reinstates the reporting prerequisite rejected during the D016 review. A truthful disclosure can describe inadequate checking. **Proposed repair:** allow `checks: []`, with the gap explained in the existing required `limits` field. Keep `not-run` for a real proposed check; in that case `performed_by` identifies its intended performer, not an action already taken. Empty checks convey no sufficiency.

### F3 — Major: completed checks need not record observations or residual limits

**Evidence:** removing `observed` and `residual` from all checks still validates, although the specification describes both as elements of the account. A label such as `issues-fixed` does not say what failed, what changed or what was established afterwards.

**Proposed repair:** require both fields for outcomes other than `not-run`. Permit explicit `not recorded` or `not assessed` instead of fabricated precision. A planned check need not invent an observation. Existing examples should gain only observations supported by their recorded history, or an explicit statement that the observation was not retained. This is a reporting requirement, not an assurance threshold.

### F4 — Major: an optional record becomes a compulsory declaration workflow

**Evidence:** the specification's final section instructs writers to produce narrative, then record, then declaration, and requires every checking sentence to trace to a check in the record. That excludes a perfectly adequate narrative or an existing claim-to-evidence register unless it is duplicated in YAML.

**Proposed replacement:**

> If using a structured record, write it alongside the narrative and derive the short declaration from the same evidence. Statements about checking should be traceable to the actual checks and their records, whether described here, in the narrative or in an existing claim-to-evidence register. Using this YAML format is optional. A link to an existing register does not mean its contents have been validated by this schema.

Defer a machine-readable external-register interface until an actual use case defines it. Also soften two overclaims in the introduction: a generic assertion of human review is difficult to audit, not logically unfalsifiable; rejecting unknown field names cannot prevent labour-share claims inside free text. These are limits of the representation, not reasons to forbid narrative.

### F5 — Major: duplicate YAML keys silently erase adverse evidence

**Evidence:** inserting `outcome: failed` immediately before an existing `outcome: passed` returns PASS. The loader retains only the latter, so schema validation never sees the failed result. A repeated field introduced during ordinary editing can therefore erase adverse evidence without a diagnostic.

**Proposed repair:** reject duplicate mapping keys before schema validation, including collisions introduced by merge keys. Retain YAML: its comments and existing use are reasonable for this optional record, and silent overwriting is a repairable loader defect. Invalid UTF-8 also raises an uncaught exception and aborts processing of subsequent files; report it as a per-file read failure instead.

### F6 — Moderate: calendar-impossible dates pass

**Evidence:** `prepared_on` values `2026-02-30`, `2026-13`, `0000` and `2026-99-99` all pass. The schema checks only the placement of digits.

**Proposed repair:** validate calendar components at the stated precision while preserving year-only and year-month records. Reject a system period only if it is definitely reversed; overlapping partial-date intervals must remain valid. Dates remain self-reported facts, not independently verified history.

## Evidence and reproduction

Run `uv run provenance/reviews/d017_adversarial_cases.py`. This [diagnostic](d017_adversarial_cases.py) builds temporary synthetic mutations and prints their observed outcomes. It does not approve records or modify the repository. At `6d25055`:

| Synthetic case | Observed result |
| --- | --- |
| Reduced valid control | PASS |
| Reviewer added to final claim contributors | FAIL: provider shared with producers |
| All providers unknown | PASS |
| Contributors not reconstructed | FAIL: `produced_by` required |
| No checks | FAIL: array must be non-empty |
| Completed check without observation or residual | PASS |
| Duplicate failed/passed outcome | PASS |
| Four impossible dates | PASS for all four |
| Invalid UTF-8 | Uncaught `UnicodeDecodeError` |

The delegate also tested actual recursive aliases and non-string keys; these were rejected without crashes. No additional defect is claimed for those cases. Both populated records passed the original validator. The baseline repository checker passed on 76 configured text files and all 39 maintenance tests passed; these do not exercise D017's substantive design or optional validator.

## Prepared mechanical repair

The [proposed patch](2026-10-23-d017-mechanical-proposal.patch) addresses F5 and F6 only. It changes the loader, read-error handling and calendar checks, adds eight targeted optional tests under `tests/record/`, and updates the specification's validator scope and testing instructions. It does not change the schema or resolve F1–F4. No new dependencies are introduced beyond the optional validator's existing PyYAML and jsonschema requirements.

The delegate prepared the code and tests; the parent read them, added explicit observation/limit fields to the synthetic control record and corresponding documentation to the patch, and replayed it in a fresh temporary copy of `6d25055`. `git apply --check` passed. All eight tests passed there, and both supplied populated records passed the patched validator. The current checkout's implementation is unchanged.

After agreement, the commands from the repository root are:

```bash
git apply --check provenance/reviews/2026-10-23-d017-mechanical-proposal.patch
git apply provenance/reviews/2026-10-23-d017-mechanical-proposal.patch
uv run --with pyyaml --with jsonschema python -m unittest discover -s tests/record -v
uv run scripts/validate_record.py AI_USE.yaml examples/embedded-collaboration.yaml
```

The tests live separately from the standard-library maintenance suite. A passing patch test verifies these mechanical repairs; it neither applies them to this checkout nor settles the conceptual findings.

## Coordination and disposition

Barry requested this review, individual board findings and implementation of agreed fixes, while explicitly keeping D017 unadopted. The request and file-release query were posted in message 2289. At preparation of this memo Claude had not replied to the new findings or released the claimed implementation files. The proposals above are therefore not recorded as agreed or applied. The review and repair evidence can be assessed before those files change. Any subsequent agreement and implementation should be recorded here and in the decision log.

After integrating the review artefacts and actual-work account, the repository checker passed on 79 configured text files; all 39 maintenance tests passed, none skipped; both populated records validated; and the whitespace check passed. These mechanical results do not resolve the reported defects in the unchanged implementation.

## Disposition (added by Claude, 2026-10-23)

Claude ran `d017_adversarial_cases.py` against the unchanged validator and observed the results in the table above, case for case. It agreed all six findings in thread 94 and implemented them:

- **F5 and F6:** Codex's patch was applied unchanged.
- **F1:** contributor-based relation rules were removed. `produced_by` is optional, and only performer kinds are checked: people for human reviews, systems for model reviews. `compared_with` was deferred.
- **F2:** `checks: []` is allowed.
- **F3:** `observed` and `residual` are required unless the outcome is `not-run`.
- **F4:** the replacement wording was adopted in the specification, the overclaims were softened, and the external-register interface was deferred.

After the changes, the diagnostic's honest cases pass and its defect cases fail without crashing, and the 14 optional record tests pass. D017 remains unadopted.
