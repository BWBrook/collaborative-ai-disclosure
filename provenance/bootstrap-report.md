# Bootstrap quality report

*Historical record, moved here on 2026-10-23. The observations and commands below describe the original 2026-09-08 archive. The ZIP packager has since been retired; current checks are documented in [maintenance tools](../scripts/README.md). The ignored local `MANIFEST.sha256` is retained as the original import receipt, not a checksum of the evolving repository.*

**Package:** Collaborative AI Research Disclosure, `0.1.0-draft`  
**Build/check date:** 2026-09-08  
**Performed by:** the drafting assistant in the ChatGPT build environment  
**Human review:** pending

This report records observations about the initial scaffold. It is not a scientific validation, a policy-compliance certificate, a claim of independent audit, or Barry's approval of the generated files.

## Environment

The tests ran on Linux with Python **3.13.5** and Git **2.47.3**. The maintenance scripts target Python 3.10+ and use only its standard library. This target was not tested across all supported Python versions. No actual WSL host, Windows filesystem or remote GitHub Actions runner was used.

A build-environment YAML parser was used for an additional syntax check; it is not a runtime dependency of the delivered project.

## Observed results

| Check | Result |
| --- | --- |
| Repository structure and public-file selection | PASS: 68 selected text files |
| Expected files, UTF-8/LF, final newlines, inline relative-file links | PASS |
| JSON syntax, record status/date consistency, source references | PASS |
| Maintenance unit tests | PASS: 46 tests; none skipped in this environment |
| Fresh ZIP extraction: repository check and unit tests | PASS: the same 46 tests passed |
| Fresh ZIP extraction: `sha256sum -c MANIFEST.sha256` | PASS: all 68 source-file entries matched |
| Temporary Git initialisation and staging of extracted source | PASS: checker selected the 68 intended tracked files |
| Repackaging temporary Git-tracked source | PASS: archive bytes matched the uninitialised-source archive in the same runtime |
| ZIP payload and integrity | 68 source files plus one generated manifest; no bundled `.git`, caches or symlinks |
| `CITATION.cff` and GitHub workflow YAML syntax | Parsed successfully; no full CFF-schema or GitHub runtime validation |
| Policy-age report for 2026-09-08 | 6 of 6 records correctly flagged for human review; one also partial and one unavailable |

The tests include missing links, invalid JSON and date/status types, missing human-review metadata, source-reference mismatch, archive hashes, repeated packaging, exclusion rules, symlink rejection, binary rejection, tracked versus untracked files, and refusal to package a project nested in another Git repository.

## Source and content review limits

Selected primary sources were retrieved separately through web tools. The [source register](../references/source-register.json) records whether full relevant passages, abstracts, metadata or no substantive content were available. These source checks were performed by the drafting assistant, not independently reviewed by a human.

The Creative Commons licence terms were copied from installed standard licence files after inspection of the official licence pages. Automated byte-for-byte equivalence to a fresh online download was not tested. The maintainer should review the proposed licence allocation before publication.

The framework was compared with the supplied discussion during drafting. The [founding synthesis](../provenance/founding-discussion.md) and decision log preserve agreed directions separately from assistant proposals. The sixth conceptual question remains unanswered. No claim is made that every future reader will interpret the categories consistently, that the templates have been empirically validated, or that related frameworks have been exhaustively reviewed.

## What the checks do not establish

The local checker does not validate every Markdown feature, heading anchors, external-link availability, source truth, journal acceptance, scientific correctness, institutional permission or absence of all confidential text. Filename exclusions reduce accidental disclosure; they are not a complete secret scanner. Mechanical checks must not be substituted for public-release review.

The GitHub Actions workflow is provided as a draft configuration, with a pinned checkout-action revision for maintainer review. It has not executed remotely. No repository was created on GitHub, no credentials were used, and no remote repository was changed. Git was initialised only in disposable validation copies, not in the delivered source directory.

## Re-run locally

```bash
python3 scripts/check_repo.py
python3 -m unittest discover -s tests -v
python3 scripts/policy_age.py --as-of 2026-09-08
sha256sum -c MANIFEST.sha256
```

The manifest is a receipt for the exact packaged source bytes. Intentional edits will change those bytes; repackage to generate a new receipt rather than claiming the old one validates modified files. The dated report remains a record of this build, not a promise of ongoing verification.
