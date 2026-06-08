---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_webhook_integration.py

Symbols in `tests/gateway/test_webhook_integration.py`.

- L33 `_make_adapter(routes, **extra_kw)` (function) — Create a WebhookAdapter with the given routes.
- L41 `_create_app(adapter: WebhookAdapter)` (function) — Build the aiohttp Application from the adapter.
- L49 `_github_signature(body: bytes, secret: str)` (function) — Compute X-Hub-Signature-256 for *body* using *secret*.
- L80 `TestGitHubPRWebhook` (class)
- L83 `test_github_pr_webhook_triggers_agent(self)` (method) — POST with a realistic GitHub PR payload should:
- L150 `TestSkillsInjection` (class)
- L153 `test_skills_injected_into_prompt(self)` (method) — When a route has skills: [code-review], the adapter should
- L212 `TestCrossPlatformDelivery` (class)
- L215 `test_cross_platform_delivery(self)` (method) — When deliver='telegram', the response is routed to the
- L270 `TestGitHubCommentDelivery` (class)
- L273 `test_github_comment_delivery(self)` (method) — When deliver='github_comment', the adapter invokes
