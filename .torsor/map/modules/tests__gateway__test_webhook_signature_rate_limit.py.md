---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_webhook_signature_rate_limit.py

Symbols in `tests/gateway/test_webhook_signature_rate_limit.py`.

- L28 `_make_adapter(routes, rate_limit=5, **extra_kw)` (function) — Create a WebhookAdapter with the given routes.
- L41 `_create_app(adapter: WebhookAdapter)` (function) — Build the aiohttp Application from the adapter.
- L49 `_github_signature(body: bytes, secret: str)` (function) — Compute X-Hub-Signature-256 for *body* using *secret*.
- L59 `TestSignatureBeforeRateLimit` (class) — Verify that invalid signatures do NOT consume rate limit quota.
- L63 `test_invalid_signature_does_not_consume_rate_limit(self)` (method) — Send requests with invalid signatures up to the rate limit, then
- L143 `test_valid_signature_still_rate_limited(self)` (method) — Verify that VALID requests still respect rate limiting normally.
- L202 `test_mixed_valid_and_invalid_signatures(self)` (method) — Interleave invalid and valid requests. Only valid ones count
