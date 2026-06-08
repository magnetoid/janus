---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_custom_provider_context_length.py

Symbols in `tests/hermes_cli/test_custom_provider_context_length.py`.

- L14 `TestGetCustomProviderContextLength` (class)
- L15 `test_returns_override_for_matching_entry(self)` (method)
- L30 `test_trailing_slash_insensitive(self)` (method)
- L58 `test_returns_none_when_url_does_not_match(self)` (method)
- L72 `test_returns_none_when_model_does_not_match(self)` (method)
- L86 `test_returns_none_for_string_value(self)` (method) — '256K' string is not a valid int — skip silently.
- L105 `test_returns_none_for_zero_or_negative(self)` (method)
- L120 `test_empty_inputs_return_none(self)` (method)
- L126 `test_ignores_non_dict_entries(self)` (method) — Malformed entries must not crash the lookup.
- L146 `TestGetModelContextLengthHonorsOverride` (class) — agent.model_metadata.get_model_context_length must honor the
- L152 `_mock_all_probes(self)` (method) — Context manager that disables every downstream resolution step.
- L163 `test_custom_providers_override_wins_over_default_fallback(self)` (method)
- L186 `test_explicit_config_context_length_still_wins(self)` (method) — Top-level model.context_length (step 0) outranks custom_providers (step 0b).
- L208 `test_no_override_falls_through_to_default(self)` (method) — With custom_providers=None and all probes disabled, resolver
- L229 `TestContextProbeTiers` (class)
- L230 `test_256k_is_top_tier_and_default(self)` (method) — The stepdown probe starts at 256K and 256K is the new default.
