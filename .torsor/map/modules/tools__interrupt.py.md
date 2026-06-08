---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/interrupt.py

Symbols in `tools/interrupt.py`.

- L39 `set_interrupt(active: bool, thread_id: int | None=None)` (function) — Set or clear interrupt for a specific thread.
- L62 `is_interrupted()` (function) — Check if an interrupt has been requested for the current thread.
- L81 `_ThreadAwareEventProxy` (class) — Drop-in proxy that maps threading.Event methods to per-thread state.
- L84 `is_set(self)` (method)
- L87 `set(self)` (method)
- L90 `clear(self)` (method)
- L93 `wait(self, timeout: float | None=None)` (method) — Not truly supported — returns current state immediately.
