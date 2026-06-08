---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/whatsapp.py

Symbols in `gateway/platforms/whatsapp.py`.

- L37 `_kill_port_process(port: int)` (function) — Kill any process listening on the given TCP port.
- L92 `_kill_stale_bridge_by_pidfile(session_path: Path)` (function) — Kill a bridge process recorded in a PID file from a previous run.
- L125 `_write_bridge_pidfile(session_path: Path, pid: int)` (function) — Write the bridge PID to a file for later cleanup.
- L133 `_terminate_bridge_process(proc, *, force: bool=False)` (function) — Terminate the bridge process using process-tree semantics where possible.
- L194 `check_whatsapp_requirements()` (function) — Check if WhatsApp dependencies are available.
- L218 `WhatsAppAdapter` (class) — WhatsApp adapter.
- L250 `__init__(self, config: PlatformConfig)` (method)
- L299 `_coerce_float_extra(self, key: str, default: float)` (method) — Read a float from ``config.extra``, guarding against bad/non-finite values.
- L318 `_effective_reply_prefix(self)` (method) — Return the prefix the Node bridge will add in self-chat mode.
- L330 `_outgoing_chunk_limit(self)` (method) — Reserve room for the bridge-side prefix so final WhatsApp text fits.
- L337 `_whatsapp_require_mention(self)` (method)
- L345 `_whatsapp_free_response_chats(self)` (method)
- L354 `_coerce_allow_list(raw)` (method) — Parse allow_from / group_allow_from from config or env var.
- L363 `_is_broadcast_chat(chat_id: str)` (method) — True for WhatsApp pseudo-chats that aren't real conversations.
- L383 `enforces_own_access_policy(self)` (method) — WhatsApp gates DM/group access at intake via dm_policy/group_policy.
- L387 `_is_dm_allowed(self, sender_id: str)` (method) — Check whether a DM from the given sender should be processed.
- L396 `_is_group_allowed(self, chat_id: str)` (method) — Check whether a group chat should be processed.
- L405 `_compile_mention_patterns(self)` (method)
- L437 `_normalize_whatsapp_id(value: Optional[str])` (method)
- L445 `_bot_ids_from_message(self, data: Dict[str, Any])` (method)
- L453 `_message_is_reply_to_bot(self, data: Dict[str, Any])` (method)
- L459 `_message_mentions_bot(self, data: Dict[str, Any])` (method)
- L479 `_message_matches_mention_patterns(self, data: Dict[str, Any])` (method)
- L485 `_clean_bot_mention_text(self, text: str, data: Dict[str, Any])` (method)
- L496 `_should_process_message(self, data: Dict[str, Any])` (method)
- L530 `connect(self)` (method) — Start the WhatsApp bridge.
- L761 `_close_bridge_log(self)` (method) — Close the bridge log file handle if open.
- L770 `_check_managed_bridge_exit(self)` (method) — Return a fatal error message if the managed bridge child exited.
- L802 `disconnect(self)` (method) — Stop the WhatsApp bridge and clean up any orphaned processes.
- L853 `format_message(self, content: str)` (method) — Convert standard markdown to WhatsApp-compatible formatting.
- L910 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a message via the WhatsApp bridge.
- L971 `edit_message(self, chat_id: str, message_id: str, content: str, *, finalize: bool=False)` (method) — Edit a previously sent message via the WhatsApp bridge.
- L1004 `_send_media_to_bridge(self, chat_id: str, file_path: str, media_type: str, caption: Optional[str]=None, file_name: Optional[str]=None)` (method) — Send any media file via bridge /send-media endpoint.
- L1053 `send_image(self, chat_id: str, image_url: str, caption: Optional[str]=None, reply_to: Optional[str]=None)` (method) — Download image URL to cache, send natively via bridge.
- L1067 `send_image_file(self, chat_id: str, image_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method) — Send a local image file natively via bridge.
- L1078 `send_video(self, chat_id: str, video_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method) — Send a video natively via bridge — plays inline in WhatsApp.
- L1089 `send_voice(self, chat_id: str, audio_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method) — Send an audio file as a WhatsApp voice message via bridge.
- L1100 `send_document(self, chat_id: str, file_path: str, caption: Optional[str]=None, file_name: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method) — Send a document/file as a downloadable attachment via bridge.
- L1115 `send_typing(self, chat_id: str, metadata=None)` (method) — Send typing indicator via bridge.
- L1137 `get_chat_info(self, chat_id: str)` (method) — Get information about a WhatsApp chat.
- L1163 `_poll_messages(self)` (method) — Poll the bridge for incoming messages.
- L1204 `_text_batch_key(self, event: MessageEvent)` (method) — Session-scoped key for text message batching.
- L1213 `_enqueue_text_event(self, event: MessageEvent)` (method) — Buffer a text event and reset the flush timer.
- L1241 `_flush_text_batch(self, key: str)` (method) — Wait for quiet period then dispatch aggregated text.
- L1260 `_build_message_event(self, data: Dict[str, Any])` (method) — Build a MessageEvent from bridge message data, downloading images to cache.
