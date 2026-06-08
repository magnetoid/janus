---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/image_gen/test_openai_provider.py

Symbols in `tests/plugins/image_gen/test_openai_provider.py`.

- L22 `_b64_png()` (function)
- L27 `_fake_response(*, b64=None, url=None, revised_prompt=None)` (function)
- L33 `_tmp_hermes_home(tmp_path, monkeypatch)` (function)
- L39 `provider(monkeypatch)` (function)
- L44 `_patched_openai(fake_client: MagicMock)` (function)
- L53 `TestMetadata` (class)
- L54 `test_name(self, provider)` (method)
- L57 `test_default_model(self, provider)` (method)
- L60 `test_list_models_three_tiers(self, provider)` (method)
- L64 `test_catalog_entries_have_display_speed_strengths(self, provider)` (method)
- L74 `TestAvailability` (class)
- L75 `test_no_api_key_unavailable(self, monkeypatch)` (method)
- L79 `test_api_key_set_available(self, monkeypatch)` (method)
- L87 `TestModelResolution` (class)
- L88 `test_default_is_medium(self)` (method)
- L93 `test_env_var_override(self, monkeypatch)` (method)
- L99 `test_env_var_unknown_falls_back(self, monkeypatch)` (method)
- L104 `test_config_openai_model(self, tmp_path)` (method)
- L113 `test_config_top_level_model(self, tmp_path)` (method) — ``image_gen.model: gpt-image-2-high`` also works (top-level).
- L127 `TestGenerate` (class)
- L128 `test_empty_prompt_rejected(self, provider)` (method)
- L133 `test_missing_api_key(self, monkeypatch)` (method)
- L139 `test_b64_saves_to_cache(self, provider, tmp_path)` (method)
- L171 `test_tier_maps_to_quality(self, provider, monkeypatch, tier, expected_quality)` (method)
- L190 `test_aspect_ratio_mapping(self, provider, aspect, expected_size)` (method)
- L199 `test_revised_prompt_passed_through(self, provider)` (method)
- L210 `test_api_error_returns_error_response(self, provider)` (method)
- L221 `test_empty_response_data(self, provider)` (method)
- L231 `test_url_response_is_cached_locally(self, provider)` (method) — OpenAI URL response (if API ever returns one) is cached locally.
- L255 `test_url_response_falls_back_to_bare_url_when_download_fails(self, provider)` (method) — Cache failure must not turn into a tool error — symmetric with xAI.
