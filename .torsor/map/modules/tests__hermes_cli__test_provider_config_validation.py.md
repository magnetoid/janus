---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_provider_config_validation.py

Symbols in `tests/hermes_cli/test_provider_config_validation.py`.

- L13 `TestNormalizeCustomProviderEntry` (class) — Tests for _normalize_custom_provider_entry validation.
- L16 `test_valid_entry_snake_case(self)` (method) — Standard snake_case entry should normalize correctly.
- L28 `test_camel_case_api_key_mapped(self)` (method) — camelCase apiKey should be auto-mapped to api_key.
- L38 `test_camel_case_base_url_mapped(self)` (method) — camelCase baseUrl should be auto-mapped to base_url.
- L48 `test_non_url_api_field_rejected(self)` (method) — Non-URL string in 'api' field should be skipped with a warning.
- L58 `test_valid_url_in_api_field_accepted(self)` (method) — Valid URL in 'api' field should still be accepted.
- L68 `test_base_url_preferred_over_api(self)` (method) — base_url should be checked before api field.
- L79 `test_unknown_keys_logged(self, caplog)` (method) — Unknown config keys should produce a warning.
- L92 `test_timeout_keys_not_flagged_unknown(self, caplog)` (method) — request_timeout_seconds and stale_timeout_seconds should not produce warnings.
- L105 `test_camel_case_warning_logged(self, caplog)` (method) — camelCase alias mapping should produce a warning.
- L117 `test_snake_case_takes_precedence_over_camel(self)` (method) — If both snake_case and camelCase exist, snake_case wins.
- L128 `test_non_dict_returns_none(self)` (method) — Non-dict entry should return None.
- L134 `test_no_url_returns_none(self)` (method) — Entry with no valid URL in any field should return None.
- L142 `test_no_name_returns_none(self)` (method) — Entry with no name and no provider_key should return None.
- L150 `test_models_list_converted_to_dict(self)` (method) — List-format models should be preserved as an empty-value dict so
- L162 `test_models_dict_preserved(self)` (method) — Dict-format models should pass through unchanged.
- L173 `test_models_list_filters_empty_and_non_string(self)` (method) — List entries that are empty strings or non-strings are skipped.
- L184 `test_models_empty_list_omitted(self)` (method) — Empty list (falsy) should not produce a models key.
