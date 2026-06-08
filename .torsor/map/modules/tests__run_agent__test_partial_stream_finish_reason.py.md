---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_partial_stream_finish_reason.py

Symbols in `tests/run_agent/test_partial_stream_finish_reason.py`.

- L29 `_make_stream_chunk(content=None, tool_calls=None, finish_reason=None)` (function)
- L38 `_make_tool_call_delta(index=0, tc_id=None, name=None, arguments=None)` (function)
- L43 `_make_agent()` (function)
- L60 `TestPartialStreamStubFinishReason` (class) — The stub returned by interruptible_streaming_api_call when the
- L66 `test_text_only_partial_returns_length(self, _mock_close, mock_create, monkeypatch)` (method) — #30963: text-only partials must classify as length so the loop
- L95 `test_partial_tool_call_uses_length(self, _mock_close, mock_create, monkeypatch)` (method) — Mid-tool-call partials now use finish_reason=length so the
- L141 `TestLengthContinuationPromptBranching` (class) — When finish_reason=length, the continuation prompt that reaches the
- L146 `_simulate_branch(self, response_id: str, dropped_tools=None)` (method) — Return the continuation prompt text the loop would inject for
- L152 `test_partial_stream_stub_uses_network_prompt(self)` (method)
- L157 `test_real_truncation_uses_length_prompt(self)` (method)
- L162 `test_no_id_falls_through_to_length_prompt(self)` (method)
- L166 `test_dropped_tool_call_uses_chunking_prompt(self)` (method) — When the stub dropped a tool call, the continuation prompt
- L183 `loop_agent()` (function) — AIAgent with a mocked OpenAI client (mirrors test_run_agent's fixture)
- L208 `TestConversationLoopPartialStreamContinuation` (class) — End-to-end: a partial-stream stub feeds the loop and the loop
- L212 `test_partial_stream_stub_does_not_exit_loop_immediately(self, loop_agent)` (method) — The stub from chat_completion_helpers used to exit the loop with
