---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/skills/test_google_workspace_api.py

Symbols in `tests/skills/test_google_workspace_api.py`.

- L26 `bridge_module(monkeypatch, tmp_path)` (function)
- L39 `api_module(monkeypatch, tmp_path)` (function)
- L57 `_write_token(path: Path, *, token='ya29.test', expiry=None, **extra)` (function)
- L71 `test_bridge_returns_valid_token(bridge_module, tmp_path)` (function) — Non-expired token is returned without refresh.
- L81 `test_bridge_refreshes_expired_token(bridge_module, tmp_path)` (function) — Expired token triggers a refresh via token_uri.
- L105 `test_bridge_refresh_passes_timeout_to_urlopen(bridge_module)` (function) — Token refresh must pass an explicit timeout so a hung Google endpoint
- L131 `test_bridge_refresh_exits_cleanly_on_network_error(bridge_module)` (function) — URLError/timeout during refresh exits 1 with a readable message
- L150 `test_bridge_exits_on_missing_token(bridge_module)` (function) — Missing token file causes exit with code 1.
- L156 `test_bridge_main_injects_token_env(bridge_module, tmp_path)` (function) — main() sets GOOGLE_WORKSPACE_CLI_TOKEN in subprocess env.
- L178 `test_api_calendar_list_uses_events_list(api_module)` (function) — calendar_list calls _run_gws with events list + params.
- L206 `test_api_calendar_list_respects_date_range(api_module)` (function) — calendar list with --start/--end passes correct time bounds.
- L239 `test_api_gmail_get_reads_headers_case_insensitively(api_module, capsys, header_names)` (function)
- L279 `test_api_gmail_search_reads_headers_case_insensitively(api_module, capsys, header_names)` (function)
- L340 `test_api_gmail_send_uses_conventional_mime_header_casing(api_module)` (function)
- L380 `test_api_gmail_reply_reads_headers_case_insensitively_and_uses_conventional_mime_header_casing(api_module, header_names)` (function)
- L438 `test_api_get_credentials_refresh_persists_authorized_user_type(api_module, monkeypatch)` (function)
