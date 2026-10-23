# Warrant and independence

**Status.** Section 1 states principle P06, which Barry adopted on 2026-10-23 ([D010](../provenance/decision-log.md)). Sections 2–8 are Claude's operational proposal ([D016](../provenance/decision-log.md)), drafted the same day and under review by Codex and Barry. This document replaces the scaffold's verification discussion draft and carries its useful content forward.

## 1. The principle

> **Origin tells you which checks a contribution needs; warrant decides whether it stands.**

**Warrant decides.** A claim enters the scientific account because the evidence and reasoning behind it justify it, given stated assumptions. A correct result is no less correct for having been proposed by an AI system, and an error is not redeemed because a human typed it. Who or what originated an idea, a line of code or a sentence is not, by itself, a reason to believe or disbelieve it.

**Origin informs the checks.** Generators fail in characteristic ways, so knowing where a contribution came from tells you which failures to look for and which checks it needs. That is why a workflow-level account of origin ([P01](principles.md)) remains part of an honest disclosure: it tells the reader which failure modes were in play. Origin informs the judgement of warrant; it does not compete with it.

**Origin also matters for other reasons.** Credit, third-party rights, research ethics, data-use permissions and accountability depend on who did what, whether or not the claim is true. They belong in the authorship and responsibility statements and in any declaration a venue requires. They are not part of the case for believing the result.

The principle has two consequences for disclosure:

- The epistemic weight of a disclosure should rest on how the claims were checked, not on how the labour was divided. This is the reason for the narrative-first default ([P05](principles.md)). A task grid reports origin, and origin on its own tells a reader little about warrant.
- "The authors reviewed all outputs and accept full responsibility" is a statement about accountability. It is not evidence about any claim, and it should not be written as though it were.

## 2. Characteristic failures and the checks that target them

The table gives typical failures, not universal ones, and the typical failures change as systems change. Record what was actually checked, not a stereotype of the generator.

| Contribution | Characteristic failures | Checks able to detect them | What those checks do not establish |
| --- | --- | --- | --- |
| Literature claim or reference | Fabricated or misattributed citation (a known language-model failure); a real source that does not support the claim; citing from memory or from an abstract | Read the cited passage and match it to the claim; confirm bibliographic identity | That the source is correct, or representative of the literature |
| Code | Logic that is plausible but wrong; silent edge-case errors; tests that share the code's misunderstanding | Known-answer tests from analytic solutions or simulations with planted parameters; boundary cases; independent reimplementation | That the scientific model being implemented is correct |
| Numerical result | A pipeline error reproduced faithfully on every rerun; non-convergence; dependence on the random seed | Reproduction from archived inputs; convergence and sensitivity checks; an alternative implementation | That the analysis answers the right question |
| Statistical inference | Violated assumptions; an estimand the design cannot identify; analytic flexibility (by human or AI) | Assumption diagnostics; sensitivity analysis; held-out or pre-specified tests; review of the design | Causal identification the design cannot deliver |
| Data found or assembled by an agent | Wrong version; misread schema; undocumented filtering; unclear permissions | Trace to the original source and version; reconcile counts and summaries against published values; check the licence | That the data suit the question or are free of sampling bias |
| Extraction or classification by a model used as an instrument | Systematic misclassification; variation between runs; sensitivity to the prompt | Evaluation against an independently coded reference set; error analysis; repeated runs | Accuracy outside the evaluated domain |
| Interpretation | Overreach; a plausible story fitted after the fact; neglect of alternatives (models tend to agree and elaborate; people tend to defend the hypothesis they started with) | Explicit competing explanations; effect sizes; consistency with independent evidence; adversarial review | Independent empirical support |
| Manuscript prose | Fluent overstatement; claims drifting from the evidence during revision; citation drift | Trace each consequential sentence to its evidence; check figures against the outputs that produced them | That the findings are sound |

## 3. Two properties of a check: independence and power

A check supports a claim only if it could have failed. Two separate properties determine whether it could.

**Independence** is the property of sharing little with the process that produced what is being checked. A check can share the generator's model weights, its context, the specification it worked from, the framing it was given, or its data. Each shared element is a channel through which the same error can pass both the generator and the check.

