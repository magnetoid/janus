---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_streaming_tool_call_repair.py

Symbols in `tests/run_agent/test_streaming_tool_call_repair.py`.

- L19 `TestStreamingAssemblyRepair` (class) — Verify that _repair_tool_call_arguments is applied to streaming tool
- L30 `test_truncated_object_no_close_brace(self)` (method) — Model stops mid-JSON, common with output length limits.
- L38 `test_truncated_nested_object(self)` (method) — Model truncates inside a nested structure.
- L45 `test_truncated_mid_value(self)` (method) — Model cuts off mid-string-value.
- L54 `test_trailing_comma_before_close_brace(self)` (method)
- L59 `test_trailing_comma_in_list(self)` (method)
- L66 `test_python_none_literal(self)` (method)
- L73 `test_empty_string(self)` (method)
- L76 `test_whitespace_only(self)` (method)
- L81 `test_valid_json_passthrough(self)` (method)
- L88 `test_extra_closing_brace(self)` (method)
- L95 `test_glm_truncation_pattern(self)` (method) — GLM-5.1 via Ollama commonly truncates like this.
- L109 `test_glm_truncation_repairable(self)` (method) — GLM-5.1 truncation pattern that IS repairable.
