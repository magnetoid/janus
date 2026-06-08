---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_tool_executor_contextvar_propagation.py

Symbols in `tests/run_agent/test_tool_executor_contextvar_propagation.py`.

- L40 `test_executor_submit_without_copy_context_does_not_propagate()` (function) — Documents the Python contract the fix relies on.
- L72 `test_executor_submit_with_copy_context_run_propagates()` (function) — Positive case: the explicit ``copy_context().run(...)`` wrapper the
- L94 `test_run_tool_worker_sees_parent_approval_session_key()` (function) — End-to-end call-site guard.
- L141 `test_run_agent_concurrent_executor_wraps_submit_with_copy_context()` (function) — Source-level guard that the fix stays at the REAL call site.
- L230 `test_two_concurrent_tool_batches_keep_session_keys_isolated()` (function) — End-to-end guard: two callers each set a different session key
