---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_repair_tool_call_arguments.py

Symbols in `tests/run_agent/test_repair_tool_call_arguments.py`.

- L8 `TestRepairToolCallArguments` (class) — Verify each repair stage in the pipeline.
- L13 `test_empty_string_returns_empty_object(self)` (method)
- L16 `test_whitespace_only_returns_empty_object(self)` (method)
- L19 `test_none_type_returns_empty_object(self)` (method) — Non-string input (e.g. None from a broken model response).
- L25 `test_python_none_literal(self)` (method)
- L28 `test_python_none_with_whitespace(self)` (method)
- L33 `test_trailing_comma_in_object(self)` (method)
- L37 `test_trailing_comma_in_array(self)` (method)
- L42 `test_multiple_trailing_commas(self)` (method)
- L50 `test_unclosed_brace(self)` (method)
- L55 `test_unclosed_bracket_and_brace(self)` (method)
- L64 `test_extra_closing_brace(self)` (method)
- L69 `test_extra_closing_bracket(self)` (method)
- L76 `test_unrepairable_garbage_returns_empty_object(self)` (method)
- L79 `test_unrepairable_partial_returns_empty_object(self)` (method)
- L85 `test_already_valid_json_passes_through(self)` (method) — When json.loads fails for a non-JSON reason (shouldn't normally
- L95 `test_trailing_comma_plus_unclosed_brace(self)` (method)
- L101 `test_real_world_glm_truncation(self)` (method) — Simulates GLM-5.1 truncating mid-argument.
- L113 `test_literal_newline_inside_string_value(self)` (method)
- L119 `test_literal_tab_inside_string_value(self)` (method)
- L125 `test_literal_control_char_reserialised_to_wire_form(self)` (method) — After repair, the output must parse under strict=True.
- L135 `test_control_chars_with_trailing_comma(self)` (method) — strict=False fails due to trailing comma, but brace-count pass
