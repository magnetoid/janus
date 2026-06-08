---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_webhook_deliver_only.py

Symbols in `tests/gateway/test_webhook_deliver_only.py`.

- L33 `_make_adapter(routes, **extra_kw)` (function)
- L40 `_create_app(adapter: WebhookAdapter)` (function)
- L47 `_wire_mock_target(adapter: WebhookAdapter, platform_name: str='telegram')` (function) — Attach a gateway_runner with a mocked target adapter.
- L64 `TestDeliverOnlyBypassesAgent` (class) — The whole point of the feature — handle_message must not be called.
- L68 `test_post_delivers_directly_without_agent(self)` (method)
- L123 `test_template_rendering_works(self)` (method) — Dot-notation template variables resolve in deliver_only mode.
- L151 `test_thread_id_passed_through(self)` (method) — deliver_extra.thread_id flows through to the target adapter.
- L183 `TestDeliverOnlyStatusCodes` (class)
- L186 `test_delivery_failure_returns_502(self)` (method) — If the target adapter returns SendResult(success=False), 502.
- L217 `test_delivery_exception_returns_502(self)` (method) — If adapter.send() raises, we return 502 (not 500).
- L246 `test_target_platform_not_connected_returns_502(self)` (method) — deliver_only to a platform the gateway doesn't have → 502.
- L274 `TestDeliverOnlyStartupValidation` (class)
- L277 `test_deliver_only_with_log_deliver_rejected(self)` (method) — deliver_only=true + deliver=log is nonsense — reject at connect().
- L292 `test_deliver_only_with_missing_deliver_rejected(self)` (method) — deliver_only=true with no deliver field defaults to 'log' → reject.
- L307 `test_deliver_only_with_real_target_accepted(self)` (method) — Sanity check — a valid deliver_only config passes validation.
- L334 `TestDeliverOnlySecurityInvariants` (class)
- L337 `test_hmac_still_enforced(self)` (method) — deliver_only does NOT bypass HMAC validation.
- L366 `test_idempotency_still_applies(self)` (method) — Same delivery_id posted twice → second is suppressed.
- L403 `test_rate_limit_still_applies(self)` (method) — Route-level rate limit caps deliver_only POSTs too.
- L440 `TestDirectDeliverUnit` (class)
- L443 `test_dispatches_to_cross_platform_for_messaging_targets(self)` (method)
- L457 `test_dispatches_to_github_comment(self)` (method)
