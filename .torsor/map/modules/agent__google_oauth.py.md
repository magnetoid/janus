---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/google_oauth.py

Symbols in `agent/google_oauth.py`.

- L144 `GoogleOAuthError` (class) — Raised for any failure in the Google OAuth flow.
- L147 `__init__(self, message: str, *, code: str='google_oauth_error')` (method)
- L156 `_credentials_path()` (function)
- L160 `_lock_path()` (function)
- L168 `_credentials_lock(timeout_seconds: float=LOCK_TIMEOUT_SECONDS)` (function) — Cross-process lock around the credentials file (fcntl POSIX / msvcrt Windows).
- L252 `_locate_gemini_cli_oauth_js()` (function) — Walk the user's gemini binary install to find its oauth2.js.
- L304 `_scrape_client_credentials()` (function) — Extract client_id + client_secret from the local gemini-cli install.
- L338 `_get_client_id()` (function)
- L348 `_get_client_secret()` (function)
- L358 `_require_client_id()` (function)
- L380 `_generate_pkce_pair()` (function) — Generate a (verifier, challenge) pair using S256.
- L393 `RefreshParts` (class)
- L399 `parse(cls, packed: str)` (method)
- L409 `format(self)` (method)
- L422 `GoogleCredentials` (class)
- L430 `to_dict(self)` (method)
- L443 `from_dict(cls, data: Dict[str, Any])` (method)
- L455 `expires_unix_seconds(self)` (method)
- L458 `access_token_expired(self, skew_seconds: int=REFRESH_SKEW_SECONDS)` (method)
- L468 `load_credentials()` (function) — Load credentials from disk. Returns None if missing or corrupt.
- L488 `save_credentials(creds: GoogleCredentials)` (function) — Atomically write creds to disk with 0o600 permissions.
- L523 `clear_credentials()` (function) — Remove the creds file. Idempotent.
- L539 `_post_form(url: str, data: Dict[str, str], timeout: float)` (function) — POST x-www-form-urlencoded and return parsed JSON response.
- L576 `exchange_code(code: str, verifier: str, redirect_uri: str, *, client_id: Optional[str]=None, client_secret: Optional[str]=None, timeout: float=TOKEN_REQUEST_TIMEOUT_SECONDS)` (function) — Exchange authorization code for access + refresh tokens.
- L600 `refresh_access_token(refresh_token: str, *, client_id: Optional[str]=None, client_secret: Optional[str]=None, timeout: float=TOKEN_REQUEST_TIMEOUT_SECONDS)` (function) — Refresh the access token.
- L625 `_fetch_user_email(access_token: str, timeout: float=TOKEN_REQUEST_TIMEOUT_SECONDS)` (function) — Best-effort userinfo fetch for display. Failures return empty string.
- L649 `get_valid_access_token(*, force_refresh: bool=False)` (function) — Load creds, refreshing if near expiry, and return a valid bearer token.
- L724 `update_project_ids(project_id: str='', managed_project_id: str='')` (function) — Persist resolved/discovered project IDs back into the credential file.
- L740 `_OAuthCallbackHandler` (class)
- L746 `log_message(self, format: str, *args: Any)` (method)
- L749 `do_GET(self)` (method)
- L784 `_respond_html(self, status: int, body: str)` (method)
- L814 `_bind_callback_server(preferred_port: int=DEFAULT_REDIRECT_PORT)` (function)
- L827 `_is_headless()` (function)
- L835 `start_oauth_flow(*, force_relogin: bool=False, open_browser: bool=True, callback_wait_seconds: float=CALLBACK_WAIT_SECONDS, project_id: str='')` (function) — Run the interactive browser OAuth flow and persist credentials.
- L951 `_paste_mode_login(verifier: str, challenge: str, state: str, client_id: str, client_secret: str, project_id: str)` (function) — Run OAuth flow without a local callback server.
- L994 `_prompt_paste_fallback()` (function)
- L1011 `_persist_token_response(token_resp: Dict[str, Any], *, project_id: str='')` (function)
- L1041 `run_gemini_oauth_login_pure()` (function) — Run the login flow and return a dict matching the credential pool shape.
- L1057 `resolve_project_id_from_env()` (function) — Return a GCP project ID from env vars, in priority order.
