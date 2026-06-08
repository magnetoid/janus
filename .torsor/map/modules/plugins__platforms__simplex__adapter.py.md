---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/platforms/simplex/adapter.py

Symbols in `plugins/platforms/simplex/adapter.py`.

- L81 `_parse_comma_list(value: str)` (function) — Split a comma-separated string into a stripped list.
- L86 `_guess_extension(data: bytes)` (function) — Guess file extension from magic bytes.
- L107 `_is_image_ext(ext: str)` (function)
- L111 `_is_audio_ext(ext: str)` (function)
- L119 `SimplexAdapter` (class) — SimpleX Chat adapter using the simplex-chat daemon WebSocket API.
- L126 `__init__(self, config: PlatformConfig, **kwargs)` (method)
- L151 `connect(self)` (method) — Connect to the simplex-chat daemon and start the WebSocket listener.
- L183 `disconnect(self)` (method) — Stop WebSocket listener and clean up.
- L218 `_ws_listener(self)` (method) — Maintain a persistent WebSocket connection to the daemon.
- L275 `_health_monitor(self)` (method) — Observe WebSocket idleness without reconnecting healthy quiet links.
- L296 `_handle_event(self, event: dict)` (method) — Dispatch a daemon event to the appropriate handler.
- L320 `_handle_new_chat_item(self, wrapper: dict)` (method) — Process a single newChatItem event into a MessageEvent.
- L440 `_fetch_file(self, file_id: Any, file_name: str)` (method) — Ask the daemon to receive and return a file attachment.
- L482 `_make_corr_id(self)` (method) — Generate a unique correlation ID for a request.
- L492 `_send_ws(self, payload: dict)` (method) — Send a JSON payload over the WebSocket, queuing if not yet connected.
- L506 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a text message to a contact or group.
- L534 `send_typing(self, chat_id: str, metadata=None)` (method) — SimpleX does not expose a typing indicator API — no-op.
- L538 `send_image(self, chat_id: str, image_url: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send an image (URL) as a message with optional caption.
- L556 `get_chat_info(self, chat_id: str)` (method) — Return basic chat info.
- L567 `check_requirements()` (function) — Plugin gate: require SIMPLEX_WS_URL AND the websockets package.
- L583 `validate_config(config)` (function) — Validate that the platform config has enough info to connect.
- L590 `is_connected(config)` (function) — Check whether SimpleX is configured (env or config.yaml).
- L597 `_env_enablement()` (function) — Seed ``PlatformConfig.extra`` from env vars during gateway config load.
- L622 `_standalone_send(pconfig, chat_id: str, message: str, *, thread_id: Optional[str]=None, media_files: Optional[List[str]]=None, force_document: bool=False)` (function) — Open an ephemeral WebSocket to the daemon, send, and close.
- L677 `interactive_setup()` (function) — Minimal stdin wizard for ``hermes setup gateway`` → SimpleX.
- L718 `register(ctx)` (function) — Plugin entry point — called by the Hermes plugin system at startup.
