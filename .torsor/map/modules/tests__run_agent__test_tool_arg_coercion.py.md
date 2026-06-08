---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_tool_arg_coercion.py

Symbols in `tests/run_agent/test_tool_arg_coercion.py`.

- L22 `TestCoerceNumber` (class) — Unit tests for _coerce_number.
- L25 `test_integer_string(self)` (method)
- L29 `test_negative_integer(self)` (method)
- L32 `test_zero(self)` (method)
- L36 `test_float_string(self)` (method)
- L40 `test_float_with_zero_fractional(self)` (method) — 3.0 should become int(3) since there's no fractional part.
- L45 `test_integer_only_rejects_float(self)` (method) — When integer_only=True, "3.14" should stay as string.
- L51 `test_integer_only_accepts_whole(self)` (method)
- L54 `test_not_a_number(self)` (method)
- L57 `test_empty_string(self)` (method)
- L60 `test_large_number(self)` (method)
- L63 `test_scientific_notation(self)` (method)
- L66 `test_inf_stays_string(self)` (method) — Infinity is not JSON-serializable, so it should stay as string.
- L72 `test_negative_inf_stays_string(self)` (method) — Negative infinity should also stay as string.
- L78 `test_nan_stays_string(self)` (method) — NaN is not JSON-serializable, so it should stay as string.
- L84 `test_negative_float(self)` (method)
- L88 `TestCoerceBoolean` (class) — Unit tests for _coerce_boolean.
- L91 `test_true_lowercase(self)` (method)
- L94 `test_false_lowercase(self)` (method)
- L97 `test_true_mixed_case(self)` (method)
- L100 `test_false_mixed_case(self)` (method)
- L103 `test_true_with_whitespace(self)` (method)
- L106 `test_not_a_boolean(self)` (method)
- L109 `test_one_zero_not_coerced(self)` (method) — '1' and '0' are not boolean values.
- L114 `test_empty_string(self)` (method)
- L118 `TestCoerceValue` (class) — Unit tests for _coerce_value.
- L121 `test_integer_type(self)` (method)
- L124 `test_number_type(self)` (method)
- L127 `test_boolean_type(self)` (method)
- L130 `test_string_type_passthrough(self)` (method) — Strings expected as strings should not be coerced.
- L134 `test_unknown_type_passthrough(self)` (method)
- L137 `test_union_type_prefers_first_match(self)` (method) — Union types try each in order.
- L141 `test_union_type_falls_through(self)` (method) — If no type matches, return original string.
- L145 `test_union_with_string_preserves_original(self)` (method) — A non-numeric string in [number, string] should stay a string.
- L149 `test_array_type_parsed_from_json_string(self)` (method) — Stringified JSON arrays are parsed into native lists.
- L154 `test_object_type_parsed_from_json_string(self)` (method) — Stringified JSON objects are parsed into native dicts.
- L159 `test_array_invalid_json_preserved(self)` (method) — Unparseable strings are returned unchanged.
- L163 `test_object_invalid_json_preserved(self)` (method)
- L166 `test_array_type_wrong_shape_preserved(self)` (method) — A JSON object passed for an 'array' slot is preserved as a string.
- L170 `test_object_type_wrong_shape_preserved(self)` (method) — A JSON array passed for an 'object' slot is preserved as a string.
- L178 `TestCoerceToolArgs` (class) — Integration tests for coerce_tool_args using the tool registry.
- L181 `_mock_schema(self, properties)` (method) — Build a minimal tool schema with the given properties.
- L192 `test_coerces_integer_arg(self)` (method)
- L200 `test_coerces_boolean_arg(self)` (method)
- L207 `test_coerces_number_arg(self)` (method)
- L214 `test_leaves_string_args_alone(self)` (method)
- L221 `test_leaves_already_correct_types(self)` (method)
- L228 `test_unknown_tool_returns_args_unchanged(self)` (method)
- L234 `test_empty_args(self)` (method)
- L237 `test_none_args(self)` (method)
- L240 `test_preserves_non_string_values(self)` (method) — Lists, dicts, and other non-string values are never touched.
- L252 `test_coerces_stringified_array_arg(self)` (method) — Regression for #3947 — MCP servers using z.array() expect lists, not strings.
- L262 `test_coerces_stringified_object_arg(self)` (method) — Stringified JSON objects get parsed into dicts.
- L270 `test_coerces_string_null_for_nullable_object_arg(self)` (method) — Models often emit literal "null" for optional MCP object args.
- L285 `test_coerces_string_null_for_nullable_array_arg(self)` (method)
- L299 `test_invalid_json_array_wrapped_in_single_element_list(self)` (method) — A bare string gets wrapped into ``[value]`` when the schema says array.
- L315 `test_bare_string_wrapped_as_array(self)` (method) — Bare string on array field → single-element list.
- L323 `test_bare_int_wrapped_as_array(self)` (method) — Bare non-string scalars (int, bool, float) also get wrapped.
- L331 `test_bare_dict_wrapped_as_array(self)` (method) — Bare dict on array field → single-element list.
- L339 `test_none_on_array_field_preserved(self)` (method) — ``None`` is never wrapped — tools with defaults handle it.
- L347 `test_existing_list_passthrough(self)` (method) — An already-valid list is not touched.
- L355 `test_json_encoded_array_still_parses(self)` (method) — JSON-encoded strings still parse (not double-wrapped).
- L363 `test_extra_args_without_schema_left_alone(self)` (method) — Args not in the schema properties are not touched.
- L372 `test_mixed_coercion(self)` (method) — Multiple args coerced in the same call.
- L393 `test_failed_coercion_preserves_original(self)` (method) — A non-parseable string stays as string even if schema says integer.
- L401 `test_real_read_file_schema(self)` (method) — Test against the actual read_file schema from the registry.
