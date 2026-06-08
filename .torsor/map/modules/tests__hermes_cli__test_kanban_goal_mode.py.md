---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_goal_mode.py

Symbols in `tests/hermes_cli/test_kanban_goal_mode.py`.

- L25 `kanban_home(tmp_path, monkeypatch)` (function)
- L38 `test_goal_mode_defaults_off(kanban_home)` (function)
- L46 `test_goal_mode_persists(kanban_home)` (function)
- L60 `test_goal_mode_without_max_turns(kanban_home)` (function)
- L70 `test_legacy_db_migrates_goal_columns(tmp_path, monkeypatch)` (function) — A tasks table created without goal columns must gain them on init.
- L124 `test_spawn_sets_goal_env_only_when_enabled(kanban_home, monkeypatch)` (function)
- L154 `test_spawn_no_goal_env_for_plain_task(kanban_home, monkeypatch)` (function)
- L181 `_patch_judge(monkeypatch, verdicts)` (function) — Make judge_goal return a scripted sequence of verdicts.
- L192 `test_loop_stops_when_worker_already_completed(monkeypatch)` (function)
- L209 `test_loop_continues_then_worker_completes(monkeypatch)` (function)
- L229 `test_loop_blocks_on_budget_exhaustion(monkeypatch)` (function)
- L250 `test_loop_finalize_nudge_when_judge_done_but_open(monkeypatch)` (function)
- L271 `test_loop_blocks_when_judge_done_but_never_finalizes(monkeypatch)` (function)
- L290 `test_loop_stops_if_task_reclaimed(monkeypatch)` (function)
