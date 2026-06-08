---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_cli_file_drop.py

Symbols in `tests/test_cli_file_drop.py`.

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
- L73 `TestImageFileDrop` (class)
- L74 `test_simple_image_path(self, tmp_image)` (method)
- L81 `test_image_with_trailing_text(self, tmp_image)` (method)
- L91 `test_all_image_extensions(self, tmp_path, ext)` (method)
- L98 `test_uppercase_extension(self, tmp_path)` (method)
- L110 `TestNonImageFileDrop` (class)
- L111 `test_python_file(self, tmp_text)` (method)
- L118 `test_non_image_with_trailing_text(self, tmp_text)` (method)
- L130 `TestEscapedSpaces` (class)
- L131 `test_escaped_spaces_in_path(self, tmp_image_with_spaces)` (method) — macOS drags produce paths like /path/to/my\ file.png
- L139 `test_escaped_spaces_with_trailing_text(self, tmp_image_with_spaces)` (method)
- L147 `test_unquoted_spaces_in_path(self, tmp_image_with_spaces)` (method)
- L154 `test_unquoted_spaces_with_trailing_text(self, tmp_image_with_spaces)` (method)
- L161 `test_file_uri_image_path(self, tmp_image_with_spaces)` (method)
- L173 `TestEdgeCases` (class)
- L174 `test_path_with_no_extension(self, tmp_path)` (method)
- L181 `test_path_that_looks_like_command_but_is_file(self, tmp_path)` (method) — A file literally named 'help' inside a directory starting with /.
- L189 `test_symlink_to_file(self, tmp_image, tmp_path)` (method)
