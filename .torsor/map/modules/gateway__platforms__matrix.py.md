---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/matrix.py

Symbols in `gateway/platforms/matrix.py`.

- L116 `_resolve_matrix_bang_command(name: str)` (function) — Resolve a ``!command`` token to a dispatchable Hermes command token.
- L167 `_normalize_matrix_bang_command(text: str)` (function) — Convert Matrix ``!command`` aliases to normal Hermes ``/command`` text.
- L181 `_MatrixApprovalPrompt` (class) — Tracks a pending Matrix reaction-based exec approval prompt.
- L184 `__init__(self, session_key: str, chat_id: str, message_id: str, resolved: bool=False)` (method)
- L228 `_looks_like_matrix_image_filename(text: str)` (function) — Return True when Matrix image body text is probably just a transport filename.
- L253 `_create_matrix_session(proxy_url: str | None)` (function) — Create an ``aiohttp.ClientSession`` whose proxy applies to *all* requests.
- L286 `_check_e2ee_deps()` (function) — Return True if mautrix E2EE dependencies are available.
- L309 `check_matrix_requirements()` (function) — Return True if the Matrix adapter can be used.
- L393 `_CryptoStateStore` (class) — Adapter that satisfies the mautrix crypto StateStore interface.
- L403 `__init__(self, client_state_store: Any, joined_rooms: set)` (method)
- L407 `is_encrypted(self, room_id: str)` (method)
- L410 `get_encryption_info(self, room_id: str)` (method)
- L415 `find_shared_rooms(self, user_id: str)` (method)
- L420 `MatrixAdapter` (class) — Gateway adapter for Matrix (any homeserver).
- L428 `__init__(self, config: PlatformConfig)` (method)
- L562 `_is_duplicate_event(self, event_id)` (method) — Return True if this event was already processed. Tracks the ID otherwise.
- L576 `_parse_thread_require_mention(config)` (method) — Parse thread_require_mention from config.extra or env var.
- L601 `_extract_server_ed25519(device_keys_obj: Any)` (method) — Extract the ed25519 identity key from a DeviceKeys object.
- L608 `_reverify_keys_after_upload(self, client: Any, local_ed25519: str)` (method) — Re-query the server after share_keys() and verify our ed25519 key matches.
- L632 `_verify_device_keys_on_server(self, client: Any, olm: Any)` (method) — Verify our device keys are on the homeserver after loading crypto state.
- L710 `connect(self)` (method) — Connect to the Matrix homeserver and start syncing.
- L1035 `disconnect(self)` (method) — Disconnect from Matrix.
- L1070 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a message to a Matrix room.
- L1147 `get_chat_info(self, chat_id: str)` (method) — Return room name and type (dm/group).
- L1169 `send_typing(self, chat_id: str, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a typing indicator.
- L1179 `stop_typing(self, chat_id: str)` (method) — Clear the typing indicator.
- L1188 `edit_message(self, chat_id: str, message_id: str, content: str, *, finalize: bool=False)` (method) — Edit an existing message (via m.replace).
- L1220 `send_image(self, chat_id: str, image_url: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Download an image URL and upload it to Matrix.
- L1275 `send_image_file(self, chat_id: str, image_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Upload a local image file to Matrix.
- L1288 `send_document(self, chat_id: str, file_path: str, caption: Optional[str]=None, file_name: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Upload a local file as a document.
- L1302 `send_voice(self, chat_id: str, audio_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Upload an audio file as a voice message (MSC3245 native voice).
- L1321 `send_video(self, chat_id: str, video_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Upload a video file.
- L1334 `send_exec_approval(self, chat_id: str, command: str, session_key: str, description: str='dangerous command', metadata: Optional[dict]=None)` (method) — Send a reaction-based exec approval prompt for Matrix.
- L1384 `format_message(self, content: str)` (method) — Pass-through — Matrix supports standard Markdown natively.
- L1394 `_upload_and_send(self, room_id: str, data: bytes, filename: str, content_type: str, msgtype: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None, is_voice: bool=False)` (method) — Upload bytes to Matrix and send as a media message.
- L1478 `_send_local_file(self, room_id: str, file_path: str, msgtype: str, caption: Optional[str]=None, reply_to: Optional[str]=None, file_name: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None, is_voice: bool=False)` (method) — Read a local file and upload it.
- L1508 `_sync_loop(self)` (method) — Continuously sync with the homeserver.
- L1585 `_is_self_sender(self, sender: str)` (method) — Return True if the sender refers to the bot's own account.
- L1605 `_is_system_or_bridge_sender(sender: str)` (method) — Return True if the sender looks like a system / bridge / appservice
- L1641 `_on_room_message(self, event: Any)` (method) — Handle incoming room message events (text, media).
- L1774 `_resolve_message_context(self, room_id: str, sender: str, event_id: str, body: str, source_content: dict, relates_to: dict)` (method) — Shared mention/thread/DM gating for text and media handlers.
- L1875 `_handle_text_message(self, room_id: str, sender: str, event_id: str, event_ts: float, source_content: dict, relates_to: dict)` (method) — Process a text message event.
- L1947 `_handle_media_message(self, room_id: str, sender: str, event_id: str, event_ts: float, source_content: dict, relates_to: dict, msgtype: str)` (method) — Process a media message event (image, audio, video, file).
- L2126 `_on_invite(self, event: Any)` (method) — Auto-join rooms when invited.
- L2137 `_join_room_by_id(self, room_id: str)` (method) — Join a room by ID and refresh local caches on success.
- L2153 `_join_pending_invites(self, sync_data: Dict[str, Any])` (method) — Join rooms still present in rooms.invite after sync processing.
- L2169 `_send_reaction(self, room_id: str, event_id: str, emoji: str)` (method) — Send an emoji reaction to a message in a room.
- L2200 `_redact_reaction(self, room_id: str, reaction_event_id: str, reason: str='')` (method) — Remove a reaction by redacting its event.
- L2209 `_schedule_reaction_redaction(self, room_id: str, reaction_event_id: str, reason: str='')` (method) — Redact a reaction after a short delay so message delivery settles.
- L2238 `on_processing_start(self, event: MessageEvent)` (method) — Add eyes reaction when the agent starts processing a message.
- L2249 `on_processing_complete(self, event: MessageEvent, outcome: ProcessingOutcome)` (method) — Replace eyes with checkmark (success) or cross (failure).
- L2277 `_on_reaction(self, event: Any)` (method) — Handle incoming reaction events.
- L2343 `_redact_bot_approval_reactions(self, room_id: str, prompt: '_MatrixApprovalPrompt')` (method) — Redact the bot's seed ✅/❎ reactions, leaving only the user's reaction.
- L2357 `_text_batch_key(self, event: MessageEvent)` (method) — Session-scoped key for text message batching.
- L2371 `_enqueue_text_event(self, event: MessageEvent)` (method) — Buffer a text event and reset the flush timer.
- L2396 `_flush_text_batch(self, key: str)` (method) — Wait for the quiet period then dispatch the aggregated text.
- L2424 `_background_read_receipt(self, room_id: str, event_id: str)` (method) — Fire-and-forget read receipt with error logging.
- L2435 `send_read_receipt(self, room_id: str, event_id: str)` (method) — Send a read receipt (m.read) for an event.
- L2465 `redact_message(self, room_id: str, event_id: str, reason: str='')` (method) — Redact (delete) a message or event from a room.
- L2490 `create_room(self, name: str='', topic: str='', invite: Optional[list]=None, is_direct: bool=False, preset: str='private_chat')` (method) — Create a new Matrix room.
- L2523 `invite_user(self, room_id: str, user_id: str)` (method) — Invite a user to a room.
- L2541 `set_presence(self, state: str='online', status_msg: str='')` (method) — Set the bot's presence status.
- L2568 `_send_simple_message(self, chat_id: str, text: str, msgtype: str)` (method) — Send a simple message (emote, notice) with optional HTML formatting.
- L2594 `_is_dm_room(self, room_id: str)` (method) — Check if a room is a DM.
- L2611 `_refresh_dm_cache(self)` (method) — Refresh the DM room cache from m.direct account data.
- L2641 `_build_text_message_content(self, text: str, msgtype: str='m.text')` (method) — Build Matrix text content with HTML and outbound mention metadata.
- L2656 `_extract_outbound_mentions(self, text: str)` (method) — Return unique Matrix user IDs mentioned in outbound text.
- L2668 `_inject_outbound_mention_links(self, text: str)` (method) — Wrap outbound Matrix mentions in markdown links outside code spans.
- L2685 `_protect_outbound_mention_regions(self, text: str)` (method) — Protect markdown regions where outbound mentions should stay literal.
- L2712 `_is_bot_mentioned(self, body: str, formatted_body: Optional[str]=None, mention_user_ids: Optional[list]=None)` (method) — Return True if the bot is mentioned in the message.
- L2745 `_strip_mention(self, body: str)` (method) — Remove explicit bot mentions from message body.
- L2775 `_get_display_name(self, room_id: str, user_id: str)` (method) — Get a user's display name in a room, falling back to user_id.
- L2792 `_mxc_to_http(self, mxc_url: str)` (method) — Convert mxc://server/media_id to an HTTP download URL.
- L2799 `_markdown_to_html(self, text: str)` (method) — Convert Markdown to Matrix-compatible HTML (org.matrix.custom.html).
- L2833 `_sanitize_link_url(url: str)` (method) — Sanitize a URL for use in an href attribute.
- L2842 `_markdown_to_html_fallback(text: str)` (method) — Comprehensive regex Markdown-to-HTML for Matrix.
