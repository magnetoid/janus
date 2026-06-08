---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_models_dev.py

Symbols in `tests/agent/test_models_dev.py`.

- L84 `TestProviderMapping` (class)
- L85 `test_xai_oauth_uses_xai_catalog(self)` (method)
- L89 `test_unmapped_provider_not_in_dict(self)` (method)
- L92 `test_openai_codex_mapped_to_openai(self)` (method)
- L97 `TestExtractContext` (class)
- L98 `test_valid_entry(self)` (method)
- L101 `test_zero_context_returns_none(self)` (method)
- L104 `test_missing_limit_returns_none(self)` (method)
- L107 `test_missing_context_returns_none(self)` (method)
- L110 `test_non_dict_returns_none(self)` (method)
- L113 `test_float_context_coerced_to_int(self)` (method)
- L117 `TestLookupModelsDevContext` (class)
- L119 `test_exact_match(self, mock_fetch)` (method)
- L124 `test_case_insensitive_match(self, mock_fetch)` (method)
- L129 `test_provider_not_mapped(self, mock_fetch)` (method)
- L134 `test_model_not_found(self, mock_fetch)` (method)
- L139 `test_provider_aware_context(self, mock_fetch)` (method) — Same model, different context per provider.
- L148 `test_xai_oauth_resolves_xai_context(self, mock_fetch)` (method) — xAI OAuth is an auth path, not a separate model catalog.
- L154 `test_zero_context_filtered(self, mock_fetch)` (method)
- L161 `test_empty_registry(self, mock_fetch)` (method)
- L166 `TestFetchModelsDev` (class)
- L168 `test_fetch_success(self, mock_get)` (method)
- L187 `test_fetch_failure_returns_stale_cache(self, mock_get)` (method)
- L200 `test_in_memory_cache_used(self, mock_get)` (method)
- L211 `test_fresh_disk_cache_skips_network(self, mock_get)` (method) — When in-mem cache is empty but disk cache exists and is fresh by
- L237 `test_stale_disk_cache_falls_through_to_network(self, mock_get)` (method) — When the disk cache is OLDER than TTL, we must hit the network
- L261 `test_force_refresh_skips_disk_cache(self, mock_get)` (method) — force_refresh=True bypasses BOTH the in-mem cache AND the
- L286 `test_missing_disk_cache_falls_through_to_network(self, mock_get)` (method) — If the disk cache file doesn't exist (first-ever run, or it
- L351 `TestGetModelCapabilities` (class) — Tests for get_model_capabilities vision detection.
- L354 `test_vision_from_attachment_flag(self)` (method) — Models with attachment=True and no modalities should report supports_vision=True.
- L361 `test_vision_from_modalities_input_image(self)` (method) — Models with 'image' in modalities.input but attachment=False should
- L369 `test_text_only_modalities_override_stale_attachment_flag(self)` (method) — Text-only modalities must win over stale attachment=True metadata.
- L376 `test_no_vision_without_attachment_or_modalities(self)` (method) — Models with neither attachment nor image modality should be non-vision.
- L383 `test_modalities_non_dict_handled(self)` (method) — Non-dict modalities field should not crash.
- L399 `test_model_not_found_returns_none(self)` (method) — Unknown model should return None.
