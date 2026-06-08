---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/video_gen_provider.py

Symbols in `agent/video_gen_provider.py`.

- L75 `VideoGenProvider` (class) — Abstract base class for a video generation backend.
- L84 `name(self)` (method) — Stable short identifier used in ``video_gen.provider`` config.
- L91 `display_name(self)` (method) — Human-readable label shown in ``hermes tools``. Defaults to ``name.title()``.
- L95 `is_available(self)` (method) — Return True when this provider can service calls.
- L103 `list_models(self)` (method) — Return catalog entries for ``hermes tools`` model picker.
- L122 `get_setup_schema(self)` (method) — Return provider metadata for the ``hermes tools`` picker.
- L131 `default_model(self)` (method) — Return the default model id, or None if not applicable.
- L138 `capabilities(self)` (method) — Return what this provider supports.
- L169 `generate(self, prompt: str, *, model: Optional[str]=None, image_url: Optional[str]=None, reference_image_urls: Optional[List[str]]=None, duration: Optional[int]=None, aspect_ratio: str=DEFAULT_ASPECT_RATIO, resolution: str=DEFAULT_RESOLUTION, negative_prompt: Optional[str]=None, audio: Optional[bool]=None, seed: Optional[int]=None, **kwargs: Any)` (method) — Generate a video from a prompt (text-to-video) or animate an image
- L204 `_videos_cache_dir()` (function) — Return ``$HERMES_HOME/cache/videos/``, creating parents as needed.
- L213 `save_b64_video(b64_data: str, *, prefix: str='video', extension: str='mp4')` (function) — Decode base64 video data and write under ``$HERMES_HOME/cache/videos/``.
- L233 `save_bytes_video(raw: bytes, *, prefix: str='video', extension: str='mp4')` (function) — Write raw video bytes (e.g. an HTTP download body) to the cache.
- L247 `success_response(*, video: str, model: str, prompt: str, modality: str='text', aspect_ratio: str='', duration: int=0, provider: str, extra: Optional[Dict[str, Any]]=None)` (function) — Build a uniform success response dict.
- L280 `error_response(*, error: str, error_type: str='provider_error', provider: str='', model: str='', prompt: str='', aspect_ratio: str='')` (function) — Build a uniform error response dict.
