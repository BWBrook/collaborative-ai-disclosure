# Optional maintenance tools

These tools use Python 3.10+ and the standard library. They do not call an AI model, fetch policies, install packages, authenticate, publish, initialise Git or alter scientific data.

| Command | What it does |
| --- | --- |
| `python3 scripts/check_repo.py` | Checks expected public files, text format, simple inline relative links and source/policy JSON consistency. |
| `python3 scripts/policy_age.py` | Reports stale, incomplete, future-dated or human-unreviewed policy records. |
| `python3 scripts/package_repo.py --output ../snapshot.zip` | Packages selected public text files plus a hash manifest; writes a separate ZIP checksum. |
| `python3 -m unittest discover -s tests -v` | Exercises the maintenance tools using local fixtures, including temporary Git repositories when Git exists. |

Every script accepts `--help`; the three command-line tools accept `--root` for an explicit project directory. `check_repo.py` returns 0 for a pass and 1 for a structural failure. The age report normally returns 0 while printing reminders; `--fail-on-due` returns 2 when attention is needed. Invalid data returns 1. The packager refuses existing output unless `--force` is deliberately supplied.

## Selection and privacy boundaries

For an uninitialised scaffold, `repo_config.json` defines allowed public roots. Within those roots, ordinary new files may be selected, so review them before sharing. Once the project has its own Git repository, selection changes to tracked files only; new public files must be staged. Current working-tree bytes are packaged, not automatically the last commit. A parent Git repository causes a refusal rather than accidental collection from the wrong project.

Common local/private/credential paths and raw-log filenames are excluded even when tracked. Symlinks in eligible paths are rejected, and the archive must be written outside the project. The archive includes only text; each source file has a SHA-256 entry. Fixed ZIP timestamps and sorted entries make repeated packaging deterministic in the same runtime. Different compression-library versions need not produce byte-identical ZIPs.

This is **not an exhaustive secret scanner**. A password pasted into `README.md` remains a password. Review the candidate files, staged Git changes and archive before making them public.

## Validation limits

The Markdown checker handles the simple inline links used here; it does not parse all Markdown, verify heading anchors, fetch external links or validate citation truth. The JSON checks enforce basic record consistency, not publisher-policy compliance. Passing tests does not establish scientific correctness or independent human review.

The bundled GitHub Actions workflow is an optional local-check runner, not a policy watcher. Its third-party checkout action is pinned to a specific release commit and should be reviewed before enabling public CI. It has not been run remotely as part of the initial scaffold. If tooling grows substantially, review the scope before adding dependencies or a documentation build system.
