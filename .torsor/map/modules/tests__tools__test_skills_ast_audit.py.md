---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_skills_ast_audit.py

Symbols in `tests/tools/test_skills_ast_audit.py`.

- L8 `_pids(findings)` (function)
- L12 `test_bypass_payload_detected(tmp_path)` (function) — The exact bypass shape from #7072 is caught.
- L27 `test_syntax_error_does_not_crash(tmp_path)` (function)
- L33 `test_recursion_error_does_not_crash(tmp_path)` (function)
- L45 `test_importer_lookalike_not_flagged(tmp_path)` (function) — `import importer` must NOT match — dot-bounded prefix.
- L52 `test_literal_dunder_import_not_flagged(tmp_path)` (function) — __import__('os') with a literal is not flagged (regex catches those).
- L59 `test_non_python_file_returns_empty(tmp_path)` (function)
- L65 `test_directory_scans_recursively_and_skips_cache_dirs(tmp_path)` (function)
- L79 `test_missing_path_returns_empty(tmp_path)` (function)
- L83 `test_dynamic_getattr_and_dict_access_detected(tmp_path)` (function)
- L91 `test_format_report_empty()` (function)
- L95 `test_format_report_with_findings()` (function)
