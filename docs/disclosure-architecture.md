# A layered disclosure architecture

**Status:** a practical proposal from the initial discussion, developed here for review. It is not a requirement to complete three separate forms.

## One account, several views

The core record should be a truthful narrative of the research relationship and process. From it, authors can derive a short declaration, method-specific details and a longer repository account. The views should agree; a restrictive word limit does not justify making the shorter version materially misleading.

### The paper-level declaration

Explain the nature and substantive extent of AI involvement, identify the systems used as accurately as records allow, characterise human scientific participation, and state responsibility in terms the authors can substantiate. Refer to the longer account where relevant and permitted.

The [concise template](../templates/declaration-concise.md) is an editable starting point, not language to certify without checking. The required placement is venue-specific.

### Method-specific information

When AI materially participates in the production of research evidence, describe the relevant procedure where readers can evaluate it. Examples include extracting outcomes from documents, producing classifications, screening records or generating data used in an analysis. A general collaboration declaration cannot substitute for the method.

Distinguish AI used to develop executable code from an AI model that remains part of the executed analytical method. The latter can require input definitions, prompts or configurations, response handling, validation and uncertainty information that the former does not. Report actual dependencies and limitations; do not imply an unavailable model can be rerun identically.

See [Methods template](../templates/methods-disclosure.md) and the [policy adaptation guide](policy-adaptation.md).

### An extended repository account

An `AI_USE.md` can describe the iterative relationship, participating systems and approximate periods, consequential interventions, acceptance practices, available records and gaps. Write it as readable prose. Add optional logs or structured records only when they clarify something important.

The extended narrative is not a substitute for disclosure in the submitted manuscript when the venue requires that disclosure. Nor should it silently contradict the declaration or Methods.

## Separate records for separate purposes

A clean reproducibility release answers “How are these results obtained from these inputs?” Development history answers “How did the implementation and analysis change?” Deliberative records answer “What discussion and redirection are preserved?”

All may matter, but none is a complete substitute for the others. A paper can be computationally reproducible without preserving its entire discovery history. Conversely, a vast transcript does not ensure that the final code runs or that the inference is justified.

## Adaptation without concealment

Read the target-journal rules and submission form. Add required names, version information, dates, oversight descriptions, placement and methodological detail. Resolve ambiguities with the editor rather than using euphemisms to make an unpermitted workflow look compliant.

When records are incomplete, say what is known, the basis for the reconstruction and what remains unknown. Never infer a historical model version solely from which model was popular or available around a project's date.
