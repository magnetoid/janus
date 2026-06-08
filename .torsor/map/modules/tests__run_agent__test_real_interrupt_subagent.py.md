---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_real_interrupt_subagent.py

Symbols in `tests/run_agent/test_real_interrupt_subagent.py`.

- L16 `_make_slow_api_response(delay=5.0)` (function) — Create a mock that simulates a slow API response (like a real LLM call).
- L38 `TestRealSubagentInterrupt` (class) — Test interrupt with real AIAgent child through delegate_tool.
- L41 `setUp(self)` (method)
- L45 `tearDown(self)` (method)
- L48 `test_interrupt_child_during_api_call(self)` (method) — Real AIAgent child interrupted while making API call.
