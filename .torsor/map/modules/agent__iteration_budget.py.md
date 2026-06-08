---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/iteration_budget.py

Symbols in `agent/iteration_budget.py`.

- L17 `IterationBudget` (class) — Thread-safe iteration counter for an agent.
- L32 `__init__(self, max_total: int)` (method)
- L37 `consume(self)` (method) — Try to consume one iteration.  Returns True if allowed.
- L45 `refund(self)` (method) — Give back one iteration (e.g. for execute_code turns).
- L52 `used(self)` (method)
- L57 `remaining(self)` (method)
