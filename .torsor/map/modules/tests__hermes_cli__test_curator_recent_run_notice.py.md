---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_curator_recent_run_notice.py

Symbols in `tests/hermes_cli/test_curator_recent_run_notice.py`.

- L22 `curator_env(tmp_path, monkeypatch, capsys)` (function)
- L44 `_set_state(curator_mod, **fields)` (function)
- L50 `test_silent_when_no_curator_run_yet(curator_env)` (function) — First-run notice handles this case; recent-run notice stays silent.
- L57 `test_silent_when_summary_is_single_line(curator_env)` (function) — No archives = no rename map = nothing to surface. But still stamps shown.
- L73 `test_prints_multiline_summary_with_rename_map(curator_env)` (function) — Multi-line summary (rename map appended) prints with timestamp + footer.
- L96 `test_show_once_semantics(curator_env)` (function) — Calling twice prints once; second call is silent until a new run lands.
- L120 `test_new_run_resets_show_once(curator_env)` (function) — A newer curator run with rename data prints again, even though one was already shown.
- L154 `test_format_time_ago_buckets(curator_env)` (function) — Smoke test the time formatter — drives the `last run Xh ago` line.
