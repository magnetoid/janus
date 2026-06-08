---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_banner_git_state.py

Symbols in `tests/hermes_cli/test_banner_git_state.py`.

- L4 `test_format_banner_version_label_without_git_state()` (function)
- L13 `test_format_banner_version_label_on_upstream_main()` (function)
- L27 `test_format_banner_version_label_with_carried_commits()` (function)
- L42 `test_get_git_banner_state_reads_origin_and_head(tmp_path)` (function)
- L66 `test_get_git_banner_state_falls_back_to_build_sha_when_no_repo()` (function) — Docker image case: no .git checkout — baked build SHA fills the gap.
- L84 `test_get_git_banner_state_returns_none_when_no_repo_and_no_build_sha()` (function) — Pip-installed wheel with neither git checkout nor baked SHA → None.
- L98 `test_get_git_banner_state_falls_back_when_live_git_returns_nothing(tmp_path)` (function) — Shallow clone without origin/main → still surface build SHA if baked.
