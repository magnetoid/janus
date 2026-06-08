---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_memory_reset.py

Symbols in `tests/hermes_cli/test_memory_reset.py`.

- L15 `memory_env(tmp_path, monkeypatch)` (function) — Set up a fake HERMES_HOME with memory files.
- L34 `_run_memory_reset(target='all', yes=False, monkeypatch=None, confirm_input='no')` (function) — Invoke the memory reset logic from cmd_memory in main.py.
- L62 `TestMemoryReset` (class) — Tests for `hermes memory reset` subcommand.
- L65 `test_reset_all_with_yes_flag(self, memory_env)` (method) — --yes flag should skip confirmation and delete both files.
- L76 `test_reset_memory_only(self, memory_env)` (method) — --target memory should only delete MEMORY.md.
- L85 `test_reset_user_only(self, memory_env)` (method) — --target user should only delete USER.md.
- L94 `test_reset_no_files_exist(self, tmp_path, monkeypatch)` (method) — Should return 'nothing' when no memory files exist.
- L103 `test_reset_confirmation_denied(self, memory_env)` (method) — Without --yes and without typing 'yes', should be cancelled.
- L113 `test_reset_confirmation_accepted(self, memory_env)` (method) — Typing 'yes' should proceed with deletion.
- L122 `test_reset_profile_scoped(self, tmp_path, monkeypatch)` (method) — Reset should work on the active profile's HERMES_HOME.
- L136 `test_reset_partial_files(self, memory_env)` (method) — Reset should work when only one memory file exists.
- L145 `test_reset_empty_memories_dir(self, tmp_path, monkeypatch)` (method) — No memories dir at all should report nothing.
