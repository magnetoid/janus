---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_gateway_shutdown.py

Symbols in `tests/gateway/test_gateway_shutdown.py`.

- L15 `test_cancel_background_tasks_cancels_inflight_message_processing()` (function)
- L40 `test_cleanup_agent_resources_reaps_stale_aux_clients()` (function)
- L53 `test_gateway_stop_interrupts_running_agents_and_cancels_adapter_tasks()` (function)
- L95 `test_gateway_stop_drains_running_agents_before_disconnect()` (function)
- L118 `test_gateway_stop_interrupts_after_drain_timeout()` (function)
- L137 `test_gateway_stop_systemd_service_restart_exits_cleanly(tmp_path, monkeypatch)` (function)
- L153 `test_gateway_stop_launchd_service_restart_keeps_nonzero_exit(tmp_path, monkeypatch)` (function)
- L167 `test_restart_shutdown_warning_uses_restart_command_reply_anchor_for_active_session()` (function)
- L197 `test_in_chat_restart_skips_home_shutdown_even_with_active_session()` (function)
- L223 `test_idle_in_chat_restart_does_not_send_interruption_warning()` (function)
- L242 `test_in_chat_restart_does_not_write_home_startup_marker(tmp_path, monkeypatch)` (function)
- L259 `test_drain_active_agents_throttles_status_updates()` (function)
- L281 `test_gateway_stop_kills_tool_subprocesses_before_adapter_disconnect_on_timeout(monkeypatch)` (function) — On drain timeout, tool subprocesses must be killed BEFORE adapter
- L334 `test_gateway_stop_kills_tool_subprocesses_on_graceful_path(monkeypatch)` (function) — Graceful shutdown (no drain timeout) must still kill tool subprocesses
