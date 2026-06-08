---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/proxy/server.py

Symbols in `hermes_cli/proxy/server.py`.

- L55 `_json_error(status: int, message: str, code: str='proxy_error')` (function) — Return an OpenAI-style error JSON response.
- L61 `_filter_request_headers(headers: 'aiohttp.typedefs.LooseHeaders')` (function) — Strip hop-by-hop + auth headers from the inbound request.
- L71 `_filter_response_headers(headers)` (function) — Strip hop-by-hop headers from the upstream response.
- L84 `create_app(adapter: UpstreamAdapter)` (function) — Build the aiohttp application bound to a specific upstream adapter.
- L243 `run_server(adapter: UpstreamAdapter, host: str=DEFAULT_HOST, port: int=DEFAULT_PORT, shutdown_event: Optional[asyncio.Event]=None)` (function) — Run the proxy in the current event loop until shutdown_event is set.
