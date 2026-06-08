---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_anthropic_keychain.py

Symbols in `tests/agent/test_anthropic_keychain.py`.

- L13 `TestReadClaudeCodeCredentialsFromKeychain` (class) — Bug 4: macOS Keychain support for Claude Code >=2.1.114.
- L16 `test_returns_none_on_linux(self)` (method) — Keychain reading is Darwin-only; must return None on other platforms.
- L21 `test_returns_none_on_windows(self)` (method)
- L25 `test_returns_none_when_security_command_not_found(self)` (method) — OSError from missing security binary must be handled gracefully.
- L32 `test_returns_none_on_nonzero_exit_code(self)` (method) — security returns non-zero when the Keychain entry doesn't exist.
- L39 `test_returns_none_for_empty_stdout(self)` (method)
- L45 `test_returns_none_for_non_json_payload(self)` (method)
- L51 `test_returns_none_when_password_field_is_missing_claude_ai_oauth(self)` (method)
- L61 `test_returns_none_when_access_token_is_empty(self)` (method)
- L71 `test_parses_valid_keychain_entry(self)` (method)
- L93 `TestReadClaudeCodeCredentialsPriority` (class) — Bug 4: Keychain must be checked before the JSON file.
- L96 `test_keychain_takes_priority_over_json_file(self, tmp_path, monkeypatch)` (method) — When both Keychain and JSON file have credentials, Keychain wins.
- L131 `test_falls_back_to_json_when_keychain_returns_none(self, tmp_path, monkeypatch)` (method) — When Keychain has no entry, JSON file is used as fallback.
- L154 `test_returns_none_when_neither_keychain_nor_json_has_creds(self, tmp_path, monkeypatch)` (method) — No credentials anywhere — must return None cleanly.
