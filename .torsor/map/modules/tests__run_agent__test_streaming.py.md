---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_streaming.py

Symbols in `tests/run_agent/test_streaming.py`.

- L15 `_make_stream_chunk(content=None, tool_calls=None, finish_reason=None, model=None, reasoning_content=None, usage=None)` (function) — Build a mock streaming chunk matching OpenAI's ChatCompletionChunk shape.
- L39 `_make_tool_call_delta(index=0, tc_id=None, name=None, arguments=None, extra_content=None, model_extra=None)` (function) — Build a mock tool call delta.
- L50 `_make_empty_chunk(model=None, usage=None)` (function) — Build a chunk with no choices (usage-only final chunk).
- L58 `TestStreamingAccumulator` (class) — Verify that _interruptible_streaming_api_call accumulates content
- L64 `test_text_only_response(self, mock_close, mock_create)` (method) — Text-only stream produces correct response shape.
- L100 `test_tool_call_response(self, mock_close, mock_create)` (method) — Tool call stream accumulates ID, name, and arguments.
- L143 `test_tool_name_not_duplicated_when_resent_per_chunk(self, mock_close, mock_create)` (method) — MiniMax M2.7 via NVIDIA NIM resends the full name in every chunk.
- L189 `test_tool_call_extra_content_preserved(self, mock_close, mock_create)` (method) — Streamed tool calls preserve provider-specific extra_content metadata.
- L237 `test_mixed_content_and_tool_calls(self, mock_close, mock_create)` (method) — Stream with both text and tool calls accumulates both.
- L276 `TestStreamingCallbacks` (class) — Verify that delta callbacks fire correctly.
- L281 `test_deltas_fire_in_order(self, mock_close, mock_create)` (method) — Callbacks receive text deltas in order.
- L316 `test_on_first_delta_fires_once(self, mock_close, mock_create)` (method) — on_first_delta callback fires exactly once.
- L351 `test_chat_stream_refreshes_activity_on_every_chunk(self, mock_close, mock_create)` (method) — Each streamed chat chunk should refresh the activity timestamp.
- L385 `test_tool_only_does_not_fire_callback(self, mock_close, mock_create)` (method) — Tool-call-only stream does not fire the delta callback.
- L423 `test_text_suppressed_when_tool_calls_present(self, mock_close, mock_create)` (method) — Text deltas are suppressed when tool calls are also in the stream.
- L469 `TestStreamingFallback` (class) — Verify streaming errors propagate to the main retry loop.
- L481 `test_stream_not_supported_sets_flag_and_raises(self, mock_close, mock_create)` (method) — 'not supported' error sets _disable_streaming and propagates.
- L510 `test_non_transport_error_propagates(self, mock_close, mock_create)` (method) — Non-transport streaming errors propagate to the main retry loop.
- L536 `test_stream_error_propagates_original(self, mock_close, mock_create)` (method) — The original streaming error propagates (not a fallback error).
- L560 `test_exhausted_transient_stream_error_propagates(self, mock_close, mock_create)` (method) — Transient stream errors retry first, then propagate after retries exhausted.
- L589 `test_sse_connection_lost_retried_as_transient(self, mock_close, mock_create)` (method) — SSE 'Network connection lost' (APIError w/ no status_code) retries like httpx errors.
- L634 `test_sse_non_connection_error_propagates_immediately(self, mock_close, mock_create)` (method) — SSE errors that aren't connection-related propagate immediately (no stream retry).
- L671 `TestReasoningStreaming` (class) — Verify reasoning content is accumulated and callback fires.
- L676 `test_reasoning_callback_fires(self, mock_close, mock_create)` (method) — Reasoning deltas fire the reasoning_callback.
- L718 `TestHasStreamConsumers` (class) — Verify _has_stream_consumers() detects registered callbacks.
- L721 `test_no_consumers(self)` (method)
- L733 `test_delta_callback_set(self)` (method)
- L746 `test_stream_callback_set(self)` (method)
- L763 `TestCodexStreamCallbacks` (class) — Verify _run_codex_stream fires delta callbacks.
- L766 `test_codex_text_delta_fires_callback(self)` (method)
- L807 `test_codex_stream_refreshes_activity_on_every_event(self)` (method)
- L846 `test_codex_remote_protocol_error_retries_then_raises(self)` (method) — Transport errors from ``responses.create`` retry once then re-raise.
- L886 `test_codex_create_stream_fallback_refreshes_activity_on_every_event(self)` (method)
- L936 `TestAnthropicStreamCallbacks` (class) — Verify Anthropic streaming refreshes activity on every event.
- L939 `test_anthropic_stream_refreshes_activity_on_every_event(self)` (method)
- L990 `test_anthropic_stream_parser_valueerror_retries_before_delivery(self, mock_replace, monkeypatch)` (method) — Malformed Anthropic event-stream frames retry instead of surfacing HTTP None.
- L1041 `test_generic_anthropic_valueerror_still_propagates_without_stream_retry(self, mock_replace, monkeypatch)` (method) — Only known provider stream parser ValueErrors are treated as transient.
- L1072 `TestPartialToolCallWarning` (class) — Regression: when a stream dies mid tool-call argument generation after
- L1090 `test_partial_tool_call_surfaces_warning(self, mock_close, mock_create)` (method) — Stream with text + partial tool-call name + mid-stream error
- L1158 `test_partial_text_only_no_warning(self, mock_close, mock_create)` (method) — Text-only partial stream (no tool call mid-flight) keeps the
- L1206 `TestSilentRetryMidToolCall` (class) — Regression: when the stream dies mid tool-call JSON after text was
- L1219 `test_silent_retry_recovers_tool_call(self, mock_close, mock_create, mock_replace)` (method) — First attempt: text + partial tool-call + connection drop.
- L1314 `test_silent_retry_exhausted_falls_back_to_stub(self, mock_close, mock_create, mock_replace)` (method) — When all retry attempts fail with connection errors, fall back
- L1369 `test_no_silent_retry_for_text_only_stall(self, mock_close, mock_create, mock_replace)` (method) — Text-only stall (no tool call in flight) must NOT trigger silent
- L1431 `_valid_acp_response()` (function) — Build a minimal valid non-streaming API response for copilot-acp.
- L1449 `_make_acp_agent(provider='copilot-acp', base_url='acp://copilot')` (function) — Create an AIAgent configured for copilot-acp with a stream consumer
- L1469 `TestCopilotACPStreamingDecision` (class) — Verify that copilot-acp routes to the non-streaming path.
- L1480 `test_provider_name_triggers_non_streaming(self, mock_acp_cls, _mock_check, _mock_tools)` (method) — provider='copilot-acp' → non-streaming path.
- L1511 `test_acp_base_url_triggers_non_streaming(self, mock_acp_cls, _mock_check, _mock_tools)` (method) — base_url='acp://copilot' → non-streaming even without provider name.
- L1532 `test_acp_tcp_url_triggers_non_streaming(self, mock_acp_cls, _mock_check, _mock_tools)` (method) — base_url='acp+tcp://...' → non-streaming.
- L1550 `test_non_acp_provider_allows_streaming(self)` (method) — Regular providers still get streaming enabled.
