---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_update_stale_dashboard.py

Symbols in `tests/hermes_cli/test_update_stale_dashboard.py`.

- L31 `_refresh_bindings_against_live_module()` (function) — Rebind module-level names to the *current* ``hermes_cli.main``.
- L62 `_ps_line(pid: int, cmd: str)` (function) — Format a line as it would appear in ``ps -A -o pid=,command=`` output.
- L67 `_ps_runner(stdout: str)` (function) — Build a subprocess.run side_effect that only stubs ps -A calls.
- L83 `TestFindStaleDashboardPids` (class) — Unit tests for the ps/wmic-based detection step.
- L86 `test_no_matches_returns_empty(self)` (method)
- L98 `test_matches_running_dashboard(self)` (method)
- L107 `test_multiple_matches(self)` (method)
- L120 `test_self_pid_excluded(self)` (method)
- L134 `test_ps_not_found_returns_empty(self)` (method)
- L138 `test_ps_timeout_returns_empty(self)` (method)
- L143 `test_unrelated_process_containing_word_dashboard_not_matched(self)` (method) — Guards against greedy pgrep-style matching catching chat sessions
- L160 `test_grep_lines_ignored(self)` (method)
- L174 `test_invalid_pid_lines_skipped(self)` (method)
- L188 `test_exclude_pids_filters_specified_pids(self)` (method) — exclude_pids removes specific PIDs from the result — used by
- L208 `test_exclude_pids_none_is_noop(self)` (method) — Passing exclude_pids=None (the default) changes nothing.
- L219 `test_exclude_all_pids_returns_empty(self)` (method) — If all matched PIDs are excluded, the result is empty.
- L232 `TestKillStaleDashboardPosix` (class) — Kill path on Linux / macOS: SIGTERM then SIGKILL any survivors.
- L235 `test_no_stale_processes_is_a_noop(self, capsys)` (method)
- L240 `test_sigterm_graceful_exit(self, capsys)` (method) — Processes that exit on SIGTERM (the probe gets ProcessLookupError)
- L272 `test_sigkill_fallback_for_survivors(self, capsys)` (method) — If a process survives SIGTERM + the grace window, SIGKILL is sent.
- L302 `test_permission_error_is_reported_not_raised(self, capsys)` (method) — os.kill raising PermissionError (e.g. another user's process)
- L319 `test_process_already_gone_counts_as_stopped(self, capsys)` (method) — ProcessLookupError on the initial SIGTERM means the process
- L336 `TestKillStaleDashboardWindows` (class) — Kill path on Windows: taskkill /F.
- L339 `test_taskkill_invoked_for_each_pid(self, monkeypatch, capsys)` (method)
- L364 `test_taskkill_failure_is_reported(self, monkeypatch, capsys)` (method)
- L381 `TestBackCompatAlias` (class) — ``_warn_stale_dashboard_processes`` is kept as an alias for the
- L385 `test_alias_is_the_kill_function(self)` (method)
- L389 `TestWindowsWmicEncoding` (class) — Regression tests for #17049 — the Windows wmic branch must not crash
- L394 `test_wmic_invoked_with_utf8_ignore_errors(self, monkeypatch)` (method) — The wmic subprocess.run call must pass encoding='utf-8' and
- L424 `test_wmic_returns_none_stdout_does_not_crash(self, monkeypatch)` (method) — If subprocess.run returns successfully but stdout is None — which
