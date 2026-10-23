# Founding discussion: substantive synthesis

**Source:** the conversation supplied for this scaffold, between Barry W. Brook and ChatGPT. This is a curated reconstruction of ideas and decisions, not a verbatim transcript or an independently audited account of Barry's projects. “Barry described” records his account; “assistant proposed” does not mean Barry subsequently endorsed every detail.

## 1. The motivating research practice

Barry described a methodology cultivated over several years of increasingly capable AI use, most recently involving agentic work with Codex and the Pro model in ChatGPT. A long-running project may span several model generations before producing a paper, reproducible code repository and dataset.

His central point was that the interaction is intertwined and iterative across the scientific process: ideation, finding and processing data and literature, coding, testing, refinement, discarding and regenerating ideas, planning the paper, structuring the argument, drafting and polishing. It is not accurately represented as a simple prompt followed by an output incorporated unchanged.

He wants declarations that are genuine, transparent and useful in explaining that process. He described sustained safeguards and scientific care, and judged the resulting work stronger than some of his earlier work constrained by time and resources. That is his assessment of his practice, not evidence here of a general superiority of AI-produced science. Human experience, knowledge and interaction remain important in his account.

## 2. The initial proposal and broad response

The assistant proposed the research workflow as the unit of disclosure; a distinction between collaborative participation and formal authorship; a short paper declaration plus method-specific reporting and a longer repository account; and concrete explanations of checking rather than a generic “authors reviewed the output”. It also suggested preserving useful records without requiring every prompt to be published.

Barry strongly welcomed that overall direction and the initial declaration. He proposed developing an open GitHub repository that others could contribute to or adapt, with continuing attention to current journal policies and avoidance of accidental deception.

The assistant's initial answer also included factual claims about policies, literature and example declarations. Those are not treated as verified merely because they appeared in the conversation. Their status is recorded in the [source register](../references/source-register.json), [reading notes](../references/README.md) and [policy register](../policies/README.md).

## 3. Why the discussion was divided into small topics

Barry requested approximately ten to fifteen small propositions, one at a time, so he could respond thoughtfully without needing to address the entire framework at once. The assistant proposed roughly twelve topics. This was a working discussion format, not a fixed twelve-principle charter.

The first five topics received substantive responses. The sixth was posed but not answered before Barry asked to move development into a full repository using Codex and Claude. Future work should preserve this boundary rather than presenting the remaining topics as agreed positions.

## 4. Topic 1: workflow-level disclosure and finer provenance

Barry broadly endorsed the workflow-level principle, with an important qualification. Granular provenance may sometimes be available and valuable. He described newer long-running Codex “mega-threads”, compacted over time, alongside complete Git commit histories where maintained. Older projects did not necessarily have those conversation records.

Git does not directly preserve the human–agent interaction, but can preserve additions, deletions, revisions, overhauls and reinventions. He regarded much of that record as unnecessary to reproducing the final result, yet potentially valuable as evidence of the messy process of actual science.

He envisaged a possible future in which a versioned working notebook and development record complement a clean repository that reproduces exactly the published data, methods and results. A summary or export of long conversations could provide further context when relevant. This was a forward-looking possibility, not a settled publication requirement or a claim that a particular export format is presently available.

The assistant reformulated the principle as workflow-level disclosure with preservation of finer provenance where practicable, not necessarily routine publication of every trace.

## 5. Topic 2: strong collaboration and the human scientific role

Barry distinguished his present practice from earlier, weaker forms of assistance that remain honest descriptions for many researchers. For his own future work, he expected strong collaboration to be the norm, potentially with AI performing most of the operational execution.

He used his role supervising doctoral students and postdoctoral researchers as an analogy: a senior scientist may contribute accumulated judgement, awareness of failed approaches, recognition of friction and practical guidance rather than most of the task execution. His motivations and scientific interests also direct which problems are pursued.

He speculated that agents might eventually select and solve many research problems with much less human participation, but explicitly disclaimed confidence in the timeline. These remarks motivate flexible categories; they are not capability forecasts to publish as established facts.

Barry also reported that participants in a recent agentic-AI workshop responded positively to the initial statement and the idea of a public repository. No names, endorsements, participant counts or consensus claims are inferred. The public repository is intended as a place for wider contribution, not evidence of an existing movement.

