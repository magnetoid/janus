---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/credential_sources.py

Symbols in `agent/credential_sources.py`.

- L54 `RemovalResult` (class) — Outcome of removing a credential source.
- L79 `RemovalStep` (class) — How to remove one specific credential source cleanly.
- L104 `matches(self, provider: str, source: str)` (method)
- L115 `register(step: RemovalStep)` (function)
- L120 `find_removal_step(provider: str, source: str)` (function) — Return the first matching RemovalStep, or None if unregistered.
- L143 `_remove_env_source(provider: str, removed)` (function) — env:<VAR> — the most common case.
- L194 `_remove_claude_code(provider: str, removed)` (function) — ~/.claude/.credentials.json is owned by Claude Code itself.
- L207 `_remove_hermes_pkce(provider: str, removed)` (function) — ~/.hermes/.anthropic_oauth.json is ours — delete it outright.
- L222 `_clear_auth_store_provider(provider: str)` (function) — Delete auth_store.providers[provider].  Returns True if deleted.
- L240 `_remove_nous_device_code(provider: str, removed)` (function) — Nous OAuth lives in auth.json providers.nous — clear it and suppress.
- L255 `_remove_minimax_oauth(provider: str, removed)` (function) — MiniMax OAuth lives in auth.json providers.minimax-oauth — clear it.
- L268 `_remove_xai_oauth_loopback_pkce(provider: str, removed)` (function) — xAI OAuth tokens live in auth.json providers.xai-oauth — clear them.
- L293 `_remove_codex_device_code(provider: str, removed)` (function) — Codex tokens live in TWO places: our auth store AND ~/.codex/auth.json.
- L327 `_remove_qwen_cli(provider: str, removed)` (function) — ~/.qwen/oauth_creds.json is owned by the Qwen CLI.
- L340 `_remove_copilot_gh(provider: str, removed)` (function) — Copilot token comes from `gh auth token` or COPILOT_GITHUB_TOKEN / GH_TOKEN / GITHUB_TOKEN.
- L369 `_remove_custom_config(provider: str, removed)` (function) — Custom provider pools are seeded from custom_providers config or
- L383 `_register_all_sources()` (function) — Called once on module import.
