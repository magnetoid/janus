---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_codex_cli_model_picker.py

Symbols in `tests/hermes_cli/test_codex_cli_model_picker.py`.

- L22 `_make_fake_jwt(expiry_offset: int=3600)` (function) — Build a fake JWT with a future expiry.
- L32 `hermes_auth_only_env(tmp_path, monkeypatch)` (function) — Tokens already in Hermes auth store (no Codex CLI needed).
- L63 `test_normal_path_still_works(hermes_auth_only_env)` (function) — openai-codex appears when tokens are already in Hermes auth store.
- L75 `test_codex_picker_uses_live_codex_catalog(hermes_auth_only_env, tmp_path, monkeypatch)` (function) — The gateway /model picker should surface Codex CLI-only listed models.
- L107 `claude_code_only_env(tmp_path, monkeypatch)` (function) — Set up an environment where Anthropic credentials only exist in
- L146 `test_claude_code_file_detected_by_model_picker(claude_code_only_env)` (function) — anthropic should appear when credentials only exist in ~/.claude/.credentials.json.
- L164 `test_no_codex_when_no_credentials(tmp_path, monkeypatch)` (function) — openai-codex should NOT appear when no credentials exist anywhere.
