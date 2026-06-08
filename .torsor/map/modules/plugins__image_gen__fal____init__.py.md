---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/image_gen/fal/__init__.py

Symbols in `plugins/image_gen/fal/__init__.py`.

- L40 `FalImageGenProvider` (class) — FAL.ai image generation backend.
- L51 `name(self)` (method)
- L55 `display_name(self)` (method)
- L58 `is_available(self)` (method)
- L69 `list_models(self)` (method)
- L82 `default_model(self)` (method)
- L86 `get_setup_schema(self)` (method)
- L100 `generate(self, prompt: str, aspect_ratio: str=DEFAULT_ASPECT_RATIO, **kwargs: Any)` (method) — Generate an image via the legacy FAL pipeline.
- L180 `register(ctx)` (function) — Plugin entry point — wire ``FalImageGenProvider`` into the registry.
