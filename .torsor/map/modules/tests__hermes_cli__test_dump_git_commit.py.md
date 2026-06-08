---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dump_git_commit.py

Symbols in `tests/hermes_cli/test_dump_git_commit.py`.

- L14 `test_get_git_commit_uses_live_git_when_available(tmp_path)` (function) — Source install: ``git rev-parse --short=8 HEAD`` wins; no fallback.
- L32 `test_get_git_commit_falls_back_to_build_sha_when_live_git_fails(tmp_path)` (function) — Docker image case: live git returns non-zero → use baked SHA.
- L47 `test_get_git_commit_falls_back_when_git_returns_empty_stdout(tmp_path)` (function) — Edge case: git exits 0 but prints nothing — still try the baked SHA.
- L62 `test_get_git_commit_falls_back_when_git_raises(tmp_path)` (function) — git binary missing (e.g. minimal container w/o git) → baked SHA path.
- L76 `test_get_git_commit_returns_unknown_when_neither_source_available(tmp_path)` (function) — Pip-installed wheel: no git, no baked SHA → '(unknown)' (legacy contract).
- L91 `test_get_git_commit_output_format_identical_between_sources(tmp_path)` (function) — Regression guard: live-git and baked-SHA outputs share the same shape.
