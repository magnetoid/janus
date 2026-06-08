---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/lsp/test_diagnostics_field.py

Symbols in `tests/agent/lsp/test_diagnostics_field.py`.

- L25 `test_writeresult_lsp_diagnostics_optional()` (function)
- L30 `test_writeresult_to_dict_omits_field_when_none()` (function)
- L35 `test_writeresult_to_dict_includes_field_when_set()` (function)
- L41 `test_patchresult_to_dict_includes_field_when_set()` (function)
- L47 `test_patchresult_to_dict_omits_field_when_none()` (function)
- L52 `test_patchresult_to_dict_omits_field_when_empty_string()` (function) — Empty string counts as falsy — agent shouldn't see an empty field.
- L63 `test_lint_and_lsp_diagnostics_are_separate_channels()` (function) — A WriteResult can carry BOTH a syntax-error lint AND an LSP
- L83 `test_write_file_populates_lsp_diagnostics_when_layer_returns_block(tmp_path)` (function) — When the LSP layer returns a non-empty block, write_file puts it
- L100 `test_write_file_lsp_diagnostics_none_when_layer_returns_empty(tmp_path)` (function)
- L110 `test_write_file_skips_lsp_when_syntax_failed(tmp_path)` (function) — If the syntax check finds errors, the LSP layer should not be
- L129 `test_patch_replace_propagates_lsp_diagnostics(tmp_path)` (function) — patch_replace's internal write_file populates lsp_diagnostics —
