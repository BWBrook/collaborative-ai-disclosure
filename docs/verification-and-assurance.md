# Verification and scientific assurance: discussion draft

**Status: unresolved topic 6.** Barry had not answered the verification question when he requested this repository. All recommendations in this document are proposals for criticism and refinement, not an agreed principle or a claim that these checks occurred in his projects.

## The question to resume

> Should the way a candidate contribution becomes warranted matter more to confidence in the scientific result than whether that contribution originated with a human or an AI?

This question does not imply that origin ceases to matter. Attribution, third-party rights, research ethics, restrictions on data use and the interpretability of a method can make provenance independently consequential. Verification and disclosure address related but distinct questions.

## A possible distinction

A candidate contribution can be proposed by a human, an AI, or the interaction between them. Its inclusion in the final scientific account should have an articulable basis. That basis might involve evidence, mathematical argument, empirical evaluation, methodological knowledge, or disciplinary interpretation—not merely the confidence of the speaker.

Three words should not be collapsed:

**Verification** asks whether a particular operation or claim satisfies a specified check. **Validation** asks whether a method or representation is suitable for its intended use. **Scientific warrant** concerns what the evidence and assumptions justify concluding. These are working definitions for this repository, not a claim to prescribe universal disciplinary terminology.

## Candidate evidence practices

| Contribution | Potentially informative evidence | What it would not establish alone |
| --- | --- | --- |
| Reference or literature claim | Inspect the actual source; match the passage to the claim; check bibliographic identity | A reference existing does not show it supports the statement |
| Discovered dataset | Document the original source, version, permission and relevant sampling process | Availability does not establish suitability or freedom from bias |
| Code | Execute tests; use known-answer cases; inspect boundary conditions and expected invariants | Code running does not establish correctness of the scientific model |
| Numerical result | Reproduce outputs; assess convergence; compare alternative implementations where meaningful | Repetition of one pipeline can reproduce the same mistake |
| Statistical inference | Examine assumptions, uncertainty, sensitivity and the relation of design to claim | Good diagnostics do not cure an unidentified causal estimand or invalid design |
| Literature-derived extraction or classification | Evaluate against an appropriate reference set; inspect errors and uncertainty | Agreement with another model is not equivalent to accuracy |
| Interpretation | Test competing explanations; assess effect size and external consistency; document limitations | A plausible story is not independent empirical support |
| Manuscript | Link consequential claims to evidence; inspect argument, citations and figures | Fluent prose is not evidence that the findings are sound |

These are candidate questions, not a mandatory ownership taxonomy or a promise that every discipline can apply identical tests.

## Avoid verification theatre

Statements such as “all outputs were independently checked” are consequential claims about the process. They must not be inserted automatically. Specify what was checked, by what means, against what evidence, and with what known limitations.

AI can assist with checks as well as production. That assistance should not disappear from the account. A second pass by the same model is a second pass, not automatically independent validation. A review by another model or provider can supply useful criticism, but agreement alone does not establish independence or correctness. Independence must be supported by the design of the check and its evidence, not merely the brand name.

Not every intermediate operation necessarily needs personal human inspection. A defensible assurance strategy may combine automated tests, targeted review, sampling, benchmark cases, source inspection and independent analyses. Whether that is adequate depends on the consequential claims and the risk of undetected failure. This proportionality proposal needs explicit discussion rather than being adopted silently.

## Governance with substance

A possible account would identify who evaluated consequential choices and what evidence they considered, while allowing the agent to perform most execution. It should remain possible to report unresolved questions, incomplete tests, non-reproducible dependencies and uncertainty about an interpretation.

A promise to accept responsibility is not an empirical check. Conversely, an automated test is not a person capable of accepting responsibility. The framework needs to preserve both ideas without pretending they are interchangeable.

## Practical draft record

The optional [verification record](../templates/verification-record.md) ties one consequential claim or artifact to actual checks and their limitations. It is not intended as a compulsory table for every output or as a gatekeeping score.

## Open questions for the next discussion

The immediate question is the balance between source attribution and evidential warrant. Later questions include what oversight suffices under extensive delegation, how to disclose AI-assisted checking, how to distinguish independent evidence from repeated model opinion, and how much evidence a short declaration should point to.
