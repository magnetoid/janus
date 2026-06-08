---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/qqbot/adapter.py

Symbols in `gateway/platforms/qqbot/adapter.py`.

- L78 `QQCloseError` (class) — Raised when QQ WebSocket closes with a specific code.
- L84 `__init__(self, code, reason='')` (method)
- L139 `check_qq_requirements()` (function) — Check if QQ runtime dependencies are available.
- L144 `_coerce_list(value: Any)` (function) — Coerce config values into a trimmed string list.
- L154 `QQAdapter` (class) — QQ Bot adapter backed by the official QQ Bot WebSocket Gateway + REST API.
- L164 `_log_tag(self)` (method) — Log prefix including app_id for multi-instance disambiguation.
- L171 `_fail_pending(self, reason: str)` (method) — Fail all pending response futures.
- L178 `_mark_transport_disconnected(self)` (method) — Mark QQ WS down without stopping the reconnect loop.
- L196 `is_connected(self)` (method) — Return True only when the QQ WebSocket transport is usable.
- L200 `__init__(self, config: PlatformConfig)` (method)
- L269 `name(self)` (method)
- L273 `enforces_own_access_policy(self)` (method) — QQBot gates DM/group access at intake via dm_policy/group_policy.
- L281 `connect(self)` (method) — Authenticate, obtain gateway URL, and open the WebSocket.
- L338 `disconnect(self)` (method) — Close all connections and stop listeners.
- L363 `_cleanup(self)` (method) — Close WebSocket, HTTP session, and client.
- L387 `_ensure_token(self)` (method) — Return a valid access token, refreshing if needed (with singleflight).
- L422 `_get_gateway_url(self)` (method) — Fetch the WebSocket gateway URL from the REST API.
- L448 `_open_ws(self, gateway_url: str)` (method) — Open a WebSocket connection to the QQ Bot gateway.
- L479 `_listen_loop(self)` (method) — Read WebSocket events and reconnect on errors.
- L657 `_reconnect(self, backoff_idx: int)` (method) — Attempt to reconnect the WebSocket. Returns True on success.
- L680 `_read_events(self)` (method) — Read WebSocket frames until connection closes.
- L705 `_heartbeat_loop(self)` (method) — Send periodic heartbeats (QQ Gateway expects op 1 heartbeat with latest seq).
- L724 `_send_identify(self)` (method) — Send op 2 Identify to authenticate the WebSocket connection.
- L761 `_send_resume(self)` (method) — Send op 6 Resume to re-authenticate after a reconnection.
- L795 `_create_task(coro)` (method) — Schedule a coroutine, silently skipping if no event loop is running.
- L807 `_dispatch_payload(self, payload: Dict[str, Any])` (method) — Route inbound WebSocket payloads (dispatch synchronously, spawn async handlers).
- L888 `_handle_ready(self, d: Any)` (method) — Handle the READY event — store session_id for resume.
- L899 `_parse_json(raw: Any)` (method)
- L908 `_next_msg_seq(msg_id: str)` (method) — Generate a message sequence number in 0..65535 range.
- L918 `handle_message(self, event: MessageEvent)` (method) — Cache the last message ID per chat, then delegate to base.
- L924 `_on_message(self, event_type: str, d: Any)` (method) — Process an inbound QQ Bot message event.
- L955 `set_interaction_callback(self, callback: Optional[Callable[[InteractionEvent], Awaitable[None]]])` (method) — Register (or clear) the interaction callback.
- L968 `_on_interaction(self, d: Any)` (method) — Handle an ``INTERACTION_CREATE`` event.
- L1025 `_acknowledge_interaction(self, interaction_id: str, code: int=0)` (method) — ACK a button interaction via ``PUT /interactions/{id}``.
- L1068 `_parse_gateway_session_key(session_key: str)` (method) — Parse ``agent:main:<platform>:<chat_type>:<chat_id>[:<user_id>]``.
- L1082 `_is_authorized_interaction_for_session(self, event: InteractionEvent, session_key: str)` (method) — Authorize approval/update interactions against session + operator.
- L1107 `_default_interaction_dispatch(self, event: InteractionEvent)` (method) — Route ``INTERACTION_CREATE`` button clicks to the right subsystem.
- L1183 `_write_update_response(answer: str, operator: str='')` (method) — Atomically write the update-prompt answer to ``.update_response``.
- L1205 `_handle_c2c_message(self, d: Dict[str, Any], msg_id: str, content: str, author: Dict[str, Any], timestamp: str)` (method) — Handle a C2C (private) message event.
- L1300 `_handle_group_message(self, d: Dict[str, Any], msg_id: str, content: str, author: Dict[str, Any], timestamp: str)` (method) — Handle a group @-message event.
- L1365 `_handle_guild_message(self, d: Dict[str, Any], msg_id: str, content: str, author: Dict[str, Any], timestamp: str)` (method) — Handle a guild/channel message event.
- L1440 `_handle_dm_message(self, d: Dict[str, Any], msg_id: str, content: str, author: Dict[str, Any], timestamp: str)` (method) — Handle a guild DM message event.
- L1514 `_process_quoted_context(self, d: Dict[str, Any])` (method) — Process the quoted message a user is replying to.
- L1609 `_merge_quote_into(text: str, quote_block: str)` (method) — Prepend ``quote_block`` to *text*, separated by a blank line.
- L1622 `_detect_message_type(media_urls: list, media_types: list)` (method) — Determine MessageType from attachment content types.
- L1641 `_process_attachments(self, attachments: Any)` (method) — Process inbound attachments (all message types).
- L1754 `_download_and_cache(self, url: str, content_type: str, original_name: str='')` (method) — Download a URL and cache it locally.
- L1800 `_is_voice_content_type(content_type: str, filename: str)` (method) — Check if an attachment is a voice/audio message.
- L1821 `_qq_media_headers(self)` (method) — Return Authorization headers for QQ multimedia CDN downloads.
- L1832 `_stt_voice_attachment(self, url: str, content_type: str, filename: str, *, asr_refer_text: Optional[str]=None, voice_wav_url: Optional[str]=None)` (method) — Download a voice attachment, convert to wav, and transcribe.
- L1956 `_convert_audio_to_wav_file(self, audio_data: bytes, filename: str)` (method) — Convert audio bytes to a temp .wav file using pilk (SILK) or ffmpeg.
- L2007 `_guess_ext_from_data(data: bytes)` (method) — Guess file extension from magic bytes.
- L2027 `_looks_like_silk(data: bytes)` (method) — Check if bytes look like a SILK audio file.
- L2031 `_convert_silk_to_wav(self, src_path: str, wav_path: str)` (method) — Convert audio file to WAV using the pilk library.
- L2085 `_convert_raw_to_wav(self, audio_data: bytes, wav_path: str)` (method) — Last resort: try writing audio data as raw PCM 16-bit mono 16kHz WAV.
- L2104 `_convert_ffmpeg_to_wav(self, src_path: str, wav_path: str)` (method) — Convert audio file to WAV using ffmpeg.
- L2149 `_resolve_stt_config(self)` (method) — Resolve STT backend configuration from config/environment.
- L2205 `_call_stt(self, wav_path: str)` (method) — Call an OpenAI-compatible STT API to transcribe a wav file.
- L2256 `_convert_audio_to_wav(self, audio_data: bytes, source_url: str)` (method) — Convert audio bytes to .wav using pilk (SILK) or ffmpeg, caching the result.
- L2321 `_api_request(self, method: str, path: str, body: Optional[Dict[str, Any]]=None, timeout: float=DEFAULT_API_TIMEOUT)` (method) — Make an authenticated REST API request to QQ Bot API.
- L2357 `_upload_media(self, target_type: str, target_id: str, file_type: int, url: Optional[str]=None, file_data: Optional[str]=None, srv_send_msg: bool=False, file_name: Optional[str]=None)` (method) — Upload media and return file_info.
- L2408 `_wait_for_reconnection(self)` (method) — Wait for the WebSocket listener to reconnect.
- L2430 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a text or markdown message to a QQ user or group.
- L2463 `_send_chunk(self, chat_id: str, content: str, reply_to: Optional[str]=None)` (method) — Send a single chunk with retry + exponential backoff.
- L2513 `_send_c2c_text(self, openid: str, content: str, reply_to: Optional[str]=None, keyboard: Optional[InlineKeyboard]=None)` (method) — Send text to a C2C user via REST API.
- L2535 `_send_group_text(self, group_openid: str, content: str, reply_to: Optional[str]=None, keyboard: Optional[InlineKeyboard]=None)` (method) — Send text to a group via REST API.
- L2559 `_send_guild_text(self, channel_id: str, content: str, reply_to: Optional[str]=None)` (method) — Send text to a guild channel via REST API.
- L2575 `send_with_keyboard(self, chat_id: str, content: str, keyboard: InlineKeyboard, reply_to: Optional[str]=None)` (method) — Send a single text message with an inline keyboard attached.
- L2624 `send_approval_request(self, chat_id: str, req: ApprovalRequest, reply_to: Optional[str]=None)` (method) — Send a 3-button approval request (``allow-once / allow-always / deny``).
- L2656 `send_exec_approval(self, chat_id: str, command: str, session_key: str, description: str='dangerous command', metadata: Optional[Dict[str, Any]]=None)` (method) — Send a button-based exec-approval prompt for a dangerous command.
- L2691 `send_update_prompt(self, chat_id: str, prompt: str, default: str='', session_key: str='', metadata: Optional[Dict[str, Any]]=None)` (method) — Send a Yes/No update-confirmation prompt with inline buttons.
- L2721 `_build_text_body(self, content: str, reply_to: Optional[str]=None)` (method) — Build the message body for C2C/group text sending.
- L2751 `send_image(self, chat_id: str, image_url: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send an image natively via QQ Bot API upload.
- L2777 `send_image_file(self, chat_id: str, image_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method) — Send a local image file natively.
- L2791 `send_voice(self, chat_id: str, audio_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method) — Send a voice message natively.
- L2805 `send_video(self, chat_id: str, video_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method) — Send a video natively.
- L2819 `send_document(self, chat_id: str, file_path: str, caption: Optional[str]=None, file_name: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method) — Send a file/document natively.
- L2840 `_send_media(self, chat_id: str, media_source: str, file_type: int, kind: str, caption: Optional[str]=None, reply_to: Optional[str]=None, file_name: Optional[str]=None)` (method) — Upload media and send as a native message.
- L2966 `_upload_local_file(self, chat_type: str, chat_id: str, media_source: str, file_type: int, file_name: Optional[str])` (method) — Chunked-upload a local file and return ``(resolved_name, complete_response)``.
- L3014 `_load_media(self, source: str, file_name: Optional[str]=None)` (method) — Load media from URL or local path. Returns (base64_or_url, content_type, filename).
- L3056 `send_typing(self, chat_id: str, metadata=None)` (method) — Send an input notify to a C2C user (only supported for C2C).
- L3100 `format_message(self, content: str)` (method) — Format message for QQ.
- L3114 `get_chat_info(self, chat_id: str)` (method) — Return chat info based on chat type heuristics.
- L3127 `_is_url(source: str)` (method)
- L3130 `_guess_chat_type(self, chat_id: str)` (method) — Determine chat type from stored inbound metadata, fallback to 'c2c'.
- L3137 `_strip_at_mention(content: str)` (method) — Strip the @bot mention prefix from group message content.
- L3145 `_is_dm_allowed(self, user_id: str)` (method)
- L3152 `_is_group_allowed(self, group_id: str, user_id: str)` (method)
- L3160 `_entry_matches(entries: List[str], target: str)` (method)
- L3168 `_parse_qq_timestamp(self, raw: str)` (method) — Parse QQ API timestamp (ISO 8601 string or integer ms).
- L3186 `_is_duplicate(self, msg_id: str)` (method)
