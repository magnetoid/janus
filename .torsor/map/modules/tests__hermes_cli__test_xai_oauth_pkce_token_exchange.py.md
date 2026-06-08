---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_xai_oauth_pkce_token_exchange.py

Symbols in `tests/hermes_cli/test_xai_oauth_pkce_token_exchange.py`.

- L46 `_PostRecorder` (class) — Capture every ``httpx.post`` call without touching the network.
- L49 `__init__(self, response: httpx.Response)` (method)
- L53 `__call__(self, url, *, headers=None, data=None, timeout=None, **kw)` (method)
- L61 `_ok_response(payload: dict)` (function)
- L65 `_err_response(status: int, body: str)` (function)
- L70 `post_recorder(monkeypatch)` (function) — Default: 200 response with a full xAI token payload.
- L92 `test_token_exchange_includes_code_verifier(post_recorder)` (function) — RFC 7636 §4.5 — ``code_verifier`` MUST be sent.
- L105 `test_token_exchange_also_echoes_code_challenge_for_xai(post_recorder)` (function) — Defense-in-depth for #26990 — xAI re-validates the challenge
- L122 `test_token_exchange_uses_correct_grant_and_client(post_recorder)` (function) — Lock the static fields too — a future refactor must not flip
- L139 `test_token_exchange_uses_form_urlencoded_content_type(post_recorder)` (function) — xAI's token endpoint expects ``application/x-www-form-urlencoded``.
- L153 `test_token_exchange_targets_the_supplied_endpoint(post_recorder)` (function) — Some test fixtures sniff the discovered token endpoint dynamically.
- L166 `test_token_exchange_passes_timeout_through(post_recorder)` (function) — Operators on slow networks pass a higher ``timeout_seconds``;
- L180 `test_token_exchange_floor_timeout_is_20s(post_recorder)` (function)
- L197 `test_empty_code_verifier_raises_without_posting(post_recorder)` (function) — If ``code_verifier`` is somehow lost upstream, we must refuse to
- L215 `test_missing_code_challenge_omits_echo_but_still_sends_verifier(post_recorder)` (function) — ``code_challenge`` is defensive — if a caller doesn't have it
- L237 `test_non_200_response_surfaces_status_and_body(monkeypatch)` (function) — When xAI returns a 4xx, the operator needs both the HTTP status
- L263 `test_transport_error_wraps_as_auth_error(monkeypatch)` (function) — A connection failure must come back as ``AuthError`` so the
- L283 `test_non_dict_payload_raises_invalid_json(monkeypatch)` (function) — xAI returning ``[]`` or a string at 200 is a server bug — fail
- L299 `test_success_returns_full_payload_dict(post_recorder)` (function) — 200 happy path: the parsed JSON dict comes back verbatim so the
- L318 `test_wire_format_is_form_urlencoded_with_all_pkce_fields(monkeypatch)` (function) — End-to-end check on the actual bytes httpx puts on the wire.
