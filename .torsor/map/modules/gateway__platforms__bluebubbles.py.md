---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/bluebubbles.py

Symbols in `gateway/platforms/bluebubbles.py`.

- L76 `_redact(text: str)` (function) — Redact phone numbers and emails from log output.
- L87 `check_bluebubbles_requirements()` (function)
- L96 `_normalize_server_url(raw: str)` (function)
- L112 `BlueBubblesAdapter` (class)
- L117 `__init__(self, config: PlatformConfig)` (method)
- L158 `_api_url(self, path: str)` (method)
- L163 `_compile_mention_patterns(raw: Any)` (method) — Compile group-mention wake words from config/env.
- L198 `_message_matches_mention_patterns(self, text: str)` (method)
- L203 `_clean_mention_text(self, text: str)` (method) — Strip a leading BlueBubbles wake word before dispatch.
- L218 `_api_get(self, path: str)` (method)
- L224 `_api_post(self, path: str, payload: Dict[str, Any])` (method)
- L234 `connect(self)` (method)
- L290 `disconnect(self)` (method)
- L303 `_webhook_url(self)` (method) — Compute the external webhook URL for BlueBubbles registration.
- L311 `_webhook_register_url(self)` (method) — Webhook URL registered with BlueBubbles, including the password as
- L326 `_webhook_register_url_for_log(self)` (method) — Webhook registration URL safe for logs.
- L333 `_find_registered_webhooks(self, url: str)` (method) — Return list of BB webhook entries matching *url*.
- L344 `_register_webhook(self)` (method) — Register this webhook URL with the BlueBubbles server.
- L393 `_unregister_webhook(self)` (method) — Unregister this webhook URL from the BlueBubbles server.
- L430 `_resolve_chat_guid(self, target: str)` (method) — Resolve an email/phone to a BlueBubbles chat GUID.
- L471 `_create_chat_for_handle(self, address: str, message: str)` (method) — Create a new chat by sending the first message to *address*.
- L493 `truncate_message(content: str, max_length: int=MAX_TEXT_LENGTH)` (method)
- L499 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method)
- L556 `_send_attachment(self, chat_id: str, file_path: str, filename: Optional[str]=None, caption: Optional[str]=None, is_audio_message: bool=False)` (method) — Send a file attachment via BlueBubbles multipart upload.
- L610 `send_image(self, chat_id: str, image_url: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method)
- L626 `send_image_file(self, chat_id: str, image_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method)
- L636 `send_voice(self, chat_id: str, audio_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method)
- L648 `send_video(self, chat_id: str, video_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method)
- L658 `send_document(self, chat_id: str, file_path: str, caption: Optional[str]=None, file_name: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method)
- L671 `send_animation(self, chat_id: str, animation_url: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method)
- L687 `send_typing(self, chat_id: str, metadata=None)` (method)
- L700 `stop_typing(self, chat_id: str)` (method)
- L717 `mark_read(self, chat_id: str)` (method)
- L740 `get_chat_info(self, chat_id: str)` (method)
- L771 `format_message(self, content: str)` (method)
- L778 `_download_attachment(self, att_guid: str, att_meta: Dict[str, Any])` (method) — Download an attachment from BlueBubbles and cache it locally.
- L842 `_extract_payload_record(self, payload: Dict[str, Any])` (method)
- L857 `_value(*candidates: Any)` (method)
- L863 `_handle_webhook(self, request)` (method)
