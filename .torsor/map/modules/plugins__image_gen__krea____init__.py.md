---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/image_gen/krea/__init__.py

Symbols in `plugins/image_gen/krea/__init__.py`.

- L105 `_load_krea_config()` (function) — Read ``image_gen.krea`` (with fallthrough to ``image_gen``) from config.yaml.
- L118 `_resolve_model()` (function) — Decide which model to use and return ``(model_id, meta)``.
- L142 `_resolve_creativity(value: Optional[str])` (function) — Coerce ``creativity`` kwarg to a valid Krea value (default ``medium``).
- L161 `KreaImageGenProvider` (class) — Krea ``Krea 2`` foundation image model backend (Medium + Large).
- L165 `name(self)` (method)
- L169 `display_name(self)` (method)
- L172 `is_available(self)` (method)
- L175 `list_models(self)` (method)
- L187 `default_model(self)` (method)
- L190 `get_setup_schema(self)` (method)
- L208 `generate(self, prompt: str, aspect_ratio: str=DEFAULT_ASPECT_RATIO, **kwargs: Any)` (method)
- L546 `register(ctx)` (function) — Plugin entry point — wire ``KreaImageGenProvider`` into the registry.
