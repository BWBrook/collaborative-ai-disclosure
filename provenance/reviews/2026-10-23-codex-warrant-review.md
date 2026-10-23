# Review of the proposed warrant account (Codex, 23 October 2026)

**Scope:** sections 2–8 of `docs/warrant-and-independence.md` as committed in `832da27`, with the linked principles and decision log. Section 1's adopted proposition was not reopened. **Reviewer:** Codex; the environment describes the model as GPT-6 but does not expose a finer deployment identifier. This review combines conceptual counterexamples with selected primary-source inspection. It is not independent scientific validation, a complete literature review or founder adoption.

**Recommendation on the reviewed version:** revise the operational proposal before considering adoption. The central distinction between origin and warrant survives these objections; the proposed ordering and sufficiency rule do not. Findings were posted individually in Correspondence thread 93 (messages 2265–2271 and 2275). Claude retains ownership of the warrant draft and structured-record specification.

**Disposition later the same day:** Claude accepted all eight findings and revised the draft in `467f2d5` and `dbd299a`. Codex read the revised warrant text and confirmed the substantive corrections, including adverse-check reporting and the narrower source-inspection scope. The original findings below are preserved as a review of `832da27`, not a list of defects still present. The P03/P06 adoption-boundary repair accompanies this memo. Agreement on these repairs does not adopt D016, validate the framework or constitute review of the new D017 specification.

## Findings

### 1. Major: the Knight–Leveson attribution is wrong

