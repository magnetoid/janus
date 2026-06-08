---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_anthropic_oauth_pkce.py

Symbols in `tests/agent/test_anthropic_oauth_pkce.py`.

- L23 `_patch_oauth_flow(monkeypatch, *, callback_code: str, token_response: Dict[str, Any] | None=None, capture_token_request: Dict[str, Any] | None=None, capture_auth_url: Dict[str, str] | None=None)` (function) — Wire up monkeypatches that let ``run_hermes_oauth_login_pure()`` run
- L87 `test_authorization_url_state_is_not_pkce_verifier(monkeypatch, tmp_path)` (function) — The ``state`` parameter in the authorization URL must NOT equal the
- L151 `test_callback_state_mismatch_aborts(monkeypatch, tmp_path, caplog)` (function) — If the state returned in the callback does not match the one we sent
