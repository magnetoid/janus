---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_boards.py

Symbols in `tests/hermes_cli/test_kanban_boards.py`.

- L39 `fresh_home(tmp_path, monkeypatch)` (function) — Isolated HERMES_HOME with no prior kanban state.
- L71 `TestSlugValidation` (class)
- L76 `test_accepts_valid(self, good)` (method)
- L85 `test_rejects_invalid(self, bad)` (method)
- L89 `test_empty_returns_none(self)` (method)
- L94 `test_auto_lowercases(self)` (method)
- L106 `TestPathResolution` (class)
- L107 `test_default_board_legacy_path(self, fresh_home)` (method) — The default board's DB lives at ``<root>/kanban.db`` for back-compat.
- L112 `test_named_board_under_boards_dir(self, fresh_home)` (method)
- L116 `test_workspaces_per_board(self, fresh_home)` (method)
- L123 `test_logs_per_board(self, fresh_home)` (method)
- L129 `test_env_var_db_override_still_wins(self, fresh_home, tmp_path, monkeypatch)` (method) — ``HERMES_KANBAN_DB`` pins the file regardless of board= arg.
- L136 `test_env_var_workspaces_override(self, fresh_home, tmp_path, monkeypatch)` (method)
- L146 `TestCurrentBoard` (class)
- L147 `test_default_when_unset(self, fresh_home)` (method)
- L150 `test_env_var_takes_precedence(self, fresh_home, monkeypatch)` (method)
- L158 `test_file_pointer_honoured(self, fresh_home)` (method)
- L163 `test_stale_file_pointer_falls_back_to_default(self, fresh_home)` (method)
- L172 `test_empty_board_dir_does_not_count_as_existing(self, fresh_home)` (method)
- L179 `test_env_beats_file(self, fresh_home, monkeypatch)` (method)
- L186 `test_stale_env_falls_through_to_file_pointer(self, fresh_home, monkeypatch)` (method)
- L192 `test_invalid_env_falls_through(self, fresh_home, monkeypatch)` (method)
- L197 `test_clear_current_board(self, fresh_home)` (method)
- L203 `test_kanban_db_path_reads_current(self, fresh_home)` (method) — kanban_db_path() with no args respects the on-disk pointer.
- L215 `TestBoardCRUD` (class)
- L216 `test_create_and_list(self, fresh_home)` (method)
- L222 `test_create_is_idempotent(self, fresh_home)` (method)
- L228 `test_create_writes_metadata(self, fresh_home)` (method)
- L245 `test_remove_archive(self, fresh_home)` (method)
- L252 `test_remove_hard_delete(self, fresh_home)` (method)
- L260 `test_remove_default_forbidden(self, fresh_home)` (method)
- L264 `test_remove_nonexistent_raises(self, fresh_home)` (method)
- L268 `test_remove_clears_current_pointer(self, fresh_home)` (method)
- L275 `test_remove_clears_init_cache_for_recreated_db(self, fresh_home, archive)` (method)
- L305 `test_rename_updates_metadata(self, fresh_home)` (method)
- L317 `TestConnectionIsolation` (class)
- L318 `test_tasks_do_not_leak_across_boards(self, fresh_home)` (method)
- L340 `test_connect_without_args_uses_current(self, fresh_home)` (method)
- L349 `test_connect_env_var_overrides_current(self, fresh_home, monkeypatch)` (method)
- L361 `test_connect_stale_env_uses_fallback_board_without_recreating_it(self, fresh_home, monkeypatch)` (method)
- L382 `TestWorkerSpawnEnv` (class) — Ensure the dispatcher pins ``HERMES_KANBAN_BOARD`` / DB / workspaces on spawn.
- L389 `test_default_spawn_sets_env_vars(self, fresh_home, monkeypatch)` (method)
- L432 `test_default_board_spawn_keeps_legacy_paths(self, fresh_home, monkeypatch)` (method)
- L470 `_cli(args: list[str], env_extra: dict | None=None)` (function) — Run ``hermes kanban …`` with PYTHONPATH pinned to the worktree.
- L486 `TestCLI` (class)
- L487 `test_boards_list_default_only(self, tmp_path)` (method)
- L496 `test_boards_create_and_switch(self, tmp_path)` (method)
- L511 `test_per_board_task_isolation_via_cli(self, tmp_path)` (method)
- L535 `test_board_flag_rejects_unknown(self, tmp_path)` (method)
- L543 `test_board_flag_rejects_empty_board_dir(self, tmp_path)` (method)
- L550 `test_boards_rm_archives(self, tmp_path)` (method)
