---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_user_providers_model_switch.py

Symbols in `tests/hermes_cli/test_user_providers_model_switch.py`.

- L17 `test_list_authenticated_providers_includes_full_models_list_from_user_providers(monkeypatch)` (function) — User-defined providers should expose both default_model and full models list.
- L60 `test_list_authenticated_providers_dedupes_models_when_default_in_list(monkeypatch)` (function) — When default_model is also in models list, don't duplicate.
- L89 `test_list_authenticated_providers_enumerates_dict_format_models(monkeypatch)` (function) — providers: dict entries with ``models:`` as a dict keyed by model id
- L134 `test_list_authenticated_providers_uses_live_models_for_user_provider(monkeypatch)` (function) — User-defined OpenAI-compatible providers should prefer live /models.
- L183 `test_list_authenticated_providers_dict_models_without_default_model(monkeypatch)` (function) — Dict-format ``models:`` without a ``default_model`` must still expose
- L215 `test_list_authenticated_providers_dict_models_dedupe_with_default(monkeypatch)` (function) — When ``default_model`` is also a key in the ``models:`` dict, it must
- L249 `test_openai_native_curated_catalog_is_non_empty()` (function) — Regression: built-in openai must have a static catalog for picker totals.
- L257 `test_list_authenticated_providers_openai_alias_not_emitted_as_phantom(monkeypatch)` (function) — Bare 'openai' is an alias to the OpenRouter aggregator, NOT a directly-
- L285 `test_resolve_provider_full_user_config_openai_beats_alias()` (function) — A providers.openai config entry must win over the built-in
- L309 `test_switch_model_user_config_openai_does_not_hop_to_openrouter(monkeypatch)` (function) — End-to-end: selecting a providers.openai config row in the picker must
- L338 `test_list_authenticated_providers_user_openai_official_url_fallback(monkeypatch)` (function) — User providers: api.openai.com with no models list uses native curated fallback.
- L361 `test_list_authenticated_providers_fallback_to_default_only(monkeypatch)` (function) — When no models array is provided, should fall back to default_model.
- L391 `test_list_authenticated_providers_accepts_base_url_and_singular_model(monkeypatch)` (function) — providers: dict entries written in canonical Hermes shape
- L429 `test_list_authenticated_providers_dedupes_when_user_and_custom_overlap(monkeypatch)` (function) — When the same slug appears in both ``providers:`` dict and
- L468 `test_list_authenticated_providers_no_duplicate_labels_across_schemas(monkeypatch)` (function) — Regression: same endpoint in both ``providers:`` dict AND ``custom_providers:``
- L516 `test_list_authenticated_providers_hides_custom_shadowing_builtin_endpoint(monkeypatch)` (function) — #16970: a custom_providers entry whose ``base_url`` matches a built-in
- L568 `test_list_authenticated_providers_keeps_custom_with_distinct_endpoint(monkeypatch)` (function) — Dedup must only apply when the endpoint matches a built-in. A custom
- L607 `test_list_authenticated_providers_dedup_honors_base_url_env_override(monkeypatch)` (function) — The dedup must track the EFFECTIVE endpoint — if DASHSCOPE_BASE_URL
- L656 `test_get_named_custom_provider_finds_user_providers_by_key(monkeypatch, tmp_path)` (function) — Should resolve providers from providers: dict (new-style), not just custom_providers.
- L681 `test_get_named_custom_provider_finds_by_display_name(monkeypatch, tmp_path)` (function) — Should match providers by their 'name' field as well as key.
- L706 `test_get_named_custom_provider_falls_back_to_legacy_format(monkeypatch, tmp_path)` (function) — Should still work with custom_providers: list format.
- L729 `test_get_named_custom_provider_returns_none_for_unknown(monkeypatch, tmp_path)` (function) — Should return None for providers that don't exist.
- L753 `test_get_named_custom_provider_skips_empty_base_url(monkeypatch, tmp_path)` (function) — Should skip providers without a base_url.
- L779 `test_switch_model_resolves_user_provider_credentials(monkeypatch, tmp_path)` (function) — /model switch should resolve credentials for providers: dict providers.
- L821 `test_get_named_custom_provider_reads_transport_field(monkeypatch)` (function) — v12+ ``providers:`` dict stores api mode under ``transport:`` (not the
- L855 `test_get_named_custom_provider_legacy_api_mode_field_still_works(monkeypatch)` (function) — Hand-edited configs that used ``api_mode:`` (legacy spelling) inside
- L880 `test_get_named_custom_provider_transport_resolves_via_display_name(monkeypatch)` (function) — When the requested name matches the entry's ``name:`` field rather
- L916 `_run_user_provider_override_case(*, slug, name, base_url, models, raw_input)` (function) — Run ``switch_model`` with a private user provider and a rejected API check.
- L982 `test_user_provider_override_accepts_listed_private_models(slug, name, base_url, models, raw_input, expected_model)` (function) — Private models listed in providers: config should override /v1/models misses.
- L1029 `test_user_provider_override_rejects_mangled_private_models(slug, name, base_url, models, raw_input)` (function) — Malformed model names should fail cleanly, not crash or auto-accept.
