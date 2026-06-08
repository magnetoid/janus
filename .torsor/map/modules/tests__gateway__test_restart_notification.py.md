---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_restart_notification.py

Symbols in `tests/gateway/test_restart_notification.py`.

- L22 `test_restart_notification_pending_false_without_marker(tmp_path, monkeypatch)` (function)
- L28 `test_restart_notification_pending_true_with_marker(tmp_path, monkeypatch)` (function)
- L35 `test_planned_restart_notification_pending_roundtrip(tmp_path, monkeypatch)` (function)
- L52 `test_restart_command_writes_notify_file(tmp_path, monkeypatch)` (function) — When /restart fires, the requester's routing info is persisted to disk.
- L81 `test_restart_command_uses_service_restart_under_systemd(tmp_path, monkeypatch)` (function) — Under systemd (INVOCATION_ID set), /restart uses via_service=True.
- L102 `test_restart_command_uses_detached_without_systemd(tmp_path, monkeypatch)` (function) — Without systemd, /restart uses the detached subprocess approach.
- L123 `test_restart_command_preserves_thread_id(tmp_path, monkeypatch)` (function) — Thread ID is saved when the requester is in a threaded chat.
- L148 `test_restart_command_uses_atomic_json_writes_for_marker_files(tmp_path, monkeypatch)` (function)
- L178 `test_sethome_updates_running_config_for_same_process_restart(tmp_path, monkeypatch)` (function) — /sethome persists to env and updates in-memory config before restart.
- L210 `test_sethome_preserves_thread_target_for_same_process_restart(tmp_path, monkeypatch)` (function) — /sethome from a topic/thread stores the thread-aware home target.
- L246 `test_send_home_channel_startup_notification_to_configured_home(tmp_path, monkeypatch)` (function)
- L267 `test_send_home_channel_startup_notification_preserves_thread_metadata(tmp_path, monkeypatch)` (function)
- L306 `test_send_home_channel_startup_notification_skips_restart_target(tmp_path, monkeypatch)` (function)
- L328 `test_send_home_channel_startup_notification_does_not_skip_different_thread(tmp_path, monkeypatch)` (function)
- L350 `test_send_home_channel_startup_notification_ignores_false_send_result(tmp_path, monkeypatch)` (function)
- L373 `test_send_restart_notification_delivers_and_cleans_up(tmp_path, monkeypatch)` (function) — On startup, the notification is sent and the file is removed.
- L398 `test_send_restart_notification_with_thread(tmp_path, monkeypatch)` (function) — Thread ID is passed as metadata so the message lands in the right topic.
- L428 `test_send_restart_notification_noop_when_no_file(tmp_path, monkeypatch)` (function) — Nothing happens if there's no pending restart notification.
- L441 `test_send_restart_notification_skips_when_adapter_missing(tmp_path, monkeypatch)` (function) — If the requester's platform isn't connected, clean up without crashing.
- L460 `test_send_restart_notification_cleans_up_on_send_failure(tmp_path, monkeypatch)` (function) — If the adapter.send() raises, the file is still cleaned up.
- L483 `test_send_restart_notification_logs_warning_on_sendresult_failure(tmp_path, monkeypatch, caplog)` (function) — Adapter that returns SendResult(success=False) must log a WARNING, not INFO.
- L536 `test_send_home_channel_startup_notification_skipped_when_flag_disabled(tmp_path, monkeypatch)` (function) — Per-platform opt-out: gateway_restart_notification=False mutes the home-channel ping.
- L558 `test_send_home_channel_startup_notification_default_flag_true(tmp_path, monkeypatch)` (function) — Default behavior is unchanged: missing flag means notifications still fire.
- L583 `test_send_restart_notification_skipped_when_flag_disabled(tmp_path, monkeypatch)` (function) — The /restart originator's notification also honors the per-platform flag.
- L612 `test_send_restart_notification_logs_info_on_sendresult_success(tmp_path, monkeypatch, caplog)` (function) — Adapter returning SendResult(success=True) keeps the INFO log line.
- L645 `test_shutdown_notifications_use_cached_live_thread_source_when_origin_missing()` (function)
- L665 `test_restart_shutdown_notification_anchors_telegram_dm_topic()` (function)
