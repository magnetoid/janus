---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_non_ascii_credential.py

Symbols in `tests/hermes_cli/test_non_ascii_credential.py`.

- L14 `TestCheckNonAsciiCredential` (class) — Tests for _check_non_ascii_credential().
- L17 `test_ascii_key_unchanged(self)` (method)
- L22 `test_strips_unicode_v_lookalike(self, capsys)` (method) — The exact scenario from issue #6843: ʋ instead of v.
- L32 `test_strips_multiple_non_ascii(self, capsys)` (method)
- L39 `test_empty_key(self)` (method)
- L43 `test_all_ascii_no_warning(self, capsys)` (method)
- L50 `TestEnvLoaderSanitization` (class) — Tests for _sanitize_loaded_credentials in env_loader.
- L53 `test_strips_non_ascii_from_api_key(self, monkeypatch)` (method)
- L61 `test_strips_non_ascii_from_token(self, monkeypatch)` (method)
- L69 `test_ignores_non_credential_vars(self, monkeypatch)` (method)
- L77 `test_ascii_credentials_untouched(self, monkeypatch)` (method)
- L84 `test_warns_to_stderr_when_stripping(self, monkeypatch, capsys)` (method) — Silent stripping masks bad keys as opaque provider 400s (see #6843 fallout).
- L102 `test_warning_fires_only_once_per_key(self, monkeypatch, capsys)` (method) — Repeated loads (user env + project env) must not double-warn.
- L118 `test_ascii_control_chars_not_stripped(self, monkeypatch, capsys)` (method) — ASCII control bytes (e.g. ESC 0x1B from terminal paste) are NOT non-ASCII.
