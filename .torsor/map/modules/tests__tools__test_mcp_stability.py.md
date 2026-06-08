---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_stability.py

Symbols in `tests/tools/test_mcp_stability.py`.

- L16 `TestMCPLoopExceptionHandler` (class) — _mcp_loop_exception_handler suppresses benign 'Event loop is closed'.
- L19 `test_suppresses_event_loop_closed(self)` (method)
- L27 `test_forwards_other_runtime_errors(self)` (method)
- L34 `test_forwards_non_runtime_errors(self)` (method)
- L41 `test_forwards_contexts_without_exception(self)` (method)
- L48 `test_handler_installed_on_mcp_loop(self)` (method) — _ensure_mcp_loop installs the exception handler on the new loop.
- L65 `TestStdioPidTracking` (class) — _snapshot_child_pids and _stdio_pids track subprocess PIDs.
- L68 `test_snapshot_returns_set(self)` (method)
- L76 `test_stdio_pids_starts_empty(self)` (method)
- L82 `test_kill_orphaned_noop_when_empty(self)` (method) — _kill_orphaned_mcp_children does nothing when no PIDs tracked.
- L98 `test_kill_orphaned_handles_dead_pids(self)` (method) — _kill_orphaned_mcp_children gracefully handles already-dead PIDs.
- L117 `test_kill_orphaned_uses_sigkill_when_available(self, monkeypatch)` (method) — SIGTERM-first then SIGKILL after 2s for orphan cleanup.
- L150 `test_kill_orphaned_falls_back_without_sigkill(self, monkeypatch)` (method) — Without SIGKILL, SIGTERM is used for both phases.
- L187 `TestStdioPgroupReaping` (class) — _kill_orphaned_mcp_children reaps via killpg when a pgid is tracked.
- L190 `_reset_state(self)` (method)
- L197 `test_killpg_used_when_pgid_tracked(self, monkeypatch)` (method) — SIGTERM and SIGKILL route through killpg when pgid is known.
- L237 `test_killpg_failure_falls_back_to_kill(self, monkeypatch)` (method) — If killpg raises ProcessLookupError (pgroup gone), try os.kill.
- L274 `test_no_pgid_uses_per_pid_kill(self, monkeypatch)` (method) — When no pgid is recorded (e.g. Windows), fall back to os.kill.
- L305 `test_grandchild_reaped_via_pgroup(self, tmp_path)` (method) — End-to-end: parent spawns grandchild, parent exits, killpg reaps grandchild.
- L396 `TestMCPReloadTimeout` (class) — _check_config_mcp_changes uses a timeout on _reload_mcp.
- L399 `test_reload_timeout_does_not_block_forever(self, tmp_path, monkeypatch)` (method) — If _reload_mcp hangs, the config watcher times out and returns.
- L435 `TestMCPInitialConnectionRetry` (class) — MCPServerTask.run() retries initial connection failures instead of giving up.
- L438 `test_initial_connect_retries_constant_exists(self)` (method) — _MAX_INITIAL_CONNECT_RETRIES should be defined.
- L443 `test_initial_connect_retry_succeeds_on_second_attempt(self)` (method) — Server succeeds after one transient initial failure.
- L479 `test_initial_connect_gives_up_after_max_retries(self)` (method) — Server gives up after _MAX_INITIAL_CONNECT_RETRIES failures.
- L508 `test_initial_connect_retry_respects_shutdown(self)` (method) — Shutdown during initial retry backoff aborts cleanly.
