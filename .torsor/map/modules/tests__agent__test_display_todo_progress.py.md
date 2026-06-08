---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_display_todo_progress.py

Symbols in `tests/agent/test_display_todo_progress.py`.

- L11 `_todo_result(total: int, completed: int)` (function) — Build a fake todo_tool return value.
- L25 `TestTodoRead` (class) — get_cute_tool_message(…, result=…) when todos_arg is None (read path).
- L28 `test_read_no_result(self)` (method)
- L33 `test_read_with_progress(self)` (method)
- L39 `test_read_all_done(self)` (method)
- L45 `test_read_zero_total(self)` (method) — Edge case: empty todo list returns summary with total=0.
- L51 `test_read_invalid_result_fallback(self)` (method) — Garbage result should not crash; fall back to reading tasks.
- L56 `test_read_result_missing_summary(self)` (method)
- L62 `TestTodoCreate` (class) — get_cute_tool_message when merge=False (new plan creation).
- L65 `test_create_default(self)` (method) — Brand-new plan: all pending, no result — plain count.
- L75 `test_create_multiple(self)` (method)
- L84 `test_create_with_result_shows_progress_when_done(self)` (method) — Even on create, if result has completed tasks show it.
- L93 `test_create_with_result_zero_done(self)` (method) — New plan with 0 done — plain count, no progress fraction.
- L106 `TestTodoUpdate` (class) — get_cute_tool_message when merge=True (incremental update).
- L109 `test_update_no_result(self)` (method) — No result available — plain update N task(s).
- L116 `test_update_partial_progress(self)` (method) — 1/4 tasks completed — show fraction with checkmark.
- L127 `test_update_halfway(self)` (method) — 2/4 — midpoint progress.
- L137 `test_update_all_completed(self)` (method) — 4/4 — full checkmark.
- L147 `test_update_zero_done(self)` (method) — No completed tasks yet — plain update N task(s).
- L158 `test_update_invalid_result_fallback(self)` (method) — Bad JSON result — fall back to plain update N task(s).
- L168 `test_update_result_missing_summary(self)` (method) — Result no summary key — fall back to plain update.
- L178 `test_update_total_not_in_summary(self)` (method) — Result summary missing total key.
- L188 `test_update_multiple_tasks_in_line(self)` (method) — Update line with several tasks in the update request.
- L202 `TestTodoEdgeCases` (class) — Boundary cases that should not crash.
- L205 `test_merge_default_value(self)` (method) — merge defaults to False in function signature, should be False when absent.
- L212 `test_duration_formatting(self)` (method) — Duration formatting works correctly.
- L223 `test_large_task_count(self)` (method) — Many tasks should not break formatting.
- L229 `test_read_with_no_args_and_no_result(self)` (method) — Completely empty call.
- L235 `TestTodoSkinIntegration` (class) — Verify the skin prefix is applied to todo messages too.
- L240 `test_default_skin_prefix(self)` (method)
