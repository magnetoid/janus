---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_sanitize_tool_error.py

Symbols in `tests/test_sanitize_tool_error.py`.

- L15 `TestRoleTagStripping` (class)
- L16 `test_strips_tool_call_tags(self)` (method)
- L22 `test_strips_function_call_tags(self)` (method)
- L27 `test_strips_role_tags(self)` (method)
- L35 `test_role_tag_strip_is_case_insensitive(self)` (method)
- L39 `test_unrelated_xml_kept(self)` (method)
- L45 `TestCDATAStripping` (class)
- L46 `test_strips_cdata(self)` (method)
- L51 `test_strips_multiline_cdata(self)` (method)
- L57 `TestCodeFenceStripping` (class)
- L58 `test_strips_leading_fence_with_lang(self)` (method)
- L62 `test_strips_trailing_fence(self)` (method)
- L66 `test_strips_bare_fence(self)` (method)
- L71 `TestTruncation` (class)
- L72 `test_caps_long_input(self)` (method)
- L80 `test_does_not_truncate_short_input(self)` (method)
- L87 `TestEnvelope` (class)
- L88 `test_wraps_with_prefix(self)` (method)
- L92 `test_empty_input(self)` (method)
- L96 `test_preserves_normal_error_text(self)` (method)
- L102 `TestHandleFunctionCallIntegration` (class) — Verify handle_function_call routes exception-path errors through the sanitizer.
- L112 `test_exception_path_error_is_sanitized(self)` (method)
