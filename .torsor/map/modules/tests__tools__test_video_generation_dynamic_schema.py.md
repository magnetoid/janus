---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_video_generation_dynamic_schema.py

Symbols in `tests/tools/test_video_generation_dynamic_schema.py`.

- L15 `_reset_registry()` (function)
- L22 `cfg_home(tmp_path, monkeypatch)` (function)
- L27 `_write_cfg(home, cfg: dict)` (function)
- L31 `_BothModalitiesProvider` (class) — Supports both text-to-video AND image-to-video (the common case).
- L35 `name(self)` (method)
- L38 `is_available(self)` (method)
- L41 `list_models(self)` (method)
- L44 `default_model(self)` (method)
- L47 `capabilities(self)` (method)
- L59 `generate(self, prompt, **kwargs)` (method)
- L63 `_ImageOnlyProvider` (class) — Backend with only image-to-video support (rare but possible).
- L67 `name(self)` (method)
- L70 `is_available(self)` (method)
- L73 `list_models(self)` (method)
- L76 `default_model(self)` (method)
- L79 `capabilities(self)` (method)
- L82 `generate(self, prompt, **kwargs)` (method)
- L86 `TestDynamicSchemaBuilder` (class)
- L87 `test_no_config_says_so(self, cfg_home)` (method)
- L94 `test_does_not_mention_edit_or_extend(self, cfg_home)` (method) — The simplified surface only does text→video and image→video.
- L109 `test_both_modalities_advertises_auto_routing(self, cfg_home)` (method)
- L129 `test_image_only_model_warns_about_required_image_url(self, cfg_home)` (method)
- L146 `test_builder_wired_into_registry(self)` (method)
