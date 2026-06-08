---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_orphan_reaper.py

Symbols in `tests/tools/test_browser_orphan_reaper.py`.

- L11 `fake_tmpdir(tmp_path)` (function) — Patch _socket_safe_tmpdir to return a temp dir we control.
- L18 `_isolate_sessions()` (function) — Ensure _active_sessions is empty for each test.
- L28 `_make_socket_dir(tmpdir, session_name, pid=None, owner_pid=None)` (function) — Create a fake agent-browser socket directory with optional PID files.
- L47 `TestReapOrphanedBrowserSessions` (class) — Tests for the orphan reaper function.
- L50 `test_no_socket_dirs_is_noop(self, fake_tmpdir)` (method) — No socket dirs => nothing happens, no errors.
- L55 `test_stale_dir_without_pid_file_is_removed(self, fake_tmpdir)` (method) — Socket dir with no PID file is cleaned up.
- L63 `test_stale_dir_with_dead_pid_is_removed(self, fake_tmpdir)` (method) — Socket dir whose daemon PID is dead gets cleaned up.
- L71 `test_orphaned_alive_daemon_is_killed(self, fake_tmpdir)` (method) — Alive daemon not tracked by _active_sessions is terminated (legacy path).
- L94 `test_tracked_session_is_not_reaped(self, fake_tmpdir)` (method) — Sessions tracked in _active_sessions are left alone (legacy path).
- L118 `test_alive_legacy_daemon_is_reaped(self, fake_tmpdir)` (method) — Alive, untracked, legacy (no owner_pid) daemon is reaped.
- L145 `test_cdp_sessions_are_also_reaped(self, fake_tmpdir)` (method) — CDP sessions (cdp_ prefix) are also scanned.
- L155 `test_non_hermes_dirs_are_ignored(self, fake_tmpdir)` (method) — Socket dirs that don't match our naming pattern are left alone.
- L169 `test_corrupt_pid_file_is_cleaned(self, fake_tmpdir)` (method) — PID file with non-integer content is cleaned up.
- L180 `TestOwnerPidCrossProcess` (class) — Tests for owner_pid-based cross-process safe reaping.
- L188 `test_alive_owner_is_not_reaped_even_when_untracked(self, fake_tmpdir)` (method) — Daemon with alive owner_pid is NOT reaped, even if not in our _active_sessions.
- L214 `test_dead_owner_triggers_reap(self, fake_tmpdir)` (method) — Daemon whose owner_pid is dead gets reaped.
- L238 `test_corrupt_owner_pid_falls_back_to_legacy(self, fake_tmpdir)` (method) — Corrupt owner_pid file → fall back to tracked_names check.
- L264 `test_owner_pid_permission_error_treated_as_alive(self, fake_tmpdir)` (method) — Owner PID owned by another user → treat as alive.
- L292 `test_write_owner_pid_creates_file_with_current_pid(self, fake_tmpdir, monkeypatch)` (method) — _write_owner_pid(dir, session) writes <session>.owner_pid with os.getpid().
- L308 `test_write_owner_pid_is_idempotent(self, fake_tmpdir)` (method) — Calling _write_owner_pid twice leaves a single owner_pid file.
- L323 `test_write_owner_pid_swallows_oserror(self, fake_tmpdir, monkeypatch)` (method) — OSError (e.g. permission denied) doesn't propagate — the reaper
- L337 `test_run_browser_command_calls_write_owner_pid(self, fake_tmpdir, monkeypatch)` (method) — _run_browser_command wires _write_owner_pid after mkdir.
- L383 `TestEmergencyCleanupRunsReaper` (class) — Verify atexit-registered cleanup sweeps orphans even without an active session.
- L386 `test_emergency_cleanup_calls_reaper(self, fake_tmpdir, monkeypatch)` (method) — _emergency_cleanup_all_sessions must call _reap_orphaned_browser_sessions.
