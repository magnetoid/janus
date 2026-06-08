---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/video_gen/test_xai_plugin.py

Symbols in `tests/plugins/video_gen/test_xai_plugin.py`.

- L11 `_reset_registry()` (function)
- L17 `test_xai_provider_registers()` (function)
- L28 `test_xai_provider_lists_text_and_current_image_video_models()` (function)
- L40 `test_xai_routes_default_models_by_modality()` (function)
- L65 `test_xai_capabilities_text_and_image_only()` (function) — xAI was previously advertised with edit/extend operations. The
- L78 `test_xai_unavailable_without_key(monkeypatch)` (function)
- L85 `test_xai_generate_requires_xai_key(monkeypatch)` (function)
- L94 `test_xai_available_with_oauth_only(monkeypatch)` (function) — The plugin must honour xAI Grok OAuth credentials, not just
- L115 `test_xai_resolved_credentials_threaded_through_request(monkeypatch)` (function) — OAuth-resolved creds must reach the HTTP layer — bug class where
- L138 `test_xai_no_operation_kwarg()` (function) — The ABC's generate() signature no longer accepts 'operation'.
