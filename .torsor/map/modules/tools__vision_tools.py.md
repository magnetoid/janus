---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/vision_tools.py

Symbols in `tools/vision_tools.py`.

- L53 `_resolve_download_timeout()` (function)
- L77 `_image_url_shape_ok(url: str)` (function) — HTTP(S) shape check only (scheme, netloc). No DNS.
- L92 `_validate_image_url(url: str)` (function) — Validate image URL for sync callers and tests (SSRF via sync DNS check).
- L101 `_validate_image_url_async(url: str)` (function) — Validate remote image URL without blocking the event loop on DNS.
- L109 `_detect_image_mime_type(image_path: Path)` (function) — Return a MIME type when the file looks like a supported image.
- L131 `_is_retryable_download_error(error: Exception)` (function) — Return True only for transient image-download failures worth retrying.
- L155 `_download_image(image_url: str, destination: Path, max_retries: int=3)` (function) — Download an image from a URL to a local destination (async) with retry logic.
- L266 `_determine_mime_type(image_path: Path)` (function) — Determine the MIME type of an image based on its file extension.
- L289 `_image_to_base64_data_url(image_path: Path, mime_type: Optional[str]=None)` (function) — Convert an image file to a base64-encoded data URL.
- L344 `_is_image_size_error(error: Exception)` (function) — Detect if an API error is related to image or payload size.
- L354 `_image_exceeds_dimension(image_path: Path, max_dimension: int)` (function) — True if the image's longest side exceeds ``max_dimension`` px.
- L372 `_resize_image_for_vision(image_path: Path, mime_type: Optional[str]=None, max_base64_bytes: int=_RESIZE_TARGET_BYTES, max_dimension: Optional[int]=None)` (function) — Convert an image to a base64 data URL, auto-resizing if too large.
- L531 `_supports_media_in_tool_results(provider: str, model: str)` (function) — Whether the given provider+model combination accepts image content
- L603 `_should_use_native_vision_fast_path()` (function) — Whether vision tools should attach the image to the main model directly
- L633 `_build_native_vision_tool_result(image_url: str, question: str, image_data_url: str, image_size_bytes: int)` (function) — Build the multimodal tool-result envelope returned by the fast path.
- L688 `_vision_analyze_native(image_url: str, question: str)` (function) — Fast path for vision-capable main models.
- L801 `vision_analyze_tool(image_url: str, user_prompt: str, model: str=None)` (function) — Analyze an image from a URL or local file path using vision AI.
- L1084 `check_vision_requirements()` (function) — Check if the configured runtime vision path can resolve a client.
- L1197 `_handle_vision_analyze(args: Dict[str, Any], **kw: Any)` (function)
- L1250 `_detect_video_mime_type(video_path: Path)` (function) — Return a video MIME type based on file extension, or None if unsupported.
- L1256 `_video_to_base64_data_url(video_path: Path, mime_type: Optional[str]=None)` (function) — Convert a video file to a base64-encoded data URL.
- L1264 `_download_video(video_url: str, destination: Path, max_retries: int=3)` (function) — Download video from URL with SSRF protection and retry.
- L1338 `video_analyze_tool(video_url: str, user_prompt: str, model: str=None)` (function) — Analyze a video via multimodal LLM. Returns JSON {success, analysis}.
- L1571 `_handle_video_analyze(args: Dict[str, Any], **kw: Any)` (function)
