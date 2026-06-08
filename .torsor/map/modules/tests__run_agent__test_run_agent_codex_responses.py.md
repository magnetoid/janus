---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_run_agent_codex_responses.py

Symbols in `tests/run_agent/test_run_agent_codex_responses.py`.

- L16 `_no_codex_backoff(monkeypatch)` (function) — Short-circuit retry backoff so Codex retry tests don't block on real
- L24 `_patch_agent_bootstrap(monkeypatch)` (function)
- L42 `_build_agent(monkeypatch)` (function)
- L60 `_build_copilot_agent(monkeypatch, *, model='gpt-5.4')` (function)
- L80 `_codex_message_response(text: str)` (function)
- L94 `_codex_tool_call_response()` (function)
- L111 `_codex_incomplete_message_response(text: str)` (function)
- L126 `_codex_commentary_message_response(text: str)` (function)
- L142 `_codex_ack_message_response(text: str)` (function)
- L157 `_FakeCreateStream` (class) — Iterable-only fake for ``responses.create(stream=True)`` outputs.
- L164 `__init__(self, events)` (method)
- L168 `__iter__(self)` (method)
- L171 `close(self)` (method)
- L175 `_codex_request_kwargs()` (function)
- L185 `test_api_mode_uses_explicit_provider_when_codex(monkeypatch)` (function)
- L201 `test_api_mode_normalizes_provider_case(monkeypatch)` (function)
- L217 `test_api_mode_respects_explicit_openrouter_provider_over_codex_url(monkeypatch)` (function) — GPT-5.x models need codex_responses even on OpenRouter.
- L239 `test_copilot_acp_stays_on_chat_completions_for_gpt_5_models(monkeypatch)` (function)
- L255 `test_copilot_gpt_5_mini_stays_on_chat_completions(monkeypatch)` (function)
- L272 `test_build_api_kwargs_codex(monkeypatch)` (function)
- L303 `test_build_api_kwargs_codex_clamps_minimal_effort(monkeypatch)` (function) — 'minimal' reasoning effort is clamped to 'low' on the Responses API.
- L336 `test_build_api_kwargs_codex_preserves_supported_efforts(monkeypatch)` (function) — Effort levels natively supported by the Responses API pass through unchanged.
- L364 `test_build_api_kwargs_copilot_responses_omits_openai_only_fields(monkeypatch)` (function)
- L377 `test_build_api_kwargs_copilot_responses_omits_reasoning_for_non_reasoning_model(monkeypatch)` (function)
- L404 `_build_xai_agent_with_slash_enum_tool(monkeypatch)` (function) — Build an xAI agent whose tool registry has a slash-containing enum.
- L455 `test_build_api_kwargs_xai_strips_slash_enum_from_outgoing_request(monkeypatch)` (function) — The xAI request sent to the API must NOT contain slash-enum values.
- L473 `test_build_api_kwargs_xai_does_not_mutate_agent_tools(monkeypatch)` (function) — Headline #27907 regression: ``agent.tools`` must survive intact.
- L508 `test_build_api_kwargs_xai_is_idempotent_across_repeated_calls(monkeypatch)` (function) — Multiple xAI requests must each produce the same sanitized output
- L529 `test_run_codex_stream_returns_collected_items_when_stream_ends_without_terminal(monkeypatch)` (function) — The event-driven path tolerates streams that end without a terminal frame.
- L565 `test_run_codex_stream_surfaces_failed_status_in_final_response(monkeypatch)` (function) — A ``response.failed`` terminal event is reflected on the returned object.
- L594 `test_run_codex_stream_parses_create_stream_events(monkeypatch)` (function) — The primary path consumes ``responses.create(stream=True)`` events directly.
- L629 `test_run_codex_stream_ignores_completed_response_with_null_output(monkeypatch)` (function) — Regression: Codex may send response.completed.response.output=null.
- L677 `test_run_conversation_codex_plain_text(monkeypatch)` (function)
- L689 `test_run_conversation_codex_empty_output_with_output_text(monkeypatch)` (function) — Regression: empty response.output + valid output_text should succeed,
- L712 `test_run_conversation_codex_empty_output_no_output_text_retries(monkeypatch)` (function) — When both output and output_text are empty, validation should
- L739 `test_run_conversation_codex_refreshes_after_401_and_retries(monkeypatch)` (function)
- L770 `_build_xai_oauth_agent(monkeypatch)` (function)
- L789 `test_build_api_kwargs_xai_oauth_sends_cache_key_via_extra_body(monkeypatch)` (function) — xai-oauth + codex_responses must route prompt caching via the
- L826 `test_run_conversation_xai_oauth_refreshes_after_401_and_retries(monkeypatch)` (function) — xai-oauth speaks the Responses API just like codex.  When the access
- L863 `test_try_refresh_codex_client_credentials_handles_xai_oauth(monkeypatch)` (function) — ``_try_refresh_codex_client_credentials`` must rebuild the OpenAI
- L910 `test_try_refresh_codex_client_credentials_skips_xai_oauth_when_singleton_differs(monkeypatch)` (function) — An xai-oauth agent constructed with a non-singleton credential
- L960 `test_run_conversation_copilot_refreshes_after_401_and_retries(monkeypatch)` (function)
- L990 `test_try_refresh_codex_client_credentials_rebuilds_client(monkeypatch)` (function)
- L1031 `test_try_refresh_copilot_client_credentials_rebuilds_client(monkeypatch)` (function)
- L1064 `test_try_refresh_copilot_client_credentials_rebuilds_even_if_token_unchanged(monkeypatch)` (function)
- L1087 `test_run_conversation_codex_tool_round_trip(monkeypatch)` (function)
- L1112 `test_chat_messages_to_responses_input_uses_call_id_for_function_call(monkeypatch)` (function)
- L1141 `test_chat_messages_to_responses_input_accepts_call_pipe_fc_ids(monkeypatch)` (function)
- L1170 `test_preflight_codex_api_kwargs_strips_optional_function_call_id(monkeypatch)` (function)
- L1197 `test_preflight_codex_api_kwargs_rejects_function_call_output_without_call_id(monkeypatch)` (function)
- L1213 `test_preflight_codex_api_kwargs_rejects_unsupported_request_fields(monkeypatch)` (function)
- L1223 `test_preflight_codex_api_kwargs_allows_reasoning_and_temperature(monkeypatch)` (function)
- L1239 `test_preflight_codex_api_kwargs_allows_service_tier(monkeypatch)` (function)
- L1249 `test_preflight_codex_api_kwargs_preserves_positive_timeout(monkeypatch)` (function) — Positive numeric timeouts survive preflight so the SDK honors them.
- L1260 `test_preflight_codex_api_kwargs_drops_invalid_timeout(monkeypatch)` (function) — Zero, negative, inf, and booleans are all dropped — not passed to SDK.
- L1272 `test_run_conversation_codex_replay_payload_keeps_call_id(monkeypatch)` (function)
- L1309 `test_run_conversation_codex_continues_after_incomplete_interim_message(monkeypatch)` (function)
- L1343 `test_normalize_codex_response_marks_commentary_only_message_as_incomplete(monkeypatch)` (function)
- L1354 `test_normalize_codex_response_preserves_message_status_for_replay(monkeypatch)` (function) — Incomplete Codex output messages must not be replayed as completed.
- L1381 `test_normalize_codex_response_detects_leaked_tool_call_text(monkeypatch)` (function) — Harmony-style `to=functions.foo` leaked into assistant content with no
- L1421 `test_normalize_codex_response_ignores_tool_call_text_when_real_tool_call_present(monkeypatch)` (function) — If the model emitted BOTH a structured function_call AND some text that
- L1459 `test_normalize_codex_response_no_leak_passes_through(monkeypatch)` (function) — Sanity: normal assistant content that doesn't contain the leak pattern
- L1488 `test_interim_commentary_is_not_marked_already_streamed_without_callbacks(monkeypatch)` (function)
- L1505 `test_interim_commentary_is_not_marked_already_streamed_when_stream_callback_fails(monkeypatch)` (function)
- L1526 `test_interim_commentary_preserves_assistant_content(monkeypatch)` (function) — Interim commentary must not silently mutate assistant text containing
- L1551 `test_stream_delta_strips_leaked_memory_context(monkeypatch)` (function)
- L1570 `test_stream_delta_strips_leaked_memory_context_across_chunks(monkeypatch)` (function) — Regression for #5719 — the real streaming case.
- L1605 `test_stream_delta_scrubber_resets_between_turns(monkeypatch)` (function) — An unterminated span from a prior turn must not taint the next turn.
- L1621 `test_stream_delta_preserves_mid_stream_leading_newlines(monkeypatch)` (function) — Mid-stream leading newlines must survive — they are legitimate
- L1644 `test_stream_delta_preserves_code_fence_newlines(monkeypatch)` (function) — Code blocks span multiple deltas.  A "\n```python\n" boundary
- L1661 `test_run_conversation_codex_continues_after_commentary_phase_message(monkeypatch)` (function)
- L1695 `test_run_conversation_codex_continues_after_ack_stop_message(monkeypatch)` (function)
- L1736 `test_run_conversation_codex_continues_after_ack_for_directory_listing_prompt(monkeypatch)` (function)
- L1777 `test_dump_api_request_debug_uses_responses_url(monkeypatch, tmp_path)` (function) — Debug dumps should show /responses URL when in codex_responses mode.
- L1790 `test_dump_api_request_debug_uses_chat_completions_url(monkeypatch, tmp_path)` (function) — Debug dumps should show /chat/completions URL for chat_completions mode.
- L1817 `_codex_reasoning_only_response(*, encrypted_content='enc_abc123', summary_text='Thinking...')` (function) — Codex response containing only reasoning items — no message text, no tool calls.
- L1835 `test_normalize_codex_response_marks_reasoning_only_as_incomplete(monkeypatch)` (function) — A response with only reasoning items and no content should be 'incomplete', not 'stop'.
- L1854 `test_normalize_codex_response_reasoning_with_content_is_stop(monkeypatch)` (function) — If a response has both reasoning and message content, it should still be 'stop'.
- L1883 `test_run_conversation_codex_continues_after_reasoning_only_response(monkeypatch)` (function) — End-to-end: reasoning-only → final message should succeed, not hit retry loop.
- L1905 `test_run_conversation_codex_preserves_encrypted_reasoning_in_interim(monkeypatch)` (function) — Encrypted codex_reasoning_items must be preserved in interim messages
- L1945 `test_chat_messages_to_responses_input_reasoning_only_has_following_item(monkeypatch)` (function) — When converting a reasoning-only interim message to Responses API input,
- L1976 `test_codex_message_item_status_survives_conversion_and_preflight(monkeypatch)` (function) — Stored Codex assistant message statuses must survive replay normalization.
- L2014 `test_duplicate_detection_distinguishes_different_codex_reasoning(monkeypatch)` (function) — Two consecutive reasoning-only responses with different encrypted content
- L2064 `test_duplicate_detection_distinguishes_different_codex_message_items(monkeypatch)` (function) — Incomplete turns with new message ids/phases/statuses must not be collapsed.
- L2116 `test_chat_messages_to_responses_input_deduplicates_reasoning_ids(monkeypatch)` (function) — Duplicate reasoning item IDs across multi-turn incomplete responses
- L2156 `test_preflight_codex_input_deduplicates_reasoning_ids(monkeypatch)` (function) — _preflight_codex_input_items should also deduplicate reasoning items by ID.
- L2181 `test_run_conversation_codex_disables_reasoning_replay_after_invalid_encrypted_content(monkeypatch)` (function)
- L2241 `test_run_conversation_codex_invalid_encrypted_content_without_replay_state_does_not_disable_replay(monkeypatch)` (function)
