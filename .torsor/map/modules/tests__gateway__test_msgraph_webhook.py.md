---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_msgraph_webhook.py

Symbols in `tests/gateway/test_msgraph_webhook.py`.

- L11 `_make_adapter(**extra_overrides)` (function)
- L21 `_FakeRequest` (class)
- L22 `__init__(self, *, query=None, json_payload=None, remote='127.0.0.1')` (method)
- L27 `json(self)` (method)
- L33 `TestMSGraphWebhookConfig` (class)
- L34 `test_gateway_config_accepts_msgraph_webhook_platform(self)` (method)
- L49 `test_env_overrides_apply_to_existing_msgraph_webhook_platform(self, monkeypatch)` (method)
- L72 `TestMSGraphValidationHandshake` (class)
- L74 `test_connect_requires_client_state(self)` (method)
- L84 `test_connect_requires_source_allowlist_on_public_bind(self)` (method)
- L93 `test_connect_allows_loopback_without_source_allowlist(self)` (method)
- L105 `test_validation_token_echo_on_get(self)` (method)
- L115 `test_bare_get_without_validation_token_rejected(self)` (method) — GET without validationToken is 400 so the endpoint can't be enumerated.
- L122 `test_post_with_validation_token_still_echoes(self)` (method) — Tolerate defensive clients that send validationToken on POST.
- L132 `TestMSGraphNotifications` (class)
- L134 `test_missing_client_state_is_auth_rejected(self)` (method)
- L150 `test_valid_notification_accepted_and_scheduled(self)` (method)
- L187 `test_bad_client_state_rejected_as_auth_failure(self)` (method) — Every-item-bad-clientState batches return 403 so forged POSTs stop retrying.
- L216 `test_client_state_compare_is_timing_safe(self, monkeypatch)` (method) — Ensure hmac.compare_digest is used for clientState comparison.
- L251 `test_duplicate_notification_deduped(self)` (method)
- L283 `test_notifications_without_id_are_not_deduped(self)` (method)
- L314 `test_resource_patterns_accept_leading_slash(self)` (method)
- L332 `test_resource_not_in_allowlist_returns_400(self)` (method) — Every-item-rejected-for-non-auth returns 400 (configuration issue).
- L348 `test_malformed_body_returns_400(self)` (method)
- L356 `test_missing_value_array_returns_400(self)` (method)
- L364 `test_seen_receipts_are_bounded(self)` (method)
- L403 `TestMSGraphSourceIPAllowlist` (class)
- L405 `test_public_bind_without_allowlist_fails_closed(self)` (method) — Public binds must not accept requests until a source allowlist is configured.
- L423 `test_loopback_bind_without_allowlist_still_accepts_local_requests(self)` (method) — Loopback-only listeners may rely on local proxying/tunnels instead of CIDRs.
- L441 `test_post_from_disallowed_ip_rejected(self)` (method)
- L458 `test_post_from_allowed_ip_accepted(self)` (method)
- L475 `test_validation_handshake_also_respects_allowlist(self)` (method) — A disallowed IP shouldn't be able to probe the handshake endpoint.
- L484 `test_health_endpoint_also_respects_allowlist(self)` (method) — The readiness endpoint should not leak counters to arbitrary sources.
- L491 `test_invalid_cidr_entries_are_ignored_at_init(self)` (method) — Malformed CIDR strings should log a warning and be ignored, not crash.
- L499 `test_cidr_list_accepts_comma_string(self)` (method) — Env-var-style 'cidr1, cidr2' strings parse as a list.
