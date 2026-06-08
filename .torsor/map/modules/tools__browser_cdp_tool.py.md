---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/browser_cdp_tool.py

Symbols in `tools/browser_cdp_tool.py`.

- L50 `_run_async(coro)` (function) — Run an async coroutine from a sync handler, safe inside or outside a loop.
- L71 `_resolve_cdp_endpoint()` (function) — Return the normalized CDP WebSocket URL, or empty string if unavailable.
- L94 `_cdp_call(ws_url: str, method: str, params: Dict[str, Any], target_id: Optional[str], timeout: float)` (function) — Make a single CDP call, optionally attaching to a target first.
- L190 `_browser_cdp_via_supervisor(task_id: str, frame_id: str, method: str, params: Optional[Dict[str, Any]], timeout: float)` (function) — Route a CDP call through the live supervisor session for an OOPIF frame.
- L300 `browser_cdp(method: str, params: Optional[Dict[str, Any]]=None, target_id: Optional[str]=None, frame_id: Optional[str]=None, timeout: float=30.0, task_id: Optional[str]=None)` (function) — Send a raw CDP command.  See ``CDP_DOCS_URL`` for method documentation.
- L525 `_browser_cdp_check()` (function) — Availability check for browser_cdp.
