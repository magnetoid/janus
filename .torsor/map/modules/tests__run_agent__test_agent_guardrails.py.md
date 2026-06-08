---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_agent_guardrails.py

Symbols in `tests/run_agent/test_agent_guardrails.py`.

- L21 `make_tc(name: str, arguments: str='{}')` (function) — Create a minimal tool_call SimpleNamespace mirroring the OpenAI SDK object.
- L28 `tool_result(call_id: str, content: str='ok')` (function)
- L32 `assistant_dict_call(call_id: str, name: str='terminal')` (function) — Dict-style tool_call (as stored in message history).
- L41 `TestSanitizeApiMessages` (class)
- L43 `test_orphaned_result_removed(self)` (method)
- L53 `test_orphaned_call_gets_stub_result(self)` (method)
- L64 `test_clean_messages_pass_through(self)` (method)
- L74 `test_mixed_orphaned_result_and_orphaned_call(self)` (method)
- L89 `test_empty_list_is_safe(self)` (method)
- L92 `test_no_tool_messages(self)` (method)
- L100 `test_sdk_object_tool_calls(self)` (method)
- L116 `TestCapDelegateTaskCalls` (class)
- L118 `test_excess_delegates_truncated(self)` (method)
- L124 `test_non_delegate_calls_preserved(self)` (method)
- L134 `test_at_limit_passes_through(self)` (method)
- L139 `test_below_limit_passes_through(self)` (method)
- L144 `test_no_delegate_calls_unchanged(self)` (method)
- L149 `test_empty_list_safe(self)` (method)
- L152 `test_original_list_not_mutated(self)` (method)
- L158 `test_interleaved_order_preserved(self)` (method)
- L175 `TestDeduplicateToolCalls` (class)
- L177 `test_duplicate_pair_deduplicated(self)` (method)
- L185 `test_multiple_duplicates(self)` (method)
- L196 `test_same_tool_different_args_kept(self)` (method)
- L204 `test_different_tools_same_args_kept(self)` (method)
- L212 `test_clean_list_unchanged(self)` (method)
- L220 `test_empty_list_safe(self)` (method)
- L223 `test_first_occurrence_kept(self)` (method)
- L230 `test_original_list_not_mutated(self)` (method)
- L244 `TestGetToolCallIdStatic` (class)
- L246 `test_dict_with_valid_id(self)` (method)
- L249 `test_dict_with_none_id(self)` (method)
- L252 `test_dict_without_id_key(self)` (method)
- L255 `test_object_with_valid_id(self)` (method)
- L259 `test_object_with_none_id(self)` (method)
- L263 `test_object_without_id_attr(self)` (method)
- L272 `TestGetToolCallNameStatic` (class)
- L274 `test_dict_with_valid_name(self)` (method)
- L279 `test_dict_with_missing_function(self)` (method)
- L282 `test_dict_with_none_function(self)` (method)
- L285 `test_dict_with_none_name(self)` (method)
- L290 `test_object_with_valid_name(self)` (method)
- L294 `test_object_without_function_attr(self)` (method)
