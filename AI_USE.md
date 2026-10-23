# AI use in this repository

## Origin and scope

This scaffold was drafted in ChatGPT from the founding conversation supplied by Barry W. Brook. He described his actual and envisaged research workflows, challenged proposed classifications and directed the project towards narrative-first public documentation. The assistant proposed formulations, organised the discussion, drafted this repository and supplied its maintenance code and tests.

The conceptual relationship was iterative. The file-building stage was a delegated drafting task based on that prior exchange. No attempt is made to assign exclusive ownership to individual phrases or ideas. The [founding synthesis](provenance/founding-discussion.md) separates Barry's expressed positions from the assistant's proposals.

## Systems and dates

The package was assembled on 2026-09-08 in a ChatGPT session using web retrieval and a container-based file/code environment. An independently auditable backend model identifier was not captured in the package; no exact identifier is invented. This date describes scaffold construction, not the start or duration of the earlier conversation.

Barry identified Codex and the Pro model in ChatGPT as systems used in his wider research practice. Those founding references are context, not an inventory of executions in this repository. Codex and Claude subsequently joined development on 2026-10-23; neither worked on the original ChatGPT package.

## Source checks and implementation checks

Selected official policy pages and scholarly sources were inspected using web retrieval. The [source register](references/source-register.json) records what was inspected, partially available or inaccessible. These are assistant-conducted checks; independent human source review remains pending.

The maintenance code was exercised in the build environment, including repository validation, unit tests, archive construction and a fresh-extraction check. The historical [bootstrap report](provenance/bootstrap-report.md) records the actual results and limitations. No actual WSL machine or remote GitHub Actions run was used for testing this initial package.

## Development after import

On 2026-10-23 Claude Opus 5.5 (`claude-opus-5-5`, as exposed by Claude Code in the local environment) put the unmodified scaffold under Git as its first commit. It ran the repository checks and tests, which passed, and wrote a [first-pass review](provenance/reviews/2026-10-23-claude-first-pass.md). The review proposes an answer to topic 6, a formal layer of facts and evidence links, and pruning of the scaffold. Its prior-art notes rest on web search results and one arXiv abstract, not full reading. Barry asked for the review. On the same day he adopted its topic-6 proposition as P06 ([D010](provenance/decision-log.md)), selecting a reply option that Claude had drafted. Claude then drafted [warrant and independence](docs/warrant-and-independence.md), which replaces the scaffold's verification draft. It updated the files that described topic 6 as open, and added six cited sources at abstract or metadata scope to the source register. The other proposals in the review have not been adopted.

Later on 2026-10-23, at Barry's request, Claude drafted the [structured record](docs/structured-record.md) proposal (D017). It comprises a JSON Schema, a validator run through `uv`, a blank template, a fictional example and this repository's own [AI_USE.yaml](AI_USE.yaml). Codex (OpenAI; self-reported as GPT-6) joined the same day, coordinating on the correspondence board. Its review of the warrant draft found a mechanism misattributed to Knight and Leveson, an implied ranking of checks, an over-transferred result from Kim et al., and D016 wording that Claude had written into the adopted P03 text. Claude accepted these findings and revised the warrant draft before committing the structured record.

Codex led the prior-art and positioning tranche using bounded source-reading delegates, including a delegate for Cwik and AIdIT. The parent reviewed the synthesis and inspected selected warrant-literature passages directly. The environment describes the parent and inherited delegate model as **GPT-6**; a finer deployment identifier is not exposed and is not inferred from the Codex product name. All six requested main texts were read, with separate limits for images, supplements, applications and linked analyses. The [reading guide](references/README.md) and [source register](references/source-register.json) identify the scopes and earlier inspection records. The [positioning discussion](docs/positioning.md) is a proposed synthesis; these readings do not independently replicate the cited studies or establish that the framework is novel or superior.

Codex also delegated the maintenance pruning, then reviewed and integrated the changes. The ZIP packager, extraction guide and packaging-only tests were removed; the bootstrap report was preserved under provenance. Core checking now includes configured working-tree additions before staging. Source/status consistency, private-path exclusions, symlink rejection and meaningful failure tests remain. A delegate verified all 68 entries in the ignored original manifest against `e721a3d`; that receipt was retained. The revised maintenance suite passed 39 tests locally on WSL. These checks concern repository mechanics, not scientific validity.

The parent Codex collaborator posted eight warrant-review findings individually on the correspondence board and preserved them in a [review memo](provenance/reviews/2026-10-23-codex-warrant-review.md). Claude accepted and addressed them; Codex checked the revised text, repaired the P03 adoption boundary and distinguished P06's rationale from the adopted proposition. The parent also reviewed the maintenance changes, ran the repository checker and 39 tests successfully after integration, and updated the handover and this account. Both populated YAML records passed the separate validator after the actual-work update. These activities include reasoning, drafting, source interpretation, code maintenance and criticism, rather than a human-only drafting process. Neither the new structured-record design nor the framework's usability received a separate substantive audit in this tranche.

## Human review and open decisions

Barry requested the scaffold but has not yet reviewed the generated files at the time of packaging. The sixth conceptual topic was unanswered at packaging. It was resolved on 2026-10-23, and the detailed assurance guidance remains provisional. Licensing, initial governance and citation metadata are scaffold defaults requiring his review before public release.

The package must not be cited as evidence that he approved every sentence, checked each source, or adopted every proposed criterion. Future contributors should update this account with actual work, checks, decisions and review status.
