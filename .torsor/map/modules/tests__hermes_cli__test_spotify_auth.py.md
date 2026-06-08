---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_spotify_auth.py

Symbols in `tests/hermes_cli/test_spotify_auth.py`.

- L10 `test_store_provider_state_can_skip_active_provider()` (function)
- L24 `test_resolve_spotify_runtime_credentials_refreshes_without_changing_active_provider(tmp_path, monkeypatch: pytest.MonkeyPatch)` (function)
- L70 `test_auth_spotify_status_command_reports_logged_in(capsys, monkeypatch: pytest.MonkeyPatch)` (function)
- L91 `test_spotify_logout_does_not_reset_model_provider(tmp_path, monkeypatch: pytest.MonkeyPatch, capsys)` (function)
- L137 `test_spotify_interactive_setup_persists_client_id(tmp_path, monkeypatch: pytest.MonkeyPatch, capsys)` (function) — The wizard writes HERMES_SPOTIFY_CLIENT_ID to .env and returns the value.
- L166 `test_spotify_interactive_setup_empty_aborts(tmp_path, monkeypatch: pytest.MonkeyPatch)` (function) — Empty input aborts cleanly instead of persisting an empty client_id.
