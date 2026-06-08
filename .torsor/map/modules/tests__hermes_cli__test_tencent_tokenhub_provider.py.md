---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_tencent_tokenhub_provider.py

Symbols in `tests/hermes_cli/test_tencent_tokenhub_provider.py`.

- L33 `TestTencentTokenhubProviderRegistry` (class) — Verify tencent-tokenhub is registered correctly in the PROVIDER_REGISTRY.
- L36 `test_registered(self)` (method)
- L39 `test_name(self)` (method)
- L42 `test_auth_type(self)` (method)
- L45 `test_inference_base_url(self)` (method)
- L48 `test_api_key_env_vars(self)` (method)
- L51 `test_base_url_env_var(self)` (method)
- L60 `TestTencentTokenhubAliases` (class) — All aliases should resolve to 'tencent-tokenhub'.
- L66 `test_alias_resolves(self, alias, monkeypatch)` (method)
- L72 `test_normalize_provider_models_py(self)` (method)
- L79 `test_normalize_provider_providers_py(self)` (method)
- L92 `TestTencentTokenhubAutoDetection` (class) — Setting TOKENHUB_API_KEY should auto-detect the provider.
- L95 `test_auto_detect(self, monkeypatch)` (method)
- L108 `TestTencentTokenhubCredentials` (class) — Test credential resolution for the tencent-tokenhub provider.
- L111 `test_status_configured(self, monkeypatch)` (method)
- L116 `test_status_not_configured(self, monkeypatch)` (method)
- L121 `test_resolve_credentials(self, monkeypatch)` (method)
- L128 `test_openrouter_key_does_not_make_tokenhub_configured(self, monkeypatch)` (method) — OpenRouter users should NOT see tencent-tokenhub as configured.
- L135 `test_custom_base_url_override(self, monkeypatch)` (method)
- L147 `TestTencentTokenhubModelCatalog` (class) — Tencent TokenHub static model list.
- L150 `test_static_model_list_exists(self)` (method)
- L155 `test_hy3_preview_in_model_list(self)` (method)
- L159 `test_default_model(self)` (method)
- L169 `TestTencentTokenhubCanonicalProvider` (class) — Tencent TokenHub appears in the interactive model picker.
- L172 `test_in_canonical_providers(self)` (method)
- L177 `test_label(self)` (method)
- L182 `test_description_contains_hy3(self)` (method)
- L193 `TestTencentInOpenRouterAndNous` (class) — tencent/hy3-preview:free and tencent/hy3-preview should appear in OpenRouter and Nous curated lists.
- L196 `test_in_openrouter_fallback(self)` (method)
- L201 `test_paid_in_openrouter_fallback(self)` (method) — tencent/hy3-preview (paid, no :free suffix) should also be in OpenRouter list.
- L207 `test_in_nous_provider_models(self)` (method)
- L217 `TestTencentTokenhubNormalization` (class) — Model name normalization — Tencent TokenHub is a direct provider
- L222 `test_bare_name_passthrough(self)` (method) — hy3-preview should remain unchanged when targeting tencent-tokenhub.
- L228 `test_vendor_prefixed_passthrough(self)` (method) — tencent/hy3-preview is not stripped since tencent-tokenhub is not in
- L236 `test_not_in_matching_prefix_strip_set(self)` (method) — tencent-tokenhub does NOT need prefix stripping — it only has
- L242 `test_not_in_lowercase_providers(self)` (method) — tencent-tokenhub does not require lowercase normalization.
- L248 `test_normalize_empty_and_none(self, empty_input)` (method) — None, empty, and whitespace-only inputs return empty string.
- L260 `TestTencentTokenhubProviderLabel` (class) — Test provider_label() from models.py for tencent-tokenhub.
- L263 `test_label_from_provider_labels_dict(self)` (method)
- L267 `test_provider_label_function(self)` (method)
- L271 `test_provider_label_via_alias(self)` (method)
- L282 `TestTencentTokenhubURLMapping` (class) — Test URL → provider inference for Tencent TokenHub endpoints.
- L285 `test_url_to_provider(self)` (method)
- L289 `test_provider_prefixes(self)` (method)
- L295 `test_infer_from_url(self)` (method)
- L305 `TestTencentTokenhubContextLength` (class) — hy3-preview has a context-length entry registered.
- L315 `test_hy3_preview_has_registered_context_length(self)` (method)
- L327 `TestTencentTokenhubProvidersModule` (class) — Test Tencent TokenHub in the unified providers module.
- L330 `test_overlay_exists(self)` (method)
- L338 `test_alias_resolves(self)` (method)
- L343 `test_label(self)` (method)
- L347 `test_get_provider(self)` (method)
- L364 `TestTencentTokenhubAuxiliary` (class) — Tencent TokenHub auxiliary model routing.
- L367 `test_aux_model_registered(self)` (method)
- L372 `test_aux_aliases(self)` (method)
- L383 `TestTencentTokenhubDoctor` (class) — Verify hermes doctor recognizes Tencent TokenHub env vars.
- L386 `test_provider_env_hints(self)` (method)
- L396 `TestTencentTokenhubAgentInit` (class) — Verify the agent can be constructed with tencent-tokenhub provider without errors.
- L399 `test_no_syntax_errors(self)` (method) — Importing run_agent with tencent-tokenhub should not raise.
- L404 `test_api_mode_is_chat_completions(self)` (method)
- L416 `TestTencentTokenhubCLIDispatch` (class) — Verify tencent-tokenhub is routed through _model_flow_api_key_provider.
- L419 `test_in_api_key_provider_tuple(self)` (method) — tencent-tokenhub must appear in the elif tuple in _model_flow dispatch
- L435 `TestTencentTokenhubModelCatalogJSON` (class) — Verify tencent/hy3-preview:free and tencent/hy3-preview are present in the website model-catalog.json.
- L438 `test_in_model_catalog_json(self)` (method)
- L469 `TestTencentTokenhubApiMode` (class) — Verify determine_api_mode routes tencent-tokenhub correctly.
- L472 `test_determine_api_mode_direct(self)` (method)
- L477 `test_determine_api_mode_with_base_url(self)` (method)
- L482 `test_determine_api_mode_via_alias(self)` (method)
- L493 `TestTencentTokenhubKnownProviderNames` (class) — Verify tencent-tokenhub and its aliases are recognized as valid
- L498 `test_canonical_id_known(self)` (method)
- L505 `test_alias_known(self, alias)` (method)
