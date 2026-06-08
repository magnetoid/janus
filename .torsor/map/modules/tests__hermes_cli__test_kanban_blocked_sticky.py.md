---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_blocked_sticky.py

Symbols in `tests/hermes_cli/test_kanban_blocked_sticky.py`.

- L41 `kanban_home(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)` (function) — Isolated HERMES_HOME with an empty kanban DB.
- L56 `test_worker_block_is_not_auto_promoted_by_recompute_ready(kanban_home: Path)` (function) — A standalone task that a worker explicitly blocks for review
- L79 `test_worker_block_on_child_with_done_parents_is_still_sticky(kanban_home: Path)` (function) — The parent-completion path is the one ``recompute_ready`` was
- L107 `test_circuit_breaker_block_still_auto_promotes(kanban_home: Path)` (function) — A child that was put into ``blocked`` *without* a worker-issued
- L146 `test_gave_up_event_alone_does_not_make_block_sticky(kanban_home: Path)` (function) — The circuit-breaker emits ``gave_up`` (not ``blocked``).  Make
- L178 `test_unblock_clears_sticky_state_and_lets_block_recover(kanban_home: Path)` (function) — ``hermes kanban unblock`` (or the ``kanban_unblock`` tool) is
- L214 `test_protocol_violation_loop_is_broken(kanban_home: Path)` (function) — Reproduces the exact #28712 loop and asserts the dispatcher
