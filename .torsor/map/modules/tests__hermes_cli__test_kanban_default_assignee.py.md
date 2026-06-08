---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_default_assignee.py

Symbols in `tests/hermes_cli/test_kanban_default_assignee.py`.

- L18 `isolated_kanban_home(monkeypatch)` (function) — Spin up a fresh HERMES_HOME with a clean kanban DB.
- L33 `_fake_spawn(*args, **kwargs)` (function) — Stand-in for the real worker spawn — returns a fake PID.
- L38 `test_unassigned_task_skipped_without_default_assignee(isolated_kanban_home)` (function) — Baseline: with no default_assignee, an unassigned ready task is
- L56 `test_unassigned_task_auto_assigned_with_default_assignee(isolated_kanban_home)` (function) — Core #27145 contract: with default_assignee set, an unassigned ready
- L91 `test_dry_run_with_default_assignee_reports_without_mutating(isolated_kanban_home)` (function) — Dry-run mode: reports what WOULD happen (task in auto_assigned_default,
- L113 `test_whitespace_default_assignee_treated_as_none(isolated_kanban_home)` (function) — Empty / whitespace-only default_assignee values must be treated as
- L130 `test_explicitly_assigned_task_untouched_by_default_assignee(isolated_kanban_home)` (function) — A task with an explicit assignee must NOT be touched by the
- L147 `test_dispatch_result_has_auto_assigned_default_field()` (function) — Schema-level invariant: DispatchResult exposes the
