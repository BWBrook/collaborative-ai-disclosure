# First-pass review of the scaffold (Claude, 23 October 2026)

**Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), in Claude Code on Barry's WSL laptop, at Barry's request: "have a first pass at it and see what you think".
**Read:** every prose file in the repository, the policy and source registers, and the issue seeds. **Ran:** `check_repo.py` (pass), the 46 unit tests (pass), `sha256sum -c MANIFEST.sha256` (all match). **Prior-art search:** five web searches and one arXiv abstract on 23 October 2026. Nothing listed in section 6 has been read in full.
**Status:** proposals for Barry and Codex to contest. Nothing here changes an established direction in the [decision log](../decision-log.md).

## Verdict

The scaffold preserves Barry's five commitments faithfully and is careful about provenance. In its current form it is guidance on writing a disclosure carefully. It does not yet formalise disclosure. It answers the problems of task attribution with "write a narrative", but it gives the narrative no required structure. Two honest authors would therefore produce statements a reader cannot compare, and a dishonest author would produce nothing that can be checked. The unanswered topic 6 carries the weight of the whole framework: until it is settled, the framework cannot say what a disclosure is for. A proposed answer follows.

## 1. Disclosure does two jobs, and the field conflates them

**The epistemic job** is to help a reader decide how far to trust the claims. **The social job** is to settle credit, accountability, rights and community norms. Task-attribution schemes descended from CRediT serve the social job and are presented as if they also served the epistemic one. Learning that "AI drafted the Discussion" tells a reader almost nothing about whether the Discussion is right.

Barry's objection to task grids in topic 5 makes this point: such grids do the epistemic job badly, and they distort practice. They encourage people to reserve tasks for humans artificially, or to describe the work strategically. The framework should say so outright. Narrative-first would then rest on a stated reason rather than a preference.

## 2. A proposed answer to topic 6

> **Origin tells you which checks a contribution needs; warrant decides whether it stands.**

- Confidence in a claim rests on its warrant, not its origin. A correct result is no less correct for having come from an AI, and a wrong one is not rescued because a human typed it.
- Origin still matters epistemically, because different generators fail in characteristic ways. Language models fabricate or misattribute citations, write code that is plausible but wrong, and overreach in interpretation. Humans show motivated reasoning, anchoring on sunk effort, and blind spots inherited from their field. Origin sets the prior over failure modes and therefore determines which checks are necessary. This is why a workflow-level account of origin belongs in a disclosure: it serves the assessment of warrant rather than competing with it.
- Origin matters separately for the social job: credit, third-party rights and accountability. The authorship and responsibility statement handles that job. The epistemic part of the disclosure should not.

This keeps faith with Barry's rejection of legitimacy through human task performance, and it gives P03 (governance by function) something substantive to rest on (section 3).

## 3. The formal core: how independent are the checks?

The [verification draft](../../docs/verification-and-assurance.md) says correctly that a second model's agreement is not independent validation, but it offers no general account of why. I propose borrowing the idea of **common-mode failure** from reliability engineering. A check is informative to the extent that its failure modes are uncorrelated with those of the process that produced what it checks. This gives an ordering based on what a check shares with the generator, not on who performed it:

| Check | Shared with the generator | Decorrelation |
| --- | --- | --- |
| Same agent re-reads its own output in the same context | Context, weights, framing | Minimal |
| Same model, fresh context | Weights, training biases | Low |
| Different model lineage (for example Claude reviewing Codex/GPT) | Overlapping training corpora, similar post-training tendencies | Partial |
| Tests written by the same agent that wrote the code | The agent's understanding of the problem | Partial |
| Human expert review of the artefact itself | Little if the expert reads the primary material; much if they read only the AI's summary | Varies; often high on domain knowledge |
| Known-answer tests derived from theory, literature or simulation with planted truth | Only the specification | High |
| Contact with external reality: the primary source text, independent data, an analytical solution, replication | Nothing generated | Highest |

Three consequences follow.

1. **Governance gains content without a labour share.** In the chain of warrant, the human's role is not "approval". It is to choose the regime of checks a claim needs, to be one decorrelated check among others where their knowledge is genuinely independent, and to rule on failures. A low share of execution with a well-designed regime of checks is strong governance. A high share of execution followed by nominal sign-off is weak.
2. **Verification theatre becomes detectable.** "All outputs were reviewed" says nothing about the classes of check involved. "The three central effect estimates were reproduced from simulated data with planted parameters, and every cited claim in the Introduction was matched to the source passage" says something specific, and anyone can falsify it.
3. **Multi-agent practice is described accurately.** Claude and Codex agreeing is a cross-lineage check with partial decorrelation. It is useful, but it is not independent validation. This repository is now developed in exactly that configuration, so the claim can be tested here.

## 4. What formalisation should mean here

Barry's word for the project was *formalisation*. The scaffold defers every structured layer: AGENTS.md says "no elaborate form system by default", and HANDOVER.md says "no scoring system, declaration wizard … before there is an agreed need". That deferral was a choice ChatGPT made in the scaffold, not a founding decision. The [founding discussion](../founding-discussion.md) records that no structured profile was *agreed*, not that one was rejected.

A formal layer is fully compatible with D001–D007 if it **formalises facts and links to evidence, never shares of labour**. A sketch follows, as a small YAML record beside or inside `AI_USE.md`:

