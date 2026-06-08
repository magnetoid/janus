---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/mcp_oauth.py

Symbols in `tools/mcp_oauth.py`.

- L84 `OAuthNonInteractiveError` (class) — Raised when OAuth requires browser interaction in a non-interactive env.
- L112 `_get_token_dir()` (function) — Return the directory for MCP OAuth token files.
- L126 `_safe_filename(name: str)` (function) — Sanitize a server name for use as a filename (no path separators).
- L131 `_find_free_port()` (function) — Find an available TCP port on localhost.
- L138 `_is_interactive()` (function) — Return True if we can reasonably expect to interact with a user.
- L146 `_can_open_browser()` (function) — Return True if opening a browser is likely to work.
- L165 `_read_json(path: Path)` (function) — Read a JSON file, returning None if it doesn't exist or is invalid.
- L176 `_write_json(path: Path, data: dict)` (function) — Write a dict as JSON with restricted permissions (0o600).
- L218 `HermesTokenStorage` (class) — Persist OAuth tokens and client registration to JSON files.
- L228 `__init__(self, server_name: str)` (method)
- L231 `_tokens_path(self)` (method)
- L234 `_client_info_path(self)` (method)
- L237 `_meta_path(self)` (method)
- L242 `get_tokens(self)` (method)
- L281 `set_tokens(self, tokens: 'OAuthToken')` (method)
- L303 `get_client_info(self)` (method)
- L313 `set_client_info(self, client_info: 'OAuthClientInformationFull')` (method)
- L325 `save_oauth_metadata(self, metadata: 'OAuthMetadata')` (method)
- L329 `load_oauth_metadata(self)` (method)
- L341 `remove(self)` (method) — Delete all stored OAuth state for this server.
- L346 `has_cached_tokens(self)` (method) — Return True if we have tokens on disk (may be expired).
- L356 `_make_callback_handler()` (function) — Create a per-flow callback HTTP handler class with its own result dict.
- L400 `_redirect_handler(authorization_url: str)` (function) — Show the authorization URL to the user.
- L451 `_wait_for_callback()` (function) — Wait for the OAuth callback to arrive on the local callback server.
- L538 `_paste_callback_reader(result: dict)` (function) — Read one line from stdin, parse it as an OAuth redirect, write to result.
- L627 `remove_oauth_tokens(server_name: str)` (function) — Delete stored OAuth tokens and client info for a server.
- L643 `_configure_callback_port(cfg: dict)` (function) — Pick or validate the OAuth callback port.
- L664 `_build_client_metadata(cfg: dict)` (function) — Build OAuthClientMetadata from the oauth config dict.
- L694 `_maybe_preregister_client(storage: 'HermesTokenStorage', cfg: dict, client_metadata: 'OAuthClientMetadata')` (function) — If cfg has a pre-registered client_id, persist it to storage.
- L725 `build_oauth_auth(server_name: str, server_url: str, oauth_config: dict | None=None)` (function) — Build an ``httpx.Auth``-compatible OAuth handler for an MCP server.
