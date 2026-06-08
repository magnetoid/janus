---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/signal.py

Symbols in `gateway/platforms/signal.py`.

- L73 `_parse_comma_list(value: str)` (function) — Split a comma-separated string into a list, stripping whitespace.
- L78 `_guess_extension(data: bytes)` (function) — Guess file extension from magic bytes.
- L101 `_is_image_ext(ext: str)` (function)
- L105 `_is_audio_ext(ext: str)` (function)
- L118 `_ext_to_mime(ext: str)` (function) — Map file extension to MIME type.
- L123 `_render_mentions(text: str, mentions: list)` (function) — Replace Signal mention placeholders (\uFFFC) with readable @identifiers.
- L144 `_is_signal_service_id(value: str)` (function) — Return True if *value* already looks like a Signal service identifier.
- L157 `_looks_like_e164_number(value: str)` (function) — Return True for a plausible E.164 phone number.
- L165 `check_signal_requirements()` (function) — Check if Signal is configured (has URL and account).
- L174 `SignalAdapter` (class) — Signal messenger adapter using signal-cli HTTP daemon.
- L183 `__init__(self, config: PlatformConfig)` (method)
- L253 `connect(self)` (method) — Connect to signal-cli daemon and start SSE listener.
- L297 `disconnect(self)` (method) — Stop SSE listener and clean up.
- L332 `_sse_listener(self)` (method) — Listen for SSE events from signal-cli daemon.
- L401 `_health_monitor(self)` (method) — Monitor SSE connection health and force reconnect if stale.
- L427 `_force_reconnect(self)` (method) — Force SSE reconnection by closing the current response.
- L442 `_handle_envelope(self, envelope: dict)` (method) — Process an incoming signal-cli envelope.
- L636 `_remember_recipient_identifiers(self, number: Optional[str], service_id: Optional[str])` (method) — Cache any number↔UUID mapping observed from Signal envelopes.
- L643 `_extract_contact_uuid(self, contact: Any, phone_number: str)` (method) — Best-effort extraction of a Signal service ID from listContacts output.
- L662 `_resolve_recipient(self, chat_id: str)` (method) — Return the preferred Signal recipient identifier for a direct chat.
- L698 `_fetch_attachment(self, attachment_id: str)` (method) — Fetch an attachment via JSON-RPC and cache it. Returns (path, ext).
- L732 `_rpc(self, method: str, params: dict, rpc_id: str=None, *, log_failures: bool=True, raise_on_rate_limit: bool=False, timeout: float=30.0)` (method) — Send a JSON-RPC 2.0 request to signal-cli daemon.
- L807 `_markdown_to_signal(text: str)` (method) — Convert markdown to plain text + Signal textStyles list.
- L946 `format_message(self, content: str)` (method) — Strip markdown for plain-text fallback (used by base class).
- L959 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a text message with native Signal formatting.
- L997 `_track_sent_timestamp(self, rpc_result)` (method) — Record outbound message timestamp for echo-back filtering.
- L1005 `send_typing(self, chat_id: str, metadata=None)` (method) — Send a typing indicator.
- L1058 `send_multiple_images(self, chat_id: str, images: List[Tuple[str, str]], metadata: Optional[Dict[str, Any]]=None, human_delay: float=0.0)` (method) — Send a batch of images via chunked Signal RPC calls.
- L1212 `_notify_batch_pacing(self, chat_id: str, next_batch_idx: int, total_batches: int, wait_s: float)` (method) — Inform the user when an inter-batch pacing wait crosses the
- L1230 `send_image(self, chat_id: str, image_url: str, caption: Optional[str]=None, **kwargs)` (method) — Send an image. Supports http(s):// and file:// URLs.
- L1276 `_send_attachment(self, chat_id: str, file_path: str, media_label: str, caption: Optional[str]=None)` (method) — Send any file as a Signal attachment via RPC.
- L1315 `send_document(self, chat_id: str, file_path: str, caption: Optional[str]=None, filename: Optional[str]=None, **kwargs)` (method) — Send a document/file attachment.
- L1326 `send_image_file(self, chat_id: str, image_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method) — Send a local image file as a native Signal attachment.
- L1341 `send_voice(self, chat_id: str, audio_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method) — Send an audio file as a Signal attachment.
- L1356 `send_video(self, chat_id: str, video_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method) — Send a video file as a Signal attachment.
- L1371 `_stop_typing_indicator(self, chat_id: str)` (method) — Stop a typing indicator loop for a chat.
- L1385 `stop_typing(self, chat_id: str)` (method) — Public interface for stopping typing — called by base adapter's
- L1394 `send_reaction(self, chat_id: str, emoji: str, target_author: str, target_timestamp: int)` (method) — Send a reaction emoji to a specific message via signal-cli RPC.
- L1427 `remove_reaction(self, chat_id: str, target_author: str, target_timestamp: int)` (method) — Remove a reaction by sending an empty-string emoji.
- L1454 `_extract_reaction_target(self, event: MessageEvent)` (method) — Extract (target_author, target_timestamp) from a MessageEvent.
- L1469 `_reactions_enabled(self, event: 'MessageEvent'=None)` (method) — Check if message reactions are enabled for this event.
- L1487 `on_processing_start(self, event: MessageEvent)` (method) — React with 👀 when processing begins.
- L1495 `on_processing_complete(self, event: MessageEvent, outcome: 'ProcessingOutcome')` (method) — Swap the 👀 reaction for ✅ (success) or ❌ (failure).
- L1520 `get_chat_info(self, chat_id: str)` (method) — Get information about a chat/contact.
