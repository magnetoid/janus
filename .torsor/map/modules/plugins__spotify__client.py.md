---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/spotify/client.py

Symbols in `plugins/spotify/client.py`.

- L17 `SpotifyError` (class) — Base Spotify tool error.
- L21 `SpotifyAuthRequiredError` (class) — Raised when the user needs to authenticate with Spotify first.
- L25 `SpotifyAPIError` (class) — Structured Spotify API failure.
- L28 `__init__(self, message: str, *, status_code: Optional[int]=None, response_body: Optional[str]=None)` (method)
- L41 `SpotifyClient` (class)
- L42 `__init__(self)` (method)
- L45 `_resolve_runtime(self, *, force_refresh: bool=False, refresh_if_expiring: bool=True)` (method)
- L55 `base_url(self)` (method)
- L58 `_headers(self)` (method)
- L64 `request(self, method: str, path: str, *, params: Optional[Dict[str, Any]]=None, json_body: Optional[Dict[str, Any]]=None, allow_retry_on_401: bool=True, empty_response: Optional[Dict[str, Any]]=None)` (method)
- L100 `_raise_api_error(self, response: httpx.Response, *, method: str, path: str)` (method)
- L113 `get_devices(self)` (method)
- L116 `transfer_playback(self, *, device_id: str, play: bool=False)` (method)
- L122 `get_playback_state(self, *, market: Optional[str]=None)` (method)
- L134 `get_currently_playing(self, *, market: Optional[str]=None)` (method)
- L146 `start_playback(self, *, device_id: Optional[str]=None, context_uri: Optional[str]=None, uris: Optional[list[str]]=None, offset: Optional[Dict[str, Any]]=None, position_ms: Optional[int]=None)` (method)
- L167 `pause_playback(self, *, device_id: Optional[str]=None)` (method)
- L170 `skip_next(self, *, device_id: Optional[str]=None)` (method)
- L173 `skip_previous(self, *, device_id: Optional[str]=None)` (method)
- L176 `seek(self, *, position_ms: int, device_id: Optional[str]=None)` (method)
- L182 `set_repeat(self, *, state: str, device_id: Optional[str]=None)` (method)
- L185 `set_shuffle(self, *, state: bool, device_id: Optional[str]=None)` (method)
- L188 `set_volume(self, *, volume_percent: int, device_id: Optional[str]=None)` (method)
- L194 `get_queue(self)` (method)
- L197 `add_to_queue(self, *, uri: str, device_id: Optional[str]=None)` (method)
- L200 `search(self, *, query: str, search_types: list[str], limit: int=10, offset: int=0, market: Optional[str]=None, include_external: Optional[str]=None)` (method)
- L219 `get_my_playlists(self, *, limit: int=20, offset: int=0)` (method)
- L222 `get_playlist(self, *, playlist_id: str, market: Optional[str]=None)` (method)
- L225 `create_playlist(self, *, name: str, public: bool=False, collaborative: bool=False, description: Optional[str]=None)` (method)
- L240 `add_playlist_items(self, *, playlist_id: str, uris: list[str], position: Optional[int]=None)` (method)
- L252 `remove_playlist_items(self, *, playlist_id: str, uris: list[str], snapshot_id: Optional[str]=None)` (method)
- L264 `update_playlist_details(self, *, playlist_id: str, name: Optional[str]=None, public: Optional[bool]=None, collaborative: Optional[bool]=None, description: Optional[str]=None)` (method)
- L280 `get_album(self, *, album_id: str, market: Optional[str]=None)` (method)
- L283 `get_album_tracks(self, *, album_id: str, limit: int=20, offset: int=0, market: Optional[str]=None)` (method)
- L290 `get_saved_tracks(self, *, limit: int=20, offset: int=0, market: Optional[str]=None)` (method)
- L293 `save_library_items(self, *, uris: list[str])` (method)
- L296 `library_contains(self, *, uris: list[str])` (method)
- L299 `get_saved_albums(self, *, limit: int=20, offset: int=0, market: Optional[str]=None)` (method)
- L302 `remove_saved_tracks(self, *, track_ids: list[str])` (method)
- L306 `remove_saved_albums(self, *, album_ids: list[str])` (method)
- L310 `get_recently_played(self, *, limit: int=20, after: Optional[int]=None, before: Optional[int]=None)` (method)
- L324 `_extract_spotify_error_detail(response: httpx.Response, *, fallback: str)` (function)
- L339 `_friendly_spotify_error_message(*, status_code: int, detail: str, method: str, path: str, retry_after: Optional[str])` (function)
- L379 `_strip_none(payload: Optional[Dict[str, Any]])` (function)
- L385 `normalize_spotify_id(value: str, expected_type: Optional[str]=None)` (function)
- L407 `normalize_spotify_uri(value: str, expected_type: Optional[str]=None)` (function)
- L423 `normalize_spotify_uris(values: Iterable[str], expected_type: Optional[str]=None)` (function)
- L434 `compact_json(data: Any)` (function)