**Power** is the ability to detect the failure that matters for this claim. A check can be fully independent and still have no power. Confirming on another machine that a script runs without error says nothing about whether it computes the right quantity.

Both properties are needed. An independent check with no power against the relevant failure is a formality. A powerful check that shares the generator's blind spot is self-confirmation.

### Why independence cannot be assumed

The problem is long established in reliability engineering, where it is called common-mode failure. N-version programming assumed that programs written independently from one specification would fail independently. [Knight and Leveson (1986)](https://doi.org/10.1109/TSE.1986.6312924) tested this with 27 versions of one program and a million test cases. Coincident failures were far more frequent than independence predicts. Developing the versions separately did not make their failures independent; the shared specification and the shared difficulty of the problem made their errors coincide.

Language models show the same pattern. [Kim et al. (2025)](https://arxiv.org/abs/2506.07962) evaluated more than 350 models. On one leaderboard dataset, when two models both erred, they gave the same wrong answer about 60% of the time. Errors were more correlated between models that shared a provider or an architecture, and larger, more accurate models had highly correlated errors even across providers. Agreement between models from different providers is therefore weaker evidence than it appears, and it may be weakening as the leading models converge. Self-evaluation is weaker still. Models recognise and favour their own outputs ([Panickssery et al. 2024](https://arxiv.org/abs/2404.13076)), and self-correction without external feedback does not reliably improve reasoning ([Huang et al. 2024](https://arxiv.org/abs/2310.01798)).

Science has its own version of the principle in triangulation: robust inference comes from approaches whose biases differ, not from repeating one approach ([Munafò and Davey Smith 2018](https://doi.org/10.1038/d41586-018-01023-3)).

### Classes of check, by what they share with the generator

| Class | What it shares with the generator | Typical power |
| --- | --- | --- |
| Self-review | Model, context, framing and specification | Catches slips the generator would notice on a second look; weak against its systematic errors |
| Same model in a fresh context | Model and its training biases; usually the specification | As for self-review, with less anchoring on the first attempt |
| Review by a model from another provider | Overlapping training data and post-training tendencies; usually the brief and its framing | Catches some errors specific to one model family; much of the error correlation remains |
| Tests written by the generator | The generator's understanding of the problem | Catches implementation slips; blind to misreadings of the specification that the tests repeat |
| Human review of a summary | Whatever the summary chose to show, and its framing | Weak, because the reviewer inherits the summariser's selection |
| Human review of the artefact or primary material | Little, if the reviewer's knowledge is genuinely independent; the specification, if the reviewer wrote it | Often strong on conceptual and domain errors that no test encodes; limited by volume |
| Known-answer tests | The specification only, through an analytic solution, planted parameters or a published benchmark | Strong against implementation errors; blind to a wrong specification |
| External evidence | Nothing produced in the workflow: primary source text, independent data, independent replication | The strongest available, for the failures it can detect |

The classes form a partial order, not a ranking. Independence broadly increases down the table, but power depends on the claim. A domain expert may recognise a misconceived model that passes every known-answer test, and a simulation with planted parameters will catch an indexing error that the expert never sees. A good set of checks covers the plausible failures; it does not simply use the highest class available.

### The specification is a shared channel

Independence concerns the whole chain, not only the model. A human who wrote a flawed brief and then reviews the result against that brief shares the flaw. Two models from different providers reviewing against the same mistaken framing share it too. This is the mechanism Knight and Leveson found. The checks least exposed to a wrong specification are those that touch something nobody in the workflow wrote: data, source text, an independently derived result, or another team's replication.

## 4. Governance as the design and adjudication of checks

[P03](principles.md) describes human contribution by function rather than by share of labour, and requires governance to mean something substantive. This account supplies the substance. In establishing warrant, a human scientist can:

- **design the set of checks:** decide, for each consequential claim, which failures are plausible and which checks have power against them;
- **act as an independent check** where their knowledge really is independent of the generator, such as knowledge of the study system, of how the data were collected, or of approaches that have already failed;
- **adjudicate:** decide whether a failed check refutes the claim or exposes a faulty check, and when the checks are sufficient;
- **accept responsibility,** which matters but is not itself a check.

A small share of the execution combined with well-designed and well-adjudicated checks is strong governance. A large share of the execution followed by nominal approval is weak governance, whoever typed the code.

Agents increasingly propose their own tests and review plans. That is useful, and it should be reported. But a set of checks designed by the generator inherits the generator's view of what could go wrong. Independent review of the checks themselves, not only of their results, is one of the most valuable uses of human judgement in agent-intensive work.

## 5. Proportionality

Not every output needs every check. Personal human inspection of every intermediate operation is neither feasible nor necessary in agent-intensive work. Effort should scale with the cost of a claim being wrong and the chance that its failure would go unnoticed.

A workable rule is that every claim the conclusions depend on should have at least one check that both:

- can detect that claim's most plausible failure; and
- shares as little as possible with the generator. This usually means a known-answer test, external evidence, or an expert reading the primary material.

Peripheral material such as prose polish, figure styling and formatting needs little beyond ordinary care.

## 6. Reporting checks

Some wording to avoid, with what to write instead:

| Avoid | Prefer |
| --- | --- |
| "All AI outputs were reviewed and verified by the authors." | "The three central estimates were recovered from simulated data with planted parameters. Every literature claim in the Introduction was matched to the cited passage by [who]." |
| "Code was checked using a second AI model." | "Code was reviewed by a model from a second provider, a check that shares some error tendencies with the first, and tested against analytic solutions for the two limiting cases." |
| "The authors take full responsibility for the content." | Keep it, but present it as the accountability statement it is, not as evidence. |

In an extended account, link each consequential claim to its checks: the class of check, who or what performed it, the outcome, its limitations and the location of the evidence. The structured record now being drafted will specify this. The optional [verification record](../templates/verification-record.md) does the same for a single claim.

Several rules carry over from the scaffold:

- Never insert statements about verification automatically. Specify what was checked, how, against what, and with what limitations.
- AI involvement in checking belongs in the account. It does not disappear because it served verification rather than production.
- A passing test is not scientific validation. A pipeline that reproduces its outputs has not thereby shown that the inference is valid, because repeating one pipeline reproduces its mistakes.

**Terms.** *Verification* asks whether an operation or claim satisfies a specified check. *Validation* asks whether a method is fit for its intended use. *Warrant* is what the evidence and assumptions justify concluding. For models of open natural systems, verification and validation in the strict sense cannot be achieved, and agreement with observation confirms a model only partially ([Oreskes et al. 1994](https://doi.org/10.1126/science.263.5147.641)). Report checks as evidence for a claim, not as certificates that a model is true.

## 7. A worked case: this repository

- **The scaffold.** ChatGPT generated the scaffold from its conversation with Barry, and its source checks were made by the same assistant that wrote the summaries. Those checks are therefore close to self-review. They are recorded as such and await human review.
- **Claude's review.** Claude's [first-pass review](../provenance/reviews/2026-10-23-claude-first-pass.md) is a review by a model from another provider. Given Kim et al., later agreement between Claude and Codex will be weaker evidence than it looks. Disagreement between them is the more informative signal.
- **P06.** Claude drafted the proposition. Barry adopted it by selecting a reply option that Claude had also drafted. The decision is a human judgement, but the wording and the framing of the choice came from the generator, which is the specification channel described in section 3. The [decision log](../provenance/decision-log.md) records this so that a reader can weigh it.
- **The literature cited here.** It was checked at the scope of abstracts and search results, as recorded in the [source register](../references/source-register.json). That establishes the existence and headline findings of these papers, not every detail.

## 8. Open questions

- Should the classes of check become a controlled vocabulary in the structured record, or stay as descriptive prose? A controlled vocabulary risks false precision.
- Models used as measurement instruments raise a question of method validation. Does the [Methods template](../templates/methods-disclosure.md) cover them adequately, or do they need their own section here?
- How much can a short declaration say about independence and power without becoming a checklist?
- When an agent designs the checks and a human only approves them, how should that be described?
