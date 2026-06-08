---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_xiaomi_provider.py

Symbols in `tests/hermes_cli/test_xiaomi_provider.py`.

- L19 `TestXiaomiProviderRegistry` (class) — Verify Xiaomi is registered correctly in the PROVIDER_REGISTRY.
- L22 `test_registered(self)` (method)
- L25 `test_name(self)` (method)
- L28 `test_auth_type(self)` (method)
- L31 `test_inference_base_url(self)` (method)
- L34 `test_api_key_env_vars(self)` (method)
- L37 `test_base_url_env_var(self)` (method)
- L46 `TestXiaomiAliases` (class) — All aliases should resolve to 'xiaomi'.
- L52 `test_alias_resolves(self, alias, monkeypatch)` (method)
- L59 `test_normalize_provider_models_py(self)` (method)
- L64 `test_normalize_provider_providers_py(self)` (method)
- L75 `TestXiaomiAutoDetection` (class) — Setting XIAOMI_API_KEY should auto-detect the provider.
- L78 `test_auto_detect(self, monkeypatch)` (method)
- L98 `TestXiaomiCredentials` (class) — Test credential resolution for the xiaomi provider.
- L101 `test_status_configured(self, monkeypatch)` (method)
- L106 `test_status_not_configured(self, monkeypatch)` (method)
- L111 `test_resolve_credentials(self, monkeypatch)` (method)
- L118 `test_custom_base_url_override(self, monkeypatch)` (method)
- L130 `TestXiaomiModelCatalog` (class) — Xiaomi uses dynamic model discovery via models.dev.
- L133 `test_models_dev_mapping(self)` (method)
- L137 `test_static_model_list_fallback(self)` (method) — Static _PROVIDER_MODELS fallback must exist for model picker.
- L148 `test_list_agentic_models_mock(self, monkeypatch)` (method) — When models.dev returns Xiaomi data, list_agentic_models should return models.
- L185 `TestXiaomiNormalization` (class) — Model name normalization — Xiaomi is a direct provider.
- L188 `test_vendor_prefix_mapping(self)` (method)
- L192 `test_matching_prefix_strip(self)` (method) — xiaomi/mimo-v2-pro should normalize to mimo-v2-pro for direct API.
- L197 `test_lowercase_model_provider(self)` (method) — Xiaomi must be in _LOWERCASE_MODEL_PROVIDERS.
- L202 `test_lowercase_subset_of_matching_prefix(self)` (method) — _LOWERCASE_MODEL_PROVIDERS must be a subset of _MATCHING_PREFIX_STRIP_PROVIDERS.
- L217 `test_normalize_strips_provider_prefix(self)` (method)
- L222 `test_normalize_bare_name_unchanged(self)` (method)
- L228 `test_normalize_empty_and_none(self, empty_input)` (method) — None, empty, and whitespace-only inputs return empty string.
- L244 `test_normalize_lowercases_mixed_case(self, input_name, expected)` (method) — Xiaomi's API requires lowercase model IDs — mixed case from docs must be lowered.
- L255 `test_normalize_strips_prefix_and_lowercases(self, input_name, expected)` (method) — Provider prefix stripping AND lowercasing must both work together.
- L267 `TestXiaomiURLMapping` (class) — Test URL → provider inference for Xiaomi endpoints.
- L270 `test_url_to_provider(self)` (method)
- L274 `test_provider_prefixes(self)` (method)
- L280 `test_infer_from_url(self)` (method)
- L284 `test_infer_from_regional_urls(self)` (method) — Regional token-plan endpoints should also resolve to xiaomi.
- L297 `TestXiaomiProvidersModule` (class) — Test Xiaomi in the unified providers module.
- L300 `test_overlay_exists(self)` (method)
- L308 `test_alias_resolves(self)` (method)
- L313 `test_label(self)` (method)
- L317 `test_get_provider(self)` (method)
- L334 `TestXiaomiAuxiliary` (class) — Xiaomi auxiliary routing: vision → omni, non-vision → user's main model, never flash.
- L337 `test_no_flash_in_aux_models(self)` (method) — mimo-v2-flash must NEVER be used for automatic aux routing.
- L342 `test_vision_model_override(self)` (method) — Xiaomi vision tasks should use mimo-v2.5 (multimodal), not the main model.
- L354 `TestXiaomiDoctor` (class) — Verify hermes doctor recognizes Xiaomi env vars.
- L357 `test_provider_env_hints(self)` (method)
- L362 `TestXiaomiAgentInit` (class) — Verify the agent can be constructed with xiaomi provider without errors.
- L365 `test_no_syntax_errors(self)` (method) — Importing run_agent with xiaomi should not raise.
- L370 `test_api_mode_is_chat_completions(self)` (method)
