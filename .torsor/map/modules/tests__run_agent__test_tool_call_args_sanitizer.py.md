---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_tool_call_args_sanitizer.py

Symbols in `tests/run_agent/test_tool_call_args_sanitizer.py`.

- L12 `_tool_call(call_id='call_1', name='read_file', arguments='{"path":"/tmp/foo"}')` (function)
- L23 `_assistant_message(*tool_calls)` (function)
- L31 `_tool_message(call_id='call_1', content='ok')` (function)
- L39 `test_valid_arguments_unchanged()` (function)
- L53 `test_truncated_arguments_replaced_with_empty_object(caplog)` (function)
- L74 `test_marker_appended_to_existing_tool_message()` (function)
- L87 `test_marker_message_inserted_when_missing()` (function)
- L94 `_disabled_test_marker_message_inserted_when_missing()` (function)
- L113 `test_multiple_corrupted_tool_calls_in_one_message()` (function)
- L135 `test_empty_string_arguments_treated_as_empty_object(caplog)` (function)
- L152 `test_non_assistant_messages_ignored()` (function)
