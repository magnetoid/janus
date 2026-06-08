---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/image_gen/test_xai_provider.py

Symbols in `tests/plugins/image_gen/test_xai_provider.py`.

- L19 `_fake_api_key(monkeypatch)` (function) — Ensure XAI_API_KEY is set for all tests.
- L29 `TestXAIImageGenProvider` (class)
- L30 `test_name(self)` (method)
- L36 `test_display_name(self)` (method)
- L42 `test_is_available_with_key(self, monkeypatch)` (method)
- L49 `test_is_available_without_key(self, monkeypatch)` (method)
- L56 `test_list_models(self)` (method)
- L64 `test_default_model(self)` (method)
- L70 `test_get_setup_schema(self)` (method)
- L89 `TestConfig` (class)
- L90 `test_default_model(self)` (method)
- L96 `test_default_resolution(self)` (method)
- L101 `test_custom_model(self, monkeypatch)` (method)
- L114 `TestGenerate` (class)
- L115 `test_missing_api_key(self, monkeypatch)` (method)
- L124 `test_successful_generation(self)` (method)
- L144 `test_successful_url_response(self)` (method) — xAI URL response is cached locally — #26942 contract.
- L184 `test_url_response_falls_back_to_bare_url_when_download_fails(self)` (method) — If caching the URL fails (network blip, 404 in-flight), the
- L215 `test_api_error(self)` (method)
- L232 `test_api_error_preserves_real_response_status(self)` (method)
- L253 `test_timeout(self)` (method)
- L265 `test_empty_response(self)` (method)
- L280 `test_auth_header(self)` (method)
- L299 `test_payload_resolution_is_literal_1k_or_2k(self)` (method) — Regression: xAI API rejects numeric resolutions ("1024"/"2048") with 422.
- L327 `TestRegistration` (class)
- L328 `test_register(self)` (method)
