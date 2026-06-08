---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_interrupt_propagation.py

Symbols in `tests/run_agent/test_interrupt_propagation.py`.

- L15 `TestInterruptPropagationToChild` (class) — Verify interrupt propagates from parent to child agent.
- L18 `setUp(self)` (method)
- L21 `tearDown(self)` (method)
- L24 `_make_bare_agent(self)` (method) — Create a bare AIAgent via __new__ with all interrupt-related attrs.
- L42 `test_parent_interrupt_sets_child_flag(self)` (method) — When parent.interrupt() is called, child._interrupt_requested should be set.
- L57 `test_child_clear_interrupt_at_start_clears_thread(self)` (method) — child.clear_interrupt() at start of run_conversation clears the
- L75 `test_interrupt_during_child_api_call_detected(self)` (method) — Interrupt set during _interruptible_api_call is detected within 0.5s.
- L110 `test_concurrent_interrupt_propagation(self)` (method) — Simulates exact CLI flow: parent runs delegate in thread, main thread interrupts.
- L138 `test_prestart_interrupt_binds_to_execution_thread(self)` (method) — An interrupt that arrives before startup should bind to the agent thread.
- L169 `TestPerThreadInterruptIsolation` (class) — Verify that interrupting one agent does NOT affect another agent's thread.
- L177 `setUp(self)` (method)
- L180 `tearDown(self)` (method)
- L183 `test_interrupt_only_affects_target_thread(self)` (method) — set_interrupt(True, tid) only makes is_interrupted() True on that thread.
- L223 `test_clear_interrupt_only_clears_target_thread(self)` (method) — Clearing one thread's interrupt doesn't clear another's.
