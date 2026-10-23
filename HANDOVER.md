# Development handover

## Project in one paragraph

Build an open, contributable framework for truthful declarations of human–AI collaborative research. The intended default is narrative, workflow-level description rather than artificial task ownership. Preserve usable categories, responsibility and evidential detail without implying that the human must personally perform most execution or originate every word and idea. The framework must accommodate bounded assistance and more deeply integrated relationships, and must not misrepresent actual practice to satisfy a journal form.

## What has been established

The founding discussion supports workflow-level disclosure with optional finer provenance; accurate collaboration language; governance distinct from labour share; four overlapping modes with a predominant descriptor; and narrative-first contribution accounts with optional role vocabulary. Read [principles](docs/principles.md), [the decision log](provenance/decision-log.md) and [the founding synthesis](provenance/founding-discussion.md).

Do not infer a fixed twelve-principle structure from the earlier “about twelve” discussion sequence. Do not resurrect a 50% cutoff or make contributor-role checklists the default.

## Where the conversation stopped

The founding discussion stopped at the sixth question: verification, and how a candidate contribution becomes part of the accepted scientific account. On 2026-10-23 Barry adopted Claude's proposed answer: "origin tells you which checks a contribution needs; warrant decides whether it stands" ([D010](provenance/decision-log.md)).

The operational account of checks in [warrant and independence](docs/warrant-and-independence.md), together with the templates, policy records and implementation details, remains **draft proposals for review**. None of it is an authorised extension of Barry's philosophy until he adopts it.

## First development tranche

Read the existing context and run the offline checks before broad rewriting. Produce a short issue-oriented audit: what accurately implements the stated direction, what the scaffold has added, and where terminology or evidence claims need refinement. Fix mechanical problems without changing the conceptual direction silently.

Topic 6 is resolved. Further conceptual discussion should follow Barry's priorities or the [roadmap](ROADMAP.md). His earlier preference was one compact proposition at a time; do not ask him to re-answer settled topics or respond to a large questionnaire. He has now moved the project into a development workflow, so do not assume continued serial questioning is the only acceptable mode of progress.

## Use Codex and Claude without inventing independence

Either system can implement changes and either can critique them. Avoid simultaneous edits to the same files without coordination; use branches or separate worktrees once Git exists. Preserve disagreements and the basis of decisions. A second model's agreement is not evidence of independent scientific validation by itself.

Update [AI_USE.md](AI_USE.md) with actual systems, observable periods and material contributions as they occur. Do not list Codex or Claude as contributors to this initial archive merely because they are planned next steps. Do not guess a model identifier that the local environment does not expose.

## Before the first public push

Review the name and project description; the scoped licensing defaults; the proposed initial maintainer arrangement; the `CITATION.cff` attribution; all public provenance notes; and any source summary likely to be read as policy advice. Check current files and whatever Git history is being published for sensitive material. No raw transcript is included in this scaffold.

The ZIP has no remote URL. After a real repository exists, add its verified URL to `CITATION.cff` and any appropriate documentation. Do not prepopulate fake badges, DOI identifiers, stars, endorsements or a release date implying public release already occurred.

## Source-check limitations

Selected policy clauses and literature passages were inspected with web retrieval on 2026-09-08. Human review is pending. Some original references are only partially checked, and a dedicated Wiley guidance page could not be retrieved even though the general ethics policy was accessible. The [source register](references/source-register.json) records these distinctions.

The source register is not an exhaustive review of journal policies or the literature. No policy watcher is running. The supplied script checks the age and review status of local records, not the content of external websites.

## Technical scope

This is a documentation repository, not a web app or AI API service. No external Python packages, API keys, database, paid service or node environment is required. Keep tooling proportionate. Do not build a scoring system, declaration wizard, website or automated policy agent before there is an agreed need.

The checker and tests assess repository mechanics. They do not establish that the framework is ethically adequate, that a project's claims are valid, or that a journal will accept a declaration.
