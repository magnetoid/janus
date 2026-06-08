---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_clean_shutdown_marker.py

Symbols in `tests/gateway/test_clean_shutdown_marker.py`.

- L22 `_make_source(platform=Platform.TELEGRAM, chat_id='123', user_id='u1')` (function)
- L26 `_make_store(tmp_path, policy=None)` (function)
- L37 `TestSuspendRecentlyActive` (class) — Verify suspend_recently_active only marks recent sessions.
- L40 `test_suspends_recently_active_sessions(self, tmp_path)` (method)
- L54 `test_does_not_suspend_old_sessions(self, tmp_path)` (method)
- L67 `test_already_resume_pending_not_double_counted(self, tmp_path)` (method)
- L89 `TestCleanShutdownMarker` (class) — Test that the marker file controls session suspension on startup.
- L92 `test_marker_written_on_graceful_stop(self, tmp_path, monkeypatch)` (method) — stop() should write .clean_shutdown marker.
- L134 `test_marker_skips_suspension_on_startup(self, tmp_path, monkeypatch)` (method) — If .clean_shutdown exists, suspend_recently_active should NOT be called.
- L163 `test_no_marker_triggers_suspension(self, tmp_path, monkeypatch)` (method) — Without .clean_shutdown marker (crash), suspension should fire.
- L188 `test_marker_written_on_restart_stop(self, tmp_path, monkeypatch)` (method) — stop(restart=True) should also write the marker.