```yaml
systems:            # one entry per product/model/period; "not recorded" is a valid value
  - product: Codex
    provider: OpenAI
    model: not recorded
    period: 2026-03/2026-08
    record: compaction summary     # original export | partial export | compaction summary | reconstruction | none
relationship:
  predominant: embedded collaboration
  secondary: [{mode: delegated problem-solving, phase: simulation study}]
records:
  clean_release: {status: present, location: <DOI or tag>}
  development_history: {status: present, location: <repo>, access: public}
  deliberative_record: {status: partial, access: on request, note: early threads lost}
claims:             # the 3–10 consequential claims of the paper, not every output
  - claim: <the central quantitative result>
    checks:
      - {kind: known-answer simulation, independence: high, by: Codex + human design, outcome: pass, evidence: <path>}
      - {kind: cross-lineage review, independence: partial, by: Claude, outcome: two issues fixed, evidence: <board thread>}
    limits: <what the checks cannot establish>
gaps: [<known missing records or unrun checks>]
```

The narrative stays primary for describing the relationship. The structured layer carries the facts that a reader or a tool should be able to query and a reviewer should be able to falsify. The table linking claims to checks earns its place: it replaces the boilerplate "the authors reviewed all outputs and take full responsibility", which no one can falsify, with specific assertions anyone can check.

Two risks need watching. The claims table could become verification theatre with extra steps, and it could become a burden that only well-resourced groups complete. It should be limited to consequential claims and remain optional for bounded assistance. This also strains the AGENTS.md rule against "elaborate form systems", so I am proposing it rather than implementing it.

## 5. Two axes are hidden in the four modes

The four modes vary along at least two separable dimensions:

- **Origin of the research question:** specified by a human, set by a broad human brief, or originated by an agent.
- **Density of human intervention during execution:** continuous, at checkpoints, or only at the end.

Assistance and governed collaboration differ mainly in the breadth of AI participation. Delegated problem-solving and agent-led exploration differ mainly in where the question came from. Naming the axes creates no score. It gives every narrative two questions it must answer, and it lets a mixed project be described without inventing a fifth mode.

Two further problems:

- **"Governed" builds the conclusion into the label.** The scaffold itself says governance has to be substantiated. A neutral name such as "embedded human–AI collaboration" would let the narrative and the checks demonstrate the governance rather than assert it.
- **The modes treat AI as a single counterparty.** Barry's current practice involves several AI systems from different lineages with distinct roles: Codex and Claude cross-reviewing on a shared board, with Barry ruling on disputes. The framework needs to describe several systems with differentiated roles, and that connects directly to section 3.

## 6. Prior art the scaffold does not engage

The scaffold cites Cwik (2026), AIdIT (abstract only) and Park (2025). It omits the CRediT-derived family of task taxonomies, which is the obvious foil for a narrative-first approach, and several recent proposals centred on provenance. All entries below are at **search-result evidence scope** unless marked otherwise:

- **GAIDeT**, the Generative AI Delegation Taxonomy (Nazarovets, Tsybuliak, Teixeira da Silva, Suchikova; *Accountability in Research*). A task-by-stage checklist with a generator at aidisclose.org and a LaTeX package, `aidisclose`.
- **The AID Framework** (Weaver; *C&RL News* 85(10), 2024; arXiv:2408.01904). Modelled on CRediT and organised by writing activity.
- **AI Usage Cards** (Wahle, Ruas, Mohammad, Meuschke and Gipp; arXiv:2303.03886, 2023). Includes a field for how outputs were verified.
- **CANGARU** (Cacciamani et al.; protocol arXiv:2307.08974). A Delphi consensus process with publishers and COPE. Whether final guidelines have been published was not established.
- **Recent proposals centred on provenance:** "Provenance, Not Prohibition" (a 2026 commentary indexed in PubMed; the page could not be retrieved); PROV-AGENT (an extension of W3C PROV to agent workflows); and Tiltack et al., arXiv:2609.17631 (2026), on falsifiable publication records. The abstract of the last was read. It is a heavyweight protocol verified by model checking, and its abstract does not address origin or the independence of checks.

The framework should state its position explicitly. Those schemes answer *which tasks were delegated*. This one answers *what the relationship was and how the claims were warranted*. Section 3 appears to be the distinctive contribution, though that needs a proper search before it is claimed.

## 7. The scaffold as an artefact

- **Too many caveats.** Nearly every document opens with a status disclaimer and repeats "proposal, not endorsed, pending human review". The substance is correct, but the repetition buries the framework and reads as defensive to an outside contributor. Status should be kept in the decision log, with a one-line status per document.
- **Too much infrastructure for the content.** The repository carries `MANIFEST.sha256`, `package_repo.py`, `START_HERE.md` (instructions for extracting a ZIP), `qa/BOOTSTRAP_REPORT.md` and a 14 KB test suite, for roughly 25 prose files. Git now supersedes the manifest and the packager. I recommend deleting the packager, the manifest and `START_HERE.md`, moving the bootstrap report into `provenance/`, and cutting the checks down to links and JSON validity.
- **Every example is fictional.** One real example, used with Barry's permission, would be worth all three. Several of his papers already have records on the shared board. This repository is the obvious first real case, so its own `AI_USE.md` should become the flagship example.
- **The templates' "checks" slot** is exactly where boilerplate returns. It should be tied to the record of claims and checks.

## Proposed next tranche

1. Barry: accept, amend or reject the proposition in section 2. This is a single question.
2. Draft `docs/warrant-and-independence.md` (sections 2–3) and a minimal specification of the structured record (section 4). Codex should attack both.
3. Prune the scaffold infrastructure and consolidate the status disclaimers.
4. Read GAIDeT, AID, AI Usage Cards, CANGARU, the full text of Cwik and the full text of AIdIT. Add them to the source register and write a positioning section.
5. Test the framework on itself: rewrite this repository's `AI_USE.md` in the new form, then draft one of Barry's papers as a real worked example. Keep that example local until he approves it.

Codex and Claude will agree on file ownership on the correspondence board before editing shared files.
