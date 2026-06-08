---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/platforms/google_chat/oauth.py

Symbols in `plugins/platforms/google_chat/oauth.py`.

- L97 `_hermes_home()` (function) — Resolve HERMES_HOME at call time (NOT module import).
- L114 `_sanitize_email(email: str)` (function)
- L119 `_legacy_token_path()` (function)
- L123 `_user_tokens_dir()` (function)
- L127 `_legacy_pending_path()` (function)
- L131 `_user_pending_dir()` (function)
- L135 `_token_path(email: Optional[str]=None)` (function) — Return the on-disk token path for ``email`` or the legacy path.
- L142 `_client_secret_path()` (function)
- L146 `_pending_auth_path(email: Optional[str]=None)` (function)
- L179 `load_user_credentials(email: Optional[str]=None)` (function) — Load + validate persisted user OAuth credentials.
- L239 `refresh_or_none(creds: Any, email: Optional[str]=None)` (function) — Refresh ``creds`` if expired. Returns the credentials or ``None``.
- L272 `build_user_chat_service(creds: Any)` (function) — Build a Google Chat API client authenticated as the user.
- L283 `list_authorized_emails()` (function) — Return the set of user emails that have stored per-user tokens.
- L302 `_persist_credentials(creds: Any, token_path: Path)` (function) — Persist refreshed credentials atomically with private permissions.
- L321 `_normalize_authorized_user_payload(payload: dict)` (function) — Ensure the persisted token JSON has the type field google-auth expects.
- L329 `_write_private_json(path: Path, data: Any)` (function) — Atomically write JSON with 0o600 permissions where supported.
- L361 `_ensure_deps()` (function) — Check deps available; install if not; exit on failure.
- L371 `install_deps()` (function)
- L395 `check_auth(email: Optional[str]=None)` (function) — Print status; return True if creds are usable.
- L414 `store_client_secret(path: str)` (function) — Validate and copy the user's OAuth client_secret.json into HERMES_HOME.
- L442 `_save_pending_auth(*, state: str, code_verifier: str, email: Optional[str]=None)` (function)
- L456 `_load_pending_auth(email: Optional[str]=None)` (function)
- L474 `_extract_code_and_state(code_or_url: str)` (function) — Accept a raw auth code OR the full failed-redirect URL the user pastes.
- L490 `get_auth_url(email: Optional[str]=None)` (function) — Print the OAuth URL for the user to visit. Persists PKCE state.
- L517 `exchange_auth_code(code: str, email: Optional[str]=None)` (function) — Exchange an auth code (or pasted redirect URL) for a refresh token.
- L592 `revoke(email: Optional[str]=None)` (function) — Revoke the stored token with Google and delete it locally.
- L629 `main()` (function)
