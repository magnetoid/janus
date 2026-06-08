---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/image_gen/test_fal_provider.py

Symbols in `tests/plugins/image_gen/test_fal_provider.py`.

- L26 `TestFalImageGenProviderSurface` (class)
- L27 `test_name(self)` (method)
- L32 `test_display_name(self)` (method)
- L37 `test_default_model_matches_legacy(self)` (method)
- L43 `test_list_models_uses_legacy_catalog(self)` (method)
- L57 `test_setup_schema_advertises_fal_key(self)` (method)
- L67 `TestFalImageGenProviderAvailability` (class)
- L68 `test_is_available_when_legacy_check_passes(self, monkeypatch)` (method)
- L75 `test_is_available_false_when_legacy_check_fails(self, monkeypatch)` (method)
- L82 `test_is_available_handles_legacy_exception(self, monkeypatch)` (method)
- L99 `TestFalImageGenProviderGenerate` (class)
- L100 `test_generate_delegates_to_legacy_image_generate_tool(self, monkeypatch)` (method) — Plugin must look up ``image_generate_tool`` at call time so
- L136 `test_generate_invalid_aspect_ratio_is_coerced(self, monkeypatch)` (method)
- L154 `test_generate_passthrough_drops_none_kwargs(self, monkeypatch)` (method)
- L182 `test_generate_catches_exception_from_legacy(self, monkeypatch)` (method)
- L197 `test_generate_invalid_json_response(self, monkeypatch)` (method)
- L216 `TestFalImageGenPluginRegistration` (class)
- L217 `test_register_wires_provider_into_registry(self)` (method)
