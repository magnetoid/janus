---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/spotify/tools.py

Symbols in `plugins/spotify/tools.py`.

- L20 `_check_spotify_available()` (function)
- L27 `_spotify_client()` (function)
- L31 `_spotify_tool_error(exc: Exception)` (function)
- L39 `_coerce_limit(raw: Any, *, default: int=20, minimum: int=1, maximum: int=50)` (function)
- L47 `_coerce_bool(raw: Any, default: bool=False)` (function)
- L59 `_as_list(raw: Any)` (function)
- L67 `_describe_empty_playback(payload: Any, *, action: str)` (function)
- L89 `_handle_spotify_playback(args: dict, **kw)` (function)
- L170 `_handle_spotify_devices(args: dict, **kw)` (function)
- L187 `_handle_spotify_queue(args: dict, **kw)` (function)
- L202 `_handle_spotify_search(args: dict, **kw)` (function)
- L224 `_handle_spotify_playlists(args: dict, **kw)` (function)
- L276 `_handle_spotify_albums(args: dict, **kw)` (function)
- L295 `_handle_spotify_library(args: dict, **kw)` (function) — Unified handler for saved tracks + saved albums (formerly two tools).
