---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_decompose_db.py

Symbols in `tests/hermes_cli/test_kanban_decompose_db.py`.

- L15 `kanban_home(tmp_path, monkeypatch)` (function)
- L24 `_create_triage(conn, title='rough idea', body=None, assignee=None, tenant=None)` (function)
- L35 `test_decompose_creates_children_and_promotes_root(kanban_home)` (function)
- L71 `test_decompose_returns_none_when_task_missing(kanban_home)` (function)
- L83 `test_decompose_returns_none_when_task_not_in_triage(kanban_home)` (function)
- L96 `test_decompose_empty_children_returns_none(kanban_home)` (function)
- L109 `test_decompose_rejects_self_parent(kanban_home)` (function)
- L122 `test_decompose_rejects_out_of_range_parent(kanban_home)` (function)
- L135 `test_decompose_rejects_cyclic_parents(kanban_home)` (function)
- L151 `test_decompose_records_audit_comment_and_event(kanban_home)` (function)
- L171 `test_decompose_children_inherit_dir_workspace(kanban_home)` (function) — Fan-out children inherit the root's dir workspace, not scratch.
- L192 `test_decompose_children_stay_scratch_when_root_scratch(kanban_home)` (function) — No regression: a scratch root still fans out into scratch children.
- L209 `test_decompose_per_child_workspace_override(kanban_home)` (function) — An explicit per-child workspace beats inheritance.
