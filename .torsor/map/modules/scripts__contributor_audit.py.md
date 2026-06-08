---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# scripts/contributor_audit.py

Symbols in `scripts/contributor_audit.py`.

- L65 `is_ignored(handle: str, email: str='')` (function) — Return True if this contributor is a bot/AI/machine account.
- L79 `git(*args, cwd=None)` (function) — Run a git command and return stdout.
- L93 `gh_pr_list()` (function) — Fetch merged PRs from GitHub using the gh CLI.
- L153 `collect_commit_authors(since_tag, until='HEAD')` (function) — Collect contributors from git commit authors.
- L193 `collect_co_authors(since_tag, until='HEAD')` (function) — Collect contributors from Co-authored-by trailers in commit messages.
- L229 `collect_salvaged_contributors(since_tag, until='HEAD')` (function) — Scan merged PR bodies for salvage/cherry-pick/co-author attribution.
- L290 `check_release_file(release_file, all_contributors)` (function) — Check which contributors are mentioned in the release file.
- L321 `main()` (function)
