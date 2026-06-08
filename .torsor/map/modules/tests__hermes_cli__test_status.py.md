---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_status.py

Symbols in `tests/hermes_cli/test_status.py`.

- L6 `test_show_status_includes_tavily_key(monkeypatch, capsys, tmp_path)` (function)
- L17 `test_show_status_termux_gateway_section_skips_systemctl(monkeypatch, capsys, tmp_path)` (function)
- L48 `test_show_status_reports_nous_auth_error(monkeypatch, capsys, tmp_path)` (function)
- L86 `test_show_status_reports_nous_inference_key_without_portal_login(monkeypatch, capsys, tmp_path)` (function)
- L140 `_base_xai_mocks(monkeypatch, tmp_path)` (function) — Set up the minimal environment for show_status, returning status_mod.
- L160 `TestShowStatusXaiOAuth` (class) — xAI OAuth row in hermes status.
- L167 `test_logged_in_shows_check_mark_and_label(self, monkeypatch, capsys, tmp_path)` (method)
- L182 `test_logged_in_shows_auth_store(self, monkeypatch, capsys, tmp_path)` (method)
- L194 `test_logged_in_shows_last_refresh(self, monkeypatch, capsys, tmp_path)` (method)
- L210 `test_logged_in_does_not_show_error_line(self, monkeypatch, capsys, tmp_path)` (method) — Error field must be suppressed when logged_in is True.
- L228 `test_no_auth_store_line_when_field_absent(self, monkeypatch, capsys, tmp_path)` (method) — Auth file line must not appear when auth_store is missing.
- L242 `test_no_refreshed_line_when_last_refresh_absent(self, monkeypatch, capsys, tmp_path)` (method) — Refreshed line must not appear when last_refresh is not present.
- L260 `test_not_logged_in_shows_login_command(self, monkeypatch, capsys, tmp_path)` (method)
- L272 `test_not_logged_in_shows_error(self, monkeypatch, capsys, tmp_path)` (method)
- L284 `test_not_logged_in_omits_error_line_when_error_absent(self, monkeypatch, capsys, tmp_path)` (method) — No Error: line when not logged in but error key is missing.
- L302 `test_import_failure_does_not_crash_show_status(self, monkeypatch, capsys, tmp_path)` (method) — show_status must complete even when get_xai_oauth_auth_status cannot be imported.
- L313 `test_import_failure_does_not_break_other_oauth_providers(self, monkeypatch, capsys, tmp_path)` (method) — Nous/Codex/MiniMax rows must still appear when xAI import fails.
- L327 `test_status_function_exception_does_not_crash(self, monkeypatch, capsys, tmp_path)` (method) — show_status must not propagate an exception raised by get_xai_oauth_auth_status.
- L342 `test_status_function_returns_none_does_not_crash(self, monkeypatch, capsys, tmp_path)` (method) — get_xai_oauth_auth_status returning None must be handled gracefully.
