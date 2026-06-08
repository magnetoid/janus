---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_whatsapp_connect.py

Symbols in `tests/gateway/test_whatsapp_connect.py`.

- L28 `_AsyncCM` (class) — Minimal async context manager returning a fixed value.
- L31 `__init__(self, value)` (method)
- L34 `__aenter__(self)` (method)
- L37 `__aexit__(self, *exc)` (method)
- L41 `_make_adapter()` (function) — Create a WhatsAppAdapter with test attributes (bypass __init__).
- L70 `_mock_aiohttp(status=200, json_data=None, json_side_effect=None)` (function) — Build a mock ``aiohttp.ClientSession`` returning a fixed response.
- L85 `_connect_patches(mock_proc, mock_fh, mock_client_cls=None)` (function) — Return a dict of common patches needed to reach the health-check loop.
- L110 `TestCloseBridgeLog` (class) — Direct tests for the _close_bridge_log() helper method.
- L114 `_bare_adapter()` (method)
- L120 `test_closes_open_handle(self)` (method)
- L130 `test_noop_when_no_handle(self)` (method)
- L137 `test_suppresses_close_exception(self)` (method)
- L152 `TestDataInitialized` (class) — Verify ``data = {}`` prevents NameError when resp.json() fails.
- L156 `test_no_name_error_when_json_always_fails(self)` (method) — HTTP 200 sets http_ready but json() always raises.
- L190 `TestFileHandleClosedOnError` (class) — Verify the bridge log file handle is closed on every failure path.
- L194 `test_closed_when_bridge_dies_phase1(self)` (method) — Bridge process exits during Phase 1 health-check loop.
- L214 `TestConnectCleanup` (class) — Verify failure paths release the scoped session lock.
- L218 `test_releases_lock_when_npm_install_fails(self)` (method)
- L238 `TestBridgeRuntimeFailure` (class) — Verify runtime bridge death is surfaced as a fatal adapter error.
- L242 `test_send_marks_retryable_fatal_when_managed_bridge_exits(self)` (method)
- L266 `test_poll_messages_marks_retryable_fatal_when_managed_bridge_exits(self)` (method)
- L289 `test_shutdown_suppresses_fatal_on_planned_bridge_exit(self, returncode)` (method) — During graceful disconnect(), SIGTERM/SIGINT/clean-exit are NOT fatal.
- L321 `test_shutdown_still_surfaces_nonzero_crash(self)` (method) — Even during shutdown, a truly crashed bridge (e.g. returncode 9) is fatal.
- L348 `test_closed_when_http_not_ready(self)` (method) — Health endpoint never returns 200 within 15 attempts.
- L368 `test_closed_when_bridge_dies_phase2(self)` (method) — Bridge alive during Phase 1 but dies during Phase 2.
- L399 `test_closed_on_unexpected_exception(self)` (method) — Popen raises, outer except block must still close the handle.
- L422 `TestKillPortProcess` (class) — Verify _kill_port_process uses platform-appropriate commands.
- L425 `test_uses_netstat_and_taskkill_on_windows(self)` (method)
- L457 `test_does_not_kill_wrong_port_on_windows(self)` (method)
- L475 `test_uses_fuser_on_linux(self)` (method)
- L488 `test_skips_fuser_kill_when_port_free(self)` (method)
- L501 `test_suppresses_exceptions(self)` (method)
- L513 `TestHttpSessionLifecycle` (class) — Verify persistent aiohttp.ClientSession is created and cleaned up.
- L517 `test_disconnect_uses_taskkill_tree_on_windows(self)` (method) — Windows disconnect should target the bridge process tree, not just the parent PID.
- L544 `test_session_closed_on_disconnect(self)` (method) — disconnect() should close self._http_session.
- L561 `test_session_not_closed_when_already_closed(self)` (method) — disconnect() should skip close() when session is already closed.
- L578 `test_poll_task_cancelled_on_disconnect(self)` (method) — disconnect() should cancel the poll task.
- L599 `test_disconnect_skips_done_poll_task(self)` (method) — disconnect() should not cancel an already-done poll task.
- L621 `TestNoCredsPreflight` (class) — Verify ``connect()`` fast-fails as non-retryable when WhatsApp is
- L636 `test_connect_returns_false_when_no_creds(self, tmp_path)` (method)
- L668 `test_connect_proceeds_when_creds_present(self, tmp_path)` (method) — When creds.json exists, the preflight check is bypassed and
