---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_interrupt.py

Symbols in `tests/tools/test_interrupt.py`.

- L16 `TestInterruptModule` (class) — Tests for tools/interrupt.py
- L19 `test_set_and_check(self)` (method)
- L30 `test_thread_safety(self)` (method) — Set from one thread targeting another thread's ident.
- L63 `TestPreToolCheck` (class) — Verify that _execute_tool_calls skips all tools when interrupted.
- L66 `test_all_tools_skipped_when_interrupted(self)` (method) — Mock an interrupted agent and verify no tools execute.
- L119 `TestMessageCombining` (class) — Verify multiple interrupt messages are joined.
- L122 `test_cli_interrupt_queue_drain(self)` (method) — Simulate draining multiple messages from the interrupt queue.
- L144 `test_gateway_pending_messages_append(self)` (method) — Simulate gateway _pending_messages append logic.
- L168 `TestSIGKILLEscalation` (class) — Test that SIGTERM-resistant processes get SIGKILL'd.
- L175 `test_sigterm_trap_killed_within_2s(self)` (method) — A process that traps SIGTERM should be SIGKILL'd after 1s grace.
- L210 `TestRunToolCleanupOnBaseException` (class) — Verify that _run_tool cleans up _interrupted_threads even when
- L220 `test_cleanup_on_base_exception(self)` (method)
