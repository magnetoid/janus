---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_secrets_bitwarden_non_tty.py

Symbols in `tests/hermes_cli/test_secrets_bitwarden_non_tty.py`.

- L14 `TestCmdSetupNonTtyGuard` (class) — cmd_setup should fail early with a clear error in non-TTY environments.
- L18 `_make_args(**overrides)` (method)
- L26 `test_missing_all_flags_returns_1(self, monkeypatch, capsys)` (method) — Non-TTY with no flags → exit 1 with missing flags listed.
- L46 `test_missing_access_token_only(self, monkeypatch, capsys)` (method) — Non-TTY with server-url and project-id but no token → reports --access-token.
- L74 `test_missing_server_url_with_env_var_passes(self, monkeypatch)` (method) — Non-TTY with BWS_SERVER_URL env set → server-url not required.
- L100 `test_all_flags_provided_passes_guard(self, monkeypatch)` (method) — Non-TTY with all three flags → guard passes, proceeds to setup.
- L126 `test_tty_does_not_trigger_guard(self, monkeypatch)` (method) — With TTY, the guard should not trigger (interactive mode allowed).
