---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/image_generation_tool.py

Symbols in `tools/image_generation_tool.py`.

- L44 `_load_fal_client()` (function) — Lazily import fal_client and rebind the module global on first use.
- L401 `_resolve_managed_fal_gateway()` (function) — Return managed fal-queue gateway config when the user prefers the gateway
- L409 `_get_managed_fal_client(managed_gateway)` (function) — Reuse the managed FAL client so its internal httpx.Client is not leaked per call.
- L433 `_submit_fal_request(model: str, arguments: Dict[str, Any])` (function) — Submit a FAL request using direct credentials or the managed queue gateway.
- L479 `_resolve_fal_model()` (function) — Resolve the active FAL model from config.yaml (primary) or default.
- L514 `_build_fal_payload(model_id: str, prompt: str, aspect_ratio: str=DEFAULT_ASPECT_RATIO, seed: Optional[int]=None, overrides: Optional[Dict[str, Any]]=None)` (function) — Build a FAL request payload for `model_id` from unified inputs.
- L560 `_upscale_image(image_url: str, original_prompt: str)` (function) — Upscale an image using FAL.ai's Clarity Upscaler.
- L609 `_looks_like_absolute_file_path(value: str)` (function)
- L620 `_active_terminal_env(task_id: str | None)` (function)
- L630 `_agent_cache_base_for_env(env: Any)` (function)
- L665 `_agent_visible_cache_path(host_path: str, env: Any)` (function)
- L682 `_force_artifact_sync(env: Any)` (function)
- L692 `_postprocess_image_generate_result(raw: str, task_id: str | None=None)` (function) — Annotate successful local image results with backend-visible paths.
- L724 `image_generate_tool(prompt: str, aspect_ratio: str=DEFAULT_ASPECT_RATIO, num_inference_steps: Optional[int]=None, guidance_scale: Optional[float]=None, num_images: Optional[int]=None, output_format: Optional[str]=None, seed: Optional[int]=None)` (function) — Generate an image from a text prompt using the configured FAL model.
- L874 `check_fal_api_key()` (function) — True if the FAL.ai API key (direct or managed gateway) is available.
- L879 `_build_no_backend_setup_message()` (function) — Build an actionable error string when no FAL backend is reachable.
- L920 `check_image_generation_requirements()` (function) — True if any image gen backend is available.
- L1033 `_read_configured_image_model()` (function) — Return the value of ``image_gen.model`` from config.yaml, or None.
- L1048 `_read_configured_image_provider()` (function) — Return the value of ``image_gen.provider`` from config.yaml, or None.
- L1072 `_dispatch_to_plugin_provider(prompt: str, aspect_ratio: str)` (function) — Route the call to a plugin-registered provider when one is selected.
- L1151 `_handle_image_generate(args, **kw)` (function)
