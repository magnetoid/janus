---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/dashboard_auth/base.py

Symbols in `hermes_cli/dashboard_auth/base.py`.

- L10 `Session` (class) — A verified identity. Returned by ``complete_login`` and ``verify_session``.
- L29 `LoginStart` (class) — First leg of the OAuth round trip.
- L44 `ProviderError` (class) — IDP unreachable, network error, or other transient failure.
- L51 `InvalidCodeError` (class) — The OAuth callback ``code`` / ``state`` failed validation.
- L58 `InvalidCredentialsError` (class) — A username/password pair was rejected by a password provider.
- L68 `RefreshExpiredError` (class) — The refresh token is dead.
- L75 `DashboardAuthProvider` (class) — Protocol every dashboard-auth provider plugin implements.
- L135 `start_login(self, *, redirect_uri: str)` (method)
- L138 `complete_login(self, *, code: str, state: str, code_verifier: str, redirect_uri: str)` (method)
- L148 `verify_session(self, *, access_token: str)` (method)
- L151 `refresh_session(self, *, refresh_token: str)` (method)
- L154 `revoke_session(self, *, refresh_token: str)` (method)
- L156 `complete_password_login(self, *, username: str, password: str)` (method) — Verify a username/password pair and mint a :class:`Session`.
- L187 `assert_protocol_compliance(cls: type)` (function) — Raise ``TypeError`` if ``cls`` doesn't fully implement the provider protocol.
