---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/acp/test_events.py

Symbols in `tests/acp/test_events.py`.

- L25 `mock_conn()` (function) — Mock ACP Client connection.
- L33 `event_loop_fixture()` (function) — Create a real event loop for testing threadsafe coroutine submission.
- L45 `TestToolProgressCallback` (class)
- L46 `test_emits_tool_call_start(self, mock_conn, event_loop_fixture)` (method) — Tool progress should emit a ToolCallStart update.
- L71 `test_handles_string_args(self, mock_conn, event_loop_fixture)` (method) — If args is a JSON string, it should be parsed.
- L88 `test_handles_non_dict_args(self, mock_conn, event_loop_fixture)` (method) — If args is not a dict, it should be wrapped.
- L105 `test_duplicate_same_name_tool_calls_use_fifo_ids(self, mock_conn, event_loop_fixture)` (method) — Multiple same-name tool calls should be tracked independently in order.
- L135 `TestThinkingCallback` (class)
- L136 `test_emits_thought_chunk(self, mock_conn, event_loop_fixture)` (method) — Thinking callback should emit AgentThoughtChunk.
- L151 `test_ignores_empty_text(self, mock_conn, event_loop_fixture)` (method) — Empty text should not emit any update.
- L168 `TestStepCallback` (class)
- L169 `test_completes_tracked_tool_calls(self, mock_conn, event_loop_fixture)` (method) — Step callback should mark tracked tools as completed.
- L187 `test_ignores_untracked_tools(self, mock_conn, event_loop_fixture)` (method) — Tools not in tool_call_ids should be silently ignored.
- L199 `test_handles_string_tool_info(self, mock_conn, event_loop_fixture)` (method) — Tool info as a string (just the name) should work.
- L216 `test_result_passed_to_build_tool_complete(self, mock_conn, event_loop_fixture)` (method) — Tool result from prev_tools dict is forwarded to build_tool_complete.
- L238 `test_none_result_passed_through(self, mock_conn, event_loop_fixture)` (method) — When result is None (e.g. first iteration), None is passed through.
- L257 `test_step_callback_passes_arguments_and_snapshot(self, mock_conn, event_loop_fixture)` (method)
- L282 `test_tool_progress_captures_snapshot_metadata(self, mock_conn, event_loop_fixture)` (method)
- L300 `test_todo_completion_emits_native_plan_update_after_tool_completion(self, mock_conn, event_loop_fixture)` (method)
- L332 `test_todo_plan_update_parses_json_with_trailing_hint(self)` (method)
- L341 `test_todo_plan_update_with_empty_todos_clears_plan(self)` (method)
- L354 `TestMessageCallback` (class)
- L355 `test_emits_agent_message_chunk(self, mock_conn, event_loop_fixture)` (method) — Message callback should emit AgentMessageChunk.
- L370 `test_ignores_empty_message(self, mock_conn, event_loop_fixture)` (method) — Empty text should not emit any update.
- L386 `TestSendUpdate` (class)
- L387 `test_scheduler_failure_closes_update_coroutine(self, event_loop_fixture)` (method) — If run_coroutine_threadsafe raises, _send_update must close the coro.
