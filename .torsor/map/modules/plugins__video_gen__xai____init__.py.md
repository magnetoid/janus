---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/video_gen/xai/__init__.py

Symbols in `plugins/video_gen/xai/__init__.py`.

- L86 `_resolve_xai_credentials()` (function) — Return ``(api_key, base_url)`` from the shared xAI credential resolver.
- L110 `_xai_user_agent()` (function)
- L119 `_xai_headers(api_key: str)` (function)
- L127 `_image_ref_to_xai_url(value: str)` (function) — Return a URL/data URI accepted by xAI for image inputs.
- L148 `_normalize_reference_images(reference_image_urls: Optional[List[str]])` (function)
- L157 `_clamp_duration(duration: Optional[int], has_reference_images: bool)` (function)
- L168 `_resolve_model_for_modality(model: Optional[str], *, modality: str, explicit_model: bool)` (function) — Select xAI's text/video model without treating config as a prompt override.
- L190 `_submit(client: httpx.AsyncClient, payload: Dict[str, Any], *, api_key: str, base_url: str)` (function) — POST to /videos/generations — xAI's only public endpoint for our
- L213 `_poll(client: httpx.AsyncClient, request_id: str, *, api_key: str, base_url: str, timeout_seconds: int, poll_interval: int)` (function)
- L250 `XAIVideoGenProvider` (class) — xAI Grok Imagine video backend (text-to-video + image-to-video).
- L254 `name(self)` (method)
- L258 `display_name(self)` (method)
- L261 `is_available(self)` (method)
- L265 `list_models(self)` (method)
- L268 `default_model(self)` (method)
- L271 `get_setup_schema(self)` (method)
- L286 `capabilities(self)` (method)
- L298 `generate(self, prompt: str, *, model: Optional[str]=None, image_url: Optional[str]=None, reference_image_urls: Optional[List[str]]=None, duration: Optional[int]=None, aspect_ratio: str=DEFAULT_ASPECT_RATIO, resolution: str=DEFAULT_RESOLUTION, negative_prompt: Optional[str]=None, audio: Optional[bool]=None, seed: Optional[int]=None, **kwargs: Any)` (method)
- L339 `_generate_async(self, *, prompt: str, model: Optional[str], explicit_model: bool, image_url: Optional[str], reference_image_urls: Optional[List[str]], duration: Optional[int], aspect_ratio: str, resolution: str)` (method)
- L502 `register(ctx)` (function) — Plugin entry point — wire ``XAIVideoGenProvider`` into the registry.
