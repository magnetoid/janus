---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_memory_sync_interrupted.py

Symbols in `tests/run_agent/test_memory_sync_interrupted.py`.

- L25 `_bare_agent()` (function) — Build an ``AIAgent`` with only the attributes
- L41 `TestSyncExternalMemoryForTurn` (class)
- L44 `test_interrupted_turn_does_not_sync(self)` (method) — The whole point of #15218: even with a final_response and a
- L57 `test_interrupted_turn_skips_even_when_response_is_full(self)` (method) — A long, seemingly-complete assistant response is still
- L73 `test_completed_turn_syncs_and_queues_prefetch(self)` (method) — Regression guard for the positive path: a normal completed
- L94 `test_completed_turn_syncs_messages_when_present(self)` (method)
- L135 `test_no_final_response_skips(self)` (method) — If the model produced no final_response (e.g. tool-only turn
- L146 `test_no_original_user_message_skips(self)` (method) — No user-origin message means this wasn't a user turn (e.g.
- L158 `test_no_memory_manager_is_a_no_op(self)` (method) — Sessions without an external memory manager must not crash
- L175 `test_sync_exception_is_swallowed(self)` (method) — External memory providers are best-effort; a misconfigured
- L193 `test_prefetch_exception_is_swallowed(self)` (method) — Same best-effort contract applies to the prefetch step — a
- L222 `test_sync_matrix(self, interrupted, final, user, expect_sync)` (method)
