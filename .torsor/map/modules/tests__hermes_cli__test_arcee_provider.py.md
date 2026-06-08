---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_arcee_provider.py

Symbols in `tests/hermes_cli/test_arcee_provider.py`.

- L30 `TestArceeProviderRegistry` (class)
- L31 `test_registered(self)` (method)
- L34 `test_name(self)` (method)
- L37 `test_auth_type(self)` (method)
- L40 `test_inference_base_url(self)` (method)
- L43 `test_api_key_env_vars(self)` (method)
- L46 `test_base_url_env_var(self)` (method)
- L55 `TestArceeAliases` (class)
- L57 `test_alias_resolves(self, alias, monkeypatch)` (method)
- L63 `test_normalize_provider_models_py(self)` (method)
- L68 `test_normalize_provider_providers_py(self)` (method)
- L79 `TestArceeCredentials` (class)
- L80 `test_status_configured(self, monkeypatch)` (method)
- L85 `test_status_not_configured(self, monkeypatch)` (method)
- L90 `test_openrouter_key_does_not_make_arcee_configured(self, monkeypatch)` (method) — OpenRouter users should NOT see arcee as configured.
- L97 `test_resolve_credentials(self, monkeypatch)` (method)
- L104 `test_custom_base_url_override(self, monkeypatch)` (method)
- L116 `TestArceeModelCatalog` (class)
- L117 `test_static_model_list(self)` (method) — Arcee has a static _PROVIDER_MODELS catalog entry. Specific model
- L125 `test_canonical_provider_entry(self)` (method)
- L136 `TestArceeNormalization` (class)
- L137 `test_in_matching_prefix_strip_set(self)` (method)
- L141 `test_strips_prefix(self)` (method)
- L145 `test_bare_name_unchanged(self)` (method)
- L155 `TestArceeURLMapping` (class)
- L156 `test_url_to_provider(self)` (method)
- L160 `test_provider_prefixes(self)` (method)
- L166 `test_trajectory_compressor_detects_arcee(self)` (method)
- L178 `TestArceeProvidersModule` (class)
- L179 `test_overlay_exists(self)` (method)
- L187 `test_label(self)` (method)
- L197 `TestArceeAuxiliary` (class)
- L198 `test_main_model_first_design(self)` (method) — Arcee uses main-model-first — no entry in _API_KEY_PROVIDER_AUX_MODELS.
