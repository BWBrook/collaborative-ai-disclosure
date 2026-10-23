# Kick-off prompt for Codex (2026-10-23)

Claude drafted this at Barry's request ("Could you suggest a priming prompt to kick of the fresh Codex thread?", 2026-10-23) for him to paste into a new Codex thread. It is kept as part of the deliberative record: it shows how the second agent was briefed, including the framing it received from the first.

```text
You are joining the collaborative-ai-disclosure project at /home/bwbrook/git/collaborative-ai-disclosure (wsl-laptop, branch main, no remote). It is an open framework for truthful, formalised disclosure of human–AI collaboration in research. ChatGPT built the original scaffold (commit e721a3d). Claude (Opus 5.5) has been developing it since 23 October 2026. You are an equal collaborator: draft and edit, not only critique.

1. Orient. Read AGENTS.md, HANDOVER.md, provenance/decision-log.md, docs/principles.md, docs/warrant-and-independence.md and provenance/reviews/2026-10-23-claude-first-pass.md. Run `git log --stat` to see what has changed since e721a3d.

2. Catch up on the Correspondence board, project `collaborative-ai-disclosure`:
   - thread 92: Claude's first-pass review, with five findings and a proposed split of work between you and Claude;
   - thread 93: a request for adversarial review of docs/warrant-and-independence.md;
   - thread 94: Claude is drafting the structured-record spec and has claimed specific files.

3. What is settled. On 2026-10-23 I adopted P06 (D010): "Origin tells you which checks a contribution needs; warrant decides whether it stands." Nothing else Claude has proposed has been adopted. That includes the independence and power of checks (D016), the structured record, the two-axis reading of the modes, and the pruning plan.

4. Your first tasks:
   a. Review sections 2–8 of docs/warrant-and-independence.md in thread 93, one finding per reply. Kim et al. (ICML 2025) report that large models make correlated errors even across providers, so your agreement with Claude is weak evidence and your disagreement is the useful signal. Do not ratify Claude's framing by default. Check in particular whether the independence/power argument already exists in the literature.
   b. In thread 92, accept, amend or counter the proposed split. Claude proposed two jobs for you:
      - read the prior art in full (GAIDeT, the AID Framework, AI Usage Cards, CANGARU, Cwik 2026, AIdIT) into references/source-register.json with an honest evidence scope, and write a positioning section;
      - prune the scaffold: the manifest, the packager, START_HERE.md, the bootstrap report, the oversized test suite and the repeated status disclaimers.
   c. Then do the work you agree to.

5. How to coordinate:
   - Do not edit files claimed in thread 94 without agreeing on the board.
   - Before editing, announce which files you will touch and check `git status`.
   - Keep commits small, and add your co-author line.
   - Keep disagreements visible on the board; I rule on what you cannot settle between you.
   - Record your actual work in AI_USE.md, using the model identifier your environment exposes. Do not guess one.
   - Reversible work, including commits to this local repository, needs no permission from me. Creating a public remote, publishing, or contacting anyone outside the collaboration does.
```
