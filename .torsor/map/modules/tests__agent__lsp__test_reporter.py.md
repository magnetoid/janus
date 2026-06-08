---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/lsp/test_reporter.py

Symbols in `tests/agent/lsp/test_reporter.py`.

- L12 `_diag(line=0, col=0, sev=1, code='E001', source='ls', msg='oops')` (function)
- L25 `test_format_diagnostic_uses_one_indexed_position()` (function)
- L30 `test_format_diagnostic_includes_severity_label()` (function)
- L37 `test_format_diagnostic_includes_code_and_source()` (function)
- L43 `test_format_diagnostic_omits_missing_optional_fields()` (function)
- L58 `test_report_for_file_returns_empty_when_only_warnings()` (function) — Default severity filter is ERROR-only.
- L64 `test_report_for_file_emits_block_with_errors()` (function)
- L72 `test_report_for_file_caps_at_max_per_file()` (function)
- L78 `test_report_for_file_respects_custom_severities()` (function)
- L84 `test_truncate_below_limit_unchanged()` (function)
- L89 `test_truncate_above_limit_appends_marker()` (function)
