---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_memory_monitor.py

Symbols in `tests/gateway/test_memory_monitor.py`.

- L19 `_ensure_monitor_stopped()` (function) — Every test starts from a clean state and leaves one behind.
- L26 `test_log_memory_usage_emits_memory_line(caplog)` (function)
- L33 `test_log_memory_usage_has_grep_friendly_format(caplog)` (function)
- L46 `test_log_memory_usage_with_prefix(caplog)` (function)
- L53 `test_start_logs_baseline_and_returns_true(caplog)` (function)
- L66 `test_double_start_is_noop()` (function)
- L72 `test_stop_logs_shutdown_snapshot(caplog)` (function)
- L84 `test_stop_without_start_is_noop()` (function)
- L90 `test_periodic_timer_fires(caplog)` (function)
- L107 `test_thread_is_daemon()` (function)
- L115 `test_unavailable_rss_warns_and_does_not_start(caplog, monkeypatch)` (function)
