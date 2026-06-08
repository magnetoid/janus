---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/image_gen/xai/__init__.py

Symbols in `plugins/image_gen/xai/__init__.py`.

- L80 `_load_xai_config()` (function) — Read ``image_gen.xai`` from config.yaml.
- L94 `_resolve_model()` (function) — Decide which model to use and return ``(model_id, meta)``.
- L108 `_resolve_resolution()` (function) — Get configured resolution.
- L122 `XAIImageGenProvider` (class) — xAI ``grok-imagine-image`` backend.
- L126 `name(self)` (method)
- L130 `display_name(self)` (method)
- L133 `is_available(self)` (method)
- L137 `list_models(self)` (method)
- L148 `get_setup_schema(self)` (method)
- L161 `generate(self, prompt: str, aspect_ratio: str=DEFAULT_ASPECT_RATIO, **kwargs: Any)` (method) — Generate an image using xAI's grok-imagine-image.
- L332 `register(ctx: Any)` (function) — Register this provider with the image gen registry.
