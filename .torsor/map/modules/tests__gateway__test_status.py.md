---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_status.py

Symbols in `tests/gateway/test_status.py`.

- L11 `TestGatewayPidState` (class)
- L12 `test_write_pid_file_records_gateway_metadata(self, tmp_path, monkeypatch)` (method)
- L23 `test_write_pid_file_is_atomic_against_concurrent_writers(self, tmp_path, monkeypatch)` (method) — Regression: two concurrent --replace invocations must not both win.
- L47 `test_get_running_pid_rejects_live_non_gateway_pid(self, tmp_path, monkeypatch)` (method)
- L55 `test_get_running_pid_cleans_stale_record_from_dead_process(self, tmp_path, monkeypatch)` (method)
- L78 `test_get_running_pid_accepts_gateway_metadata_when_cmdline_unavailable(self, tmp_path, monkeypatch)` (method)
- L98 `test_get_running_pid_accepts_script_style_gateway_cmdline(self, tmp_path, monkeypatch)` (method)
- L122 `test_get_running_pid_accepts_explicit_pid_path_without_cleanup(self, tmp_path, monkeypatch)` (method)
- L149 `test_runtime_lock_claims_and_releases_liveness(self, tmp_path, monkeypatch)` (method)
- L160 `test_get_running_pid_treats_pid_file_as_stale_without_runtime_lock(self, tmp_path, monkeypatch)` (method)
- L177 `test_get_running_pid_cleans_stale_metadata_from_dead_foreign_pid(self, tmp_path, monkeypatch)` (method) — Stale PID file from a *different* PID (crashed process) must still be cleaned.
- L211 `test_get_running_pid_falls_back_to_live_lock_record(self, tmp_path, monkeypatch)` (method)
- L248 `TestGatewayRuntimeStatus` (class)
- L249 `test_write_json_file_uses_atomic_json_write(self, tmp_path, monkeypatch)` (method)
- L270 `test_write_runtime_status_overwrites_stale_pid_on_restart(self, tmp_path, monkeypatch)` (method) — Regression: setdefault() preserved stale PID from previous process (#1631).
- L290 `test_write_runtime_status_overwrites_stale_argv_on_restart(self, tmp_path, monkeypatch)` (method) — Regression: gateway_state.json must not keep the previous launch argv.
- L314 `test_write_runtime_status_records_platform_failure(self, tmp_path, monkeypatch)` (method)
- L333 `test_write_runtime_status_explicit_none_clears_stale_fields(self, tmp_path, monkeypatch)` (method)
- L362 `TestTerminatePid` (class)
- L363 `test_force_uses_taskkill_on_windows(self, monkeypatch)` (method)
- L379 `test_force_falls_back_to_sigterm_when_taskkill_missing(self, monkeypatch)` (method)
- L397 `TestScopedLocks` (class)
- L398 `test_windows_file_lock_uses_high_offset(self, tmp_path, monkeypatch)` (method)
- L427 `test_acquire_scoped_lock_rejects_live_other_process(self, tmp_path, monkeypatch)` (method)
- L447 `test_acquire_scoped_lock_replaces_pid_reused_by_unrelated_process(self, tmp_path, monkeypatch)` (method) — macOS regression: PID reused by an unrelated process with start_time=None.
- L482 `test_acquire_scoped_lock_keeps_lock_when_cmdline_unreadable_but_record_is_gateway(self, tmp_path, monkeypatch)` (method) — Windows regression: ps unavailable so cmdline cannot be read.
- L513 `test_acquire_scoped_lock_keeps_lock_when_pid_reused_by_gateway(self, tmp_path, monkeypatch)` (method) — When start_time is None but the live PID still looks like a gateway, keep the lock.
- L534 `test_acquire_scoped_lock_replaces_stale_record(self, tmp_path, monkeypatch)` (method)
- L554 `test_acquire_scoped_lock_recovers_empty_lock_file(self, tmp_path, monkeypatch)` (method) — Empty lock file (0 bytes) left by a crashed process should be treated as stale.
- L568 `test_acquire_scoped_lock_recovers_corrupt_lock_file(self, tmp_path, monkeypatch)` (method) — Lock file with invalid JSON should be treated as stale.
- L581 `test_release_scoped_lock_only_removes_current_owner(self, tmp_path, monkeypatch)` (method)
- L592 `test_release_all_scoped_locks_can_target_single_owner(self, tmp_path, monkeypatch)` (method)
- L619 `test_release_all_scoped_locks_skips_pid_reuse_mismatch(self, tmp_path, monkeypatch)` (method)
- L640 `TestTakeoverMarker` (class) — Tests for the --replace takeover marker.
- L649 `test_write_marker_records_target_identity(self, tmp_path, monkeypatch)` (method)
- L664 `test_consume_returns_true_when_marker_names_self(self, tmp_path, monkeypatch)` (method) — Primary happy path: planned takeover is recognised.
- L679 `test_consume_returns_false_for_different_pid(self, tmp_path, monkeypatch)` (method) — A marker naming a DIFFERENT process must not be consumed as ours.
- L696 `test_consume_returns_false_on_start_time_mismatch(self, tmp_path, monkeypatch)` (method) — PID reuse defence: old marker's start_time mismatches current process.
- L710 `test_consume_returns_true_on_windows_when_start_time_unavailable(self, tmp_path, monkeypatch)` (method) — Takeover consume must also recognise a self-marker on platforms
- L737 `test_consume_returns_false_when_marker_missing(self, tmp_path, monkeypatch)` (method)
- L744 `test_consume_returns_false_for_stale_marker(self, tmp_path, monkeypatch)` (method) — A marker older than 60s must be ignored.
- L766 `test_consume_handles_malformed_marker_gracefully(self, tmp_path, monkeypatch)` (method)
- L776 `test_consume_handles_marker_with_missing_fields(self, tmp_path, monkeypatch)` (method)
- L787 `test_clear_takeover_marker_is_idempotent(self, tmp_path, monkeypatch)` (method)
- L804 `test_write_marker_returns_false_on_write_failure(self, tmp_path, monkeypatch)` (method) — write_takeover_marker is best-effort; returns False but doesn't raise.
- L817 `test_consume_ignores_marker_for_different_process_and_prevents_stale_grief(self, tmp_path, monkeypatch)` (method) — Regression: a stale marker from a dead replacer naming a dead
- L845 `TestPlannedStopMarker` (class) — Tests for intentional service/manual gateway stop markers.
- L848 `test_write_marker_records_target_identity(self, tmp_path, monkeypatch)` (method)
- L863 `test_consume_returns_true_when_marker_names_self(self, tmp_path, monkeypatch)` (method)
- L874 `test_consume_returns_false_for_different_pid(self, tmp_path, monkeypatch)` (method)
- L885 `test_consume_returns_false_for_stale_marker(self, tmp_path, monkeypatch)` (method)
- L904 `test_clear_planned_stop_marker_is_idempotent(self, tmp_path, monkeypatch)` (method)
- L917 `test_write_marker_returns_false_on_write_failure(self, tmp_path, monkeypatch)` (method)
- L929 `test_consume_returns_true_on_windows_when_start_time_unavailable(self, tmp_path, monkeypatch)` (method) — Regression for #34597: a legitimate stop must be recognised on
- L959 `test_consume_still_rejects_foreign_pid_when_start_time_unavailable(self, tmp_path, monkeypatch)` (method) — The PID-only fallback must NOT match a marker naming another PID.
- L977 `test_consume_still_rejects_start_time_mismatch_when_both_known(self, tmp_path, monkeypatch)` (method) — PID-reuse defence is preserved when BOTH start_times are present.
- L998 `TestReadProcessCmdlinePsFallback` (class) — Tests for _read_process_cmdline falling back to ps on non-Linux.
- L1001 `test_ps_fallback_when_proc_unavailable(self, monkeypatch)` (method)
- L1010 `test_ps_fallback_returns_none_on_failure(self, monkeypatch)` (method)
- L1019 `test_proc_cmdline_takes_priority_over_ps(self, monkeypatch)` (method)
- L1031 `test_ps_fallback_used_when_proc_returns_empty(self, monkeypatch)` (method)
- L1041 `TestCorruptStatusFiles` (class) — A status / pid file holding non-UTF-8 (binary) bytes must read as
- L1045 `test_read_json_file_returns_none_on_binary_garbage(self, tmp_path)` (method)
- L1050 `test_read_json_file_still_parses_valid_json(self, tmp_path)` (method)
- L1055 `test_read_pid_record_returns_none_on_binary_garbage(self, tmp_path)` (method)
- L1060 `test_read_pid_record_still_parses_bare_pid(self, tmp_path)` (method)
