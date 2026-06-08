---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/video_gen/test_xai_plugin_integration.py

Symbols in `tests/plugins/video_gen/test_xai_plugin_integration.py`.

- L20 `_reset_registry()` (function)
- L26 `_FakeResponse` (class)
- L27 `__init__(self, status: int=200, payload: Optional[Dict[str, Any]]=None)` (method)
- L32 `raise_for_status(self)` (method)
- L37 `json(self)` (method)
- L41 `_FakeAsyncClient` (class)
- L42 `__init__(self)` (method)
- L45 `__aenter__(self)` (method)
- L48 `__aexit__(self, *args)` (method)
- L51 `post(self, url, headers=None, json=None, timeout=None)` (method)
- L55 `get(self, url, headers=None, timeout=None)` (method)
- L64 `xai_provider(monkeypatch)` (function)
- L86 `_last_post(captured)` (function)
- L90 `TestXAIEndpoint` (class) — xAI uses one endpoint — ``/videos/generations`` — for both modes.
- L93 `test_text_to_video_hits_generations(self, xai_provider)` (method)
- L100 `test_image_to_video_hits_generations(self, xai_provider)` (method)
- L111 `TestXAIPayload` (class)
- L112 `test_text_payload_has_no_image_field(self, xai_provider)` (method)
- L121 `test_image_payload_has_image_field(self, xai_provider)` (method)
- L128 `test_local_image_path_is_sent_as_data_uri(self, xai_provider, tmp_path)` (method)
- L139 `test_explicit_model_override_is_honored_for_image(self, xai_provider)` (method)
- L150 `test_reference_images_payload(self, xai_provider)` (method)
- L166 `TestXAIValidation` (class)
- L167 `test_missing_prompt_rejects(self, xai_provider)` (method)
- L175 `test_image_plus_refs_rejects(self, xai_provider)` (method)
- L186 `test_too_many_references_rejects(self, xai_provider)` (method)
- L196 `TestXAIClamping` (class)
- L197 `test_duration_clamped_to_15(self, xai_provider)` (method)
- L202 `test_duration_clamped_when_refs_present(self, xai_provider)` (method)
- L212 `test_invalid_aspect_ratio_soft_clamps(self, xai_provider)` (method)
