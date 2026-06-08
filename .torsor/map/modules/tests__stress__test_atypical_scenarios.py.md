---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/stress/test_atypical_scenarios.py

Symbols in `tests/stress/test_atypical_scenarios.py`.

- L40 `scenario(name)` (function) — Decorator: run `fn` in its own HERMES_HOME, collect failures.
- L87 `_(home, kb)` (function)
- L134 `_(home, kb)` (function) — 1MB body + 1MB summary + deeply nested metadata.
- L162 `_(home, kb)` (function) — SQLite parameterized queries should neutralize all of these, but
- L194 `_(home, kb)` (function) — Summaries with newlines, tabs, and shell metachars.
- L219 `_(home, kb)` (function) — CLI rejects malformed JSON and non-dict JSON cleanly.
- L261 `_(home, kb)` (function) — A → B → A should be refused. If it's allowed, recompute_ready
- L299 `_(home, kb)` (function) — A task cannot be its own parent.
- L315 `_(home, kb)` (function) — Root → (A, B) → leaf. Leaf should promote to ready only when
- L350 `_(home, kb)` (function) — One parent, 500 children. Completing the parent should promote
- L380 `_(home, kb)` (function) — 500 parents, 1 child. Child should not promote until all 500 done.
- L414 `_(home, kb)` (function) — `workspace_path='../../../etc/passwd'` or absolute-outside-home
- L452 `_(home, kb)` (function) — Dispatching a task whose workspace can't be resolved should go
- L491 `_(home, kb)` (function) — NTP jumps backward. Run.started_at gets written as 1234 but by
- L531 `_(home, kb)` (function) — HERMES_HOME at a path with spaces — should work but catches
- L558 `_(home, kb)` (function) — HERMES_HOME with non-ASCII chars.
- L580 `_(home, kb)` (function) — HERMES_HOME is a symlink to the real dir. _INITIALIZED_PATHS
- L623 `_(home, kb)` (function) — 1000 reclaim cycles on a single task → 1000 run rows. Verify
- L659 `_(home, kb)` (function) — 100 distinct tenants with 50 tasks each. board_stats + list_tasks
- L688 `_idempotency_race_worker(hermes_home: str, key: str, result_file: str, barrier_path: str)` (function) — Subprocess body for the idempotency race test.
- L713 `_(home, kb)` (function) — Two processes concurrently call create_task with the same
- L763 `_(home, kb)` (function) — Profile names can contain @-signs, dots, hyphens. Some users
- L790 `_(home, kb)` (function) — A task in 'done' should NOT be reclaimable — reclaim/claim paths
- L814 `_(home, kb)` (function) — An archived task should be invisible to normal ops.
- L843 `_(home, kb)` (function) — Task without an assignee should never be claimed by dispatch_once,
- L862 `_(home, kb)` (function) — 1000 comments on a single task — build_worker_context should still
- L884 `_(home, kb)` (function) — Empty title should be rejected (we already do this). Empty body,
- L916 `_(home, kb)` (function) — Someone pastes a multi-line string into --tenant. Kernel should
- L935 `_(home, kb)` (function) — recompute_ready promotes a todo child only if ALL parents are
- L978 `_(home, kb)` (function) — FastAPI TestClient POST /tasks with atypical JSON bodies.
- L1037 `main()` (function)
