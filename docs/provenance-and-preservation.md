# Provenance and preservation

**Status:** the distinction among clean results, development history and deliberative records was discussed and supported. The operational suggestions below are scaffold proposals.

## Three complementary records

**Clean research release.** Preserve the inputs that can lawfully be shared, code, environment information, execution instructions and output mapping needed to reproduce the published results. A clean release removes irrelevant development clutter; it must not hide consequential exclusions, analytic choices or failed checks necessary to interpret the evidence.

**Development history.** Git commits, notebooks, issues and decision records can preserve changes, abandoned approaches, rewrites and reversals. Such records may reveal a much less linear process than the article's exposition. A commit records a change in tracked files, not automatically who originated an idea or everything that happened between commits.

**Deliberative record.** Long-running conversations may preserve question formation, objections and redirection that code history misses. Where available, retain useful transcripts, summaries or task records under suitable access controls. The format should follow the available export, not assume XML, JSON, or any vendor-specific capability exists.

## Long threads and compaction

Barry described a newer practice of keeping a problem in a long-running Codex thread, periodically compacted, sometimes lasting weeks or months. He also emphasised that many older projects were not conducted this way.

For this framework, a compacted summary is not assumed to be a complete transcript. Label whether a record is an original export, a partial export, a contemporaneous summary or a later reconstruction. Record known omissions and changes of system. Do not claim that a “mega-thread” automatically provides a complete history.

Use observable conversations, task instructions, decisions and artifacts. The framework neither requires nor assumes access to a model's private internal reasoning.

## Prospective practice without retrospective fiction

Record periods and tool identities as accurately as available evidence permits. Distinguish a product or interface name from a model identifier. Where several generations participated, report several entries or a defensible date range, with uncertainty made explicit.

A missing record is not evidence of no AI use. Nor is it by itself proof of misconduct. Do not manufacture exact prompts, dates or attributions to fill gaps. A short account of the available evidence is preferable to a detailed invented history.

## Preserve is not the same as publish

Data licences, participant confidentiality, sensitive locations, unpublished third-party work, credentials and private correspondence may restrict sharing. Records can be retained privately, redacted, summarised or made available under controlled access where appropriate. Record why material is withheld and what public substitute is provided; do not promise access that cannot be granted.

Before publication, inspect both current files and any Git history being made public. Removing a secret from the latest version or adding a path to `.gitignore` does not remove earlier commits. This scaffold contains no `.git` directory and no raw conversation export.

## Selection and accountability

Representative extracts should be labelled as selected examples, with selection criteria and known limitations. A polished summary must not be represented as an exhaustive audit log. Preserve consequential changes to inclusion criteria, inferential strategy and interpretation when they bear on the reported claims.

## The longer-term vision

The founding discussion envisaged a future research object combining an executable clean release with a versioned working notebook and, when appropriate, records of human–AI deliberation. This is an aspiration for richer scientific provenance, not a prediction that journal articles will disappear.

Do not claim such records are historically unprecedented. The proposal is to make process documentation practical for these collaborative workflows, and to connect it usefully to the research result.
