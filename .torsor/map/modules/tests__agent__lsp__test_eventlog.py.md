---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/lsp/test_eventlog.py

Symbols in `tests/agent/lsp/test_eventlog.py`.

- L18 `_reset()` (function)
- L25 `caplog_lsp(caplog)` (function)
- L35 `test_clean_emits_at_debug(caplog_lsp)` (function)
- L44 `test_disabled_emits_at_debug(caplog_lsp)` (function)
- L55 `test_active_for_fires_once_per_root(caplog_lsp)` (function)
- L65 `test_active_for_fires_per_distinct_root(caplog_lsp)` (function)
- L72 `test_active_for_separate_per_server(caplog_lsp)` (function)
- L79 `test_no_project_root_fires_once_per_path(caplog_lsp)` (function)
- L91 `test_diagnostics_always_info(caplog_lsp)` (function)
- L104 `test_server_unavailable_warns_once_per_binary(caplog_lsp)` (function)
- L112 `test_server_unavailable_separate_per_binary(caplog_lsp)` (function)
- L119 `test_no_server_configured_warns_once(caplog_lsp)` (function)
- L126 `test_timeout_warns_every_call(caplog_lsp)` (function)
- L133 `test_server_error_warns_every_call(caplog_lsp)` (function)
- L140 `test_spawn_failed_warns(caplog_lsp)` (function)
- L152 `test_log_lines_use_lsp_prefix(caplog_lsp)` (function)
- L165 `test_thousand_clean_writes_emit_one_info(caplog_lsp)` (function) — A long session writes lots of files cleanly; agent.log should
- L181 `test_short_path_uses_relative_when_inside_cwd(tmp_path, monkeypatch)` (function)
- L189 `test_short_path_keeps_absolute_when_outside(tmp_path, monkeypatch)` (function)
- L198 `test_short_path_handles_empty_string()` (function)
