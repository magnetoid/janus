---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_gemini_provider.py

Symbols in `tests/hermes_cli/test_gemini_provider.py`.

- L15 `TestGeminiProviderRegistry` (class)
- L16 `test_gemini_in_registry(self)` (method)
- L19 `test_gemini_config(self)` (method)
- L26 `test_gemini_env_vars(self)` (method)
- L31 `test_gemini_base_url(self)` (method)
- L45 `_clean_provider_env(monkeypatch)` (function)
- L50 `TestGeminiAliases` (class)
- L51 `test_explicit_gemini(self)` (method)
- L54 `test_alias_google(self)` (method)
- L57 `test_alias_google_gemini(self)` (method)
- L60 `test_alias_google_ai_studio(self)` (method)
- L63 `test_models_py_aliases(self)` (method)
- L68 `test_normalize_provider(self)` (method)
- L76 `TestGeminiAutoDetection` (class)
- L77 `test_auto_detects_google_api_key(self, monkeypatch)` (method)
- L81 `test_auto_detects_gemini_api_key(self, monkeypatch)` (method)
- L85 `test_google_api_key_priority_over_gemini(self, monkeypatch)` (method)
- L95 `TestGeminiCredentials` (class)
- L96 `test_resolve_with_google_api_key(self, monkeypatch)` (method)
- L103 `test_resolve_with_gemini_api_key(self, monkeypatch)` (method)
- L108 `test_resolve_with_custom_base_url(self, monkeypatch)` (method)
- L114 `test_runtime_gemini(self, monkeypatch)` (method)
- L126 `TestGeminiModelCatalog` (class)
- L127 `test_provider_entry_exists(self)` (method) — Gemini provider has a model catalog entry. Specific model names
- L134 `test_provider_label(self)` (method)
- L141 `TestGeminiModelNormalization` (class)
- L142 `test_passthrough_bare_name(self)` (method)
- L145 `test_strip_vendor_prefix(self)` (method)
- L148 `test_gemma_vendor_detection(self)` (method)
- L151 `test_gemini_vendor_detection(self)` (method)
- L154 `test_aggregator_prepends_vendor(self)` (method)
- L158 `test_gemma_aggregator_prepends_vendor(self)` (method)
- L165 `TestGeminiContextLength` (class)
- L166 `test_gemma_4_31b_context(self)` (method)
- L174 `test_gemini_3_context(self)` (method)
- L181 `TestGeminiAgentInit` (class)
- L182 `test_agent_imports_without_error(self)` (method) — Verify run_agent.py has no SyntaxError (the critical bug).
- L188 `test_gemini_agent_uses_chat_completions(self, monkeypatch)` (method) — Gemini still reports chat_completions even though the transport is native.
- L203 `test_gemini_agent_uses_native_client(self, monkeypatch)` (method)
- L220 `test_gemini_custom_base_url_keeps_openai_client(self, monkeypatch)` (method)
- L236 `test_gemini_openai_compat_base_url_keeps_openai_client(self, monkeypatch)` (method)
- L252 `test_gemini_resolve_provider_client_uses_native_client(self, monkeypatch)` (method) — resolve_provider_client('gemini') should build GeminiNativeClient.
- L263 `test_gemini_resolve_provider_client_keeps_openai_for_non_native_base_url(self, monkeypatch)` (method)
- L276 `TestGeminiModelsDev` (class)
- L277 `test_gemini_mapped_to_google(self)` (method)
- L280 `test_noise_filter_excludes_tts(self)` (method)
- L283 `test_noise_filter_excludes_dated_preview(self)` (method)
- L286 `test_noise_filter_excludes_embedding(self)` (method)
- L289 `test_noise_filter_excludes_live(self)` (method)
- L292 `test_noise_filter_excludes_image(self)` (method)
- L295 `test_noise_filter_excludes_customtools(self)` (method)
- L298 `test_noise_filter_passes_stable(self)` (method)
- L301 `test_noise_filter_passes_preview(self)` (method)
- L305 `test_noise_filter_passes_gemma(self)` (method)
- L308 `test_list_agentic_models_with_mock_data(self)` (method) — list_agentic_models filters correctly from mock models.dev data.
- L334 `test_list_provider_models_hides_low_tpm_google_gemmas(self)` (method)
