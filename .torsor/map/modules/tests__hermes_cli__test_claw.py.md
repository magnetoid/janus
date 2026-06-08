---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_claw.py

Symbols in `tests/hermes_cli/test_claw.py`.

- L18 `TestFindMigrationScript` (class) — Test script discovery in known locations.
- L21 `test_finds_project_root_script(self, tmp_path)` (method)
- L27 `test_finds_installed_script(self, tmp_path)` (method)
- L36 `test_returns_none_when_missing(self, tmp_path)` (method)
- L49 `TestFindOpenclawDirs` (class) — Test discovery of OpenClaw directories.
- L52 `test_finds_openclaw_dir(self, tmp_path)` (method)
- L59 `test_finds_legacy_dirs(self, tmp_path)` (method)
- L70 `test_returns_empty_when_none_exist(self, tmp_path)` (method)
- L81 `TestScanWorkspaceState` (class) — Test scanning for workspace state files.
- L84 `test_finds_root_state_files(self, tmp_path)` (method)
- L92 `test_finds_workspace_state_files(self, tmp_path)` (method)
- L102 `test_ignores_hidden_dirs(self, tmp_path)` (method)
- L111 `test_empty_dir_returns_empty(self, tmp_path)` (method)
- L123 `TestArchiveDirectory` (class) — Test directory archival (rename).
- L126 `test_renames_to_pre_migration(self, tmp_path)` (method)
- L137 `test_adds_timestamp_when_archive_exists(self, tmp_path)` (method)
- L148 `test_dry_run_does_not_rename(self, tmp_path)` (method)
- L162 `TestClawCommand` (class) — Test the claw_command router.
- L165 `test_routes_to_migrate(self)` (method)
- L173 `test_routes_to_cleanup(self)` (method)
- L179 `test_routes_clean_alias(self)` (method)
- L185 `test_shows_help_for_no_action(self, capsys)` (method)
- L198 `TestCmdMigrate` (class) — Test the migrate command handler.
- L202 `_mock_openclaw_running(self)` (method)
- L206 `test_error_when_source_missing(self, tmp_path, capsys)` (method)
- L217 `test_error_when_script_missing(self, tmp_path, capsys)` (method)
- L234 `test_dry_run_succeeds(self, tmp_path, capsys)` (method)
- L273 `test_execute_with_confirmation(self, tmp_path, capsys)` (method)
- L314 `test_dry_run_does_not_touch_source(self, tmp_path, capsys)` (method) — Dry run should not modify the source directory.
- L347 `test_execute_cancelled_by_user(self, tmp_path, capsys)` (method)
- L385 `test_execute_with_yes_skips_confirmation(self, tmp_path, capsys)` (method)
- L417 `test_handles_migration_error(self, tmp_path, capsys)` (method)
- L442 `test_full_preset_does_not_enable_secrets_silently(self, tmp_path, capsys)` (method) — The 'full' preset must NOT auto-enable migrate_secrets.
- L485 `test_full_preset_with_explicit_migrate_secrets_passes_through(self, tmp_path, capsys)` (method) — Explicit --migrate-secrets still works under --preset full.
- L526 `TestCmdCleanup` (class) — Test the cleanup command handler.
- L530 `_mock_openclaw_running(self)` (method)
- L534 `test_no_dirs_found(self, tmp_path, capsys)` (method)
- L541 `test_dry_run_lists_dirs(self, tmp_path, capsys)` (method)
- L556 `test_archives_with_yes(self, tmp_path, capsys)` (method)
- L572 `test_skips_when_user_declines(self, tmp_path, capsys)` (method)
- L591 `test_explicit_source(self, tmp_path, capsys)` (method)
- L603 `test_shows_workspace_details(self, tmp_path, capsys)` (method)
- L619 `test_handles_multiple_dirs(self, tmp_path, capsys)` (method)
- L640 `TestPrintMigrationReport` (class) — Test the report formatting function.
- L643 `test_dry_run_report(self, capsys)` (method)
- L661 `test_execute_report(self, capsys)` (method)
- L675 `test_empty_report(self, capsys)` (method)
- L685 `TestDetectOpenclawProcesses` (class)
- L686 `test_returns_match_when_pgrep_finds_openclaw(self)` (method)
- L700 `test_returns_empty_when_pgrep_finds_nothing(self)` (method)
- L712 `test_detects_systemd_service(self)` (method)
- L725 `test_returns_match_on_windows_when_openclaw_exe_running(self)` (method)
- L736 `test_returns_match_on_windows_when_node_exe_has_openclaw_in_cmdline(self)` (method)
- L749 `test_returns_empty_on_windows_when_nothing_found(self)` (method)
- L762 `TestWarnIfOpenclawRunning` (class)
- L763 `test_noop_when_not_running(self, capsys)` (method)
- L769 `test_warns_and_exits_when_running_and_user_declines(self, capsys)` (method)
- L779 `test_warns_and_continues_when_running_and_user_accepts(self, capsys)` (method)
- L787 `test_warns_and_continues_in_auto_yes_mode(self, capsys)` (method)
- L793 `test_warns_and_continues_in_non_interactive_session(self, capsys)` (method)
