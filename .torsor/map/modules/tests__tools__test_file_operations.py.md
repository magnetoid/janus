---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_file_operations.py

Symbols in `tests/tools/test_file_operations.py`.

- L28 `TestIsWriteDenied` (class)
- L29 `test_ssh_authorized_keys_denied(self)` (method)
- L33 `test_ssh_id_rsa_denied(self)` (method)
- L37 `test_netrc_denied(self)` (method)
- L41 `test_aws_prefix_denied(self)` (method)
- L45 `test_kube_prefix_denied(self)` (method)
- L49 `test_normal_file_allowed(self, tmp_path)` (method)
- L53 `test_project_file_allowed(self)` (method)
- L56 `test_tilde_expansion(self)` (method)
- L74 `test_hermes_control_files_oauth_and_mcp_tokens_denied(self, path)` (method) — Hermes control files, PKCE creds, mcp-tokens, and pairing entries must be write-denied.
- L90 `test_hermes_control_files_and_oauth_traversal_denied(self, path)` (method) — Path traversal attempts to protected Hermes files must be blocked.
- L105 `test_standard_paths_allowed(self, path)` (method) — Unrelated paths must still be allowed.
- L113 `test_control_files_and_oauth_protected_in_profile_mode(self, tmp_path, monkeypatch, name)` (method) — Under a profile, BOTH <profile>/X and <root>/X must be denied (#15981 shape).
- L134 `test_mcp_tokens_dir_protected_in_profile_mode(self, tmp_path, monkeypatch)` (method) — mcp-tokens/ under profile AND under root must both be denied.
- L146 `test_pairing_dir_denied(self, tmp_path, monkeypatch)` (method) — Regression: pairing/ must be write-denied under both profile and root.
- L175 `TestReadResult` (class)
- L176 `test_to_dict_omits_defaults(self)` (method)
- L182 `test_to_dict_preserves_empty_content(self)` (method) — Empty file should still have content key in the dict.
- L191 `test_to_dict_includes_values(self)` (method)
- L198 `test_binary_fields(self)` (method)
- L206 `TestWriteResult` (class)
- L207 `test_to_dict_omits_none(self)` (method)
- L214 `test_to_dict_includes_error(self)` (method)
- L220 `TestPatchResult` (class)
- L221 `test_to_dict_success(self)` (method)
- L228 `test_to_dict_error(self)` (method)
- L235 `TestSearchResult` (class)
- L236 `test_to_dict_with_matches(self)` (method)
- L244 `test_to_dict_empty(self)` (method)
- L250 `test_to_dict_files_mode(self)` (method)
- L255 `test_to_dict_count_mode(self)` (method)
- L260 `test_truncated_flag(self)` (method)
- L266 `TestLintResult` (class)
- L267 `test_skipped(self)` (method)
- L273 `test_success(self)` (method)
- L278 `test_error(self)` (method)
- L290 `mock_env()` (function) — Create a mock terminal environment.
- L299 `file_ops(mock_env)` (function)
- L303 `TestShellFileOpsHelpers` (class)
- L304 `test_normalize_read_pagination_clamps_invalid_values(self)` (method)
- L310 `test_normalize_search_pagination_clamps_invalid_values(self)` (method)
- L315 `test_escape_shell_arg_simple(self, file_ops)` (method)
- L318 `test_escape_shell_arg_with_quotes(self, file_ops)` (method)
- L324 `test_is_likely_binary_by_extension(self, file_ops)` (method)
- L330 `test_is_likely_binary_by_content(self, file_ops)` (method)
- L338 `test_is_image(self, file_ops)` (method)
- L345 `test_add_line_numbers(self, file_ops)` (method)
- L353 `test_add_line_numbers_with_offset(self, file_ops)` (method)
- L359 `test_add_line_numbers_truncates_long_lines(self, file_ops)` (method)
- L364 `test_unified_diff(self, file_ops)` (method)
- L372 `test_cwd_from_env(self, mock_env)` (method)
- L377 `test_cwd_fallback_to_slash(self)` (method)
- L382 `test_read_file_strips_leaked_terminal_fence_markers(self, mock_env)` (method)
- L411 `test_read_file_raw_strips_leaked_terminal_fence_markers(self, mock_env)` (method)
- L435 `TestSearchPathValidation` (class) — Test that search() returns an error for non-existent paths.
- L438 `test_search_nonexistent_path_returns_error(self, mock_env)` (method) — search() should return an error when the path doesn't exist.
- L452 `test_search_nonexistent_path_files_mode(self, mock_env)` (method) — search(target='files') should also return error for bad paths.
- L466 `test_search_existing_path_proceeds(self, mock_env)` (method) — search() should proceed normally when the path exists.
- L481 `test_search_rg_error_exit_code(self, mock_env)` (method) — search() should report error when rg returns exit code 2.
- L499 `TestSearchFilesFallbackHiddenPaths` (class)
- L500 `_make_env(self)` (method)
- L519 `test_hidden_root_with_hidden_ancestor_includes_files(self, tmp_path, monkeypatch)` (method) — Fallback find should include visible files when path is inside hidden root.
- L539 `test_normal_root_still_excludes_hidden_descendants(self, tmp_path, monkeypatch)` (method) — Fallback find should still exclude hidden descendant paths for normal roots.
- L559 `TestShellFileOpsWriteDenied` (class)
- L560 `test_write_file_denied_path(self, file_ops)` (method)
- L565 `test_patch_replace_denied_path(self, file_ops)` (method)
- L570 `test_delete_file_denied_path(self, file_ops)` (method)
- L575 `test_move_file_src_denied(self, file_ops)` (method)
- L580 `test_move_file_dst_denied(self, file_ops)` (method)
- L585 `test_move_file_failure_path(self, mock_env)` (method)
- L593 `TestPatchReplacePostWriteVerification` (class) — Tests for the post-write verification added in patch_replace.
- L601 `test_patch_replace_fails_when_file_not_persisted(self, mock_env)` (method) — write_file reports success but the re-read returns old content:
- L637 `test_patch_replace_succeeds_when_file_persisted(self, mock_env)` (method) — Normal success path: write persists, verify read returns new bytes.
- L664 `test_patch_replace_fails_when_verify_read_errors(self, mock_env)` (method) — If the verify-read step itself fails (exit code != 0), return an error.
- L696 `_DeletedTestGitBaselineCheck` (class) — Removed May 2026 — these tests asserted on a ``_check_git_baseline``
