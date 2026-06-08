---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_tool_output_limits.py

Symbols in `tests/tools/test_tool_output_limits.py`.

- L26 `_reset_limits_cache()` (function) — get_tool_output_limits() now memoizes its result for the process
- L35 `TestDefaults` (class)
- L36 `test_defaults_match_previous_hardcoded_values(self)` (method)
- L41 `test_get_limits_returns_defaults_when_config_missing(self)` (method)
- L50 `test_get_limits_returns_defaults_when_config_not_a_dict(self)` (method)
- L56 `test_get_limits_returns_defaults_when_load_config_raises(self)` (method)
- L65 `TestOverrides` (class)
- L66 `test_user_config_overrides_all_three(self)` (method)
- L82 `test_partial_override_preserves_other_defaults(self)` (method)
- L90 `test_section_not_a_dict_falls_back(self)` (method)
- L97 `TestCoercion` (class)
- L99 `test_invalid_values_fall_back_to_defaults(self, bad)` (method)
- L107 `test_string_integer_is_coerced(self)` (method)
- L114 `TestShortcuts` (class)
- L115 `test_individual_accessors_delegate_to_get_tool_output_limits(self)` (method)
- L129 `TestDefaultConfigHasSection` (class) — The DEFAULT_CONFIG in hermes_cli.config must expose tool_output so
- L134 `test_default_config_contains_tool_output_section(self)` (method)
- L144 `TestIntegrationReadPagination` (class) — normalize_read_pagination uses get_max_lines() — verify the plumbing.
- L147 `test_pagination_limit_clamped_by_config_value(self)` (method)
- L156 `test_pagination_default_when_config_missing(self)` (method)
