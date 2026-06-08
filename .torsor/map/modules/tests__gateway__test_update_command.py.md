---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_update_command.py

Symbols in `tests/gateway/test_update_command.py`.

- L18 `_make_event(text='/update', platform=Platform.TELEGRAM, user_id='12345', chat_id='67890', thread_id=None)` (function) — Build a MessageEvent for testing.
- L31 `_make_runner()` (function) — Create a bare GatewayRunner without calling __init__.
- L45 `TestHandleUpdateCommand` (class) — Tests for GatewayRunner._handle_update_command.
- L49 `test_managed_install_returns_package_manager_guidance(self, monkeypatch)` (method)
- L60 `test_no_git_directory(self, tmp_path)` (method) — Returns an error when .git does not exist.
- L100 `test_no_hermes_binary(self, tmp_path)` (method) — Returns error when hermes is not on PATH and hermes_cli is not importable.
- L123 `test_fallback_to_sys_executable(self, tmp_path)` (method) — Falls back to sys.executable -m hermes_cli.main when hermes not on PATH.
- L154 `test_resolve_hermes_bin_prefers_which(self, tmp_path)` (method) — _resolve_hermes_bin returns argv parts from shutil.which when available.
- L164 `test_resolve_hermes_bin_fallback(self)` (method) — _resolve_hermes_bin falls back to sys.executable argv when which fails.
- L177 `test_resolve_hermes_bin_returns_none_when_both_fail(self)` (method) — _resolve_hermes_bin returns None when both strategies fail.
- L188 `test_writes_pending_marker(self, tmp_path)` (method) — Writes .update_pending.json with correct platform and chat info.
- L220 `test_writes_pending_marker_with_thread_id(self, tmp_path)` (method) — Persists thread_id so update notifications can route back to the thread.
- L250 `test_spawns_setsid(self, tmp_path)` (method) — Uses setsid when available.
- L279 `test_fallback_when_no_setsid(self, tmp_path)` (method) — Falls back to start_new_session=True when setsid is not available.
- L319 `test_popen_failure_cleans_up(self, tmp_path)` (method) — Cleans up pending file and returns error on Popen failure.
- L345 `test_returns_user_friendly_message(self, tmp_path)` (method) — The success response is user-friendly.
- L373 `TestUpdateCommandPlatformGate` (class) — Tests for the platform-allowlist gate at the top of
- L383 `test_blocks_programmatic_interface(self, monkeypatch)` (method) — ``Platform.WEBHOOK`` is not a messaging platform and must be
- L400 `test_blocks_api_server_platform(self, monkeypatch)` (method) — ``Platform.API_SERVER`` (programmatic, not messaging) must be
- L413 `test_allows_plugin_platform_via_registry_fallback(self, monkeypatch)` (method) — A plugin-migrated platform (DISCORD) is no longer in
- L448 `test_allows_mattermost_via_registry_fallback(self, monkeypatch)` (method) — Same as DISCORD: MATTERMOST is now plugin-migrated and not in
- L472 `test_allows_homeassistant_via_registry_fallback(self, monkeypatch)` (method) — Same as DISCORD/MATTERMOST: HOMEASSISTANT is now plugin-migrated
- L497 `test_allows_builtin_platform_in_allowlist(self, monkeypatch)` (method) — ``Platform.TELEGRAM`` is in the hardcoded allowlist — gate
- L519 `TestSendUpdateNotification` (class) — Tests for GatewayRunner._send_update_notification.
- L523 `test_no_pending_file_is_noop(self, tmp_path)` (method) — Does nothing when no pending file exists.
- L534 `test_defers_notification_while_update_still_running(self, tmp_path)` (method) — Returns False and keeps marker files when the update has not exited yet.
- L557 `test_recovers_from_claimed_pending_file(self, tmp_path)` (method) — A claimed pending file from a crashed notifier is still deliverable.
- L581 `test_sends_notification_with_output(self, tmp_path)` (method) — Sends update output to the correct platform and chat.
- L614 `test_sends_notification_with_thread_metadata(self, tmp_path)` (method) — Final update notification preserves thread metadata when present.
- L646 `test_strips_ansi_codes(self, tmp_path)` (method) — ANSI escape codes are removed from output.
- L670 `test_truncates_long_output(self, tmp_path)` (method) — Output longer than 3500 chars is truncated.
- L694 `test_sends_failure_message_when_update_fails(self, tmp_path)` (method) — Non-zero exit codes produce a failure notification with captured output.
- L717 `test_sends_generic_message_when_no_output(self, tmp_path)` (method) — Sends a success message even if the output file is missing.
- L738 `test_cleans_up_files_after_notification(self, tmp_path)` (method) — Both marker and output files are deleted after notification.
- L764 `test_cleans_up_on_error(self, tmp_path)` (method) — Files are cleaned up even if notification fails.
- L793 `test_handles_corrupt_pending_file(self, tmp_path)` (method) — Gracefully handles a malformed pending JSON file.
- L810 `test_no_adapter_for_platform_preserves_markers(self, tmp_path)` (method) — A finished update whose platform is offline keeps its markers.
- L848 `test_deferred_notification_delivers_after_reconnect(self, tmp_path)` (method) — A deferred completion is delivered once the platform reconnects.
- L898 `TestUpdateInHelp` (class) — Verify /update appears in help text and known commands set.
- L902 `test_update_in_help_output(self)` (method) — The /help output includes /update.
- L909 `test_update_is_known_command(self)` (method) — The /update command is in the help text (proxy for _known_commands).
