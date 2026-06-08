---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_ollama_cloud_provider.py

Symbols in `tests/hermes_cli/test_ollama_cloud_provider.py`.

- L15 `TestOllamaCloudProviderRegistry` (class)
- L16 `test_ollama_cloud_in_registry(self)` (method)
- L19 `test_ollama_cloud_config(self)` (method)
- L26 `test_ollama_cloud_env_vars(self)` (method)
- L31 `test_ollama_cloud_base_url(self)` (method)
- L45 `_clean_provider_env(monkeypatch)` (function)
- L50 `TestOllamaCloudAliases` (class)
- L51 `test_explicit_ollama_cloud(self)` (method)
- L54 `test_alias_ollama_underscore(self)` (method) — ollama_cloud (underscore) is the unambiguous cloud alias.
- L58 `test_bare_ollama_stays_local(self)` (method) — Bare 'ollama' alias routes to 'custom' (local) — not cloud.
- L62 `test_models_py_aliases(self)` (method)
- L67 `test_normalize_provider(self)` (method)
- L73 `TestOllamaCloudAutoDetection` (class)
- L74 `test_auto_detects_ollama_api_key(self, monkeypatch)` (method)
- L81 `TestOllamaCloudCredentials` (class)
- L82 `test_resolve_with_ollama_api_key(self, monkeypatch)` (method)
- L89 `test_resolve_with_custom_base_url(self, monkeypatch)` (method)
- L95 `test_runtime_ollama_cloud(self, monkeypatch)` (method)
- L107 `TestOllamaCloudModelCatalog` (class)
- L108 `test_no_static_model_list(self)` (method) — Ollama Cloud models are fetched dynamically — no static list to maintain.
- L112 `test_provider_label(self)` (method)
- L116 `test_provider_model_ids_returns_dynamic_models(self, tmp_path, monkeypatch)` (method) — provider_model_ids('ollama-cloud') should call fetch_ollama_cloud_models().
- L141 `TestOllamaCloudModelPicker` (class)
- L142 `test_ollama_cloud_shows_model_count(self, tmp_path, monkeypatch)` (method) — Ollama Cloud should show non-zero model count in provider picker.
- L165 `test_ollama_cloud_not_shown_without_creds(self, monkeypatch)` (method) — Ollama Cloud should not appear without credentials.
- L178 `TestOllamaCloudMergedDiscovery` (class)
- L179 `test_merges_live_and_models_dev(self, tmp_path, monkeypatch)` (method) — Live API models appear first, models.dev additions fill gaps.
- L206 `test_falls_back_to_models_dev_without_api_key(self, tmp_path, monkeypatch)` (method) — Without API key, only models.dev results are returned.
- L225 `test_uses_disk_cache(self, tmp_path, monkeypatch)` (method) — Second call returns cached results without hitting APIs.
- L243 `test_force_refresh_bypasses_cache(self, tmp_path, monkeypatch)` (method) — force_refresh=True always hits the API even with fresh cache.
- L256 `test_stale_cache_used_on_total_failure(self, tmp_path, monkeypatch)` (method) — If both API and models.dev fail, stale cache is returned.
- L281 `test_empty_on_total_failure_no_cache(self, tmp_path, monkeypatch)` (method) — Returns empty list when everything fails and no cache exists.
- L296 `TestOllamaCloudModelNormalization` (class)
- L297 `test_passthrough_bare_name(self)` (method) — Ollama Cloud is a passthrough provider — model names used as-is.
- L301 `test_passthrough_with_tag(self)` (method)
- L304 `test_passthrough_no_tag(self)` (method)
- L310 `TestOllamaCloudUrlMapping` (class)
- L311 `test_url_to_provider(self)` (method)
- L314 `test_provider_prefix_canonical(self)` (method)
- L317 `test_provider_prefix_alias(self)` (method)
- L323 `TestOllamaCloudModelsDev` (class)
- L324 `test_ollama_cloud_mapped(self)` (method)
- L327 `test_list_agentic_models_with_mock_data(self)` (method) — list_agentic_models filters correctly from mock models.dev data.
- L349 `TestOllamaCloudAgentInit` (class)
- L350 `test_agent_imports_without_error(self)` (method) — Verify run_agent.py has no SyntaxError.
- L356 `test_ollama_cloud_agent_uses_chat_completions(self, monkeypatch)` (method) — Ollama Cloud falls through to chat_completions — no special elif needed.
- L374 `TestOllamaCloudProvidersNew` (class)
- L375 `test_overlay_exists(self)` (method)
- L382 `test_alias_resolves(self)` (method)
- L387 `test_label_override(self)` (method)
- L391 `test_get_label(self)` (method)
- L395 `test_get_provider(self)` (method)
- L405 `TestOllamaCloudSuffixStripping` (class) — models.dev appends :cloud / -cloud suffixes that the live API omits.
- L412 `test_strips_colon_cloud_suffix(self, tmp_path, monkeypatch)` (method) — :cloud suffix from models.dev is stripped before merge.
- L430 `test_strips_dash_cloud_suffix(self, tmp_path, monkeypatch)` (method) — -cloud suffix from models.dev is stripped before merge.
- L448 `test_no_duplicate_when_live_clean_and_mdev_suffixed(self, tmp_path, monkeypatch)` (method) — Live API returns clean ID; mdev has :cloud variant — result has exactly one entry.
- L472 `test_unsuffixed_model_id_unchanged(self, tmp_path, monkeypatch)` (method) — Model IDs without :cloud / -cloud suffix are passed through unchanged.
- L489 `test_strip_suffix_helper(self)` (method) — Unit test for the _strip_ollama_cloud_suffix helper.
