---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_branch_command.py

Symbols in `tests/cli/test_branch_command.py`.

- L20 `session_db(tmp_path)` (function) — Create a real SessionDB for testing.
- L31 `cli_instance(tmp_path, session_db)` (function) — Create a minimal HermesCLI-like object for testing _handle_branch_command.
- L64 `TestBranchCommandCLI` (class) — Test the /branch command logic for the CLI.
- L67 `test_branch_creates_new_session(self, cli_instance, session_db)` (method) — Branching should create a new session in the DB.
- L79 `test_branch_copies_history(self, cli_instance, session_db)` (method) — Branching should copy all messages to the new session.
- L88 `test_branch_preserves_parent_link(self, cli_instance, session_db)` (method) — The new session should reference the original as parent.
- L98 `test_branch_ends_original_session(self, cli_instance, session_db)` (method) — The original session should be marked as ended with 'branched' reason.
- L108 `test_branch_with_custom_name(self, cli_instance, session_db)` (method) — Custom branch name should be used as the title.
- L117 `test_branch_auto_title_lineage(self, cli_instance, session_db)` (method) — Without a name, branch should auto-generate a title from the parent's title.
- L126 `test_branch_empty_conversation(self, cli_instance, session_db)` (method) — Branching with no history should show an error.
- L136 `test_branch_no_session_db(self, cli_instance)` (method) — Branching without a session DB should show an error.
- L146 `test_branch_syncs_agent(self, cli_instance, session_db)` (method) — If an agent is active, branch should sync it to the new session.
- L161 `test_branch_sets_resumed_flag(self, cli_instance, session_db)` (method) — Branch should set _resumed=True to prevent auto-title generation.
- L169 `test_branch_rotates_hermes_session_id_env_and_context(self, cli_instance, session_db)` (method) — Branching must update process-local session-id readers too.
- L188 `test_branch_fires_on_session_switch_hook(self, cli_instance, session_db)` (method) — The /branch command must notify memory providers of the rotation.
- L215 `test_fork_alias(self)` (method) — The /fork alias should resolve to 'branch'.
- L223 `TestBranchCommandDef` (class) — Test the CommandDef registration for /branch.
- L226 `test_branch_in_registry(self)` (method) — The branch command should be in the command registry.
- L232 `test_branch_has_fork_alias(self)` (method) — The branch command should have 'fork' as an alias.
- L238 `test_branch_in_session_category(self)` (method) — The branch command should be in the Session category.
