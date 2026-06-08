---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/platforms/google_chat/adapter.py

Symbols in `plugins/platforms/google_chat/adapter.py`.

- L76 `_load_google_modules()` (function) — Lazily import the heavy google-cloud + googleapiclient stack.
- L191 `_is_retryable_error(exc: BaseException)` (function) — Classify outbound API errors as transient (retryable) vs permanent.
- L231 `check_google_chat_requirements()` (function) — Check if Google Chat optional dependencies are installed.
- L259 `_is_google_owned_host(url: str)` (function) — Return True iff *url* is https and targets a Google-owned domain.
- L275 `_redact_sensitive(text: str)` (function) — Sanitize subscription paths and email-like tokens from an error string.
- L302 `_mime_for_message_type(mime: str)` (function) — Map a MIME string to a hermes MessageType.
- L319 `_ThreadCountStore` (class) — Per-(chat_id, thread_name) inbound message counter, persisted to disk.
- L350 `__init__(self, path: _Path)` (method)
- L355 `load(self)` (method) — Load counts from disk. Safe to call multiple times.
- L396 `get(self, chat_id: str, thread_name: str)` (method) — Return the current count for (chat_id, thread_name), or 0.
- L400 `incr(self, chat_id: str, thread_name: str)` (method) — Increment count and write through to disk. Returns the
- L410 `_save(self)` (method) — Atomic write of the counts dict to disk.
- L429 `GoogleChatAdapter` (class) — Google Chat bot adapter using Pub/Sub pull + Chat REST API.
- L451 `__init__(self, config: PlatformConfig)` (method)
- L555 `_load_sa_credentials(self)` (method) — Load Service Account credentials from env or config.extra,
- L628 `_validate_config(self)` (method) — Return (project_id, subscription_path) after validation.
- L660 `_log_background_failure(future: Any)` (method)
- L667 `_loop_accepts_callbacks(loop: Optional[asyncio.AbstractEventLoop])` (method)
- L670 `_submit_on_loop(self, coro: Any)` (method) — Schedule a coroutine on the adapter loop from a Pub/Sub callback thread.
- L696 `_bot_id_cache_path(self)` (method) — Location where the resolved bot user_id is cached across restarts.
- L701 `_load_cached_bot_id(self)` (method)
- L711 `_save_cached_bot_id(self, bot_user_id: str)` (method)
- L722 `_resolve_bot_user_id(self)` (method) — Resolve ``users/{id}`` via Chat API members.list on a known space.
- L764 `connect(self)` (method) — Validate config, authenticate, start Pub/Sub pull, resolve bot id.
- L922 `disconnect(self)` (method) — Clean shutdown: stop accepting new messages, wait in-flight, close clients.
- L950 `_run_supervisor(self)` (method) — Run the streaming_pull with exponential backoff; fatal after 10 attempts.
- L1025 `_extract_message_payload(envelope: Dict[str, Any], ce_type: str='')` (method) — Detect Pub/Sub envelope format and return ``(message, space, format_name)``.
- L1136 `_on_pubsub_message(self, message: Any)` (method) — Pub/Sub callback — parse envelope and dispatch to asyncio loop.
- L1265 `_dispatch_message(self, msg: Dict[str, Any], envelope: Dict[str, Any])` (method) — Translate a Chat message payload to a MessageEvent and hand off.
- L1303 `_handle_setup_files_command(self, chat_id: str, thread_id: Optional[str], raw_text: str, sender_email: Optional[str]=None)` (method) — Run the in-chat OAuth setup flow for native attachment delivery.
- L1527 `_build_message_event(self, msg: Dict[str, Any], envelope: Dict[str, Any])` (method) — Parse a Chat API message into a hermes MessageEvent.
- L1653 `_download_attachment(self, attachment: Dict[str, Any])` (method) — Download an inbound attachment to the local cache; return (path, mime).
- L1771 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a text message.
- L1873 `edit_message(self, chat_id: str, message_id: str, content: str, *, finalize: bool=False)` (method) — Edit a previously sent message via ``messages.patch``.
- L1918 `delete_message(self, chat_id: str, message_id: str)` (method) — Delete a message — used sparingly (deletion creates a tombstone).
- L1955 `_patch_message(self, message_name: str, body: Dict[str, Any])` (method) — Update a message's text (and optionally cards) in-place.
- L1980 `_chunk_text(self, text: str)` (method)
- L2021 `format_message(cls, content: str)` (method) — Convert standard Markdown to Google Chat's formatting dialect.
- L2100 `_resolve_thread_id(self, reply_to: Optional[str], metadata: Optional[Dict[str, Any]], chat_id: Optional[str]=None)` (method) — Return the Google Chat thread resource name to reply under, or None.
- L2137 `_new_authed_http(self)` (method) — Return a fresh AuthorizedHttp.
- L2147 `_call_with_retry(self, sync_fn: Callable[[], Any], *, op_name: str='chat-api-call')` (method) — Run ``sync_fn`` in a thread with bounded retry + jittered backoff.
- L2193 `_create_message(self, chat_id: str, body: Dict[str, Any])` (method) — POST spaces/{space}/messages via REST, returning SendResult.
- L2245 `send_typing(self, chat_id: str, metadata: Any=None)` (method) — Post a visible 'Hermes is thinking…' marker message.
- L2344 `stop_typing(self, chat_id: str)` (method) — Stop the typing indicator — NO-OP when a live card is tracked.
- L2381 `on_processing_complete(self, event: MessageEvent, outcome: ProcessingOutcome)` (method) — Reap typing card(s) after the message-handling cycle ends.
- L2441 `_consume_typing_card_with_text(self, chat_id: str, text: str)` (method) — Patch the tracked typing card with ``text`` (no tombstone).
- L2473 `send_image(self, chat_id: str, image_url: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send an inline image via attachment URL (no upload).
- L2505 `send_image_file(self, chat_id: str, image_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs: Any)` (method)
- L2519 `send_document(self, chat_id: str, file_path: str, caption: Optional[str]=None, file_name: Optional[str]=None, reply_to: Optional[str]=None, **kwargs: Any)` (method)
- L2535 `send_voice(self, chat_id: str, audio_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs: Any)` (method)
- L2549 `send_video(self, chat_id: str, video_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs: Any)` (method)
- L2563 `send_animation(self, chat_id: str, animation_url: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Google Chat has no native animation type; fall back to send_image.
- L2594 `_is_app_auth_attachment_error(exc: HttpError)` (method) — Detect Google Chat's media.upload bot-auth rejection.
- L2613 `_load_per_user_chat_api(self, email: str)` (method) — Get (or build + cache) a user-authed Chat client for ``email``.
- L2661 `_acquire_user_chat_api(self, sender_email: Optional[str])` (method) — Resolve the user-authed Chat client for an outbound attachment.
- L2708 `_invalidate_user_creds(self, identity: Optional[str])` (method) — Drop creds for ``identity`` after an auth failure.
- L2724 `_send_file(self, chat_id: str, path: str, caption: Optional[str], mime_hint: Optional[str], thread_id: Optional[str]=None, override_filename: Optional[str]=None)` (method) — Native Chat attachment via user-OAuth media.upload.
- L2874 `_post_attachment_fallback(self, chat_id: str, path: str, filename: str, caption: Optional[str], thread_id: Optional[str])` (method) — Post a text notice when native attachment delivery is unavailable.
- L2919 `get_chat_info(self, chat_id: str)` (method) — Return {name, type, chat_id} for a space.
- L2946 `_validate_config(config: PlatformConfig)` (function) — Plugin-side config gate: require both Pub/Sub project and subscription.
- L2959 `_check_for_registry()` (function) — ``check_fn`` for the platform registry pass — stricter than the
- L2983 `_is_connected(config: PlatformConfig)` (function) — ``GatewayConfig.get_connected_platforms()`` polls this.
- L2988 `_env_enablement()` (function) — Seed ``PlatformConfig.extra`` from env vars during
- L3031 `interactive_setup()` (function) — Walk the user through Google Chat configuration via ``hermes setup``.
- L3130 `_standalone_send(pconfig, chat_id: str, message: str, *, thread_id: Optional[str]=None, media_files: Optional[List[str]]=None, force_document: bool=False)` (function) — POST a single Google Chat message via the REST API without the SDK.
- L3282 `register(ctx)` (function) — Plugin entry point — called by the Hermes plugin system at startup.
