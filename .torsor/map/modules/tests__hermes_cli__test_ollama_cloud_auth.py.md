---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_ollama_cloud_auth.py

Symbols in `tests/hermes_cli/test_ollama_cloud_auth.py`.

- L19 `TestOllamaCloudCredentials` (class) — runtime_provider should use OLLAMA_API_KEY for ollama.com endpoints.
- L22 `test_ollama_api_key_used_for_ollama_endpoint(self, monkeypatch, tmp_path)` (method) — When base_url contains ollama.com, OLLAMA_API_KEY is in the candidate chain.
- L48 `test_ollama_key_not_used_for_non_ollama_endpoint(self, monkeypatch)` (method) — OLLAMA_API_KEY should NOT be used for non-ollama endpoints.
- L76 `TestDirectAliases` (class) — model_switch direct aliases from config.yaml model_aliases.
- L79 `test_direct_alias_loaded_from_config(self, monkeypatch)` (method) — Direct aliases load from config.yaml model_aliases section.
- L103 `test_direct_alias_resolved_before_catalog(self, monkeypatch)` (method) — Direct aliases take priority over models.dev catalog lookup.
- L120 `test_reverse_lookup_by_model_id(self, monkeypatch)` (method) — Full model names (e.g. 'kimi-k2.5') match via reverse lookup.
- L138 `test_reverse_lookup_case_insensitive(self, monkeypatch)` (method) — Reverse lookup is case-insensitive.
- L157 `TestModelSwitchPersistence` (class) — CLI /model command should update requested_provider for session persistence.
- L160 `test_model_switch_result_fields(self)` (method) — ModelSwitchResult has all required fields for CLI state update.
- L185 `TestFallbackBaseUrlPassthrough` (class) — _try_activate_fallback should pass base_url from fallback config.
- L188 `test_fallback_config_has_base_url(self)` (method) — Verify fallback_providers config structure supports base_url.
- L198 `test_ollama_key_lookup_for_fallback(self, monkeypatch)` (method) — When fallback base_url is ollama.com and no api_key, OLLAMA_API_KEY is used.
- L222 `TestLoadDirectAliasesEdgeCases` (class) — Edge cases for _load_direct_aliases parsing.
- L225 `test_empty_model_aliases_config(self, monkeypatch)` (method) — Empty model_aliases dict returns only builtins (if any).
- L237 `test_model_aliases_not_a_dict(self, monkeypatch)` (method) — Non-dict model_aliases value is gracefully ignored.
- L249 `test_model_aliases_none_value(self, monkeypatch)` (method) — model_aliases: null in config is handled gracefully.
- L261 `test_malformed_entry_without_model_key(self, monkeypatch)` (method) — Entries missing 'model' key are skipped.
- L285 `test_malformed_entry_non_dict_value(self, monkeypatch)` (method) — Non-dict entry values are skipped.
- L307 `test_load_config_exception_returns_builtins(self, monkeypatch)` (method) — If load_config raises, _load_direct_aliases returns builtins only.
- L318 `test_alias_name_normalized_lowercase(self, monkeypatch)` (method) — Alias names are lowercased and stripped.
- L338 `test_empty_model_string_skipped(self, monkeypatch)` (method) — Entries with empty model string are skipped.
- L361 `TestEnsureDirectAliases` (class) — _ensure_direct_aliases lazy-loading behavior.
- L364 `test_ensure_populates_on_first_call(self, monkeypatch)` (method) — DIRECT_ALIASES is populated after _ensure_direct_aliases.
- L381 `test_ensure_no_reload_when_populated(self, monkeypatch)` (method) — _ensure_direct_aliases does not reload if already populated.
- L405 `TestResolveAliasEdgeCases` (class) — Edge cases for resolve_alias.
- L408 `test_unknown_alias_returns_none(self, monkeypatch)` (method) — Unknown alias not in direct or catalog returns None.
- L416 `test_whitespace_input_handled(self, monkeypatch)` (method) — Input with whitespace is stripped before lookup.
- L435 `TestSwitchModelDirectAliasOverride` (class) — switch_model should use base_url from direct alias.
- L438 `test_switch_model_uses_alias_base_url(self, monkeypatch)` (method) — When resolved alias has base_url, switch_model should use it.
- L466 `test_switch_model_alias_no_api_key_gets_default(self, monkeypatch)` (method) — When alias has base_url but no api_key, 'no-key-required' is set.
- L496 `TestCLIStateUpdate` (class) — CLI /model handler should update requested_provider and explicit fields.
- L499 `test_model_switch_result_has_provider_label(self)` (method) — ModelSwitchResult supports provider_label for display.
- L515 `test_model_switch_result_defaults(self)` (method) — ModelSwitchResult has sensible defaults.
- L536 `TestFallbackEdgeCases` (class) — Edge cases for fallback OLLAMA_API_KEY logic.
- L539 `test_ollama_key_not_injected_for_localhost(self, monkeypatch)` (method) — OLLAMA_API_KEY should not be injected for localhost URLs.
- L557 `test_explicit_api_key_not_overridden_by_ollama_key(self, monkeypatch)` (method) — Explicit api_key in fallback config is not overridden by OLLAMA_API_KEY.
- L576 `test_no_base_url_in_fallback(self, monkeypatch)` (method) — Fallback with no base_url doesn't crash.
