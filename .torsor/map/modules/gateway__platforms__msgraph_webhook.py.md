---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/msgraph_webhook.py

Symbols in `gateway/platforms/msgraph_webhook.py`.

- L40 `check_msgraph_webhook_requirements()` (function) — Return whether required webhook dependencies are available.
- L45 `MSGraphWebhookAdapter` (class) — Receive Microsoft Graph change notifications and surface them internally.
- L48 `__init__(self, config: PlatformConfig)` (method)
- L77 `_string_or_none(value: Any)` (method)
- L84 `_normalize_path(path: Any)` (method)
- L89 `_build_receipt_key(notification: Dict[str, Any])` (method)
- L96 `_normalize_resource_value(resource: str)` (method)
- L100 `_parse_allowed_source_cidrs(raw: Any)` (method) — Parse an optional list of CIDR ranges allowed to POST to the webhook.
- L133 `set_notification_scheduler(self, scheduler: Optional[NotificationScheduler])` (method)
- L136 `_source_allowlist_required_but_missing(self)` (method)
- L139 `connect(self)` (method)
- L173 `disconnect(self)` (method)
- L179 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method)
- L189 `get_chat_info(self, chat_id: str)` (method)
- L192 `_handle_health(self, request: 'web.Request')` (method)
- L205 `_handle_validation(self, request: 'web.Request')` (method) — Handle Microsoft Graph subscription validation handshake.
- L221 `_handle_notification(self, request: 'web.Request')` (method)
- L286 `_source_ip_allowed(self, request: 'web.Request')` (method) — Return True if the request's source IP is in the configured allowlist.
- L306 `_resource_accepted(self, resource: str)` (method)
- L326 `_verify_client_state(self, notification: Dict[str, Any])` (method) — Verify the Graph-supplied clientState matches the configured secret.
- L343 `_has_seen_receipt(self, receipt_key: str)` (method)
- L346 `_remember_receipt(self, receipt_key: str)` (method)
- L353 `_build_message_event(self, notification: Dict[str, Any], receipt_key: Optional[str])` (method)
- L375 `_render_prompt(self, notification: Dict[str, Any])` (method)
- L388 `_render_template(self, template: str, payload: Dict[str, Any])` (method)
- L405 `_schedule_notification(self, notification: Dict[str, Any], event: MessageEvent)` (method)
