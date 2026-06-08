---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_resume_display.py

Symbols in `tests/cli/test_resume_display.py`.

- L18 `_make_cli(config_overrides=None, env_overrides=None, **kwargs)` (function) — Create a HermesCLI instance with minimal mocking.
- L54 `_simple_history()` (function) — Two-turn conversation: user → assistant → user → assistant.
- L65 `_tool_call_history()` (function) — Conversation with tool calls and tool results.
- L92 `_large_history(n_exchanges=15)` (function) — Build a history with many exchanges to test truncation.
- L101 `_multimodal_history()` (function) — Conversation with multimodal (image) content.
- L119 `TestDisplayResumedHistory` (class) — _display_resumed_history() renders a Rich panel with conversation recap.
- L122 `_capture_display(self, cli_obj)` (method) — Run _display_resumed_history and capture the Rich console output.
- L129 `test_simple_history_shows_user_and_assistant(self)` (method)
- L140 `test_system_messages_hidden(self)` (method)
- L147 `test_tool_messages_hidden(self)` (method)
- L156 `test_tool_calls_shown_as_summary(self)` (method)
- L172 `test_tool_only_message_skipped_by_default(self)` (method) — Assistant messages with only tool_calls (no text) are skipped when
- L185 `test_long_user_message_truncated(self)` (method)
- L202 `test_long_assistant_message_truncated(self)` (method) — Non-last assistant messages are still truncated.
- L219 `test_multiline_assistant_truncated(self)` (method) — Non-last multiline assistant messages are truncated to 3 lines.
- L238 `test_last_assistant_response_shown_in_full(self)` (method) — The last assistant response is shown un-truncated so the user
- L253 `test_last_assistant_multiline_shown_in_full(self)` (method) — The last assistant response shows all lines, not just 3.
- L268 `test_large_history_shows_truncation_indicator(self)` (method)
- L278 `test_multimodal_content_handled(self)` (method)
- L286 `test_empty_history_no_output(self)` (method)
- L293 `test_minimal_config_suppresses_display(self)` (method)
- L302 `test_panel_has_title(self)` (method)
- L309 `test_panel_is_stored_as_resize_aware_history_entry(self)` (method)
- L324 `test_assistant_with_no_content_no_tools_skipped(self)` (method) — Assistant messages with no visible output (e.g. pure reasoning)
- L338 `test_only_system_messages_no_output(self)` (method)
- L347 `test_reasoning_scratchpad_stripped(self)` (method) — <REASONING_SCRATCHPAD> blocks should be stripped from display.
- L366 `test_pure_reasoning_message_skipped(self)` (method) — Assistant messages that are only reasoning should be skipped.
- L382 `test_think_tags_stripped(self)` (method) — <think>...</think> blocks should be stripped from display (#11316).
- L399 `test_thinking_tags_stripped(self)` (method) — <thinking>...</thinking> blocks should be stripped from display.
- L415 `test_reasoning_tags_stripped(self)` (method) — <reasoning>...</reasoning> blocks should be stripped from display.
- L434 `test_thought_tags_stripped(self)` (method) — <thought>...</thought> blocks (Gemma 4) should be stripped.
- L450 `test_unclosed_think_tag_stripped(self)` (method) — Unclosed <think> (truncated generation) should not leak reasoning.
- L466 `test_multiple_reasoning_blocks_all_stripped(self)` (method) — Multiple interleaved reasoning blocks are all stripped.
- L488 `test_orphan_closing_think_tag_stripped(self)` (method) — A stray </think> with no matching open should not render to user.
- L503 `test_assistant_with_text_and_tool_calls(self)` (method) — When an assistant message has both text content AND tool_calls.
- L530 `TestPreloadResumedSession` (class) — _preload_resumed_session() loads session from DB early.
- L533 `test_returns_false_when_not_resumed(self)` (method)
- L537 `test_returns_false_when_no_session_db(self)` (method)
- L542 `test_returns_false_when_session_not_found(self)` (method)
- L556 `test_returns_false_when_session_has_no_messages(self)` (method)
- L571 `test_loads_session_successfully(self)` (method)
- L591 `test_reopens_session_in_db(self)` (method)
- L611 `test_singular_user_message_grammar(self)` (method) — 1 user message should say 'message' not 'messages'.
- L636 `TestHandleResumeCommandRecap` (class) — In-session /resume should show the same recap panel as startup resume.
- L639 `test_resume_command_displays_recap_when_messages_restored(self)` (method)
- L663 `test_resume_command_skips_recap_when_session_has_no_messages(self)` (method)
- L685 `TestInitAgentSkipsPreloaded` (class) — _init_agent() should skip DB load when history is already populated.
- L688 `test_init_agent_skips_db_when_preloaded(self)` (method) — If conversation_history is already set, _init_agent should not
- L709 `TestResumeDisplayConfig` (class) — resume_display config option defaults and behavior.
- L712 `test_default_config_has_resume_display(self)` (method) — DEFAULT_CONFIG in hermes_cli/config.py includes resume_display.
- L719 `test_cli_defaults_have_resume_display(self)` (method) — cli.py load_cli_config defaults include resume_display.
