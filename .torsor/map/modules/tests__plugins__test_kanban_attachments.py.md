---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/test_kanban_attachments.py

Symbols in `tests/plugins/test_kanban_attachments.py`.

- L31 `_load_plugin_router()` (function)
- L46 `kanban_home(tmp_path, monkeypatch)` (function)
- L56 `client(kanban_home)` (function)
- L62 `_make_task(conn, title='t')` (function)
- L71 `test_add_list_get_delete_attachment(kanban_home, tmp_path)` (function)
- L113 `test_add_attachment_rejects_unknown_task(kanban_home)` (function)
- L124 `test_add_attachment_appends_event(kanban_home)` (function)
- L137 `test_delete_attachment_missing_returns_none(kanban_home)` (function)
- L145 `test_attachments_root_is_per_board(kanban_home, monkeypatch)` (function)
- L155 `test_attachments_root_env_override(kanban_home, monkeypatch, tmp_path)` (function)
- L167 `test_worker_context_lists_attachments_with_absolute_path(kanban_home)` (function)
- L192 `test_worker_context_no_attachments_section_when_empty(kanban_home)` (function)
- L207 `_create_task_via_api(client)` (function)
- L213 `test_upload_list_download_delete_roundtrip(client)` (function)
- L251 `test_upload_sanitizes_traversal_filename(client)` (function)
- L265 `test_upload_name_collision_gets_suffixed(client)` (function)
- L282 `test_upload_unknown_task_404(client)` (function)
- L290 `test_download_unknown_attachment_404(client)` (function)
