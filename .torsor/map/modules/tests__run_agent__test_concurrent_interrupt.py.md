---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_concurrent_interrupt.py

Symbols in `tests/run_agent/test_concurrent_interrupt.py`.

- L11 `_isolate_hermes(tmp_path, monkeypatch)` (function)
- L16 `_make_agent(monkeypatch)` (function) — Create a minimal AIAgent-like object with just the methods under test.
- L87 `_FakeToolCall` (class)
- L88 `__init__(self, name, args='{}', call_id='tc_1')` (method)
- L94 `_FakeAssistantMsg` (class)
- L95 `__init__(self, tool_calls)` (method)
- L101 `test_concurrent_preflight_interrupt_skips_all(monkeypatch)` (function) — When _interrupt_requested is already set before concurrent execution,
- L123 `test_clear_interrupt_clears_worker_tids(monkeypatch)` (function) — After clear_interrupt(), stale worker-tid bits must be cleared so the
