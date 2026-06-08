---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_file_drop.py

Symbols in `tests/cli/test_cli_file_drop.py`.

- L15 `tmp_image(tmp_path)` (function) — Create a temporary .png file and return its path.
- L23 `tmp_text(tmp_path)` (function) — Create a temporary .py file and return its path.
- L31 `tmp_image_with_spaces(tmp_path)` (function) — Create a file whose name contains spaces (like macOS screenshots).
- L42 `TestNonFileInputs` (class)
- L43 `test_regular_slash_command(self)` (method)
- L46 `test_unknown_slash_command(self)` (method)
- L49 `test_slash_command_with_args(self)` (method)
- L52 `test_empty_string(self)` (method)
- L55 `test_non_slash_input(self)` (method)
- L58 `test_non_string_input(self)` (method)
- L61 `test_nonexistent_path(self)` (method)
- L64 `test_directory_not_file(self, tmp_path)` (method) — A directory path should not be treated as a file drop.
- L68 `test_long_slash_command_does_not_raise(self)` (method) — Regression: long pasted slash commands like `/goal <long prose>`
- L92 `test_path_longer_than_namemax_does_not_raise(self)` (method) — Defensive: a single token longer than NAME_MAX should return
- L104 `TestImageFileDrop` (class)
- L105 `test_simple_image_path(self, tmp_image)` (method)
- L112 `test_image_with_trailing_text(self, tmp_image)` (method)
- L122 `test_all_image_extensions(self, tmp_path, ext)` (method)
- L129 `test_uppercase_extension(self, tmp_path)` (method)
- L141 `TestNonImageFileDrop` (class)
- L142 `test_python_file(self, tmp_text)` (method)
- L149 `test_non_image_with_trailing_text(self, tmp_text)` (method)
- L161 `TestEscapedSpaces` (class)
- L162 `test_escaped_spaces_in_path(self, tmp_image_with_spaces)` (method) — macOS drags produce paths like /path/to/my\ file.png
- L170 `test_escaped_spaces_with_trailing_text(self, tmp_image_with_spaces)` (method)
- L178 `test_unquoted_spaces_in_path(self, tmp_image_with_spaces)` (method)
- L185 `test_unquoted_spaces_with_trailing_text(self, tmp_image_with_spaces)` (method)
- L192 `test_mixed_escaped_and_literal_spaces_in_path(self, tmp_path)` (method)
- L202 `test_file_uri_image_path(self, tmp_image_with_spaces)` (method)
- L209 `test_tilde_prefixed_path(self, tmp_path, monkeypatch)` (method)
- L228 `TestEdgeCases` (class)
- L229 `test_path_with_no_extension(self, tmp_path)` (method)
- L236 `test_path_that_looks_like_command_but_is_file(self, tmp_path)` (method) — A file literally named 'help' inside a directory starting with /.
- L244 `test_symlink_to_file(self, tmp_image, tmp_path)` (method)
