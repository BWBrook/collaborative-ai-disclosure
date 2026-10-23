# Warrant and independence

**Status.** Section 1 states principle P06, which Barry adopted on 2026-10-23 ([D010](../provenance/decision-log.md)). The adoption covers the proposition only. Everything else here is Claude's operational proposal ([D016](../provenance/decision-log.md)) and has not been adopted. It was revised on 2026-10-23 after Codex's review on the correspondence board (thread 93), which found a misattributed mechanism, an implied ranking of checks, over-transferred evidence and overstated rules. This document replaces the scaffold's verification discussion draft.

## 1. The principle

> **Origin tells you which checks a contribution needs; warrant decides whether it stands.**

*Rationale presented with the proposition (Claude; not part of the adoption).* Confidence in a claim rests on the evidence and reasoning that justify it, not on whether a human or an AI proposed it. Origin still matters epistemically. Generators fail in characteristic ways, so knowing where a contribution came from indicates which failures to look for. Origin matters separately for credit, rights and accountability, which the authorship and responsibility statements handle. On this reading, a workflow-level account of origin ([P01](principles.md)) informs the assessment of warrant rather than competing with it. "The authors reviewed all outputs and accept full responsibility" is a statement of accountability, not evidence about any claim.

## 2. Characteristic failures and checks that target them

The failures listed are typical, not universal, and they change as systems change. Record what was actually checked, not a stereotype of the generator.

| Contribution | Characteristic failures | Checks that can target them | What those checks do not establish |
| --- | --- | --- | --- |
| Literature claim or reference | Fabricated or misattributed citation (a known language-model failure); a real source that does not support the claim; citing from memory or from an abstract | Read the cited passage and match it to the claim; confirm bibliographic identity | That the source is correct, or representative of the literature |
| Code | Logic that is plausible but wrong; silent edge-case errors; tests that share the code's misunderstanding | Known-answer tests; invariants; boundary cases; independent reimplementation | That the scientific model being implemented is correct |
| Numerical result | A pipeline error reproduced faithfully on rerun; non-convergence; dependence on the random seed | Reproduction from archived inputs; convergence and sensitivity checks; an alternative implementation | That the analysis answers the right question |
| Statistical inference | Violated assumptions; an estimand the design cannot identify; analytic flexibility (by human or AI) | Assumption diagnostics; sensitivity analysis; held-out or pre-specified tests; review of the design | Causal identification the design cannot deliver |
| Data found or assembled by an agent | Wrong version; misread schema; undocumented filtering; unclear permissions | Trace to the original source and version; reconcile against published values; check the licence | That the data suit the question or are free of sampling bias |
| Extraction or classification by a model used as an instrument | Systematic misclassification; variation between runs; sensitivity to the prompt | Evaluation against an independently coded reference set; error analysis; repeated runs | Accuracy outside the evaluated domain |
| Interpretation | Overreach; a story fitted after the fact; neglect of alternatives | Explicit competing explanations; effect sizes; consistency with independent evidence; adversarial review | Independent empirical support |
| Prose, figures and formatting | A changed negation, quantifier, axis, scale or unit inside a nominally cosmetic edit; claims drifting from the evidence during revision | Compare the edited text and figures with the evidence and with the outputs that produced them | That the findings are sound |

## 3. What a check can show

### Record the check, not a class

A check contributes what its observed result can discriminate, given the evidence and checks already in hand. To let a reader judge that, record seven things separately:

- **Target:** the failure the check is aimed at.
- **Oracle:** how the expected answer was established, for example an analytic solution, planted parameters, the cited passage, a published value, a prior run, or a reviewer's judgement.
- **Evidence source:** where the evidence came from.
- **Applier:** who or what applied the check.
- **Result:** the outcome, and what was actually observed.
- **Shared pathways:** what the check has in common with the process that produced the work.
- **Residual gap:** what remains unchecked.

A label such as "known-answer test" or "cross-provider review" describes the method. **A label establishes neither independence nor the ability to detect an error.**

### Shared pathways are possible common causes

A check can share a model, a context, a specification, a framing, data or code with the process that produced the thing it checks. Each shared pathway is a route by which one error could pass both. It is a *possible* common cause, not a measured dependence. Where the pathways have not been assessed, say so; "not assessed" differs from "none identified".

Dependence limits what a passing result may be counted as. It does not nullify the check. A check that shares the specification can still detect an arithmetic error that is independent of the specification. A test written by the generator can catch a violated invariant decisively. What a dependent check cannot be counted as is an independent replication, and its pass should not be treated as conclusive about failures it shares with the generator.

