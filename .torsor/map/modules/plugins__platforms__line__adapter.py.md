---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/platforms/line/adapter.py

Symbols in `plugins/platforms/line/adapter.py`.

- L174 `strip_markdown_preserving_urls(text: str)` (function) — Strip Markdown that LINE can't render, but keep URLs usable.
- L212 `split_for_line(text: str, max_chars: int=LINE_SAFE_BUBBLE_CHARS)` (function) — Split ``text`` into LINE-sized bubbles, preferring paragraph/line breaks.
- L258 `verify_line_signature(body: bytes, signature: str, channel_secret: str)` (function) — Verify a LINE webhook's ``X-Line-Signature`` header.
- L283 `State` (class)
- L291 `_CacheEntry` (class)
- L299 `RequestCache` (class) — In-memory cache for slow-LLM postback retrieval.
- L307 `__init__(self, ttl_seconds: int=3600, pending_ttl_seconds: int=86400)` (method)
- L316 `register_pending(self, chat_id: str)` (method)
- L321 `get(self, request_id: str)` (method)
- L324 `set_ready(self, request_id: str, payload: Any)` (method)
- L332 `set_error(self, request_id: str, message: str)` (method)
- L340 `mark_delivered(self, request_id: str)` (method)
- L347 `find_pending_for_chat(self, chat_id: str)` (method)
- L353 `prune(self)` (method)
- L373 `_MessageDeduplicator` (class) — Bounded LRU of LINE webhook event IDs to ignore at-least-once retries.
- L376 `__init__(self, max_size: int=1000)` (method)
- L380 `is_duplicate(self, event_id: str)` (method)
- L397 `_resolve_chat(source: Dict[str, Any])` (function) — Return ``(chat_id, chat_type)`` from a LINE event ``source`` block.
- L417 `_allowed_for_source(source: Dict[str, Any], *, allow_all: bool, user_ids: Set[str], group_ids: Set[str], room_ids: Set[str])` (function) — Three-list gate — credit PR #18153.
- L445 `_LineClient` (class) — Thin async wrapper around the LINE Messaging API.
- L453 `__init__(self, channel_access_token: str, *, timeout: float=15.0)` (method)
- L461 `reply(self, reply_token: str, messages: List[Dict[str, Any]])` (method)
- L474 `push(self, chat_id: str, messages: List[Dict[str, Any]])` (method)
- L487 `loading(self, chat_id: str, seconds: int=60)` (method) — Loading indicator (DM only). LINE rejects this for groups/rooms.
- L505 `fetch_content(self, message_id: str)` (method) — Download an inbound media message's binary content.
- L516 `get_bot_user_id(self)` (method) — Fetch this channel's own userId so we can filter self-messages.
- L535 `_text_message(text: str)` (function) — Build a LINE text message object, capped to per-bubble max.
- L542 `_image_message(original_url: str, preview_url: Optional[str]=None)` (function)
- L550 `_audio_message(url: str, duration_ms: int=1000)` (function)
- L558 `_video_message(url: str, preview_url: str)` (function)
- L566 `build_postback_button_message(text: str, button_label: str, request_id: str)` (function) — Template Buttons message — the slow-LLM postback bubble.
- L611 `_is_system_bypass(content: str)` (function)
- L621 `_csv_set(value: str)` (function)
- L627 `_truthy_env(name: str, default: bool=False)` (function)
- L638 `LineAdapter` (class) — LINE Messaging API gateway adapter.
- L644 `__init__(self, config, **kwargs)` (method)
- L743 `connect(self)` (method)
- L824 `disconnect(self)` (method)
- L862 `_handle_health(self, request)` (method)
- L866 `_handle_webhook(self, request)` (method)
- L897 `_dispatch_event(self, event: Dict[str, Any])` (method)
- L932 `_handle_message_event(self, event: Dict[str, Any])` (method)
- L996 `_handle_postback_event(self, event: Dict[str, Any])` (method) — User tapped the slow-LLM postback button — deliver cached payload.
- L1055 `_download_media(self, message_id: str, msg_type: str)` (method)
- L1079 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method)
- L1104 `_send_text_chunks(self, chat_id: str, content: str, *, force_push: bool)` (method)
- L1135 `_consume_reply_token(self, chat_id: str)` (method) — Consume a stashed reply token if present and unexpired.
- L1148 `send_typing(self, chat_id: str, metadata=None)` (method) — Trigger LINE's loading-animation indicator (DM only).
- L1153 `get_chat_info(self, chat_id: str)` (method) — Best-effort chat info derived from the chat_id prefix.
- L1165 `format_message(self, content: str)` (method) — Strip Markdown that LINE can't render. URLs are preserved.
- L1173 `_keep_typing(self, chat_id: str, *args, **kwargs)` (method) — Override the base loop to fire the postback button at threshold.
- L1226 `interrupt_session_activity(self, session_key: str, chat_id: str)` (method) — Resolve any orphan PENDING postback so the button doesn't loop.
- L1237 `_register_media(self, file_path: str, *, cleanup: bool=False)` (method) — Register a local file for HTTPS serving; return the URL token.
- L1259 `_media_url(self, token: str, filename: str)` (method) — Build the public HTTPS URL for a media token. PR #8398 style.
- L1273 `_handle_media(self, request)` (method) — Serve a registered local file over HTTPS for LINE's media URLs.
- L1320 `send_image_file(self, chat_id: str, image_path: str, caption: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method)
- L1350 `send_voice(self, chat_id: str, audio_path: str, duration_ms: int=1000, metadata: Optional[Dict[str, Any]]=None)` (method)
- L1374 `send_video(self, chat_id: str, video_path: str, preview_path: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method)
- L1419 `_send_messages(self, chat_id: str, messages: List[Dict[str, Any]])` (method) — Send already-built message objects, batched at 5/call.
- L1463 `_is_relative_to(child: Path, parent: Path)` (function) — Backport for Path.is_relative_to (Python 3.9+) — defensive against
- L1480 `check_requirements()` (function) — Plugin gate: require credentials AND aiohttp at runtime.
- L1493 `validate_config(config)` (function)
- L1504 `is_connected(config)` (function) — Surface in ``hermes status`` even before the adapter is instantiated.
- L1509 `_env_enablement()` (function) — Auto-seed PlatformConfig.extra from env-only setups.
- L1533 `_standalone_send(pconfig, chat_id: str, message: str, *, thread_id: Optional[str]=None, media_files: Optional[List[str]]=None, force_document: bool=False)` (function) — Out-of-process push delivery for cron jobs running detached from the gateway.
- L1578 `interactive_setup()` (function) — Minimal stdin wizard for ``hermes setup line``.
- L1620 `register(ctx)` (function) — Plugin entry point — called by the Hermes plugin system at startup.
