---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/dashboard_auth/basic/__init__.py

Symbols in `plugins/dashboard_auth/basic/__init__.py`.

- L115 `hash_password(password: str)` (function) — Return a ``scrypt$n$r$p$<salt_b64>$<dk_b64>`` hash string.
- L139 `_verify_password(password: str, encoded: str)` (function) — Constant-time scrypt verify. False on any malformed hash string.
- L176 `_sign(payload: dict, secret: bytes)` (function)
- L182 `_unsign(token: str, secret: bytes)` (function)
- L201 `BasicAuthProvider` (class) — Username/password provider with stateless HMAC-signed sessions.
- L208 `__init__(self, *, username: str, password_hash: str, secret: bytes, ttl_seconds: int=_DEFAULT_TTL_SECONDS)` (method)
- L229 `start_login(self, *, redirect_uri: str)` (method)
- L235 `complete_login(self, *, code: str, state: str, code_verifier: str, redirect_uri: str)` (method)
- L244 `complete_password_login(self, *, username: str, password: str)` (method)
- L263 `verify_session(self, *, access_token: str)` (method)
- L273 `refresh_session(self, *, refresh_token: str)` (method)
- L285 `revoke_session(self, *, refresh_token: str)` (method)
- L293 `_mint_session(self, user_id: str)` (method)
- L314 `_session_from_payload(self, access_token: str, refresh_token: str, payload: dict)` (method)
- L335 `_load_config_basic_auth_section()` (function) — Return ``dashboard.basic_auth`` from config.yaml, or ``{}``.
- L356 `_resolve(env_name: str, cfg_section: dict, cfg_key: str)` (function) — Env-wins-over-config resolution; empty env treated as unset.
- L364 `_resolve_secret(cfg_section: dict)` (function) — Resolve the token-signing secret.
- L394 `register(ctx)` (function) — Plugin entry — registers BasicAuthProvider when credentials exist.
