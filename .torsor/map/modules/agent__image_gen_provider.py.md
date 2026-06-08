---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/image_gen_provider.py

Symbols in `agent/image_gen_provider.py`.

- L51 `ImageGenProvider` (class) — Abstract base class for an image generation backend.
- L60 `name(self)` (method) — Stable short identifier used in ``image_gen.provider`` config.
- L67 `display_name(self)` (method) — Human-readable label shown in ``hermes tools``. Defaults to ``name.title()``.
- L71 `is_available(self)` (method) — Return True when this provider can service calls.
- L79 `list_models(self)` (method) — Return catalog entries for ``hermes tools`` model picker.
- L96 `get_setup_schema(self)` (method) — Return provider metadata for the ``hermes tools`` picker.
- L123 `default_model(self)` (method) — Return the default model id, or None if not applicable.
- L131 `generate(self, prompt: str, aspect_ratio: str=DEFAULT_ASPECT_RATIO, **kwargs: Any)` (method) — Generate an image.
- L151 `resolve_aspect_ratio(value: Optional[str])` (function) — Clamp an aspect_ratio value to the valid set, defaulting to landscape.
- L165 `_images_cache_dir()` (function) — Return ``$HERMES_HOME/cache/images/``, creating parents as needed.
- L174 `save_b64_image(b64_data: str, *, prefix: str='image', extension: str='png')` (function) — Decode base64 image data and write it under ``$HERMES_HOME/cache/images/``.
- L207 `save_url_image(url: str, *, prefix: str='image', timeout: float=60.0, max_bytes: int=25 * 1024 * 1024)` (function) — Download an image URL and write it under ``$HERMES_HOME/cache/images/``.
- L276 `success_response(*, image: str, model: str, prompt: str, aspect_ratio: str, provider: str, extra: Optional[Dict[str, Any]]=None)` (function) — Build a uniform success response dict.
- L305 `error_response(*, error: str, error_type: str='provider_error', provider: str='', model: str='', prompt: str='', aspect_ratio: str=DEFAULT_ASPECT_RATIO)` (function) — Build a uniform error response dict.
