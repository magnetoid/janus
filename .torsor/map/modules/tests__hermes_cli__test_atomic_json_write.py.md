---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_atomic_json_write.py

Symbols in `tests/hermes_cli/test_atomic_json_write.py`.

- L13 `TestAtomicJsonWrite` (class) — Core atomic write behavior.
- L16 `test_writes_valid_json(self, tmp_path)` (method)
- L24 `test_creates_parent_directories(self, tmp_path)` (method)
- L31 `test_overwrites_existing_file(self, tmp_path)` (method)
- L39 `test_preserves_original_on_serialization_error(self, tmp_path)` (method)
- L52 `test_no_leftover_temp_files_on_success(self, tmp_path)` (method)
- L61 `test_no_leftover_temp_files_on_failure(self, tmp_path)` (method)
- L71 `test_cleans_up_temp_file_on_baseexception(self, tmp_path)` (method)
- L87 `test_accepts_string_path(self, tmp_path)` (method)
- L94 `test_writes_list_data(self, tmp_path)` (method)
- L102 `test_empty_list(self, tmp_path)` (method)
- L109 `test_custom_indent(self, tmp_path)` (method)
- L116 `test_accepts_json_dump_default_hook(self, tmp_path)` (method)
- L127 `test_unicode_content(self, tmp_path)` (method)
- L136 `test_mode_does_not_crash_without_fchmod(self, tmp_path)` (method) — Regression: os.fchmod is Unix-only and absent on Windows. Passing a
- L156 `test_mode_applied_when_supported(self, tmp_path)` (method)
- L168 `test_concurrent_writes_dont_corrupt(self, tmp_path)` (method) — Multiple rapid writes should each produce valid JSON.
