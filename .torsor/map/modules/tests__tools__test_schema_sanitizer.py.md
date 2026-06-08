---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_schema_sanitizer.py

Symbols in `tests/tools/test_schema_sanitizer.py`.

- L19 `_tool(name: str, parameters: dict)` (function)
- L23 `test_object_without_properties_gets_empty_properties()` (function)
- L29 `test_nested_object_without_properties_gets_empty_properties()` (function)
- L45 `test_bare_string_object_value_replaced_with_schema_dict()` (function)
- L61 `test_bare_string_primitive_value_replaced_with_schema_dict()` (function)
- L70 `test_nullable_type_array_collapsed_to_single_string()` (function)
- L83 `test_anyof_nested_objects_sanitized()` (function)
- L101 `test_missing_parameters_gets_default_object_schema()` (function)
- L107 `test_non_dict_parameters_gets_default_object_schema()` (function)
- L113 `test_required_pruned_to_existing_properties()` (function)
- L123 `test_required_all_missing_is_dropped()` (function)
- L133 `test_well_formed_schema_unchanged()` (function)
- L147 `test_additional_properties_bool_preserved()` (function)
- L163 `test_additional_properties_schema_sanitized()` (function)
- L178 `test_deepcopy_does_not_mutate_input()` (function)
- L189 `test_items_sanitized_in_array_schema()` (function)
- L204 `test_empty_tools_list_returns_empty()` (function)
- L208 `test_none_tools_returns_none()` (function)
- L219 `test_strip_pattern_removes_schema_pattern_keyword()` (function) — `pattern` as a sibling of `type` → stripped.
- L234 `test_strip_format_removes_schema_format_keyword()` (function) — `format` as a sibling of `type` → stripped.
- L247 `test_strip_preserves_property_named_pattern()` (function) — Property literally *named* 'pattern' (search_files) must survive.
- L266 `test_strip_recurses_into_anyof_variants()` (function) — Pattern/format inside anyOf variant schemas are also stripped.
- L287 `test_strip_is_idempotent()` (function) — Second call on already-stripped tools is a no-op.
- L299 `test_strip_empty_tools_returns_zero()` (function)
- L305 `test_strip_none_returns_zero()` (function)
- L312 `test_strip_responses_format_strips_format_keyword()` (function) — Responses-format:  keyword should be stripped.
- L335 `test_top_level_allof_stripped_for_codex_backend_compat()` (function) — OpenAI Codex backend rejects top-level allOf/oneOf/anyOf/enum/not.
- L359 `test_top_level_oneof_anyof_enum_not_stripped()` (function) — All five forbidden top-level combinators are dropped.
- L375 `test_nested_allof_preserved()` (function) — Combinators inside a property's schema are preserved (only top is strict).
- L393 `test_strip_responses_format_tools()` (function) — strip_pattern_and_format should handle Responses-format tools (no function wrapper).
- L427 `test_strip_responses_idempotent()` (function) — Second call on already-stripped Responses-format tools should return 0.
- L453 `test_strip_responses_mixed_formats()` (function) — Mixed list of OpenAI-format and Responses-format tools should both be sanitized.
- L509 `test_strip_slash_enum_removes_huggingface_id_enum()` (function) — enum containing HF-style 'owner/name' IDs → stripped.
- L528 `test_strip_slash_enum_preserves_slashless_enum()` (function) — enum without any '/' → preserved.
- L541 `test_strip_slash_enum_partial_match_strips_whole_enum()` (function) — Any single value containing '/' triggers removal of the entire enum.
- L559 `test_strip_slash_enum_responses_format()` (function) — Responses-format tools (no `function` wrapper) are also handled.
- L579 `test_strip_slash_enum_recurses_into_anyof()` (function) — enum-with-slash inside an anyOf variant is also stripped.
- L599 `test_strip_slash_enum_is_idempotent()` (function) — Second call on already-stripped tools is a no-op.
- L611 `test_strip_slash_enum_empty_returns_zero()` (function)
- L617 `test_strip_slash_enum_none_returns_zero()` (function)
- L623 `test_strip_slash_enum_ignores_non_string_enum_values()` (function) — Integer/boolean enum values can't contain '/' — leave them alone.
