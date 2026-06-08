---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/e2e/test_platform_commands.py

Symbols in `tests/e2e/test_platform_commands.py`.

- L23 `TestSlashCommands` (class) — Gateway slash commands dispatched through the full adapter pipeline.
- L27 `test_help_returns_command_list(self, adapter, platform)` (method)
- L36 `test_status_shows_session_info(self, adapter, platform)` (method)
- L44 `test_new_resets_session(self, adapter, runner, platform)` (method)
- L51 `test_stop_when_no_agent_running(self, adapter, platform)` (method)
- L60 `test_commands_shows_listing(self, adapter, platform)` (method)
- L69 `test_sequential_commands_share_session(self, adapter, platform)` (method) — Two commands from the same chat_id should both succeed.
- L78 `test_verbose_responds(self, adapter, platform)` (method)
- L87 `test_plaintext_restart_gateway_routes_to_safe_restart_command(self, adapter, runner, platform, monkeypatch)` (method)
- L102 `test_plaintext_restart_gateway_in_group_stays_plain_text(self, adapter, runner, platform, monkeypatch)` (method)
- L118 `test_personality_lists_options(self, adapter, platform)` (method)
- L126 `test_yolo_toggles_mode(self, adapter, platform)` (method)
- L134 `test_compress_command(self, adapter, platform)` (method)
- L142 `test_quick_command_alias_targets_builtin_command_with_args(self, adapter, runner, platform)` (method) — Alias targets with args must reach the built-in command handler.
- L165 `TestSessionLifecycle` (class) — Verify session state changes across command sequences.
- L169 `test_new_then_status_reflects_reset(self, adapter, runner, session_entry, platform)` (method) — After /new, /status should report the fresh session.
- L181 `test_new_is_idempotent(self, adapter, runner, platform)` (method) — /new called twice should not crash.
- L188 `TestAuthorization` (class) — Verify the pipeline handles unauthorized users.
- L192 `test_unauthorized_user_gets_pairing_response(self, adapter, runner, platform)` (method) — Unauthorized DM should trigger pairing code, not a command response.
- L208 `test_unauthorized_user_does_not_get_help(self, adapter, runner, platform)` (method) — Unauthorized user should NOT see the help command output.
- L223 `TestSendFailureResilience` (class) — Verify the pipeline handles send failures gracefully.
- L227 `test_send_failure_does_not_crash_pipeline(self, adapter, platform)` (method) — If send() returns failure, the pipeline should not raise.
