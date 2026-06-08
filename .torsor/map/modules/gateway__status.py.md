---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/status.py

Symbols in `gateway/status.py`.

- L44 `_get_pid_path()` (function) — Return the path to the gateway PID file, respecting HERMES_HOME.
- L50 `_get_gateway_lock_path(pid_path: Optional[Path]=None)` (function) — Return the path to the runtime gateway lock file.
- L58 `_get_runtime_status_path()` (function) — Return the persisted runtime health/status file path.
- L63 `_get_lock_dir()` (function) — Return the machine-local directory for token-scoped gateway locks.
- L72 `_utc_now_iso()` (function)
- L76 `terminate_pid(pid: int, *, force: bool=False)` (function) — Terminate a PID with platform-appropriate force semantics.
- L103 `_scope_hash(identity: str)` (function)
- L107 `_get_scope_lock_path(scope: str, identity: str)` (function)
- L111 `_get_process_start_time(pid: int)` (function) — Return the kernel start time for a process when available.
- L121 `get_process_start_time(pid: int)` (function) — Public wrapper for retrieving a process start time when available.
- L126 `_read_process_cmdline(pid: int)` (function) — Return the process command line as a space-separated string.
- L167 `_looks_like_gateway_process(pid: int)` (function) — Return True when the live PID still looks like the Hermes gateway.
- L183 `_record_looks_like_gateway(record: dict[str, Any])` (function) — Validate gateway identity from PID-file metadata when cmdline is unavailable.
- L203 `_build_pid_record()` (function)
- L212 `_build_runtime_status_record()` (function)
- L225 `_read_json_file(path: Path)` (function)
- L244 `_write_json_file(path: Path, payload: dict[str, Any])` (function)
- L248 `_read_pid_record(pid_path: Optional[Path]=None)` (function)
- L277 `_read_gateway_lock_record(lock_path: Optional[Path]=None)` (function)
- L281 `_pid_from_record(record: Optional[dict[str, Any]])` (function)
- L290 `_cleanup_invalid_pid_path(pid_path: Path, *, cleanup_stale: bool)` (function) — Delete a stale gateway PID file (and its sibling lock metadata).
- L312 `_write_gateway_lock_record(handle)` (function)
- L323 `_try_acquire_file_lock(handle)` (function)
- L339 `_pid_exists(pid: int)` (function) — Cross-platform "is this PID alive" check that does NOT kill the target.
- L414 `_release_file_lock(handle)` (function)
- L425 `acquire_gateway_runtime_lock()` (function) — Claim the cross-process runtime lock for the gateway.
- L446 `release_gateway_runtime_lock()` (function) — Release the gateway runtime lock when owned by this process.
- L460 `is_gateway_runtime_lock_active(lock_path: Optional[Path]=None)` (function) — Return True when some process currently owns the gateway runtime lock.
- L483 `write_pid_file()` (function) — Write the current process PID and metadata to the gateway PID file.
- L508 `write_runtime_status(*, gateway_state: Any=_UNSET, exit_reason: Any=_UNSET, restart_requested: Any=_UNSET, active_agents: Any=_UNSET, platform: Any=_UNSET, platform_state: Any=_UNSET, error_code: Any=_UNSET, error_message: Any=_UNSET)` (function) — Persist gateway runtime health information for diagnostics/status.
- L553 `read_runtime_status()` (function) — Read the persisted gateway runtime health/status information.
- L558 `remove_pid_file()` (function) — Remove the gateway PID file, but only if it belongs to this process.
- L582 `acquire_scoped_lock(scope: str, identity: str, metadata: Optional[dict[str, Any]]=None)` (function) — Acquire a machine-local lock keyed by scope + identity.
- L685 `release_scoped_lock(scope: str, identity: str)` (function) — Release a previously-acquired scope lock when owned by this process.
- L701 `release_all_scoped_locks(*, owner_pid: Optional[int]=None, owner_start_time: Optional[int]=None)` (function) — Remove scoped lock files in the lock directory.
- L771 `_get_takeover_marker_path()` (function) — Return the path to the --replace takeover marker file.
- L777 `_get_planned_stop_marker_path()` (function) — Return the path to the intentional gateway stop marker file.
- L783 `_marker_is_stale(written_at: str, ttl_s: int)` (function)
- L792 `_consume_pid_marker_for_self(path: Path, *, pid_field: str, start_time_field: str, ttl_s: int)` (function)
- L850 `write_takeover_marker(target_pid: int)` (function) — Record that ``target_pid`` is being replaced by the current process.
- L875 `consume_takeover_marker_for_self()` (function) — Check & unlink the takeover marker if it names the current process.
- L894 `clear_takeover_marker()` (function) — Remove the takeover marker unconditionally. Safe to call repeatedly.
- L902 `write_planned_stop_marker(target_pid: int)` (function) — Record that ``target_pid`` is being stopped intentionally.
- L923 `consume_planned_stop_marker_for_self()` (function) — Return True when the current process is being intentionally stopped.
- L933 `planned_stop_marker_targets_self()` (function) — Return True only when a live planned-stop marker names the current process.
- L995 `clear_planned_stop_marker()` (function) — Remove the planned-stop marker unconditionally.
- L1003 `get_running_pid(pid_path: Optional[Path]=None, *, cleanup_stale: bool=True)` (function) — Return the PID of a running gateway instance, or ``None``.
- L1043 `is_gateway_running(pid_path: Optional[Path]=None, *, cleanup_stale: bool=True)` (function) — Check if the gateway daemon is currently running.
