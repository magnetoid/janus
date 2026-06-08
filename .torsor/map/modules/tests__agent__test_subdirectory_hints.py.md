---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_subdirectory_hints.py

Symbols in `tests/agent/test_subdirectory_hints.py`.

- L11 `project(tmp_path)` (function) — Create a mock project tree with hint files in subdirectories.
- L42 `TestSubdirectoryHintTracker` (class) — Unit tests for SubdirectoryHintTracker.
- L45 `test_working_dir_not_loaded(self, project)` (method) — Working dir is pre-marked as loaded (startup handles it).
- L52 `test_discovers_agents_md_via_ancestor_walk(self, project)` (method) — Reading backend/src/main.py discovers backend/AGENTS.md via ancestor walk.
- L67 `test_discovers_claude_md(self, project)` (method) — Frontend CLAUDE.md should be discovered.
- L76 `test_no_duplicate_loading(self, project)` (method) — Same directory should not be loaded twice.
- L89 `test_no_hints_in_empty_directory(self, project)` (method) — Directories without hint files return None.
- L97 `test_terminal_command_path_extraction(self, project)` (method) — Paths extracted from terminal commands.
- L106 `test_terminal_cd_command(self, project)` (method) — cd into a directory with hints.
- L115 `test_relative_path(self, project)` (method) — Relative paths resolved against working_dir.
- L124 `test_outside_working_dir_rejected(self, tmp_path, project)` (method) — Paths outside working_dir are rejected — no hints from outside workspace.
- L147 `test_outside_working_dir_absolute_path_rejected(self, tmp_path, project)` (method) — Absolute paths like ~/.codex/AGENTS.md are rejected.
- L161 `test_inside_workspace_subdir_allowed(self, project)` (method) — Paths inside working_dir are still allowed.
- L170 `test_sibling_repo_not_loaded_via_ancestor_walk(self, tmp_path, project)` (method) — Ancestor walk from inside working_dir should NOT discover sibling repo hints.
- L194 `test_workdir_arg(self, project)` (method) — The workdir argument from terminal tool is checked.
- L203 `test_deeply_nested_cursorrules(self, project)` (method) — Deeply nested .cursorrules should be discovered.
- L212 `test_hint_format_includes_path(self, project)` (method) — Discovered hints should indicate which file they came from.
- L222 `test_truncation_of_large_hints(self, tmp_path)` (method) — Hint files over the limit are truncated.
- L237 `test_empty_args(self, project)` (method) — Empty args should not crash.
- L243 `test_url_in_command_ignored(self, project)` (method) — URLs in shell commands should not be treated as paths.
- L252 `TestPermissionErrorHandling` (class) — Regression tests for PermissionError in filesystem checks (ref #6214).
- L255 `test_is_valid_subdir_permission_error(self, tmp_path)` (method) — _is_valid_subdir should return False when is_dir() raises PermissionError.
- L263 `test_load_hints_permission_error_on_is_file(self, tmp_path)` (method) — _load_hints_for_directory should skip files when is_file() raises PermissionError.
- L277 `test_check_tool_call_survives_inaccessible_path(self, project)` (method) — Full check_tool_call should not crash when a path is inaccessible.
- L294 `TestOutsideWorkspaceRejection` (class) — Direct tests for _is_valid_subdir rejecting outside-workspace paths.
- L297 `test_is_valid_subdir_rejects_outside_path(self, tmp_path, project)` (method) — _is_valid_subdir should return False for paths outside working_dir.
- L309 `test_is_valid_subdir_allows_inside_path(self, project)` (method) — _is_valid_subdir should return True for paths inside working_dir.
- L315 `test_is_valid_subdir_rejects_parent_dir(self, tmp_path, project)` (method) — _is_valid_subdir should reject parent directories outside working_dir.
- L321 `test_is_valid_subdir_rejects_sibling_dir(self, tmp_path, project)` (method) — _is_valid_subdir should reject a sibling directory (simulating ~/.codex).
