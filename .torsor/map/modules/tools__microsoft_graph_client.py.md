---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/microsoft_graph_client.py

Symbols in `tools/microsoft_graph_client.py`.

- L18 `MicrosoftGraphClientError` (class) — Base class for Graph client failures.
- L22 `MicrosoftGraphAPIError` (class) — Raised when a Graph API request fails.
- L25 `__init__(self, status_code: int, method: str, url: str, message: str, *, retry_after_seconds: float | None=None, payload: Any=None)` (method)
- L45 `MicrosoftGraphClient` (class) — Minimal async Microsoft Graph client with retries and pagination.
- L48 `__init__(self, token_provider: MicrosoftGraphTokenProvider, *, base_url: str=DEFAULT_GRAPH_BASE_URL, timeout: float=60.0, max_retries: int=3, transport: httpx.AsyncBaseTransport | None=None, sleep: Callable[[float], Awaitable[None]] | None=None, user_agent: str='Hermes-Agent/graph-client')` (method)
- L68 `from_env(cls, **kwargs: Any)` (method)
- L73 `get_json(self, path: str, *, params: dict[str, Any] | None=None, headers: dict[str, str] | None=None)` (method)
- L83 `post_json(self, path: str, *, json_body: Any | None=None, headers: dict[str, str] | None=None)` (method)
- L93 `patch_json(self, path: str, *, json_body: Any | None=None, headers: dict[str, str] | None=None)` (method)
- L105 `delete(self, path: str, *, headers: dict[str, str] | None=None)` (method)
- L116 `iterate_pages(self, path: str, *, params: dict[str, Any] | None=None, headers: dict[str, str] | None=None)` (method)
- L141 `collect_paginated(self, path: str, *, params: dict[str, Any] | None=None, headers: dict[str, str] | None=None)` (method)
- L155 `download_to_file(self, path: str, destination: str | Path, *, headers: dict[str, str] | None=None, chunk_size: int=65536)` (method) — Download a Graph resource to disk, streaming the response body.
- L259 `_request(self, method: str, path_or_url: str, *, params: dict[str, Any] | None=None, json_body: Any | None=None, headers: dict[str, str] | None=None)` (method)
- L331 `_resolve_url(self, path_or_url: str)` (method)
- L338 `_decode_json(response: httpx.Response)` (method)
- L348 `_should_retry(response: httpx.Response | None)` (method)
- L354 `_should_refresh_token(error: Exception | None)` (method)
- L358 `_retry_delay(response: httpx.Response | None, attempt: int)` (method)
- L369 `_build_api_error(method: str, url: str, response: httpx.Response)` (method)
