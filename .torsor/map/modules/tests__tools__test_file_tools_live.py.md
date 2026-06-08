---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_file_tools_live.py

Symbols in `tests/tools/test_file_tools_live.py`.

- L42 `_assert_clean(text: str, context: str='output')` (function) — Assert text contains zero shell noise contamination.
- L66 `env(tmp_path)` (function) — A real LocalEnvironment rooted in a temp directory.
- L72 `ops(env, tmp_path)` (function) — ShellFileOperations wired to the real local environment.
- L78 `populated_dir(tmp_path)` (function) — A temp directory with known files for search/read tests.
- L89 `TestLocalEnvironmentExecute` (class)
- L90 `test_echo_exact_output(self, env)` (method)
- L96 `test_printf_no_trailing_newline(self, env)` (method)
- L102 `test_exit_code_propagated(self, env)` (method)
- L106 `test_stderr_captured_in_output(self, env)` (method)
- L111 `test_cwd_respected(self, env, tmp_path)` (method)
- L119 `test_multiline_exact(self, env)` (method)
- L125 `test_env_var_home(self, env)` (method)
- L132 `test_pipe_exact(self, env)` (method)
- L138 `test_cat_deterministic_content(self, env, tmp_path)` (method)
- L149 `TestHasCommand` (class)
- L150 `test_finds_echo(self, ops)` (method)
- L153 `test_finds_cat(self, ops)` (method)
- L156 `test_finds_sed(self, ops)` (method)
- L159 `test_finds_wc(self, ops)` (method)
- L162 `test_finds_find(self, ops)` (method)
- L165 `test_missing_command(self, ops)` (method)
- L168 `test_rg_or_grep_available(self, ops)` (method)
- L175 `TestReadFile` (class)
- L176 `test_exact_content(self, ops, tmp_path)` (method)
- L188 `test_absolute_path(self, ops, tmp_path)` (method)
- L196 `test_tilde_expansion(self, ops)` (method)
- L207 `test_nonexistent_returns_error(self, ops, tmp_path)` (method)
- L211 `test_pagination_exact_window(self, ops, tmp_path)` (method)
- L223 `test_no_noise_in_content(self, ops, tmp_path)` (method)
- L233 `TestWriteFile` (class)
- L234 `test_write_and_verify(self, ops, tmp_path)` (method)
- L241 `test_creates_nested_dirs(self, ops, tmp_path)` (method)
- L248 `test_overwrites_exact(self, ops, tmp_path)` (method)
- L255 `test_large_content_via_stdin(self, ops, tmp_path)` (method)
- L262 `test_special_characters_preserved(self, ops, tmp_path)` (method)
- L268 `test_roundtrip_read_write(self, ops, tmp_path)` (method) — Write -> read back -> verify exact match.
- L281 `TestPatchReplace` (class)
- L282 `test_exact_replacement(self, ops, tmp_path)` (method)
- L289 `test_not_found_error(self, ops, tmp_path)` (method)
- L296 `test_multiline_patch(self, ops, tmp_path)` (method)
- L306 `TestSearch` (class)
- L307 `test_content_search_finds_exact_match(self, ops, populated_dir)` (method)
- L316 `test_content_search_no_false_positives(self, ops, populated_dir)` (method)
- L322 `test_file_search_finds_py_files(self, ops, populated_dir)` (method)
- L336 `test_file_search_no_false_file_entries(self, ops, populated_dir)` (method) — Every entry in the files list must be a real path, not noise.
- L344 `test_content_search_with_glob_filter(self, ops, populated_dir)` (method)
- L352 `test_search_output_has_zero_noise(self, ops, populated_dir)` (method) — Dedicated noise check: search must return only real content.
- L363 `TestExpandPath` (class)
- L364 `test_tilde_exact(self, ops)` (method)
- L370 `test_absolute_unchanged(self, ops)` (method)
- L373 `test_relative_unchanged(self, ops)` (method)
- L376 `test_bare_tilde(self, ops)` (method)
- L381 `test_tilde_injection_blocked(self, ops)` (method) — Paths like ~; rm -rf / must NOT execute shell commands.
- L391 `test_tilde_username_with_subpath(self, ops)` (method) — ~root/file.txt should attempt expansion (valid username).
- L402 `TestTerminalOutputCleanliness` (class) — Every command the agent might run must produce noise-free output.
- L405 `test_echo(self, env)` (method)
- L410 `test_cat(self, env, tmp_path)` (method)
- L417 `test_ls(self, env, tmp_path)` (method)
- L425 `test_wc(self, env, tmp_path)` (method)
- L432 `test_head(self, env, tmp_path)` (method)
- L440 `test_env_var_expansion(self, env)` (method)
- L445 `test_command_substitution(self, env)` (method)
- L450 `test_command_v_detection(self, env)` (method) — This is how _has_command works -- must return clean 'yes'.
