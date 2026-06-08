---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_commit_memory_session_context_engine.py

Symbols in `tests/run_agent/test_commit_memory_session_context_engine.py`.

- L16 `_make_minimal_agent(memory_manager, context_compressor, session_id='abc')` (function) — Build an object with just enough surface for commit_memory_session to run.
- L34 `test_commit_memory_session_notifies_context_engine()` (function) — Both the memory manager AND the context engine receive on_session_end.
- L47 `test_commit_memory_session_with_no_messages_passes_empty_list()` (function) — Empty/None messages must still fire both hooks with an empty list.
- L59 `test_commit_memory_session_no_memory_manager_still_notifies_context_engine()` (function) — If only the context engine is configured, it still gets the hook.
- L69 `test_commit_memory_session_no_context_engine_still_notifies_memory_manager()` (function) — If only the memory manager is configured, it still gets the hook.
- L79 `test_commit_memory_session_tolerates_memory_manager_failure()` (function) — A raising memory manager must not block the context engine notification.
- L92 `test_commit_memory_session_tolerates_context_engine_failure()` (function) — A raising context engine must not surface the exception.
