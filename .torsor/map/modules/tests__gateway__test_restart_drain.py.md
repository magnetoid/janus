---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_restart_drain.py

Symbols in `tests/gateway/test_restart_drain.py`.

- L18 `test_restart_command_while_busy_requests_drain_without_interrupt(monkeypatch)` (function)
- L51 `test_drain_queue_mode_queues_follow_up_without_interrupt()` (function)
- L75 `test_draining_rejects_new_session_messages()` (function)
- L92 `test_load_busy_input_mode_prefers_env_then_config_then_default(tmp_path, monkeypatch)` (function)
- L119 `test_load_busy_text_mode_follows_input_mode_and_honors_legacy(tmp_path, monkeypatch)` (function)
- L152 `test_load_restart_drain_timeout_prefers_env_then_config_then_default(tmp_path, monkeypatch, caplog)` (function)
- L180 `test_request_restart_is_idempotent()` (function)
- L196 `test_launch_detached_restart_command_uses_setsid(monkeypatch)` (function)
- L226 `test_shutdown_notification_sent_to_active_sessions()` (function) — Active sessions receive a notification when the gateway starts shutting down.
- L241 `test_shutdown_notification_says_restarting_when_restart_requested()` (function) — When _restart_requested is True, the message says 'restarting' and mentions /retry.
- L256 `test_shutdown_notification_deduplicates_per_chat()` (function) — Multiple sessions in the same chat only get one notification.
- L269 `test_shutdown_notification_skipped_when_no_active_agents()` (function) — No notification is sent when there are no active agents.
- L279 `test_shutdown_notification_ignores_pending_sentinels()` (function) — Pending sentinels (not-yet-started agents) don't trigger notifications.
- L292 `test_shutdown_notification_send_failure_does_not_block()` (function) — If sending a notification fails, the method still completes.
- L304 `test_shutdown_notification_suppressed_when_flag_disabled()` (function) — Active-session ping is muted when gateway_restart_notification=False on the platform.
- L320 `test_shutdown_notification_home_channel_suppressed_when_flag_disabled()` (function) — Home-channel ping during shutdown is muted when the flag is False.
- L338 `test_shutdown_notification_uses_persisted_origin_for_colon_ids()` (function) — Shutdown notifications should route from persisted origin, not reparsed keys.
