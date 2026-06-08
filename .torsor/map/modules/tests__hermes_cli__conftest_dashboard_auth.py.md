---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/conftest_dashboard_auth.py

Symbols in `tests/hermes_cli/conftest_dashboard_auth.py`.

- L43 `_sign(payload: dict)` (function) — Produce a tamper-evident opaque token.
- L56 `_unsign(token: str)` (function) — Inverse of ``_sign``; returns None on any tamper/decode failure.
- L71 `StubAuthProvider` (class) — Local fake IDP for E2E tests.
- L84 `__init__(self, default_ttl: int=3600)` (method)
- L89 `start_login(self, *, redirect_uri: str)` (method)
- L100 `complete_login(self, *, code: str, state: str, code_verifier: str, redirect_uri: str)` (method)
- L135 `verify_session(self, *, access_token: str)` (method)
- L153 `refresh_session(self, *, refresh_token: str)` (method)
- L182 `revoke_session(self, *, refresh_token: str)` (method)
