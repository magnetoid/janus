---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_thinking_only_sanitizer.py

Symbols in `tests/run_agent/test_thinking_only_sanitizer.py`.

- L22 `TestIsThinkingOnlyAssistant` (class)
- L24 `test_plain_assistant_reply_is_not_thinking_only(self)` (method)
- L28 `test_assistant_with_tool_calls_is_not_thinking_only(self)` (method)
- L37 `test_empty_content_plus_reasoning_is_thinking_only(self)` (method)
- L41 `test_none_content_plus_reasoning_content_is_thinking_only(self)` (method)
- L45 `test_whitespace_only_content_plus_reasoning_is_thinking_only(self)` (method)
- L49 `test_empty_content_no_reasoning_is_not_thinking_only(self)` (method)
- L56 `test_list_content_all_thinking_blocks_is_thinking_only(self)` (method)
- L67 `test_list_content_with_real_text_is_not_thinking_only(self)` (method)
- L78 `test_list_content_with_tool_use_block_is_not_thinking_only(self)` (method)
- L88 `test_list_content_thinking_plus_whitespace_text_is_thinking_only(self)` (method)
- L99 `test_reasoning_details_list_form_detected(self)` (method)
- L107 `test_user_message_never_thinking_only(self)` (method)
- L110 `test_tool_message_never_thinking_only(self)` (method)
- L115 `test_non_dict_returns_false(self)` (method)
- L125 `TestDropThinkingOnlyAndMergeUsers` (class)
- L127 `test_empty_list_passthrough(self)` (method)
- L130 `test_no_thinking_only_messages_is_noop_identity(self)` (method)
- L139 `test_drops_thinking_only_between_user_messages_and_merges(self)` (method)
- L150 `test_preserves_alternation_after_drop(self)` (method)
- L163 `test_does_not_merge_when_drop_leaves_non_adjacent_users(self)` (method)
- L174 `test_multiple_thinking_only_in_sequence_collapses(self)` (method)
- L185 `test_does_not_touch_stored_messages_original_list_unmutated(self)` (method)
- L197 `test_tool_result_between_user_and_thinking_preserved(self)` (method)
- L212 `test_merge_concatenates_list_content_user_messages(self)` (method)
- L225 `test_merge_mixed_string_and_list_content(self)` (method)
- L238 `test_system_messages_ignored_by_pass(self)` (method)
