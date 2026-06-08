---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_moonshot_schema.py

Symbols in `tests/agent/test_moonshot_schema.py`.

- L24 `TestMoonshotModelDetection` (class) — is_moonshot_model() must match across aggregator prefixes.
- L39 `test_positive_matches(self, model)` (method)
- L53 `test_negative_matches(self, model)` (method)
- L57 `TestMissingTypeFilled` (class) — Rule 1: every property must carry a type.
- L60 `test_property_without_type_gets_string(self)` (method)
- L68 `test_property_with_enum_infers_type_from_first_value(self)` (method)
- L76 `test_nested_properties_are_repaired(self)` (method)
- L91 `test_array_items_without_type_get_repaired(self)` (method)
- L104 `test_ref_node_is_not_given_synthetic_type(self)` (method) — $ref nodes should NOT get a synthetic type — the referenced
- L117 `TestAnyOfParentType` (class) — Rule 2: type must not appear at the anyOf parent level.
- L125 `test_anyof_null_branch_collapsed_to_single_type(self)` (method) — anyOf [string, null] → plain string (anyOf removed).
- L145 `test_anyof_multiple_non_null_preserved(self)` (method) — anyOf [string, integer] (no null) → kept as-is with parent type stripped.
- L163 `test_anyof_enum_with_null_collapsed(self)` (method) — anyOf [{enum: [...], type: string}, {type: null}] → enum + type only.
- L183 `TestTopLevelGuarantees` (class) — The returned top-level schema is always a well-formed object.
- L186 `test_non_dict_input_returns_empty_object(self)` (method)
- L191 `test_non_object_top_level_coerced(self)` (method)
- L197 `test_does_not_mutate_input(self)` (method)
- L211 `TestToolListSanitizer` (class) — sanitize_moonshot_tools() walks an OpenAI-format tool list.
- L214 `test_applies_per_tool(self)` (method)
- L241 `test_empty_list_is_passthrough(self)` (method)
- L245 `test_skips_malformed_entries(self)` (method) — Entries without a function dict are passed through untouched.
- L252 `TestRealWorldMCPShape` (class) — End-to-end: a realistic MCP-style schema that used to 400 on Moonshot.
- L255 `test_combined_rewrites(self)` (method)
- L285 `TestEnumNullStripping` (class) — Rule 3: Moonshot rejects null/empty-string inside enum arrays.
- L288 `test_enum_null_value_stripped(self)` (method) — enum containing Python None must have it removed for Moonshot.
- L305 `test_enum_empty_string_stripped(self)` (method) — enum containing empty string '' must have it removed for Moonshot.
- L321 `test_enum_all_null_becomes_no_enum(self)` (method) — enum that only had null/empty values is dropped entirely.
- L335 `test_dataslayer_db_type_after_mcp_normalize(self)` (method) — Real-world: dataslayer db_type anyOf+enum after MCP normalization.
- L360 `test_enum_on_object_type_not_stripped(self)` (method) — enum on non-scalar types (object) should NOT be touched.
- L376 `test_anyof_collapse_still_runs_nullable_and_enum_cleanup(self)` (method) — After anyOf collapses to a single non-null branch, the merged
