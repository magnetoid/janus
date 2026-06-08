---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_plugins_cmd.py

Symbols in `tests/hermes_cli/test_plugins_cmd.py`.

- L26 `TestSanitizePluginName` (class) — Reject path-traversal attempts while accepting valid names.
- L29 `test_valid_simple_name(self, tmp_path)` (method)
- L33 `test_valid_name_with_hyphen_and_digits(self, tmp_path)` (method)
- L37 `test_rejects_dot_dot(self, tmp_path)` (method)
- L41 `test_rejects_single_dot_dot(self, tmp_path)` (method)
- L45 `test_rejects_single_dot(self, tmp_path)` (method)
- L49 `test_rejects_forward_slash(self, tmp_path)` (method)
- L53 `test_rejects_backslash(self, tmp_path)` (method)
- L57 `test_rejects_absolute_path(self, tmp_path)` (method)
- L61 `test_rejects_empty_name(self, tmp_path)` (method)
- L67 `test_allow_subdir_accepts_single_slash(self, tmp_path)` (method)
- L73 `test_allow_subdir_strips_leading_trailing_slash(self, tmp_path)` (method)
- L79 `test_allow_subdir_still_rejects_dot_dot(self, tmp_path)` (method)
- L83 `test_allow_subdir_still_rejects_backslash(self, tmp_path)` (method)
- L87 `test_allow_subdir_rejects_empty_after_strip(self, tmp_path)` (method)
- L91 `test_allow_subdir_resolves_inside_plugins_dir(self, tmp_path)` (method)
- L99 `TestResolveGitUrl` (class) — Shorthand and full-URL resolution.
- L102 `test_owner_repo_shorthand(self)` (method)
- L106 `test_https_url_passthrough(self)` (method)
- L110 `test_ssh_url_passthrough(self)` (method)
- L114 `test_http_url_passthrough(self)` (method)
- L118 `test_file_url_passthrough(self)` (method)
- L122 `test_invalid_single_word_raises(self)` (method)
- L126 `test_invalid_three_parts_raises(self)` (method)
- L134 `TestResolveGitExecutable` (class) — Fallback resolution when bare ``git`` is not discoverable via ``PATH``.
- L137 `teardown_method(self)` (method)
- L140 `test_prefers_shutil_which(self)` (method)
- L147 `test_fallback_posix_first_matching_path(self)` (method)
- L160 `test_returns_none_when_unavailable(self)` (method)
- L169 `test_git_pull_uses_resolved_executable(self, tmp_path)` (method)
- L185 `test_install_core_raises_when_git_unresolved(self)` (method)
- L197 `TestRepoNameFromUrl` (class) — Extract plugin directory name from Git URLs.
- L200 `test_https_with_dot_git(self)` (method)
- L205 `test_https_without_dot_git(self)` (method)
- L208 `test_trailing_slash(self)` (method)
- L211 `test_ssh_style(self)` (method)
- L214 `test_ssh_protocol(self)` (method)
- L224 `TestReadManifest` (class) — Manifest reading edge cases.
- L227 `test_valid_yaml(self, tmp_path)` (method)
- L234 `test_missing_file_returns_empty(self, tmp_path)` (method)
- L238 `test_invalid_yaml_returns_empty_and_logs(self, tmp_path, caplog)` (method)
- L245 `test_empty_file_returns_empty(self, tmp_path)` (method)
- L254 `TestCmdInstall` (class) — Test the install command.
- L257 `test_install_requires_identifier(self)` (method)
- L264 `test_install_validates_identifier(self, mock_resolve)` (method)
- L279 `test_install_rejects_manifest_name_pointing_at_plugins_root(self, mock_run, mock_read_manifest, mock_plugins_dir, mock_rmtree, mock_move, mock_display_after_install, tmp_path)` (method)
- L309 `TestCmdUpdate` (class) — Test the update command.
- L315 `test_update_git_pull_success(self, mock_run, mock_plugins_dir, mock_sanitize)` (method)
- L335 `test_update_plugin_not_found(self, mock_plugins_dir, mock_sanitize)` (method)
- L354 `TestCmdRemove` (class) — Test the remove command.
- L360 `test_remove_deletes_plugin(self, mock_rmtree, mock_plugins_dir, mock_sanitize)` (method)
- L374 `test_remove_plugin_not_found(self, mock_plugins_dir, mock_sanitize)` (method)
- L393 `TestCmdList` (class) — Test the list command.
- L397 `test_list_empty_plugins_dir(self, mock_plugins_dir)` (method)
- L408 `test_list_with_plugins(self, mock_read_manifest, mock_plugins_dir)` (method)
- L428 `TestCopyExampleFiles` (class) — Test example file copying.
- L431 `test_copies_example_files(self, tmp_path)` (method)
- L446 `test_skips_existing_files(self, tmp_path)` (method)
- L462 `test_handles_copy_error_gracefully(self, tmp_path)` (method)
- L483 `TestPromptPluginEnvVars` (class) — Tests for _prompt_plugin_env_vars.
- L486 `test_skips_when_no_requires_env(self)` (method)
- L494 `test_skips_already_set_vars(self, monkeypatch)` (method)
- L504 `test_prompts_for_missing_var_simple_format(self)` (method)
- L521 `test_prompts_for_missing_var_rich_format(self)` (method)
- L548 `test_secret_uses_masked_prompt(self)` (method)
- L565 `test_empty_input_skips(self)` (method)
- L579 `test_keyboard_interrupt_skips_gracefully(self)` (method)
- L598 `TestCursesRadiolist` (class) — Test the curses_radiolist function.
- L601 `test_non_tty_returns_default(self)` (method)
- L608 `test_non_tty_returns_cancel_value(self)` (method)
- L615 `test_keyboard_interrupt_returns_cancel_value(self)` (method)
- L627 `TestProviderDiscovery` (class) — Test provider plugin discovery and config helpers.
- L630 `test_get_current_memory_provider_default(self, tmp_path, monkeypatch)` (method) — Empty config returns empty string.
- L639 `test_get_current_context_engine_default(self, tmp_path, monkeypatch)` (method) — Default config returns 'compressor'.
- L648 `test_save_memory_provider(self, tmp_path, monkeypatch)` (method) — Saving a memory provider persists to config.yaml.
- L658 `test_save_context_engine(self, tmp_path, monkeypatch)` (method) — Saving a context engine persists to config.yaml.
- L668 `test_discover_memory_providers_empty(self)` (method) — Discovery returns empty list when import fails.
- L676 `test_discover_context_engines_empty(self)` (method) — Discovery returns empty list when import fails.
- L688 `TestNoAutoActivation` (class) — Verify that plugin engines don't auto-activate when config says 'compressor'.
- L691 `test_compressor_default_ignores_plugin(self)` (method) — When context.engine is 'compressor', a plugin-registered engine should NOT
