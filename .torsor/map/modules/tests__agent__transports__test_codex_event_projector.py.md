---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/transports/test_codex_event_projector.py

Symbols in `tests/agent/transports/test_codex_event_projector.py`.

- L45 `TestProjectionInvariants` (class) — Universal invariants that must hold across all projection paths.
- L48 `test_streaming_deltas_dont_materialize(self)` (method)
- L63 `test_turn_started_and_completed_are_silent(self)` (method)
- L69 `test_unknown_method_silent(self)` (method)
- L75 `TestCommandExecutionProjection` (class) — Real captured notification → assistant tool_call + tool result.
- L78 `test_command_completed_produces_two_messages(self)` (method)
- L84 `test_first_message_is_assistant_tool_call(self)` (method)
- L98 `test_second_message_is_tool_result_correlating_by_id(self)` (method)
- L106 `test_nonzero_exit_code_annotated_in_tool_result(self)` (method)
- L118 `test_deterministic_call_id_across_replay(self)` (method)
- L127 `TestAgentMessageProjection` (class) — assistant text → final_text + assistant message.
- L130 `test_agent_message_projects_to_assistant(self)` (method)
- L141 `test_pending_reasoning_attaches_to_next_assistant_message(self)` (method)
- L162 `test_reasoning_consumed_after_attaching(self)` (method)
- L174 `TestFileChangeProjection` (class)
- L175 `test_file_change_summary_no_inlined_content(self)` (method)
- L197 `TestMcpToolCallProjection` (class)
- L198 `test_mcp_tool_call_namespaced(self)` (method)
- L215 `test_mcp_error_surfaced(self)` (method)
- L228 `TestUserAndOpaqueProjection` (class)
- L229 `test_user_message_text_fragments_only(self)` (method)
- L245 `test_opaque_item_recorded_without_fabricated_tool_calls(self)` (method)
- L256 `TestHelpers` (class)
- L257 `test_deterministic_call_id_stable(self)` (method)
- L261 `test_deterministic_call_id_handles_missing_id(self)` (method)
- L268 `test_format_tool_args_sorted_keys(self)` (method)
- L275 `TestRoleAlternationInvariant` (class) — The project must never emit two assistant messages back-to-back from
- L295 `test_tool_items_emit_assistant_then_tool(self, item)` (method)
