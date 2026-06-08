---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/wecom_callback.py

Symbols in `gateway/platforms/wecom_callback.py`.

- L61 `check_wecom_callback_requirements()` (function)
- L65 `WecomCallbackAdapter` (class)
- L66 `__init__(self, config: PlatformConfig)` (method)
- L88 `_user_app_key(corp_id: str, user_id: str)` (method)
- L92 `_normalize_apps(extra: Dict[str, Any])` (method)
- L113 `connect(self)` (method)
- L163 `disconnect(self)` (method)
- L176 `_cleanup(self)` (method)
- L190 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method)
- L235 `_resolve_app_for_chat(self, chat_id: str)` (method) — Pick the app associated with *chat_id*, falling back sensibly.
- L246 `get_chat_info(self, chat_id: str)` (method)
- L253 `_handle_health(self, request: web.Request)` (method)
- L256 `_handle_verify(self, request: web.Request)` (method) — GET endpoint — WeCom URL verification handshake.
- L271 `_handle_callback(self, request: web.Request)` (method) — POST endpoint — receive an encrypted message callback.
- L316 `_poll_loop(self)` (method) — Drain the message queue and dispatch to the gateway runner.
- L331 `_decrypt_request(self, app: Dict[str, Any], body: str, msg_signature: str, timestamp: str, nonce: str)` (method)
- L340 `_build_event(self, app: Dict[str, Any], xml_text: str)` (method)
- L376 `_crypt_for_app(self, app: Dict[str, Any])` (method)
- L383 `_get_app_by_name(self, name: Optional[str])` (method)
- L395 `_get_access_token(self, app: Dict[str, Any])` (method)
- L402 `_refresh_access_token(self, app: Dict[str, Any])` (method)
