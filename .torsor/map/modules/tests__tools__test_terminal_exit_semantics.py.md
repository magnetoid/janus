---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_terminal_exit_semantics.py

Symbols in `tests/tools/test_terminal_exit_semantics.py`.

- L8 `TestInterpretExitCode` (class) — Test _interpret_exit_code returns correct notes for known command semantics.
- L13 `test_success_returns_none(self)` (method)
- L28 `test_grep_family_no_matches(self, cmd)` (method)
- L33 `test_grep_real_error_no_note(self)` (method) — grep exit 2+ is a real error — should return None.
- L40 `test_diff_files_differ(self)` (method)
- L45 `test_colordiff_files_differ(self)` (method)
- L50 `test_diff_real_error_no_note(self)` (method)
- L55 `test_test_condition_false(self)` (method)
- L60 `test_bracket_condition_false(self)` (method)
- L67 `test_find_partial_success(self)` (method)
- L74 `test_curl_timeout(self)` (method)
- L79 `test_curl_connection_refused(self)` (method)
- L86 `test_git_diff_exit_1(self)` (method)
- L93 `test_pipeline_last_command(self)` (method) — In a pipeline, the last command determines the exit code.
- L99 `test_and_chain_last_command(self)` (method)
- L104 `test_semicolon_chain_last_command(self)` (method)
- L109 `test_or_chain_last_command(self)` (method)
- L116 `test_full_path_command(self)` (method)
- L123 `test_env_var_prefix_stripped(self)` (method)
- L128 `test_multiple_env_vars(self)` (method)
- L142 `test_unknown_commands_return_none(self, cmd)` (method)
- L147 `test_empty_command(self)` (method)
- L150 `test_only_env_vars(self)` (method) — Command with only env var assignments, no actual command.
