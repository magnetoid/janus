---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_db_init.py

Symbols in `tests/hermes_cli/test_kanban_db_init.py`.

- L10 `_make_legacy_db(path: Path)` (function) — Write a kanban DB with the pre-AUTOINCREMENT (TEXT PK) schema for the
- L48 `_setup_home(tmp_path, monkeypatch)` (function)
- L59 `_table_struct(conn: sqlite3.Connection, table: str)` (function)
- L72 `test_connect_initialization_is_thread_safe(tmp_path, monkeypatch)` (function)
- L104 `test_legacy_text_pk_tables_rebuilt_to_integer_autoincrement(tmp_path, monkeypatch)` (function) — A pre-AUTOINCREMENT DB is migrated in place: id columns become INTEGER
- L138 `test_rebuilt_schema_matches_fresh_db(tmp_path, monkeypatch)` (function) — The rebuilt tables must be structurally identical to a fresh DB, so the
- L152 `test_migration_is_idempotent(tmp_path, monkeypatch)` (function) — Re-opening an already-migrated DB is a no-op and leaves data intact.
- L166 `test_unseen_events_for_sub_survives_migrated_db(tmp_path, monkeypatch)` (function) — The crash that motivated #35096 — ``int(None)`` on a NULL cursor — is
