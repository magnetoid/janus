---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_spotify_client.py

Symbols in `tests/tools/test_spotify_client.py`.

- L11 `_FakeResponse` (class)
- L12 `__init__(self, status_code: int, payload: dict | None=None, *, text: str='', headers: dict | None=None)` (method)
- L19 `json(self)` (method)
- L25 `_StubSpotifyClient` (class)
- L26 `__init__(self, payload)` (method)
- L29 `get_currently_playing(self, *, market=None)` (method)
- L33 `test_spotify_client_retries_once_after_401(monkeypatch: pytest.MonkeyPatch)` (function)
- L67 `test_normalize_spotify_uri_accepts_urls()` (function)
- L98 `test_spotify_client_formats_friendly_api_errors(monkeypatch: pytest.MonkeyPatch, status_code: int, path: str, payload: dict, expected: str)` (function)
- L126 `test_get_currently_playing_returns_explanatory_empty_payload(monkeypatch: pytest.MonkeyPatch)` (function)
- L151 `test_spotify_playback_get_currently_playing_returns_explanatory_empty_result(monkeypatch: pytest.MonkeyPatch)` (function)
- L173 `test_library_contains_uses_generic_library_endpoint(monkeypatch: pytest.MonkeyPatch)` (function)
- L211 `test_library_remove_uses_generic_library_endpoint(monkeypatch: pytest.MonkeyPatch, method_name: str, item_key: str, item_value: list[str], expected_uris: list[str])` (function)
- L248 `test_spotify_library_tracks_list_routes_to_saved_tracks(monkeypatch: pytest.MonkeyPatch)` (function)
- L265 `test_spotify_library_albums_list_routes_to_saved_albums(monkeypatch: pytest.MonkeyPatch)` (function)
- L282 `test_spotify_library_rejects_missing_kind()` (function)
- L287 `test_spotify_playback_recently_played_action(monkeypatch: pytest.MonkeyPatch)` (function) — recently_played is now an action on spotify_playback (folded from spotify_activity).
