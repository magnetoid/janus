---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/browser_connect.py

Symbols in `hermes_cli/browser_connect.py`.

- L73 `get_chrome_debug_candidates(system: str)` (function)
- L123 `chrome_debug_data_dir()` (function)
- L127 `_chrome_debug_args(port: int)` (function)
- L136 `is_browser_debug_ready(url: str, timeout: float=1.0)` (function) — Return True when ``url`` exposes a reachable Chrome DevTools endpoint.
- L172 `manual_chrome_debug_command(port: int=DEFAULT_BROWSER_CDP_PORT, system: str | None=None)` (function)
- L190 `_detach_kwargs(system: str)` (function)
- L199 `try_launch_chrome_debug(port: int=DEFAULT_BROWSER_CDP_PORT, system: str | None=None)` (function)
