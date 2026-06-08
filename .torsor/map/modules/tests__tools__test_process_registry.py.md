---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_process_registry.py

Symbols in `tests/tools/test_process_registry.py`.

- L22 `registry()` (function) — Create a fresh ProcessRegistry.
- L27 `_make_session(sid='proc_test123', command='echo hello', task_id='t1', exited=False, exit_code=None, output='', started_at=None)` (function) — Helper to create a ProcessSession for testing.
- L49 `_spawn_python_sleep(seconds: float)` (function) — Spawn a portable short-lived Python sleep process.
- L56 `_wait_until(predicate, timeout: float=5.0, interval: float=0.05)` (function) — Poll a predicate until it returns truthy or the timeout elapses.
- L70 `TestGetAndPoll` (class)
- L71 `test_get_not_found(self, registry)` (method)
- L74 `test_get_running(self, registry)` (method)
- L79 `test_get_finished(self, registry)` (method)
- L84 `test_poll_not_found(self, registry)` (method)
- L88 `test_poll_running(self, registry)` (method)
- L96 `test_poll_exited(self, registry)` (method)
- L109 `TestOrphanedPipeReconciliation` (class) — Regression tests for issue #17327.
- L122 `test_reconcile_flips_exited_when_direct_child_done(self, registry)` (method) — Direct child exited but reader thread is blocked on orphaned pipe.
- L167 `test_reconcile_noop_when_child_still_running(self, registry)` (method) — Reconcile must NOT flip exited when the direct child is alive.
- L182 `test_reconcile_noop_on_already_exited(self, registry)` (method) — Reconcile is a no-op when session.exited is already True.
- L193 `test_reconcile_noop_on_no_process(self, registry)` (method) — Reconcile is a no-op for sessions without a local Popen (env/PTY).
- L201 `test_wait_returns_when_reader_blocked(self, registry)` (method) — wait() must also reconcile — not just poll().
- L236 `TestReadLog` (class)
- L237 `test_not_found(self, registry)` (method)
- L241 `test_read_full_log(self, registry)` (method)
- L248 `test_read_with_limit(self, registry)` (method)
- L256 `test_read_with_offset(self, registry)` (method)
- L268 `TestStdinHelpers` (class)
- L269 `test_close_stdin_not_found(self, registry)` (method)
- L273 `test_close_stdin_pipe_mode(self, registry)` (method)
- L285 `test_close_stdin_pty_mode(self, registry)` (method)
- L296 `test_close_stdin_allows_eof_driven_process_to_finish(self, registry, tmp_path)` (method) — PTY mode: writing data + sending EOF lets an EOF-driven child finish.
- L333 `TestListSessions` (class)
- L334 `test_empty(self, registry)` (method)
- L337 `test_lists_running_and_finished(self, registry)` (method)
- L345 `test_filter_by_task_id(self, registry)` (method)
- L354 `test_list_entry_fields(self, registry)` (method)
- L369 `TestActiveQueries` (class)
- L370 `test_has_active_processes(self, registry)` (method)
- L376 `test_has_active_for_session(self, registry)` (method)
- L383 `test_exited_not_active(self, registry)` (method)
- L393 `TestPruning` (class)
- L394 `test_prune_expired_finished(self, registry)` (method)
- L404 `test_prune_keeps_recent(self, registry)` (method)
- L410 `test_prune_over_max_removes_oldest(self, registry)` (method)
- L433 `TestSpawnEnvSanitization` (class)
- L434 `test_spawn_local_strips_blocked_vars_from_background_env(self, registry)` (method)
- L476 `test_spawn_via_env_uses_backend_temp_dir_for_artifacts(self, registry)` (method)
- L504 `test_spawn_via_env_checks_returncode_when_wrapper_fails(self, registry)` (method)
- L528 `test_spawn_via_env_disables_rewrite_for_bg_wrapper(self, registry)` (method)
- L550 `test_env_poller_quotes_temp_paths_with_spaces(self, registry)` (method)
- L588 `TestPopenLeakOnSetupFailure` (class) — Regression for issue #2749: subprocess orphaned when post-Popen setup raises.
- L591 `test_popen_killed_when_thread_creation_fails(self, registry)` (method) — If Thread() raises after Popen, proc must be killed — not orphaned.
- L628 `test_popen_killed_when_write_checkpoint_fails(self, registry)` (method) — If _write_checkpoint raises after Popen, proc must still be killed.
- L660 `test_popen_not_killed_on_success(self, registry)` (method) — Successful spawn must NOT kill the process.
- L692 `TestCheckpoint` (class)
- L693 `test_write_checkpoint(self, registry, tmp_path)` (method)
- L703 `test_recover_no_file(self, registry, tmp_path)` (method)
- L707 `test_recover_dead_pid(self, registry, tmp_path)` (method)
- L719 `test_write_checkpoint_includes_watcher_metadata(self, registry, tmp_path)` (method)
- L740 `test_recover_enqueues_watchers(self, registry, tmp_path)` (method)
- L768 `test_recover_skips_watcher_when_no_interval(self, registry, tmp_path)` (method)
- L782 `test_recovery_keeps_live_checkpoint_entries(self, registry, tmp_path)` (method)
- L803 `test_recovery_skips_explicit_sandbox_backed_entries(self, registry, tmp_path)` (method)
- L822 `test_detached_recovered_process_eventually_exits(self, registry, tmp_path)` (method)
- L869 `TestKillProcess` (class)
- L870 `test_kill_not_found(self, registry)` (method)
- L874 `test_kill_already_exited(self, registry)` (method)
- L880 `test_kill_detached_session_uses_host_pid(self, registry)` (method)
- L918 `TestProcessToolHandler` (class)
- L919 `test_list_action(self)` (method)
- L924 `test_poll_missing_session_id(self)` (method)
- L929 `test_unknown_action(self)` (method)
- L942 `test_format_completion_event()` (function)
- L957 `test_format_watch_match_event()` (function)
- L971 `test_format_watch_match_with_suppressed()` (function)
- L984 `test_format_watch_disabled_event()` (function)
- L993 `test_format_returns_none_for_empty_event()` (function)
- L1000 `test_drain_notifications_returns_pending_events()` (function)
- L1036 `test_drain_notifications_skips_consumed()` (function)
- L1060 `test_drain_notifications_empty_queue()` (function)
- L1075 `TestTerminateHostPidWindows` (class) — Windows branch uses ``taskkill /T /F`` — the documented MS tree-kill
- L1084 `test_windows_invokes_taskkill_with_tree_and_force_flags(self, monkeypatch)` (method) — The Windows branch must shell out to ``taskkill /PID N /T /F``.
- L1106 `test_windows_falls_back_to_os_kill_when_taskkill_missing(self, monkeypatch)` (method) — If ``taskkill.exe`` is somehow unavailable, fall back to a bare
- L1127 `test_windows_does_not_call_psutil(self, monkeypatch)` (method) — The Windows branch must NOT exercise the psutil tree-walk
- L1160 `TestTerminateHostPidPosix` (class) — POSIX branch walks the tree via psutil and SIGTERMs children first.
- L1163 `test_posix_walks_tree_and_terminates_children_then_parent(self, monkeypatch)` (method)
- L1196 `test_posix_no_such_process_swallowed(self, monkeypatch)` (method)
- L1209 `test_posix_oserror_falls_back_to_os_kill(self, monkeypatch)` (method)
