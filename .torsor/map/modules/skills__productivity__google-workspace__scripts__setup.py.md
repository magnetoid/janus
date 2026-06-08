---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# skills/productivity/google-workspace/scripts/setup.py

Symbols in `skills/productivity/google-workspace/scripts/setup.py`.

- L65 `_normalize_authorized_user_payload(payload: dict)` (function)
- L72 `_load_token_payload(path: Path=TOKEN_PATH)` (function)
- L79 `_missing_scopes_from_payload(payload: dict)` (function)
- L87 `_format_missing_scopes(missing_scopes: list[str])` (function)
- L96 `install_deps()` (function) — Install Google API packages if missing. Returns True on success.
- L149 `_ensure_deps()` (function) — Check deps are available, install if not, exit on failure.
- L159 `check_auth_live()` (function) — Check auth with a real API call to detect disabled_client/account issues.
- L185 `check_auth(quiet: bool=False)` (function) — Check if stored credentials are valid. Prints status, exits 0 or 1.
- L255 `store_client_secret(path: str)` (function) — Copy and validate client_secret.json to Hermes home.
- L277 `_save_pending_auth(*, state: str, code_verifier: str)` (function) — Persist the OAuth session bits needed for a later token exchange.
- L291 `_load_pending_auth()` (function) — Load the pending OAuth session created by get_auth_url().
- L312 `_extract_code_and_state(code_or_url: str)` (function) — Accept either a raw auth code or the full redirect URL pasted by the user.
- L329 `get_auth_url()` (function) — Print the OAuth authorization URL. User visits this in a browser.
- L353 `exchange_auth_code(code: str)` (function) — Exchange the authorization code for a token and save it.
- L419 `revoke()` (function) — Revoke stored token and delete it.
- L452 `main()` (function)