Section 3 attributes coincident failures to a flawed shared specification as though this were the mechanism established by [Knight and Leveson](https://people.cs.rutgers.edu/~uli/cs673/papers/EvaluationMultiVersionProgramming86.pdf). Their sections 6 and 8 instead discuss numerical misunderstandings and incomplete case analysis, and reject specification deficiencies as an explanation for their observed common faults. Separately developed programs failed dependently even with a carefully prepared specification.

Keep that result. Present a flawed common brief as a further possible failure pathway, without attributing it to this experiment. Problem difficulty is a proposed explanation in their discussion, not an experimentally isolated mechanism. Claude accepted this correction in message 2272.

### 2. Major: the table does not establish a partial order

The phrases “independence broadly increases”, “the specification only” and “nothing produced in the workflow” give classes unwarranted guarantees. A benchmark can be training-contaminated; a simulator can reuse the likelihood code's error; an external reviewer can share the same sampling assumptions. A generator-written invariant can still expose a decisive counterexample.

Use unordered examples. For each actual check distinguish the evidence source, the performer, the basis for its expected answer, its targeted error and possible shared failure pathways. Record what is unknown. A label describes a method; it does not measure independence or error detection. Claude accepted this restructuring in message 2273. The remaining wording should say that shared elements **can** create common error pathways, rather than assuming every shared element carries the relevant error.

### 3. Major: dependence limits evidence without making every check worthless

Section 3's requirement for both independence and power suggests a binary gate. Dependent checks may still distinguish some errors from correct results. A test can share a specification while checking arithmetic conditional on that specification; it cannot then establish that the specification answers the scientific question. Conversely, an indiscriminate check that always fails detects all errors but is uninformative.

The useful question is what the observed result adds to the evidence already available. Describe the error a check could detect and the conditions under which it could do so. Reserve numerical power or sensitivity for a defined error model and evaluation; an informal review does not acquire measured operating characteristics from its label.

### 4. Major: close intellectual precedents already exist

[Nascimento and da Silva (2026)](https://doi.org/10.1007/s43681-026-01330-w), especially sections 3.2–4.1 and 5, already apply independent and proportionate verification to AI-assisted scientific writing. Their account addresses relevant error detection, shared model errors, framing dependence and the difference between disclosure and justification. This is a close normative precedent, not an empirical demonstration that their proposed criteria work.

Earlier foundations include [Lawlor, Tilling and Davey Smith](https://doi.org/10.1093/ije/dyw314) on triangulation across bias structures and [Mayo's severe-testing account](https://assets.cambridge.org/97811076/64647/excerpt/9781107664647_excerpt.pdf) on methods' capacity to expose error. The inspected scopes are listed below. D016 should be presented as a practical adaptation and synthesis. The accompanying [positioning discussion](../../docs/positioning.md) compares the disclosure frameworks; no conceptual priority or exhaustive novelty claim is established.

### 5. Major: one check is neither sufficient assurance nor a universal reporting prerequisite

Section 5 can be satisfied by a good implementation check while a conclusion remains vulnerable to sampling bias or non-identification. Selecting only the most plausible failure neglects less frequent but consequential errors. In the other direction, bounded language editing does not justify demanding a new assurance case for every scientific conclusion in the paper.

Separate truthful reporting from a judgement that evidence is sufficient. The record must accommodate missing checks, adverse evidence and unresolved limits. Where these undermine a claim, narrow or qualify it, seek further evidence, or withhold it. Proportionality should concern scientific consequences, including changes to meaning introduced through apparently cosmetic prose or figure edits.

### 6. Major: the proposed governance mechanism leaked into adopted prose

P03 said that P06 gives governance its substance through designing checks, acting as an independent check and ruling on failures. D010 adopted only the origin/warrant proposition. This operational account belongs to D016.

The narrow repair in `docs/principles.md` retains the established requirement for substantive evaluation and identifies the operational account as a proposal. Section 4 should distinguish accountability from the performance of checks: agents may design or apply effective checks, while human presence or approval does not itself establish their epistemic value. This repair preserves the adoption boundary; it adopts no replacement governance criterion.

### 7. Moderate: Kim et al. do not calibrate this collaboration

[Kim et al., arXiv v1](https://arxiv.org/html/2506.07962v1), report agreement conditional on both models answering incorrectly, including a mean of 0.60 on HELM. This is not the probability that an agreed answer is incorrect. Sections 4 and 6 discuss calibration and limitations of their tasks and measures. Their study does not estimate the incremental value of this project's 2026 long-form reviews.

Avoid interpreting agreement as independent confirmation. Treat disagreement as a lead for investigation, not proof that either reviewer is right. The substantive evidence in finding 1 is the primary text contradicting the draft, not the difference between model names.

### 8. Moderate: favourable-check selection remains possible

Section 6 should require material adverse checks and their disposition where needed to interpret the current claim. Reporting only successful checks can mislead even when every reported sentence is true. Changes to a test after seeing its result also matter when they affect evidential interpretation. This does not require an exhaustive historical transcript.

The simulation example needs narrower wording: recovery of planted parameters evaluates an estimator under the simulated scenarios. It does not independently validate the empirical estimates or the fit of the scientific model to the world.

## Replacement wording offered for discussion

For section 3:

> Assess a check in relation to the claim and the error it targets. Describe where its evidence came from, how its expected result was established, who or what applied it, and what happened. Identify shared assumptions or processes that could let the same error survive generation and checking, including what is not known about those dependencies. A dependent check may still detect particular errors; its result should not be counted as an independent replication. The method's name alone establishes neither its independence nor its ability to detect error.

For section 5:

> Report the consequential AI involvement and the checks actually applied to it, with evidence and limitations proportionate to the scientific consequences. Explain which important failures the checks address, which remain unresolved, and how those limits affect the claims advanced. A disclosure may faithfully describe inadequate checking; completing it does not establish adequate warrant. Bounded assistance may need only a short account, provided changes to scientific meaning receive appropriate scrutiny.

These are Codex's proposed replacements, not adopted principles or agreed minimum requirements.

## Evidence scope and continuity

| Source | Actually inspected for this review |
| --- | --- |
| Knight and Leveson (1986) | Selected manuscript text: abstract, introduction excerpts, section 6 examples and section 8 conclusions, especially printed pp. 16–17 and 19–21. Not the full specification appendix or experimental replay. |
| Kim et al. (2025) | arXiv v1 abstract, sections 1, 3–4, relevant 5.2 results and section 6. Not a complete appendix reading or code/data replay. |
| Nascimento and da Silva (2026) | Publisher HTML abstract, sections 1–4.1 and section 5 passages; table caption but not full Table 1. Not the complete article. |
| Lawlor et al. (2016 issue; online 2017) | Publisher metadata, abstract and introduction passages. Later retrieval failed; full article and examples not read. |
| Mayo (2018) | Publisher excerpt, opening discussion and section 1.1 (printed pp. 3–5). Not the full excerpt or book. |

The [source register](../../references/source-register.json) retains the earlier inspection histories and these updates. A search lead for *RSI for Science: A Verifier-First Framework for AI Scientists* led to an OpenReview browser challenge; its text was not inspected and is not evidence for the findings above.

The original repository checker and 46 maintenance tests passed before editing. Subsequent mechanical verification and the maintenance changes belong in the handover and changelog; they do not test the truth of this review. No publisher-policy refresh, independent human source review or evaluation of disclosure usability was performed in this tranche. Further adjudication belongs on the board; only Barry can adopt an unresolved conceptual proposal.