## 6. Topic 3: governance and three agent-intensive relationships

The assistant asked whether governance captured the irreducible human role. Barry distinguished three broad cases in which an agent performs substantial execution.

In the first, a scientist points an agent towards a general field, problem set or accumulated dataset and asks it to discover useful research. His example was a large camera-trap database gathered over years, offered without a specific scientific question. He distinguished the scientist's connection through data collection from originating the research questions; authorship eligibility was not settled by the analogy.

In the second, a scientist supplies a sharp problem or motivation, perhaps a bespoke dataset, initial ideas or failed attempts, then delegates the search for a solution. The human sets a more specific intellectual direction but may not be embedded in each intermediate step.

In the third, the human remains embedded throughout: directing attention to literature, reading selected sources, providing feedback, editing prose, developing the research framework, and participating in consequential choices, even if an agent performs most of the operational work.

Barry explored labour percentages as an intuition for the changing balance of work, including the possibility of very small human execution shares with substantial governance. He also recognised that a 50% dividing line was too crude to capture the range of interactions. The assistant recommended separating workload from governance rather than adopting a percentage rule. **No numerical cutoff was adopted.**

Combining these three relationships with bounded assistance produced the four working descriptors in [interaction modes](../docs/interaction-modes.md).

## 7. Topic 4: useful categories despite blurred boundaries

Barry anticipated that modes would blend, integrate and rarely be cleanly separable. Nevertheless, he thought categorisation useful. He proposed a clearly defined category that best describes a project's predominant mode, supplemented by an account of overlap with other modes.

The assistant called this a predominant-mode plus interaction-profile approach. Qualitative descriptions were suggested as possibilities, but no scoring instrument or mandatory structured profile was agreed. The repository uses narrative qualification by default.

## 8. Topic 5: why narrative should be the default

When asked about standardised scientific roles versus free-form description, Barry separated his own increasingly integrated practice from the likely diversity of research generally.

He was concerned that some researchers and assessors attach legitimacy to humans performing particular tasks, especially writing. He rejected the inference that the human must be the main producer of the words and grammar to be a valid intellectual contributor. In embedded collaboration, thought and expression can develop together.

He described two possible distortions from a rigid task-attribution scheme: researchers might artificially reserve tasks to satisfy convention, disrupting an efficient collaboration; or they might describe work strategically to claim the human performed a conventionally valued function. He also noted that heavily overlapping contributor-role lists can cease to communicate much about the interaction.

His preferred default is therefore a free-form, integrated account, with scope for role attribution where it is useful or desired, but not forced predetermined boxes. He did not propose abandoning required human-author contribution statements or the truthful disclosure of particular scientific uses.

The assistant distilled the design rule that transparency should document authentic practice rather than prescribe a workflow for the convenience of the framework. That formulation is preserved as a synthesis of his concern, not as a verbatim quotation.

## 9. Topic 6: what remained unanswered

The assistant next proposed verification and the basis for accepting scientific claims as a possible alternative to reassuring readers through ownership of tasks. Examples included checking source support, testing code, examining assumptions and considering competing interpretations.

The narrow question was whether the process by which a candidate contribution becomes warranted should matter more than whether it originated with a human or AI. **Barry did not answer this question.** His earlier endorsement of rigorous checking remains part of the context, but it does not settle the priority relationship or the detailed criteria.

The repository preserves an explicitly provisional discussion of verification. It must not be converted into an agreed sixth principle without further deliberation.

## 10. The handover request

Barry stopped the serial ideation and requested a draft repository to unpack in WSL, with further development using Codex and Claude and eventual publication on GitHub. He authorised creation of a public repository if suitable tools existed, otherwise a downloadable ZIP.

The available GitHub connector exposed actions for existing repositories but no creation action for a new repository. A capability search found no additional enabled route, and the build environment had no GitHub CLI. This scaffold therefore supplies local files and WSL/GitHub instructions, without claiming to have created or pushed a remote.

## Interpretive safeguards for future contributors

Preserve the distinction between the founder's reported practice, broad design commitments, assistant formulations and new implementation proposals. Do not treat predictions as facts, an expressive analogy as a settled equivalence, or workshop interest as endorsement. Criticism and revision are welcome; changing an established commitment should be explicit and reasoned rather than an unnoticed rewrite.
