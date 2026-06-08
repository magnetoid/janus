---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# scripts/release.py

Symbols in `scripts/release.py`.

- L1479 `git(*args, cwd=None)` (function) — Run a git command and return stdout.
- L1492 `git_result(*args, cwd=None)` (function) — Run a git command and return the full CompletedProcess.
- L1502 `get_last_tag()` (function) — Get the most recent CalVer tag.
- L1510 `next_available_tag(base_tag: str)` (function) — Return a tag/calver pair, suffixing same-day releases when needed.
- L1522 `get_current_version()` (function) — Read current semver from __init__.py.
- L1529 `bump_version(current: str, part: str)` (function) — Bump a semver version string.
- L1551 `update_version_files(semver: str, calver_date: str)` (function) — Update version strings in source files.
- L1597 `_update_acp_registry_versions(semver: str)` (function) — Bump the ACP Registry manifest's version + uvx package pin in lockstep
- L1616 `build_release_artifacts(semver: str)` (function) — Build sdist/wheel artifacts for the current release.
- L1657 `resolve_author(name: str, email: str)` (function) — Resolve a git author to a GitHub @mention.
- L1678 `categorize_commit(subject: str)` (function) — Categorize a commit by its conventional commit prefix.
- L1712 `clean_subject(subject: str)` (function) — Clean up a commit subject for display.
- L1724 `parse_coauthors(body: str)` (function) — Extract Co-authored-by trailers from a commit message body.
- L1746 `get_commits(since_tag=None)` (function) — Get commits since a tag (or all commits if None).
- L1798 `get_pr_number(subject: str)` (function) — Extract PR number from commit subject if present.
- L1806 `generate_changelog(commits, tag_name, semver, repo_url='https://github.com/NousResearch/hermes-agent', prev_tag=None, first_release=False)` (function) — Generate markdown changelog from categorized commits.
- L1910 `main()` (function)
