---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_background_command.py

Symbols in `tests/gateway/test_background_command.py`.

- L17 `_make_event(text='/background', platform=Platform.TELEGRAM, user_id='12345', chat_id='67890')` (function) — Build a MessageEvent for testing.
- L29 `_make_runner()` (function) — Create a bare GatewayRunner with minimal mocks.
- L56 `TestHandleBackgroundCommand` (class) — Tests for GatewayRunner._handle_background_command.
- L60 `test_no_prompt_shows_usage(self)` (method) — Running /background with no prompt shows usage.
- L69 `test_bg_alias_no_prompt_shows_usage(self)` (method) — Running /bg with no prompt shows usage.
- L77 `test_empty_prompt_shows_usage(self)` (method) — Running /background with only whitespace shows usage.
- L85 `test_valid_prompt_starts_task(self)` (method) — Running /background with a prompt returns confirmation and starts task.
- L111 `test_telegram_dm_topic_passes_trigger_anchor_to_task(self)` (method) — Telegram private-topic completion sends need the original command message id.
- L143 `test_prompt_truncated_in_preview(self)` (method) — Long prompts are truncated to 60 chars in the confirmation message.
- L157 `test_task_id_is_unique(self)` (method) — Each background task gets a unique task ID.
- L175 `test_works_across_platforms(self)` (method) — The /background command works for all platforms.
- L193 `TestRunBackgroundTask` (class) — Tests for GatewayRunner._run_background_task (the actual execution).
- L197 `test_no_adapter_returns_silently(self)` (method) — When no adapter is available, the task returns without error.
- L210 `test_no_credentials_sends_error(self)` (method) — When provider credentials are missing, an error is sent.
- L233 `test_successful_task_sends_result(self)` (method) — When the agent completes successfully, the result is sent.
- L271 `test_media_files_routed_by_type(self, monkeypatch)` (method) — Result media is routed to the type-specific sender, not send_document.
- L353 `test_telegram_dm_topic_completion_preserves_reply_anchor_metadata(self, monkeypatch)` (method) — Background completion metadata must let Telegram send thread id plus reply id.
- L405 `test_agent_cleanup_runs_when_background_agent_raises(self)` (method) — Temporary background agents must be cleaned up on error paths too.
- L434 `test_exception_sends_error_message(self)` (method) — When the agent raises an exception, an error message is sent.
- L462 `TestBackgroundInHelp` (class) — Verify /background appears in help text and known commands.
- L466 `test_background_in_help_output(self)` (method) — The /help output includes /background.
- L473 `test_background_is_known_command(self)` (method) — The /background command is in GATEWAY_KNOWN_COMMANDS.
- L478 `test_bg_alias_is_known_command(self)` (method) — The /bg alias is in GATEWAY_KNOWN_COMMANDS.
- L489 `TestBackgroundInCLICommands` (class) — Verify /background is registered in the CLI command system.
- L492 `test_background_in_commands_dict(self)` (method) — The /background command is in the COMMANDS dict.
- L497 `test_bg_alias_in_commands_dict(self)` (method) — The /bg alias is in the COMMANDS dict.
- L502 `test_background_in_session_category(self)` (method) — The /background command is in the Session category.
- L507 `test_background_autocompletes(self)` (method) — The /background command appears in autocomplete results.
