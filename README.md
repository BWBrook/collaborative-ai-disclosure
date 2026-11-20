# Collaborative AI Research Disclosure

**Describe how the science was done—not an artificial division of who wrote which words.**

A draft, narrative-first framework for describing human–AI collaboration in research, with adaptable declaration templates, provenance guidance, and a source-backed policy register.

**Status: `0.1.0-draft`, public but not yet released (no tagged version).** The [decision log](provenance/decision-log.md) distinguishes adopted direction from proposals under development. The working repository name is `collaborative-ai-disclosure`.

## Why this exists

A research project may develop through months of intertwined discussion, coding, testing, criticism, abandoned approaches, reinterpretation and writing, sometimes involving successive AI models. In such a workflow, assigning ownership to each idea, sentence or line of code can be misleading. Yet a generic statement that AI “helped with writing” can conceal substantive involvement.

This project aims to make that process understandable without inventing clean boundaries, inflating human review, or asking researchers to reorganise productive work to fit a disclosure form. It accommodates bounded assistance as well as deeply embedded collaboration. It does not require researchers to adopt a particular philosophy of AI agency.

## The emerging framework

The founding discussion established five working design commitments:

1. **Workflow-level disclosure, with finer provenance where practicable.** A clean research release, development history and deliberative record serve different purposes.
2. **Accurate language for actual participation.** “Collaboration” can describe substantive intellectual interaction without assigning formal authorship or accountability to AI.
3. **Governance is not a labour percentage.** Scientific direction and judgement cannot be inferred from keystrokes, elapsed hours or a 50% threshold.
4. **Predominant mode, with overlapping modes.** Use categories to orient readers, not to force messy workflows into exclusive boxes.
5. **Narrative first; role labels optional.** Explain what happened without requiring a partition of intellectual labour that did not exist.

Their precise wording remains editable. A sixth commitment was adopted on 2026-10-23:

6. **Origin tells you which checks a contribution needs; warrant decides whether it stands.** Its operational account, in [warrant and independence](docs/warrant-and-independence.md) and the [structured record](docs/structured-record.md), is a proposal under review.

## Where to start

| Your purpose | Start here |
| --- | --- |
| Continue development in WSL with Codex or Claude | [HANDOVER.md](HANDOVER.md) and [maintenance commands](scripts/README.md) |
| Understand the framework | [Principles](docs/principles.md) and [interaction modes](docs/interaction-modes.md) |
| Compare existing approaches | [Positioning](docs/positioning.md) and [source-reading scopes](references/README.md) |
| Adapt a declaration for a paper | [Template guide](templates/README.md) |
| Record the checkable facts behind a declaration (proposal) | [Structured record](docs/structured-record.md) and [its template](templates/AI_USE.yaml) |
| Understand the reasoning behind the design | [Founding discussion](provenance/founding-discussion.md) and [decision log](provenance/decision-log.md) |
| Check journal-specific requirements | [Policy register and review procedure](policies/README.md) |
| Contribute or challenge a proposal | [CONTRIBUTING.md](CONTRIBUTING.md) and [ROADMAP.md](ROADMAP.md) |

## A proposed reporting architecture

Use a short statement in the paper, method-specific information wherever AI affects the research procedure, and an extended repository narrative where useful. These are complementary views of the same truthful account, not three compulsory forms. See [disclosure architecture](docs/disclosure-architecture.md).

A possible headline description is:

> Predominant mode: governed human–AI collaboration, with periods of delegated problem-solving and bounded assistance.

That label is not sufficient on its own. A short narrative should explain the actual relationship, the consequential AI involvement, and the limits of the available account.

## What is included

The repository contains the framework; concise and extended declarations; Methods and `AI_USE.md` templates; fictional examples; a proposed structured record; a curated account of the founding discussion; source and policy registers; contribution guidance; and local maintenance tools.

The prose and templates are usable as plain text. Optional Python tools check repository mechanics. The core checks use the standard library; the separate structured-record validator declares its dependencies in its script. See [maintenance tools](scripts/README.md).

## Policy and evidence status

Selected primary sources were checked during scaffold construction on **2026-09-08**. The literature comparison was extended on **2026-10-23**, with [inspection scopes](references/README.md) recorded. This did not refresh publisher policies. These are assistant-conducted readings; independent human review remains pending.

The framework's preferred terminology is not a claim that every journal permits every described workflow. Read the actual target-journal policy at submission. Do not disguise an incompatible practice with softer wording. See [policy adaptation](docs/policy-adaptation.md).

## Licensing and attribution

The scaffold proposes CC BY 4.0 for the explanatory framework, CC0 for reusable templates and fictional examples, and MIT for maintenance code and configuration. These are **scaffold-selected defaults for maintainer review before publication**, not a decision recorded in the founding discussion. See [LICENSE.md](LICENSE.md). Third-party sources keep their own rights.

The project originated in a discussion between Barry W. Brook and ChatGPT, which drafted the original scaffold. Claude and Codex subsequently developed and reviewed it. See [this repository's own AI-use account](AI_USE.md).
