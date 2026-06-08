---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_specify_db.py

Symbols in `tests/hermes_cli/test_kanban_specify_db.py`.

- L14 `kanban_home(tmp_path, monkeypatch)` (function) — Isolated HERMES_HOME with an empty kanban DB.
- L24 `_create_triage(conn, title='rough idea', body=None, assignee=None)` (function)
- L34 `test_specify_promotes_triage_to_todo(kanban_home)` (function)
- L55 `test_specify_with_open_parent_lands_in_todo_not_ready(kanban_home)` (function)
- L79 `test_specify_refuses_non_triage_task(kanban_home)` (function)
- L91 `test_specify_returns_false_for_unknown_id(kanban_home)` (function)
- L97 `test_specify_rejects_blank_title(kanban_home)` (function)
- L104 `test_specify_emits_event(kanban_home)` (function)
- L124 `test_specify_records_audit_comment_only_when_author_given(kanban_home)` (function)
- L144 `test_specify_skips_comment_when_nothing_changed(kanban_home)` (function)
- L165 `test_specify_with_only_body_preserves_title(kanban_home)` (function)
- L176 `test_specify_second_call_noop_false(kanban_home)` (function)
