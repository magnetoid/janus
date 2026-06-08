---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_reasoning_command.py

Symbols in `tests/cli/test_reasoning_command.py`.

- L21 `TestParseReasoningConfig` (class) — Verify _parse_reasoning_config handles all effort levels.
- L24 `_parse(self, effort)` (method)
- L28 `test_none_disables(self)` (method)
- L32 `test_valid_levels(self)` (method)
- L39 `test_empty_returns_none(self)` (method)
- L43 `test_unknown_returns_none(self)` (method)
- L47 `test_case_insensitive(self)` (method)
- L57 `TestHandleReasoningCommand` (class) — Test the combined _handle_reasoning_command method.
- L60 `_make_cli(self, reasoning_config=None, show_reasoning=False)` (method) — Create a minimal CLI stub with the reasoning attributes.
- L69 `test_show_enables_display(self)` (method)
- L78 `test_hide_disables_display(self)` (method)
- L88 `test_on_enables_display(self)` (method)
- L95 `test_off_disables_display(self)` (method)
- L102 `test_effort_level_sets_config(self)` (method) — Setting an effort level should update reasoning_config.
- L111 `test_effort_none_disables_reasoning(self)` (method)
- L118 `test_invalid_argument_rejected(self)` (method) — Invalid arguments should be rejected (parsed returns None).
- L124 `test_no_args_shows_status(self)` (method) — With no args, should show current state (no crash).
- L138 `test_status_with_disabled_reasoning(self)` (method)
- L149 `test_status_with_explicit_level(self)` (method)
- L163 `TestLastReasoningInResult` (class) — Verify reasoning extraction from the messages list.
- L166 `_build_messages(self, reasoning=None)` (method)
- L177 `test_reasoning_present(self)` (method)
- L188 `test_reasoning_none(self)` (method)
- L199 `test_picks_last_assistant(self)` (method)
- L215 `test_empty_reasoning_treated_as_none(self)` (method)
- L231 `TestReasoningCollapse` (class) — Verify long reasoning is collapsed to 10 lines in the box.
- L234 `test_short_reasoning_not_collapsed(self)` (method)
- L239 `test_long_reasoning_collapsed(self)` (method)
- L250 `test_exactly_10_lines_not_collapsed(self)` (method)
- L256 `test_intermediate_callback_collapses_to_5(self)` (method) — _on_reasoning shows max 5 lines.
- L274 `TestReasoningCallback` (class) — Verify reasoning_callback invocation.
- L277 `test_callback_invoked_with_reasoning(self)` (method)
- L288 `test_callback_not_invoked_without_reasoning(self)` (method)
- L299 `test_callback_none_does_not_crash(self)` (method)
- L307 `TestReasoningPreviewBuffering` (class)
- L308 `_make_cli(self)` (method)
- L319 `test_streamed_reasoning_chunks_wait_for_boundary(self, mock_cprint)` (method)
- L335 `test_pending_reasoning_flushes_when_thinking_stops(self, mock_cprint)` (method)
- L354 `test_reasoning_preview_compacts_newlines_and_wraps_to_terminal(self, _mock_term, mock_cprint)` (method)
- L369 `test_reasoning_flush_threshold_tracks_terminal_width(self, _mock_term)` (method)
- L377 `TestReasoningDisplayModeSelection` (class)
- L378 `_make_cli(self, *, show_reasoning=False, streaming_enabled=False, verbose=False)` (method)
- L389 `test_show_reasoning_non_streaming_uses_final_box_only(self)` (method)
- L394 `test_show_reasoning_streaming_uses_live_reasoning_box(self)` (method)
- L401 `test_verbose_without_show_reasoning_uses_preview_callback(self)` (method)
- L413 `TestExtractReasoningFormats` (class) — Test _extract_reasoning with real provider response formats.
- L416 `_get_extractor(self)` (method)
- L420 `test_openrouter_reasoning_details(self)` (method)
- L432 `test_deepseek_reasoning_field(self)` (method)
- L441 `test_moonshot_reasoning_content(self)` (method)
- L449 `test_no_reasoning_returns_none(self)` (method)
- L460 `TestInlineThinkBlockExtraction` (class) — Test _build_assistant_message extracts inline <think> blocks as reasoning
- L464 `_build_msg(self, content, reasoning=None, reasoning_content=None, reasoning_details=None, tool_calls=None)` (method) — Create a mock API response message.
- L475 `_make_agent(self)` (method) — Create a minimal agent with _build_assistant_message.
- L487 `test_single_think_block_extracted(self)` (method)
- L493 `test_multiple_think_blocks_extracted(self)` (method)
- L500 `test_no_think_blocks_no_reasoning(self)` (method)
- L507 `test_structured_reasoning_takes_priority(self)` (method) — When structured API reasoning exists, inline think blocks should NOT override.
- L517 `test_empty_think_block_ignored(self)` (method)
- L524 `test_multiline_think_block(self)` (method)
- L531 `test_callback_fires_for_inline_think(self)` (method) — Reasoning callback should fire when reasoning is extracted from inline think blocks.
- L546 `TestConfigDefault` (class) — Verify config default for show_reasoning.
- L549 `test_default_config_has_show_reasoning(self)` (method)
- L556 `TestCommandRegistered` (class) — Verify /reasoning is in the COMMANDS dict.
- L559 `test_reasoning_in_commands(self)` (method)
- L568 `TestEndToEndPipeline` (class) — Simulate the full pipeline: extraction -> result dict -> display.
- L571 `test_openrouter_claude_pipeline(self)` (method)
- L609 `test_no_reasoning_model_pipeline(self)` (method)
- L624 `TestReasoningDeltasFiredFlag` (class) — _build_assistant_message should not re-fire reasoning_callback when
- L628 `_make_agent(self)` (method)
- L637 `test_fire_reasoning_delta_calls_callback(self)` (method)
- L644 `test_build_assistant_message_skips_callback_when_already_streamed(self)` (method) — When streaming already fired reasoning deltas, the post-stream
- L666 `test_build_assistant_message_skips_callback_when_streaming_active(self)` (method) — When streaming is active, callback should NEVER fire from
- L691 `test_build_assistant_message_fires_callback_without_streaming(self)` (method) — When no streaming is active, callback always fires for structured
- L712 `TestReasoningShownThisTurnFlag` (class) — Post-response reasoning display should be suppressed when reasoning
- L716 `_make_cli(self)` (method)
- L735 `test_streaming_reasoning_sets_turn_flag(self, mock_cprint)` (method)
- L742 `test_turn_flag_survives_reset_stream_state(self, mock_cprint)` (method) — _reasoning_shown_this_turn must NOT be cleared by
- L756 `test_turn_flag_cleared_before_new_turn(self, mock_cprint)` (method) — The turn flag should be reset at the start of a new user turn.
