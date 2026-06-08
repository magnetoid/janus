---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dashboard_auth_stub_provider.py

Symbols in `tests/hermes_cli/test_dashboard_auth_stub_provider.py`.

- L17 `_pkce_payload(ls)` (function) — Parse ``state=...;verifier=...`` out of the LoginStart cookie payload.
- L25 `test_stub_complies_with_protocol()` (function)
- L29 `test_stub_start_login_returns_callback_redirect()` (function)
- L37 `test_stub_complete_login_with_matching_state_succeeds()` (function)
- L55 `test_stub_complete_login_rejects_mismatched_state()` (function)
- L67 `test_stub_complete_login_rejects_wrong_code()` (function)
- L80 `test_stub_verify_session_round_trips()` (function)
- L96 `test_stub_verify_expired_session_returns_none()` (function)
- L111 `test_stub_verify_tampered_token_returns_none()` (function)
- L116 `test_stub_refresh_round_trips()` (function)
- L141 `test_stub_refresh_expired_raises()` (function)
- L147 `test_stub_revoke_is_silent()` (function)
