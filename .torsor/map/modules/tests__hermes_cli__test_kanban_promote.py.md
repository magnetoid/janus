---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_promote.py

Symbols in `tests/hermes_cli/test_kanban_promote.py`.

- L22 `kanban_home(tmp_path, monkeypatch)` (function)
- L34 `conn(kanban_home)` (function)
- L39 `_stuck_todo(conn, *, parents_done=True, n_parents=1)` (function) — Build the #28822 scenario: child in 'todo' whose parents may
- L59 `test_promote_stuck_todo_succeeds(conn)` (function)
- L66 `test_promote_refuses_when_parent_not_done(conn)` (function)
- L75 `test_promote_with_force_bypasses_dependency_check(conn)` (function)
- L84 `test_promote_emits_audit_event(conn)` (function)
- L99 `test_promote_force_records_forced_flag(conn)` (function)
- L110 `test_promote_does_not_change_assignee(conn)` (function)
- L118 `test_promote_dry_run_does_not_mutate(conn)` (function)
- L131 `test_promote_dry_run_reports_dependency_failure(conn)` (function)
- L138 `test_promote_rejects_non_todo_status(conn)` (function)
- L146 `test_promote_rejects_unknown_task(conn)` (function)
- L152 `test_promote_blocked_task_works(conn)` (function)
- L168 `_promote_ns(task_id, *, ids=None, reason=None, force=False, dry_run=False, as_json=False)` (function)
- L180 `test_cli_promote_bulk_ids_promotes_all(kanban_home, capsys)` (function)
- L198 `test_cli_promote_bulk_partial_failure_exits_1(kanban_home, capsys)` (function) — Bulk with one bad id: good ones still promote, exit code reflects failure.
- L213 `test_cli_promote_bulk_json_emits_list(kanban_home, capsys)` (function)
- L227 `test_cli_promote_single_json_stays_flat_object(kanban_home, capsys)` (function) — Back-compat: single-id JSON is still a flat object, not a list.
- L240 `test_cli_promote_dedupes_duplicate_ids(kanban_home, capsys)` (function) — Same id in positional + --ids must only attempt the promotion once.
