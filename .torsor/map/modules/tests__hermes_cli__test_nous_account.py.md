---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_nous_account.py

Symbols in `tests/hermes_cli/test_nous_account.py`.

- L21 `_jwt(claims: dict[str, Any])` (function)
- L29 `_state(token: str)` (function)
- L37 `_account_payload(*, allowed: bool, subscription: dict[str, Any] | None, subscription_credits: float, purchased_credits: float)` (function)
- L76 `_reset_cache()` (function)
- L82 `test_valid_jwt_with_paid_access_true(monkeypatch)` (function)
- L110 `test_valid_jwt_with_paid_access_false(monkeypatch)` (function)
- L129 `test_valid_jwt_missing_paid_access_is_unknown_not_paid(monkeypatch)` (function)
- L147 `test_expired_jwt_falls_back_to_fresh_account(monkeypatch)` (function)
- L239 `test_fresh_account_payload_normalization(monkeypatch, payload, expected_paid)` (function)
- L258 `test_force_fresh_uses_account_api_even_when_jwt_is_valid(monkeypatch)` (function)
- L283 `test_no_oauth_token_reports_inference_key_present(monkeypatch)` (function)
- L322 `test_pool_oauth_entry_uses_jwt_snapshot(monkeypatch)` (function)
- L372 `test_pool_oauth_entry_force_fresh_uses_account_api(monkeypatch)` (function)
- L429 `test_entitlement_message_returns_none_for_paid_access()` (function)
- L441 `test_entitlement_message_for_inference_key_without_portal_login()` (function)
- L461 `test_entitlement_message_for_active_paid_subscription_with_no_credits()` (function)
- L490 `test_entitlement_message_for_no_subscription_or_credits()` (function)
- L514 `test_entitlement_message_for_unknown_entitlement_is_explicit()` (function)
- L532 `test_entitlement_message_for_account_missing()` (function)
