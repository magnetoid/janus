---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_config_validation.py

Symbols in `tests/hermes_cli/test_config_validation.py`.

- L7 `TestCustomProvidersValidation` (class) — custom_providers must be a YAML list, not a dict.
- L10 `test_dict_instead_of_list(self)` (method) — The exact Discord user scenario — custom_providers as flat dict.
- L31 `test_dict_detects_misplaced_fields(self)` (method) — When custom_providers is a dict, detect fields that look misplaced.
- L45 `test_dict_detects_nested_fallback(self)` (method) — When fallback_model gets swallowed into custom_providers dict.
- L56 `test_valid_list_no_issues(self)` (method) — Properly formatted custom_providers should produce no issues.
- L66 `test_list_entry_missing_name(self)` (method) — List entry without name should warn.
- L74 `test_list_entry_missing_base_url(self)` (method) — List entry without base_url should warn.
- L82 `test_list_entry_not_dict(self)` (method) — Non-dict list entries should warn.
- L90 `test_none_custom_providers_no_issues(self)` (method) — No custom_providers at all should be fine.
- L98 `TestFallbackModelValidation` (class) — fallback_model should be a top-level dict with provider + model.
- L101 `test_missing_provider(self)` (method)
- L107 `test_missing_model(self)` (method)
- L113 `test_valid_fallback(self)` (method)
- L124 `test_non_dict_fallback(self)` (method)
- L130 `test_empty_fallback_dict_no_issues(self)` (method) — Empty fallback_model dict means disabled — no warnings needed.
- L138 `test_valid_fallback_list(self)` (method) — List-form fallback_model (chain) should validate when every entry has provider+model.
- L149 `test_fallback_list_entry_missing_provider(self)` (method)
- L158 `test_fallback_list_entry_missing_model(self)` (method)
- L166 `test_fallback_list_entry_not_a_dict(self)` (method)
- L173 `TestMissingModelSection` (class) — Warn when custom_providers exists but model section is missing.
- L176 `test_custom_providers_without_model(self)` (method)
- L184 `test_custom_providers_with_model(self)` (method)
- L195 `TestConfigIssueDataclass` (class) — ConfigIssue should be a proper dataclass.
- L198 `test_fields(self)` (method)
- L204 `test_equality(self)` (method)
