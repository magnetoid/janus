---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_codex_responses_adapter.py

Symbols in `tests/agent/test_codex_responses_adapter.py`.

- L11 `test_normalize_codex_response_drops_transient_rs_tmp_reasoning_items()` (function)
- L50 `test_normalize_codex_response_treats_summary_only_reasoning_as_incomplete()` (function)
- L80 `test_format_responses_error_combines_code_and_message()` (function)
- L85 `test_format_responses_error_message_only()` (function)
- L90 `test_format_responses_error_code_only_when_message_empty()` (function)
- L99 `test_format_responses_error_code_only_when_message_missing()` (function)
- L104 `test_format_responses_error_attribute_style_payload()` (function)
- L112 `test_format_responses_error_falls_back_to_status_when_empty()` (function)
- L123 `test_format_responses_error_stringifies_opaque_payload()` (function)
- L130 `test_format_responses_error_ignores_non_string_code_message()` (function)
- L137 `test_normalize_codex_response_failed_includes_code_in_error()` (function) — Regression: response_status == 'failed' should surface the error
- L160 `test_normalize_codex_response_failed_with_message_only()` (function) — Backwards-compat: a failed response with only a message field
