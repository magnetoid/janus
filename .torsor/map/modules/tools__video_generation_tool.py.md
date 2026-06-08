---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/video_generation_tool.py

Symbols in `tools/video_generation_tool.py`.

- L168 `_read_video_gen_section()` (function)
- L180 `_read_configured_video_provider()` (function)
- L187 `_read_configured_video_model()` (function)
- L199 `check_video_generation_requirements()` (function) — Return True when at least one registered provider reports available.
- L226 `_resolve_active_provider()` (function) — Return the active provider object or None.
- L247 `_missing_provider_error(configured: Optional[str])` (function)
- L273 `_coerce_int(value: Any)` (function)
- L282 `_coerce_bool(value: Any)` (function)
- L296 `_normalize_reference_images(value: Any)` (function)
- L310 `_handle_video_generate(args: Dict[str, Any], **_kw: Any)` (function)
- L428 `_format_model_caveats(model_meta: Dict[str, Any], backend_caps: Dict[str, Any])` (function) — Pull human-readable caveats out of one model's catalog metadata.
- L457 `_build_dynamic_video_schema()` (function) — Build a description that reflects the active backend's actual surface.
