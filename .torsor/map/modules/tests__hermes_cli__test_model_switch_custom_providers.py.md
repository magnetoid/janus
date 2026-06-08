---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_model_switch_custom_providers.py

Symbols in `tests/hermes_cli/test_model_switch_custom_providers.py`.

- L21 `test_list_authenticated_providers_includes_custom_providers(monkeypatch)` (function) — No-args /model menus should include saved custom_providers entries.
- L48 `test_resolve_provider_full_finds_named_custom_provider()` (function) — Explicit /model --provider should resolve saved custom_providers entries.
- L68 `test_switch_model_accepts_explicit_named_custom_provider(monkeypatch)` (function) — Shared /model switch pipeline should accept --provider for custom_providers.
- L107 `test_list_groups_same_name_custom_providers_into_one_row(monkeypatch)` (function) — Multiple custom_providers entries sharing a name should produce one row
- L138 `test_list_deduplicates_same_model_in_group(monkeypatch)` (function) — Duplicate model entries under the same provider name should not produce
- L161 `test_list_enumerates_dict_format_models_alongside_default(monkeypatch)` (function) — custom_providers entry with dict-format ``models:`` plus singular
- L197 `test_list_enumerates_dict_format_models_without_singular_model(monkeypatch)` (function) — Dict-format ``models:`` with no singular ``model:`` should still
- L230 `test_list_dedupes_dict_model_matching_singular_default(monkeypatch)` (function) — When the singular ``model:`` is also a key in the ``models:`` dict,
- L263 `test_list_authenticated_providers_groups_same_endpoint(monkeypatch)` (function) — Multiple custom_providers entries sharing a base_url+api_key must be
- L296 `test_list_authenticated_providers_current_endpoint_uses_current_slug(monkeypatch)` (function) — When current_base_url matches the grouped endpoint, the slug must
- L322 `test_list_authenticated_providers_bare_custom_slug_recovers(monkeypatch)` (function) — Regression for #17478: when a prior failed switch left the bare
- L349 `test_list_authenticated_providers_distinct_endpoints_stay_separate(monkeypatch)` (function) — Entries with different base_urls must produce separate picker rows
- L377 `test_list_authenticated_providers_same_url_different_keys_disambiguated(monkeypatch)` (function) — Two custom_providers entries with the same base_url but different
- L406 `test_list_authenticated_providers_same_url_different_key_env_and_api_mode_stay_separate(monkeypatch)` (function) — Same gateway host but different key_env/api_mode entries are distinct providers.
- L444 `test_list_authenticated_providers_total_models_reflects_grouped_count(monkeypatch)` (function) — After grouping six entries into one row, total_models must reflect
- L469 `test_lmstudio_picker_probes_active_config_base_url(monkeypatch)` (function) — When `provider: lmstudio` is saved with a remote base_url and no
- L498 `test_lmstudio_picker_lm_base_url_env_wins_over_active_config(monkeypatch)` (function) — LM_BASE_URL env var must still take precedence over the saved
- L524 `test_lmstudio_picker_skips_probe_when_not_configured(monkeypatch)` (function) — If the user has never configured LM Studio (no LM_API_KEY / LM_BASE_URL
- L550 `test_custom_providers_uses_live_models_for_multi_model_endpoint(monkeypatch)` (function) — Custom providers with api_key + base_url should prefer live /models.
- L611 `test_custom_providers_discover_models_false_keeps_explicit_subset(monkeypatch)` (function) — Custom providers (section 4) with ``discover_models: false`` must keep
- L672 `test_custom_providers_discover_models_false_string_is_normalised(monkeypatch)` (function) — String ``discover_models: "false"`` (hand-edited / env-style configs)
