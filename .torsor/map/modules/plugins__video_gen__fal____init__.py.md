---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/video_gen/fal/__init__.py

Symbols in `plugins/video_gen/fal/__init__.py`.

- L169 `_is_duration_range(durations: Any)` (function) — Heuristic: a 2-tuple of ints with a gap > 1 is treated as ``(min, max)``.
- L178 `_clamp_duration(family: Dict[str, Any], duration: Optional[int])` (function)
- L198 `_load_video_gen_section()` (function)
- L210 `_resolve_family(explicit: Optional[str])` (function) — Decide which FAL family to use. Returns ``(family_id, meta)``.
- L237 `_build_payload(family: Dict[str, Any], *, prompt: str, image_url: Optional[str], duration: Optional[int], aspect_ratio: str, resolution: str, negative_prompt: Optional[str], audio: Optional[bool], seed: Optional[int])` (function) — Build a family-specific payload, dropping keys the family doesn't declare.
- L296 `_load_fal_client()` (function) — Lazy-load the ``fal_client`` SDK and cache it on this module.
- L319 `_resolve_managed_fal_video_gateway()` (function) — Return managed fal-queue gateway config when the user prefers the gateway
- L331 `_get_managed_fal_video_client(managed_gateway)` (function) — Reuse the managed FAL client so its internal httpx.Client is not leaked per call.
- L354 `_submit_fal_video_request(endpoint: str, arguments: Dict[str, Any])` (function) — Submit a FAL video request using direct credentials or the managed queue gateway.
- L387 `_check_fal_video_available()` (function) — True if the FAL.ai video backend is reachable (direct key or managed gateway).
- L401 `FALVideoGenProvider` (class) — FAL.ai multi-family video generation backend.
- L409 `name(self)` (method)
- L413 `display_name(self)` (method)
- L416 `is_available(self)` (method)
- L422 `list_models(self)` (method)
- L441 `default_model(self)` (method)
- L444 `get_setup_schema(self)` (method)
- L458 `capabilities(self)` (method)
- L470 `generate(self, prompt: str, *, model: Optional[str]=None, image_url: Optional[str]=None, reference_image_urls: Optional[List[str]]=None, duration: Optional[int]=None, aspect_ratio: str='16:9', resolution: str='720p', negative_prompt: Optional[str]=None, audio: Optional[bool]=None, seed: Optional[int]=None, **kwargs: Any)` (method)
- L611 `register(ctx)` (function) — Plugin entry point — wire ``FALVideoGenProvider`` into the registry.
