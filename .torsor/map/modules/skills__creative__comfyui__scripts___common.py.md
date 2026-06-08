---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# skills/creative/comfyui/scripts/_common.py

Symbols in `skills/creative/comfyui/scripts/_common.py`.

- L102 `folder_aliases_for(folder: str)` (function) — Return the search order of folder names (primary first).
- L335 `is_cloud_host(host: str)` (function) — True if the host points at Comfy Cloud (or staging/preview subdomain).
- L344 `build_cloud_aware_url(base: str, path: str, *, force_cloud: bool | None=None)` (function) — Build a URL that adds /api prefix when targeting Comfy Cloud.
- L362 `cloud_endpoint(path: str)` (function) — Map a cloud endpoint path to its current canonical form.
- L379 `resolve_url(base: str, path: str, *, is_cloud: bool | None=None)` (function) — Top-level URL resolver. Applies cloud rename + /api prefix as needed.
- L391 `resolve_api_key(explicit: str | None)` (function) — Look up API key from CLI flag → env var. Strips whitespace and quotes.
- L405 `HTTPResponse` (class)
- L411 `text(self, encoding: str='utf-8')` (method)
- L414 `json(self)` (method)
- L418 `_sleep_backoff(attempt: int, base: float=RETRY_BASE_DELAY, cap: float=RETRY_MAX_DELAY)` (function) — Sleep with full-jitter exponential backoff.
- L425 `http_request(method: str, url: str, *, headers: dict[str, str] | None=None, json_body: Any=None, data: bytes | None=None, files: dict | None=None, form: dict | None=None, timeout: float=DEFAULT_HTTP_TIMEOUT, follow_redirects: bool=True, retries: int=DEFAULT_RETRIES, stream: bool=False, sink: Path | None=None)` (function) — Single entry point for all HTTP traffic.
- L523 `_http_once(*, method: str, url: str, headers: dict[str, str], json_body: Any, data: bytes | None, files: dict | None, form: dict | None, timeout: float, follow_redirects: bool, stream: bool, sink: Path | None)` (function) — One HTTP attempt. No retry.
- L631 `http_get(url: str, **kwargs: Any)` (function)
- L635 `http_post(url: str, **kwargs: Any)` (function)
- L643 `is_api_format(workflow: Any)` (function) — API format = top-level dict where each value has `class_type`.
- L655 `unwrap_workflow(payload: Any)` (function) — Unwrap common wrapper variants. Returns API-format workflow or raises ValueError.
- L674 `is_link(value: Any)` (function) — True if `value` is a [node_id, output_index] connection (length-2 list).
- L684 `iter_nodes(workflow: dict)` (function) — Yield (node_id, node) for each valid API-format node.
- L691 `iter_model_deps(workflow: dict)` (function) — Yield {node_id, class_type, field, value, folder} for each model dependency.
- L710 `iter_embedding_refs(workflow: dict)` (function) — Yield (node_id, embedding_name) for every embedding mention in prompts.
- L727 `safe_path_join(base: Path, *parts: str)` (function) — Join paths, raising if the result escapes `base`.
- L744 `media_type_from_filename(filename: str)` (function)
- L757 `looks_like_video_workflow(workflow: dict)` (function) — Used to bump default timeout for video workflows.
- L776 `coerce_seed(value: Any)` (function) — Convert -1 or None to a fresh random seed; otherwise return int(value).
- L796 `parse_model_list(payload: Any)` (function) — Normalize model-list responses from local ComfyUI vs Comfy Cloud.
- L819 `new_client_id()` (function)
- L823 `fmt_kv(d: dict)` (function) — Pretty key=value for log lines.
- L828 `emit_json(obj: Any, *, indent: int=2)` (function) — Print JSON to stdout. Centralised so behavior can be tweaked (e.g., --raw).
- L833 `log(msg: str)` (function) — stderr log with consistent prefix (so JSON stdout stays clean).
