---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_video_generation_dispatch.py

Symbols in `tests/tools/test_video_generation_dispatch.py`.

- L15 `_reset_registry()` (function)
- L21 `_RecordingProvider` (class) — Captures the kwargs the tool layer hands it.
- L24 `__init__(self, name: str='fake')` (method)
- L29 `name(self)` (method)
- L32 `list_models(self)` (method)
- L35 `default_model(self)` (method)
- L38 `generate(self, prompt, **kwargs)` (method)
- L53 `_RaisingProvider` (class)
- L55 `name(self)` (method)
- L58 `generate(self, prompt, **kwargs)` (method)
- L62 `TestUnifiedDispatch` (class)
- L63 `_run(self, args: Dict[str, Any], *, configured: Optional[str]=None)` (method)
- L78 `test_no_provider_returns_clear_error(self)` (method)
- L83 `test_unknown_provider_returns_clear_error(self)` (method)
- L88 `test_text_to_video_routes_without_image_url(self)` (method)
- L98 `test_image_to_video_routes_with_image_url(self)` (method)
- L109 `test_prompt_required(self)` (method)
- L116 `test_provider_exception_caught(self)` (method)
- L122 `test_operation_field_not_in_schema(self)` (method) — Make sure we removed the operation field from the schema.
