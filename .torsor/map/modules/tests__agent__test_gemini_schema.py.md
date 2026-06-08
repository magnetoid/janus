---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_gemini_schema.py

Symbols in `tests/agent/test_gemini_schema.py`.

- L9 `TestSanitizeGeminiSchema` (class)
- L10 `test_strips_unknown_top_level_keys(self)` (method) — $schema / additionalProperties etc. must not reach Gemini.
- L24 `test_preserves_string_enums(self)` (method) — String-valued enums are valid for Gemini and must pass through.
- L31 `test_drops_integer_enum_to_satisfy_gemini(self)` (method) — Gemini rejects int-typed enums; the sanitizer must drop the enum.
- L51 `test_drops_number_enum(self)` (method) — Same rule applies to ``type: number``.
- L58 `test_drops_boolean_enum(self)` (method) — And to ``type: boolean`` (Gemini rejects non-string entries).
- L65 `test_keeps_string_enum_even_when_numeric_values_coexist_as_strings(self)` (method) — Stringified-numeric enums ARE valid for Gemini; don't drop them.
- L71 `test_drops_nested_integer_enum_inside_properties(self)` (method) — The fix must apply recursively — the Discord case is nested.
- L95 `test_drops_integer_enum_inside_array_items(self)` (method) — Array item schemas recurse through ``items``.
- L105 `test_non_dict_input_returns_empty(self)` (method)
- L111 `TestSanitizeGeminiToolParameters` (class)
- L112 `test_empty_parameters_return_valid_object_schema(self)` (method) — Gemini requires ``parameters`` to be a valid object schema.
- L117 `test_discord_create_thread_parameters_no_longer_trip_gemini(self)` (method) — End-to-end regression: the exact shape that was rejected in prod.
