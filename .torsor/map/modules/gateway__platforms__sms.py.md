---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/sms.py

Symbols in `gateway/platforms/sms.py`.

- L47 `check_sms_requirements()` (function) — Check if SMS adapter dependencies are available.
- L56 `SmsAdapter` (class) — Twilio SMS <-> Hermes gateway adapter.
- L66 `__init__(self, config: PlatformConfig)` (method)
- L79 `_basic_auth_header(self)` (method) — Build HTTP Basic auth header value for Twilio.
- L89 `connect(self)` (method)
- L143 `disconnect(self)` (method)
- L153 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method)
- L209 `get_chat_info(self, chat_id: str)` (method)
- L216 `format_message(self, content: str)` (method) — Strip markdown — SMS renders it as literal characters.
- L224 `_validate_twilio_signature(self, url: str, post_params: dict, signature: str)` (method) — Validate ``X-Twilio-Signature`` header (HMAC-SHA1, base64).
- L243 `_check_signature(self, url: str, post_params: dict, signature: str)` (method) — Compute and compare a single Twilio signature.
- L259 `_port_variant_url(url: str)` (method) — Return the URL with the default port toggled, or None.
- L292 `_handle_webhook(self, request)` (method)
