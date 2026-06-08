---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/copilot_auth.py

Symbols in `hermes_cli/copilot_auth.py`.

- L46 `validate_copilot_token(token: str)` (function) — Validate that a token is usable with the Copilot API.
- L67 `resolve_copilot_token()` (function) — Resolve a GitHub token suitable for Copilot API use.
- L98 `_gh_cli_candidates()` (function) — Return candidate ``gh`` binary paths, including common Homebrew installs.
- L119 `_try_gh_cli_token()` (function) — Return a token from ``gh auth token`` when the GitHub CLI is available.
- L155 `copilot_device_code_login(*, host: str='github.com', timeout_seconds: float=300)` (function) — Run the GitHub OAuth device code flow for Copilot.
- L291 `_token_fingerprint(raw_token: str)` (function) — Short fingerprint of a raw token for cache keying (avoids storing full token).
- L297 `exchange_copilot_token(raw_token: str, *, timeout: float=10.0)` (function) — Exchange a raw GitHub token for a short-lived Copilot API token.
- L353 `get_copilot_api_token(raw_token: str)` (function) — Exchange a raw GitHub token for a Copilot API token, with fallback.
- L373 `copilot_request_headers(*, is_agent_turn: bool=True, is_vision: bool=False)` (function) — Build the standard headers for Copilot API requests.
