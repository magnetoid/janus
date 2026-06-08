---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_read_loop_detection.py

Symbols in `tests/tools/test_read_loop_detection.py`.

- L30 `_FakeReadResult` (class) — Minimal stand-in for FileOperations.read_file return value.
- L32 `__init__(self, content='line1\nline2\n', total_lines=2)` (method)
- L36 `to_dict(self)` (method)
- L40 `_fake_read_file(path, offset=1, limit=500)` (function)
- L44 `_FakeSearchResult` (class) — Minimal stand-in for FileOperations.search return value.
- L46 `__init__(self)` (method)
- L49 `to_dict(self)` (method)
- L53 `_make_fake_file_ops()` (function)
- L60 `TestReadLoopDetection` (class) — Verify that read_file_tool detects and warns on consecutive re-reads.
- L63 `setUp(self)` (method)
- L66 `tearDown(self)` (method)
- L70 `test_first_read_has_no_warning(self, _mock_ops)` (method)
- L76 `test_second_consecutive_read_no_warning(self, _mock_ops)` (method) — 2nd consecutive read should NOT warn (threshold is 3).
- L86 `test_third_consecutive_read_has_warning(self, _mock_ops)` (method) — 3rd consecutive read of the same region triggers a warning.
- L97 `test_fourth_consecutive_read_is_blocked(self, _mock_ops)` (method) — 4th consecutive read of the same region is BLOCKED — no content.
- L108 `test_fifth_consecutive_read_still_blocked(self, _mock_ops)` (method) — Subsequent reads remain blocked with incrementing count.
- L117 `test_different_region_resets_consecutive(self, _mock_ops)` (method) — Reading a different region of the same file resets consecutive count.
- L128 `test_different_file_resets_consecutive(self, _mock_ops)` (method) — Reading a different file resets the consecutive counter.
- L136 `test_different_tasks_isolated(self, _mock_ops)` (method) — Different task_ids have separate consecutive counters.
- L145 `test_warning_still_returns_content(self, _mock_ops)` (method) — Even with a warning (3rd read), the file content is still returned.
- L155 `TestNotifyOtherToolCall` (class) — Verify that notify_other_tool_call resets the consecutive counter.
- L158 `setUp(self)` (method)
- L161 `tearDown(self)` (method)
- L165 `test_other_tool_resets_consecutive(self, _mock_ops)` (method) — After another tool runs, re-reading the same file is NOT consecutive.
- L177 `test_other_tool_prevents_block(self, _mock_ops)` (method) — Agent can keep reading if other tools are used in between.
- L189 `test_notify_on_unknown_task_is_safe(self, _mock_ops)` (method) — notify_other_tool_call on a task that hasn't read anything is a no-op.
- L197 `TestSearchLoopDetection` (class) — Verify that search_tool detects and blocks consecutive repeated searches.
- L200 `setUp(self)` (method)
- L203 `tearDown(self)` (method)
- L207 `test_first_search_no_warning(self, _mock_ops)` (method)
- L213 `test_second_consecutive_search_no_warning(self, _mock_ops)` (method) — 2nd consecutive search should NOT warn (threshold is 3).
- L221 `test_third_consecutive_search_has_warning(self, _mock_ops)` (method) — 3rd consecutive identical search triggers a warning.
- L232 `test_fourth_consecutive_search_is_blocked(self, _mock_ops)` (method) — 4th consecutive identical search is BLOCKED.
- L242 `test_different_pattern_resets_consecutive(self, _mock_ops)` (method) — A different search pattern resets the consecutive counter.
- L251 `test_different_task_isolated(self, _mock_ops)` (method) — Different tasks have separate consecutive counters.
- L258 `test_other_tool_resets_search_consecutive(self, _mock_ops)` (method) — notify_other_tool_call resets search consecutive counter too.
- L268 `test_pagination_offset_does_not_count_as_repeat(self, _mock_ops)` (method) — Paginating truncated results should not be blocked as a repeat search.
- L276 `test_read_between_searches_resets_consecutive(self, _mock_ops)` (method) — A read_file call between searches resets search consecutive counter.
- L287 `TestTodoInjectionFiltering` (class) — Verify that format_for_injection filters completed/cancelled todos.
- L290 `test_filters_completed_and_cancelled(self)` (method)
- L305 `test_all_completed_returns_none(self)` (method)
- L314 `test_empty_store_returns_none(self)` (method)
- L319 `test_all_active_included(self)` (method)
