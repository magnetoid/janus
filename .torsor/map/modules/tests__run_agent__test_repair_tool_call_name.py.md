---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_repair_tool_call_name.py

Symbols in `tests/run_agent/test_repair_tool_call_name.py`.

- L32 `repair()` (function) — Return a bound _repair_tool_call built on a minimal shell agent.
- L45 `TestExistingBehaviorStillWorks` (class) — Pre-existing repairs must keep working (no regressions).
- L48 `test_lowercase_already_matches(self, repair)` (method)
- L51 `test_uppercase_simple(self, repair)` (method)
- L54 `test_dash_to_underscore(self, repair)` (method)
- L57 `test_space_to_underscore(self, repair)` (method)
- L60 `test_fuzzy_near_miss(self, repair)` (method)
- L64 `test_unknown_returns_none(self, repair)` (method)
- L68 `TestClassLikeEmissions` (class) — Regression coverage for #14784 — CamelCase + _tool suffix variants.
- L71 `test_camel_case_no_suffix(self, repair)` (method)
- L74 `test_camel_case_with_underscore_tool_suffix(self, repair)` (method)
- L77 `test_camel_case_with_Tool_class_suffix(self, repair)` (method)
- L80 `test_double_tacked_class_and_snake_suffix(self, repair)` (method)
- L85 `test_simple_name_with_tool_suffix(self, repair)` (method)
- L88 `test_simple_name_with_dash_tool_suffix(self, repair)` (method)
- L91 `test_camel_case_preserves_multi_word_match(self, repair)` (method)
- L95 `test_mixed_separators_and_suffix(self, repair)` (method)
- L99 `TestEdgeCases` (class) — Edge inputs that must not crash or produce surprising results.
- L102 `test_empty_string(self, repair)` (method)
- L105 `test_only_tool_suffix(self, repair)` (method)
- L110 `test_none_passed_as_name(self, repair)` (method)
- L115 `test_very_long_name_does_not_match_by_accident(self, repair)` (method)
