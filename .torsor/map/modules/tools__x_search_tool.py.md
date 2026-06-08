---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/x_search_tool.py

Symbols in `tools/x_search_tool.py`.

- L69 `_load_x_search_config()` (function)
- L78 `_get_x_search_model()` (function)
- L83 `_get_x_search_timeout_seconds()` (function)
- L92 `_get_x_search_retries()` (function)
- L105 `_resolve_xai_bearer()` (function) — Return ``(api_key, base_url, source)``.
- L127 `check_x_search_requirements()` (function) — Return True when xAI credentials are available AND valid.
- L146 `_normalize_handles(handles: Optional[List[str]], field_name: str)` (function)
- L157 `_parse_iso_date(value: str, field_name: str)` (function) — Parse a strict YYYY-MM-DD string into a ``date``.
- L176 `_validate_date_range(from_date: str, to_date: str)` (function) — Validate ``from_date`` / ``to_date`` before they reach xAI.
- L208 `_extract_response_text(payload: Dict[str, Any])` (function)
- L226 `_extract_inline_citations(payload: Dict[str, Any])` (function)
- L246 `_http_error_message(exc: requests.HTTPError)` (function)
- L274 `x_search_tool(query: str, allowed_x_handles: Optional[List[str]]=None, excluded_x_handles: Optional[List[str]]=None, from_date: str='', to_date: str='', enable_image_understanding: bool=False, enable_video_understanding: bool=False)` (function)
- L504 `_handle_x_search(args, **kw)` (function)
