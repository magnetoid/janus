---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_zombie_process_cleanup.py

Symbols in `tests/tools/test_zombie_process_cleanup.py`.

- L16 `_spawn_sleep(seconds: float=60)` (function) — Spawn a portable long-lived Python sleep process (no shell wrapper).
- L23 `_pid_alive(pid: int)` (function) — Return True if a process with the given PID is still running.
- L32 `TestZombieReproduction` (class) — Demonstrate that subprocesses survive when cleanup is not called.
- L35 `test_orphaned_processes_survive_without_cleanup(self)` (method) — REPRODUCTION: processes spawned directly survive if no one kills
- L65 `test_explicit_terminate_reaps_processes(self)` (method) — Explicitly terminating+waiting on Popen handles works.
- L95 `TestAgentCloseMethod` (class) — Verify AIAgent.close() exists, is idempotent, and calls cleanup.
- L98 `test_close_calls_cleanup_functions(self)` (method) — close() should call kill_all, cleanup_vm, cleanup_browser.
- L121 `test_close_is_idempotent(self)` (method) — close() can be called multiple times without error.
- L137 `test_close_propagates_to_children(self)` (method) — close() should call close() on all active child agents.
- L158 `test_close_survives_partial_failures(self)` (method) — close() continues cleanup even if one step fails.
- L185 `TestGatewayCleanupWiring` (class) — Verify gateway lifecycle calls close() on agents.
- L188 `test_gateway_stop_calls_close(self)` (method) — gateway stop() should call close() on all running agents.
- L244 `test_evict_does_not_call_close(self)` (method) — _evict_cached_agent() should NOT call close() — it's also used
- L264 `TestDelegationCleanup` (class) — Verify subagent delegation cleans up child agents.
- L267 `test_run_single_child_calls_close(self)` (method) — _run_single_child finally block should call close() on child.