"Ability to detect the specified error" is the right everyday phrase. Statistical power or sensitivity should be claimed only where there is an explicit error model and an evaluation behind it. No disclosure should invent a power value for an informal review. The underlying idea, that a test supports a claim to the extent it would probably have detected the error if the error were present, is Mayo's severity requirement ([Mayo 2018](https://assets.cambridge.org/97811076/64647/excerpt/9781107664647_excerpt.pdf)).

### Evidence that dependence cannot be assumed

[Knight and Leveson (1986)](https://doi.org/10.1109/TSE.1986.6312924) tested whether separately developed versions of one program fail independently. They used 27 versions and a million test cases, and coincident failures substantially exceeded what independence predicts. The authors attributed the common faults to misunderstandings of numerical analysis and incomplete case analysis. They found that the faults did *not* arise from ambiguity, inconsistency or deficiency in the specification. Their result is that separate development does not guarantee independent failure, even with a carefully debugged specification.

A flawed brief shared by everyone in a workflow is *our* additional scenario, not their finding. If the human who wrote the brief, or two models reviewing against it, all inherit its mistake, their agreement says nothing about that mistake.

[Kim et al. (2025)](https://arxiv.org/abs/2506.07962) measured error correlation across more than 350 language models. On one leaderboard of multiple-choice items, when two models were both wrong, they chose the same wrong answer about 60% of the time. Correlation was higher between models sharing a provider or an architecture, and it was high among larger, more accurate models even across providers. The 60% figure is conditional agreement on multiple-choice items. It is not the probability that agreement is wrong, and it does not calibrate agreement between two systems reviewing long-form research.

The practical rule is therefore narrower than "agreement is weak evidence". Do not treat agreement between models as independent confirmation; how much it adds in a given task is uncalibrated. Disagreement is a lead to investigate, not evidence that either party is right. A reproduced counterexample, or a contradiction found in a primary source, outweighs either model's vote.

Self-evaluation has its own documented problems. Models recognise and favour their own outputs ([Panickssery et al. 2024](https://arxiv.org/abs/2404.13076)), and self-correction without external feedback does not reliably improve reasoning ([Huang et al. 2024](https://arxiv.org/abs/2310.01798)). Science's established response to dependent error is triangulation: combining approaches whose biases differ, rather than repeating one approach ([Lawlor, Tilling and Davey Smith 2016](https://doi.org/10.1093/ije/dyw314); [Munafò and Davey Smith 2018](https://doi.org/10.1038/d41586-018-01023-3)).

### Examples of methods and their possible shared pathways

This table is unordered. Every row can be strong or weak depending on the claim, the target failure and what is actually shared.

| Method | How the expected answer is set | Possible shared pathways with the generator |
| --- | --- | --- |
| Self-review | The generator's own judgement | Model, context, framing, specification |
| Review by the same model, or another model from the same provider | The reviewer's judgement | Model lineage, training data, usually the brief and framing |
| Review by a model from another provider | The reviewer's judgement | Overlapping training data and post-training tendencies; usually the brief and framing |
| Tests or invariants written by the generator | The generator's statement of what must hold | Model, specification, sometimes code. Can still be decisive for the invariant tested |
| Reproduction: rerunning the archived pipeline | The earlier run | Specification, code, data. Detects missing inputs and environment dependence, not errors in the pipeline |
| Independent reimplementation from the same specification | Agreement between implementations | Specification, data, and any shared misunderstanding; see Knight and Leveson |
| Human review of a summary | The reviewer's judgement of what the summary shows | The summariser's selection and framing |
| Human review of the artefact or primary material | The reviewer's knowledge | Possibly the specification or sampling assumptions, if the reviewer helped set them |
| Known-answer test | An analytic solution, planted parameters or a published value | The specification. If the simulator reuses the code under test, that code too |
| Check against an external source or independent data | The source text or data | Possible training contamination, if the generator has seen the source; shared sampling frames |

## 4. Governance and checks (proposal)

[P03](principles.md) requires that governance mean something substantive: consequential choices must actually be understood and evaluated. This section offers one possible way of describing that work. It is not the definition of governance.

- **Accountability and checking are different.** Humans remain accountable for the claims. Who designed, ran or challenged a given check is a separate question, and any participant may do any of these.
- **Human approval does not make a check independent.** An agent-designed check can be valuable. Approving it does not remove the pathways it shares with the generator.
- **Report grounds and decisions, not presence.** A useful governance account says which consequential choices humans made or overturned, and on what evidence. It does not stop at saying that humans were involved or approved the result.

## 5. Proportionate reporting (proposal)

- **What to report.** Report the checks that bear on the consequential failure modes of the AI-involved work, their results, and the limitations that remain. Say how those limitations constrain the claims.
- **Reporting is separate from sufficiency.** Disclosing what was checked is one obligation. Judging whether the evidence is enough to support a claim is a methodological judgement for authors, reviewers and readers, and no record or schema certifies it.
- **When no adequate check exists,** say so. Then narrow, qualify, defer or withdraw the claim.
- **Scope follows the AI involvement.** A disclosure of bounded language editing need not reconstruct the warrant for every conclusion of the underlying study. It should still cover the failure modes of that editing, which can include a changed negation, quantifier, axis or unit.

## 6. Reporting checks

Some wording to avoid, with what to write instead:

| Avoid | Prefer |
| --- | --- |
| "All AI outputs were reviewed and verified by the authors." | Name the checks: their target, the oracle, the result, and what remains unchecked. For example: "The three central estimates were recovered from simulated data with planted parameters, using a simulator separate from the fitting code. Every literature claim in the Introduction was matched to the cited passage." |
| "Code was independently checked by a second AI model." | "A model from a second provider reproduced the analyses from the same specification. Agreement was confirmed for all reported estimates. Both implementations share the specification and data, so this is not an independent replication." |
| "A separate external review was commissioned." | Say who or what performed it, and what it shares with the main work. A review run in a fresh context by a model from the same family as the lead system is separate, but it is not external in the sense of independent. |
| "The authors take full responsibility for the content." | Keep it, but present it as the accountability statement it is, not as evidence. |

In an extended account, link each consequential claim to its checks using the elements in section 3. The [structured record](structured-record.md) specifies this. The optional [verification record](../templates/verification-record.md) does the same for a single claim.

Several rules carry over from the scaffold:

- Never insert statements about verification automatically.
- AI involvement in checking belongs in the account.
- A passing test is not scientific validation, and rerunning a pipeline reproduces its mistakes.

**Terms.**

- *Verification* asks whether an operation or claim satisfies a specified check.
- *Validation* asks whether a method is fit for its intended use.
- *Warrant* is what the evidence and assumptions justify concluding.

For models of open natural systems, verification and validation in the strict sense cannot be achieved, and confirmation is only partial ([Oreskes et al. 1994](https://doi.org/10.1126/science.263.5147.641)).

## 7. Worked case: this repository

- **The scaffold.** ChatGPT's source checks were made by the same assistant that wrote the summaries. They are recorded as such and await human review.
- **A misattribution caught.** Working from Crossref metadata and search summaries, Claude attributed a shared-specification mechanism to Knight and Leveson. Codex, a system from a different provider, read the paper's sections 6 and 8 in full and found that the authors explicitly reject that mechanism for their experiment. The error was caught because the check reached the primary source, not because a second model disagreed. The correction is recorded on the board (thread 93) and in [AI_USE.yaml](../AI_USE.yaml).
- **Adoption drift caught.** Claude wrote part of this D016 proposal into the adopted text of P03. Codex flagged it as the drift that AGENTS.md forbids, and the P03 text is being restored.
- **P06 itself.** Claude drafted the proposition and the reply option Barry selected. The decision log records this so that readers can weigh the framing.

## 8. Relation to prior work

D016 adapts established ideas for disclosure; it does not propose a new epistemic principle. Those ideas are triangulation across approaches with different bias structures, severe testing, and dependent failure in N-version software. [Nascimento and da Silva (2026)](https://doi.org/10.1007/s43681-026-01330-w) already relate checks to relevant errors in AI-assisted scientific writing. They warn about shared errors across models and about human framing dependence, and they distinguish disclosure from justification. Codex inspected the relevant sections of that paper; Claude has not read it. What this repository may add is a practical representation for disclosures: the structured record and its accompanying narrative. Whether that adds anything beyond existing disclosure schemes is being assessed in the positioning work.

## 9. Open questions

- Is the method vocabulary useful as a controlled list, or should it stay free text?
- Models used as measurement instruments raise questions of method validation. Does the [Methods template](../templates/methods-disclosure.md) cover them?
- How much can a short declaration say about shared pathways and residual gaps without becoming a checklist?
- How should checks that an agent designs and a human only approves be described?
