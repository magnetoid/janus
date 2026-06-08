---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/webhook.py

Symbols in `gateway/platforms/webhook.py`.

- L82 `_is_loopback_host(host: str)` (function) — True when `host` binds only to the local machine.
- L95 `check_webhook_requirements()` (function) — Check if webhook adapter dependencies are available.
- L100 `WebhookAdapter` (class) — Generic webhook receiver that triggers agent runs from HTTP POSTs.
- L103 `__init__(self, config: PlatformConfig)` (method)
- L147 `connect(self)` (method)
- L215 `disconnect(self)` (method)
- L222 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Deliver the agent's response to the configured destination.
- L267 `_prune_delivery_info(self, now: float)` (method) — Drop delivery_info entries older than the idempotency TTL.
- L284 `get_chat_info(self, chat_id: str)` (method)
- L291 `_handle_health(self, request: 'web.Request')` (method) — GET /health — simple health check.
- L295 `_reload_dynamic_routes(self)` (method) — Reload agent-created subscriptions from disk if the file changed.
- L354 `_handle_webhook(self, request: 'web.Request')` (method) — POST /webhooks/{route_name} — receive and process a webhook event.
- L643 `_validate_signature(self, request: 'web.Request', body: bytes, secret: str)` (method) — Validate webhook signature (GitHub, GitLab, Svix, generic HMAC-SHA256).
- L699 `_validate_svix_signature(self, body: bytes, secret: str, msg_id: str, timestamp: str, signature_header: str, tolerance_seconds: int=300)` (method) — Validate Svix-compatible signatures used by AgentMail webhooks.
- L753 `_render_prompt(self, template: str, payload: dict, event_type: str, route_name: str)` (method) — Render a prompt template with the webhook payload.
- L793 `_render_delivery_extra(self, extra: dict, payload: dict)` (method) — Render delivery_extra template values with payload data.
- L809 `_direct_deliver(self, content: str, delivery: dict)` (method) — Deliver *content* directly without invoking the agent.
- L837 `_deliver_github_comment(self, content: str, delivery: dict)` (method) — Post agent response as a GitHub PR/issue comment via ``gh`` CLI.
- L891 `_deliver_cross_platform(self, platform_name: str, content: str, delivery: dict)` (method) — Route response to another platform (telegram, discord, etc.).
