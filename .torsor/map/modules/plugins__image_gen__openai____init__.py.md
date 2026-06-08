---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/image_gen/openai/__init__.py

Symbols in `plugins/image_gen/openai/__init__.py`.

- L83 `_load_openai_config()` (function) — Read ``image_gen`` from config.yaml (returns {} on any failure).
- L96 `_resolve_model()` (function) — Decide which tier to use and return ``(model_id, meta)``.
- L125 `OpenAIImageGenProvider` (class) — OpenAI ``images.generate`` backend — gpt-image-2 at low/medium/high.
- L129 `name(self)` (method)
- L133 `display_name(self)` (method)
- L136 `is_available(self)` (method)
- L145 `list_models(self)` (method)
- L157 `default_model(self)` (method)
- L160 `get_setup_schema(self)` (method)
- L174 `generate(self, prompt: str, aspect_ratio: str=DEFAULT_ASPECT_RATIO, **kwargs: Any)` (method)
- L314 `register(ctx)` (function) — Plugin entry point — wire ``OpenAIImageGenProvider`` into the registry.
