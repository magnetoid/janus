---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_auxiliary_named_custom_providers.py

Symbols in `tests/agent/test_auxiliary_named_custom_providers.py`.

- L9 `_isolate(tmp_path, monkeypatch)` (function) — Redirect HERMES_HOME and clear module caches.
- L18 `_write_config(tmp_path, config_dict)` (function) — Write a config.yaml to the test HERMES_HOME.
- L25 `TestNormalizeVisionProvider` (class) — _normalize_vision_provider should resolve 'main' to actual main provider.
- L28 `test_main_resolves_to_named_custom(self, tmp_path)` (method)
- L36 `test_main_resolves_to_openrouter(self, tmp_path)` (method)
- L43 `test_main_resolves_to_deepseek(self, tmp_path)` (method)
- L50 `test_main_falls_back_to_custom_when_no_provider(self, tmp_path)` (method)
- L55 `test_bare_provider_name_unchanged(self)` (method)
- L60 `test_custom_colon_named_provider_preserved(self)` (method)
- L64 `test_codex_alias_still_works(self)` (method)
- L68 `test_auto_unchanged(self)` (method)
- L74 `TestResolveProviderClientMainAlias` (class) — resolve_provider_client('main', ...) should resolve to actual main provider.
- L77 `test_main_resolves_to_named_custom_provider(self, tmp_path)` (method)
- L90 `test_main_with_custom_colon_prefix(self, tmp_path)` (method)
- L102 `test_main_resolves_github_copilot_alias(self, tmp_path)` (method)
- L123 `TestResolveProviderClientNamedCustom` (class) — resolve_provider_client should resolve named custom providers directly.
- L126 `test_named_custom_provider(self, tmp_path)` (method)
- L139 `test_named_custom_provider_default_model(self, tmp_path)` (method)
- L152 `test_named_custom_no_api_key_uses_fallback(self, tmp_path)` (method)
- L164 `test_nonexistent_named_custom_falls_through(self, tmp_path)` (method)
- L177 `TestResolveProviderClientModelNormalization` (class) — Direct-provider auxiliary routing should normalize models like main runtime.
- L180 `test_matching_native_prefix_is_stripped_for_main_provider(self, tmp_path)` (method)
- L199 `test_non_matching_prefix_is_preserved_for_direct_provider(self, tmp_path)` (method)
- L218 `test_aggregator_vendor_slug_is_preserved(self, monkeypatch)` (method)
- L232 `TestResolveVisionProviderClientModelNormalization` (class) — Vision auto-routing should reuse the same provider-specific normalization.
- L235 `test_vision_auto_strips_matching_main_provider_prefix(self, tmp_path)` (method)
- L257 `TestVisionPathApiMode` (class) — Vision path should propagate api_mode to _get_cached_client.
- L260 `test_explicit_provider_passes_api_mode(self, tmp_path)` (method)
- L276 `TestProvidersDictApiModeAnthropicMessages` (class) — Regression guard for #15033.
- L289 `test_providers_dict_propagates_api_mode(self, tmp_path, monkeypatch)` (method)
- L309 `test_providers_dict_invalid_api_mode_is_dropped(self, tmp_path)` (method)
- L325 `test_providers_dict_without_api_mode_is_unchanged(self, tmp_path)` (method)
- L341 `test_resolve_provider_client_returns_anthropic_client(self, tmp_path, monkeypatch)` (method) — Named custom provider with api_mode=anthropic_messages must
- L373 `test_aux_task_override_routes_named_provider_to_anthropic(self, tmp_path, monkeypatch)` (method) — The full chain: auxiliary.<task>.provider: myrelay with
- L409 `test_provider_without_api_mode_still_uses_openai(self, tmp_path)` (method) — Named providers that don't declare api_mode should still go
- L431 `TestCustomProviderAliasCollision` (class) — A user-declared custom_providers entry whose name matches a built-in
- L441 `test_custom_named_kimi_wins_over_builtin_alias(self, tmp_path)` (method)
- L461 `test_bare_kimi_without_custom_still_routes_to_builtin(self, tmp_path, monkeypatch)` (method) — Regression guard: bare 'kimi' with no custom entry must still
- L475 `test_explicit_overrides_applied_on_api_key_branch(self, tmp_path, monkeypatch)` (method) — Explicit base_url/api_key from the caller must override the
