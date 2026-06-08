---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_video_generation_tool_surface_matrix.py

Symbols in `tests/tools/test_video_generation_tool_surface_matrix.py`.

- L26 `_reset_registry()` (function)
- L34 `matrix_env(tmp_path, monkeypatch)` (function) — Set up HERMES_HOME, stub fal_client + httpx, force plugin discovery.
- L103 `_invoke_tool(home, cfg: dict, args: dict)` (function) — Write config, invoke the registered tool handler, return parsed JSON.
- L124 `_all_fal_families()` (function)
- L130 `test_fal_text_only_routes_to_text_endpoint(matrix_env, family_id)` (function)
- L156 `test_fal_text_plus_image_routes_to_image_endpoint(matrix_env, family_id)` (function)
- L190 `test_xai_text_only_via_tool_surface(matrix_env)` (function)
- L210 `test_xai_text_plus_image_via_tool_surface(matrix_env)` (function)
- L229 `test_xai_explicit_model_override_via_tool_surface(matrix_env)` (function)
- L252 `test_tool_model_arg_overrides_config(matrix_env)` (function) — When the tool call passes model=, it wins over video_gen.model in config.
- L269 `test_tool_model_arg_with_image_url_routes_to_override_image_endpoint(matrix_env)` (function) — model= override on text+image goes to the override family's image endpoint.
