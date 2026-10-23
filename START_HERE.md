# Start here: WSL and agent handover

This package is an ordinary directory of UTF-8, LF-terminated files. It intentionally contains **no Git history, credentials, installed environment or remote repository**. Python 3.10 or later is enough for the optional checks; all maintenance code uses the standard library.

## Open the project

Extract `collaborative-ai-disclosure-0.1.0-draft.zip` into your preferred WSL workspace. The archive already contains the top-level directory `collaborative-ai-disclosure/`; there is no need to create another directory with the same name.

For example, from the directory containing the ZIP:

```bash
mkdir -p "$HOME/projects"
unzip -n collaborative-ai-disclosure-0.1.0-draft.zip -d "$HOME/projects"
cd "$HOME/projects/collaborative-ai-disclosure"
python3 scripts/check_repo.py
python3 -m unittest discover -s tests -v
sha256sum -c MANIFEST.sha256
```

Use a fresh destination for a fresh import. `unzip -n` avoids overwriting existing files; extracting a newer archive over an old directory can otherwise leave a misleading mixture. The manifest checks the packaged bytes, not scientific validity.

## Give the next agent its context

Open this directory in your existing Codex or Claude environment. Ask it to read [AGENTS.md](AGENTS.md), [HANDOVER.md](HANDOVER.md) and the [founding discussion](provenance/founding-discussion.md) before proposing changes. [CLAUDE.md](CLAUDE.md) points to the same instructions, so the two systems do not develop conflicting project briefs.

A ready-to-use initial instruction is in [prompts/first-session.md](prompts/first-session.md). It resumes from the present state rather than restarting the five topics already discussed.

## Establish Git locally

First check whether the directory is already inside a repository:

```bash
git rev-parse --show-toplevel
```

For this fresh ZIP, a “not a git repository” response is expected. If the command instead reports an existing parent repository, move the extracted directory to a separate workspace before initialising it. Do not accidentally stage it into another project.

Review the scaffold's licensing defaults in [LICENSE.md](LICENSE.md), the public-release considerations in [HANDOVER.md](HANDOVER.md), and the actual files. Then initialise a new repository:

```bash
git init -b main
git status --short --untracked-files=all
# Review the proposed public contents before staging them.
git add .
git diff --cached --stat
git diff --cached --check
git commit -m "Initial draft: collaborative AI research disclosure framework"
```

Use your existing Git identity. If Git requests a name or email, configure your own appropriate identity; the package does not set one or invent an address. The first commit should record import of this scaffold, not pretend to reconstruct the earlier conversation's development history.

## Create the public GitHub repository

These commands require an installed and authenticated GitHub CLI. Use the correct account and owner for the project. The unqualified name below uses the authenticated account; replace it with an explicit `OWNER/NAME` when appropriate.

```bash
gh auth status
# Only if authentication is needed:
# gh auth login

gh repo create collaborative-ai-disclosure \
  --public \
  --source=. \
  --remote=origin \
  --push \
  --description "Narrative-first disclosure of human-AI collaboration in research"
```

**The last command makes the committed contents public.** Review the actual account, licences and public contents first. If the remote already exists or the name is unavailable, inspect the situation rather than deleting or force-pushing anything. Codex or Claude can handle the Git machinery in your local environment under your direction.

The CLI creation flags and authentication flow were checked against the official [repository-creation manual](https://cli.github.com/manual/gh_repo_create) and [authentication manual](https://cli.github.com/manual/gh_auth_login) during scaffold construction. The package does not install the CLI or authenticate on your behalf.

## Subsequent local checks

```bash
python3 scripts/check_repo.py
python3 -m unittest discover -s tests -v
python3 scripts/policy_age.py --as-of 2026-09-08
```

Replace the date with the date relevant to your review, or omit `--as-of` to use the local date. The age report does not fetch policies. The original source records still require human review even when recent.

To package the current public files without `.git` or local/private material:

```bash
python3 scripts/package_repo.py --output ../collaborative-ai-disclosure-working.zip
```

When this directory is itself a Git repository, the packager uses tracked files only. Stage new public files deliberately before packaging. It packages the current working-tree bytes of tracked files, not a historical commit, so record the revision and review uncommitted changes. Review the archive before sharing it; exclusion rules and checks are not a complete confidentiality audit.
