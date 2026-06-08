---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/wecom.py

Symbols in `gateway/platforms/wecom.py`.

- L108 `check_wecom_requirements()` (function) — Check if WeCom runtime dependencies are available.
- L113 `_coerce_list(value: Any)` (function) — Coerce config values into a trimmed string list.
- L124 `_normalize_entry(raw: str)` (function) — Normalize allowlist entries such as ``wecom:user:foo``.
- L132 `_entry_matches(entries: List[str], target: str)` (function) — Case-insensitive allowlist match with ``*`` support.
- L142 `WeComAdapter` (class) — WeCom AI Bot adapter backed by a persistent WebSocket connection.
- L151 `__init__(self, config: PlatformConfig)` (method)
- L200 `connect(self)` (method) — Connect to the WeCom AI Bot gateway.
- L240 `disconnect(self)` (method) — Disconnect from WeCom.
- L271 `_cleanup_ws(self)` (method) — Close the live websocket/session, if any.
- L281 `_open_connection(self)` (method) — Open and authenticate a websocket connection.
- L310 `_wait_for_handshake(self, req_id: str)` (method) — Wait for the subscribe acknowledgement.
- L334 `_listen_loop(self)` (method) — Read websocket events forever, reconnecting on errors.
- L361 `_read_events(self)` (method) — Read websocket frames until the connection closes.
- L375 `_heartbeat_loop(self)` (method) — Send lightweight application-level pings.
- L395 `_dispatch_payload(self, payload: Dict[str, Any])` (method) — Route inbound websocket payloads.
- L414 `_fail_pending_responses(self, exc: Exception)` (method) — Fail all outstanding request futures.
- L421 `_send_json(self, payload: Dict[str, Any])` (method) — Send a raw JSON frame over the active websocket.
- L427 `_send_request(self, cmd: str, body: Dict[str, Any], timeout: float=REQUEST_TIMEOUT_SECONDS)` (method) — Send a JSON request and await the correlated response.
- L442 `_send_reply_request(self, reply_req_id: str, body: Dict[str, Any], cmd: str=APP_CMD_RESPONSE, timeout: float=REQUEST_TIMEOUT_SECONDS)` (method) — Send a reply frame correlated to an inbound callback req_id.
- L469 `_new_req_id(prefix: str)` (method)
- L473 `_payload_req_id(payload: Dict[str, Any])` (method)
- L480 `_parse_json(raw: Any)` (method)
- L492 `_on_message(self, payload: Dict[str, Any])` (method) — Process an inbound WeCom message callback event.
- L573 `_text_batch_key(self, event: MessageEvent)` (method) — Session-scoped key for text message batching.
- L582 `_enqueue_text_event(self, event: MessageEvent)` (method) — Buffer a text event and reset the flush timer.
- L612 `_flush_text_batch(self, key: str)` (method) — Wait for the quiet period then dispatch the aggregated text.
- L652 `_extract_text(body: Dict[str, Any])` (method) — Extract plain text and quoted text from a callback payload.
- L702 `_extract_media(self, body: Dict[str, Any])` (method) — Best-effort extraction of inbound media to local cache paths.
- L749 `_cache_media(self, kind: str, media: Dict[str, Any])` (method) — Cache an inbound image/file/media reference to local storage.
- L800 `_decode_base64(data: str)` (method)
- L805 `_detect_image_ext(data: bytes)` (method)
- L817 `_mime_for_ext(ext: str, fallback: str='application/octet-stream')` (method)
- L821 `_guess_extension(url: str, content_type: str, fallback: str)` (method)
- L831 `_guess_filename(url: str, content_disposition: Optional[str], content_type: str)` (method)
- L844 `_derive_message_type(body: Dict[str, Any], text: str, media_types: List[str])` (method) — Choose the normalized inbound message type.
- L859 `enforces_own_access_policy(self)` (method) — WeCom gates DM/group access at intake via dm_policy/group_policy.
- L863 `_is_dm_allowed(self, sender_id: str)` (method)
- L870 `_is_group_allowed(self, chat_id: str, sender_id: str)` (method)
- L882 `_resolve_group_cfg(self, chat_id: str)` (method)
- L894 `_remember_reply_req_id(self, message_id: str, req_id: str)` (method)
- L903 `_remember_chat_req_id(self, chat_id: str, req_id: str)` (method) — Cache the most recent inbound req_id per chat.
- L920 `_reply_req_id_for_message(self, reply_to: Optional[str])` (method)
- L931 `_guess_mime_type(filename: str)` (method)
- L940 `_normalize_content_type(content_type: str, filename: str)` (method)
- L950 `_detect_wecom_media_type(content_type: str)` (method)
- L961 `_apply_file_size_limits(file_size: int, detected_type: str, content_type: Optional[str]=None)` (method)
- L1025 `_response_error(response: Dict[str, Any])` (method)
- L1033 `_raise_for_wecom_error(cls, response: Dict[str, Any], operation: str)` (method)
- L1039 `_decrypt_file_bytes(encrypted_data: bytes, aes_key: str)` (method)
- L1068 `_download_remote_bytes(self, url: str, max_bytes: int)` (method)
- L1113 `_looks_like_url(media_source: str)` (method)
- L1117 `_load_outbound_media(self, media_source: str, file_name: Optional[str]=None)` (method)
- L1152 `_prepare_outbound_media(self, media_source: str, file_name: Optional[str]=None)` (method)
- L1168 `_upload_media_bytes(self, data: bytes, media_type: str, filename: str)` (method)
- L1226 `_send_media_message(self, chat_id: str, media_type: str, media_id: str)` (method)
- L1238 `_send_reply_markdown(self, reply_req_id: str, content: str)` (method)
- L1249 `_send_reply_media_message(self, reply_req_id: str, media_type: str, media_id: str)` (method)
- L1265 `_send_followup_markdown(self, chat_id: str, content: str, reply_to: Optional[str]=None)` (method)
- L1278 `_send_media_source(self, chat_id: str, media_source: str, caption: Optional[str]=None, file_name: Optional[str]=None, reply_to: Optional[str]=None)` (method)
- L1361 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send markdown to a WeCom chat via proactive ``aibot_send_msg``.
- L1407 `send_image(self, chat_id: str, image_url: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method)
- L1430 `send_image_file(self, chat_id: str, image_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method)
- L1446 `send_document(self, chat_id: str, file_path: str, caption: Optional[str]=None, file_name: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method)
- L1464 `send_voice(self, chat_id: str, audio_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method)
- L1480 `send_video(self, chat_id: str, video_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method)
- L1496 `send_typing(self, chat_id: str, metadata=None)` (method) — WeCom does not expose typing indicators in this adapter.
- L1500 `get_chat_info(self, chat_id: str)` (method) — Return minimal chat info.
- L1519 `qr_scan_for_bot_info(*, timeout_seconds: int=_QR_POLL_TIMEOUT)` (function) — Run the WeCom QR scan flow to obtain bot_id and secret.
