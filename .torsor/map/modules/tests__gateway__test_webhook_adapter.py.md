---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_webhook_adapter.py

Symbols in `tests/gateway/test_webhook_adapter.py`.

- L42 `_make_config(routes=None, secret='', rate_limit=30, max_body_bytes=1048576, host='0.0.0.0', port=0)` (function) — Build a PlatformConfig suitable for WebhookAdapter.
- L63 `_make_adapter(routes=None, **kwargs)` (function) — Create a WebhookAdapter with sensible defaults for testing.
- L69 `_create_app(adapter: WebhookAdapter)` (function) — Build the aiohttp Application from the adapter (without starting a full server).
- L77 `_mock_request(headers=None, body=b'', content_length=None, match_info=None)` (function) — Build a lightweight mock aiohttp request for non-HTTP tests.
- L92 `_github_signature(body: bytes, secret: str)` (function) — Compute X-Hub-Signature-256 for *body* using *secret*.
- L99 `_generic_signature(body: bytes, secret: str)` (function) — Compute X-Webhook-Signature (plain HMAC-SHA256 hex) for *body*.
- L104 `_svix_signature(body: bytes, secret: str, msg_id: str, timestamp: str)` (function) — Compute a Svix v1 signature header for *body* using *secret*.
- L121 `TestValidateSignature` (class) — Tests for WebhookAdapter._validate_signature.
- L124 `test_validate_github_signature_valid(self)` (method) — Valid X-Hub-Signature-256 is accepted.
- L133 `test_validate_github_signature_invalid(self)` (method) — Wrong X-Hub-Signature-256 is rejected.
- L141 `test_validate_gitlab_token(self)` (method) — GitLab plain-token match via X-Gitlab-Token.
- L148 `test_validate_gitlab_token_wrong(self)` (method) — Wrong X-Gitlab-Token is rejected.
- L154 `test_validate_no_signature_with_secret_rejects(self)` (method) — Secret configured but no recognised signature header → reject.
- L160 `test_validate_no_secret_allows_all(self)` (method) — When the secret is empty/falsy, the validator is never even called
- L177 `test_validate_generic_signature_valid(self)` (method) — Valid X-Webhook-Signature (generic HMAC-SHA256 hex) is accepted.
- L186 `test_validate_svix_signature_valid(self)` (method) — Valid Svix/AgentMail v1 signature headers are accepted.
- L203 `test_validate_svix_signature_wrong_body_rejects(self)` (method) — Svix/AgentMail signatures are bound to the exact raw request body.
- L221 `test_validate_svix_signature_old_timestamp_rejects(self)` (method) — Svix/AgentMail signatures outside the replay window are rejected.
- L238 `test_validate_svix_signature_multiple_entries_accepts_matching_v1(self)` (method) — Svix rotation headers may contain multiple space-separated signatures.
- L255 `test_validate_svix_signature_missing_signature_rejects(self)` (method) — Partial Svix headers reject instead of falling through to another scheme.
- L261 `test_validate_svix_signature_unsupported_version_rejects(self)` (method) — Only Svix v1 signatures are accepted.
- L278 `test_validate_svix_signature_invalid_whsec_rejects(self)` (method) — Malformed whsec_ secrets are rejected, not silently treated as raw secrets.
- L297 `test_validate_svix_signature_raw_secret_valid(self)` (method) — Raw shared secrets are accepted for Svix-style senders without whsec_ secrets.
- L320 `TestRenderPrompt` (class) — Tests for WebhookAdapter._render_prompt.
- L323 `test_render_prompt_dot_notation(self)` (method) — Dot-notation {pull_request.title} resolves nested keys.
- L335 `test_render_prompt_missing_key_preserved(self)` (method) — {nonexistent} is left as-is when key doesn't exist in payload.
- L346 `test_render_prompt_no_template_dumps_json(self)` (method) — Empty template → JSON dump fallback with event/route context.
- L361 `TestRenderDeliveryExtra` (class)
- L362 `test_render_delivery_extra_templates(self)` (method) — String values in deliver_extra are rendered with payload data.
- L378 `TestEventFilter` (class) — Tests for event type filtering in _handle_webhook.
- L382 `test_event_filter_accepts_matching(self)` (method) — Matching event type passes through.
- L405 `test_event_filter_rejects_non_matching(self)` (method) — Non-matching event type returns 200 with status=ignored.
- L428 `test_event_filter_empty_allows_all(self)` (method) — No events list → accept any event type.
- L449 `test_event_filter_accepts_payload_type_field(self)` (method) — Svix-style payloads often use a top-level `type` event field.
- L475 `TestHTTPHandling` (class)
- L478 `test_unknown_route_returns_404(self)` (method) — POST to an unknown route returns 404.
- L487 `test_webhook_handler_returns_202(self)` (method) — Valid request returns 202 Accepted.
- L502 `test_route_without_secret_rejects_unsigned_request(self)` (method) — Missing HMAC secret must fail closed even if connect() was bypassed.
- L518 `test_health_endpoint(self)` (method) — GET /health returns 200 with status=ok.
- L530 `test_connect_starts_server(self)` (method) — connect() starts the HTTP listener and marks adapter as connected.
- L553 `test_disconnect_cleans_up(self)` (method) — disconnect() stops the server and marks adapter disconnected.
- L572 `TestIdempotency` (class)
- L575 `test_duplicate_delivery_id_returns_200(self)` (method) — Second request with same delivery ID returns 200 duplicate.
- L593 `test_expired_delivery_id_allows_reprocess(self)` (method) — After TTL expires, the same delivery ID is accepted again.
- L614 `test_svix_id_used_as_delivery_id_for_deduplication(self)` (method) — Svix retries reuse svix-id, so use it as the delivery ID when present.
- L638 `TestRateLimiting` (class)
- L641 `test_rate_limit_rejects_excess(self)` (method) — Exceeding the rate limit returns 429.
- L667 `test_rate_limit_window_resets(self)` (method) — After the 60-second window passes, requests are allowed again.
- L698 `TestBodySize` (class)
- L701 `test_oversized_payload_rejected(self)` (method) — Content-Length > max_body_bytes returns 413.
- L722 `TestInsecureNoAuth` (class)
- L725 `test_insecure_no_auth_skips_validation(self)` (method) — Setting secret to _INSECURE_NO_AUTH bypasses signature check.
- L743 `TestSessionIsolation` (class)
- L746 `test_concurrent_webhooks_get_independent_sessions(self)` (method) — Two events on the same route produce different session keys.
- L787 `TestDeliveryCleanup` (class)
- L790 `test_delivery_info_survives_multiple_sends(self)` (method) — send() must NOT pop delivery_info.
- L820 `test_delivery_info_pruned_via_ttl(self)` (method) — Stale delivery_info entries are dropped on the next POST.
- L847 `TestCheckRequirements` (class)
- L848 `test_returns_true_when_aiohttp_available(self)` (method)
- L852 `test_returns_false_without_aiohttp(self)` (method)
- L861 `TestRawTemplateToken` (class) — Tests for the {__raw__} special token in _render_prompt.
- L864 `test_raw_resolves_to_full_json_payload(self)` (method) — {__raw__} in a template dumps the entire payload as JSON.
- L874 `test_raw_truncated_at_4000_chars(self)` (method) — {__raw__} output is truncated at 4000 characters for large payloads.
- L882 `test_raw_mixed_with_other_variables(self)` (method) — {__raw__} can be mixed with regular template variables.
- L899 `TestDeliverCrossPlatformThreadId` (class) — Tests for thread_id passthrough in _deliver_cross_platform.
- L902 `_setup_adapter_with_mock_target(self)` (method) — Set up a webhook adapter with a mocked gateway_runner and target adapter.
- L916 `test_thread_id_passed_as_metadata(self)` (method) — thread_id from deliver_extra is passed as metadata to adapter.send().
- L931 `test_message_thread_id_passed_as_thread_id(self)` (method) — message_thread_id from deliver_extra is mapped to thread_id in metadata.
- L946 `test_no_thread_id_sends_no_metadata(self)` (method) — When no thread_id is present, metadata is None.
- L960 `TestInsecureNoAuthSafetyRail` (class) — connect() refuses to start when INSECURE_NO_AUTH is combined with a
- L966 `test_connect_rejects_insecure_no_auth_on_public_bind(self)` (method) — INSECURE_NO_AUTH + 0.0.0.0 is refused before the server starts.
- L974 `test_connect_rejects_insecure_no_auth_on_lan_ip(self)` (method) — A LAN IP is treated as public.
- L982 `test_connect_rejects_insecure_no_auth_on_empty_host(self)` (method) — Empty host is conservatively treated as non-loopback.
- L994 `test_connect_allows_insecure_no_auth_on_loopback(self, host)` (method) — Recognised loopback hosts are permitted with INSECURE_NO_AUTH.
- L1009 `test_is_loopback_host_accepts(self, host)` (method) — _is_loopback_host covers all documented loopback spellings.
- L1018 `test_is_loopback_host_rejects(self, host)` (method) — _is_loopback_host treats public/LAN/empty as non-loopback.
- L1024 `test_connect_allows_real_secret_on_public_bind(self)` (method) — A real HMAC secret bound to 0.0.0.0 is the normal production case.
