---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/platforms/ntfy/adapter.py

Symbols in `plugins/platforms/ntfy/adapter.py`.

- L74 `_FatalStreamError` (class) — Raised when a stream error is unrecoverable (e.g. 401, 404).
- L87 `_build_auth_header(token: str)` (function) — Build an ``Authorization`` header from an ntfy token.
- L111 `_truncate_body(message: str, *, context: str)` (function) — Apply the ntfy 4096-char limit, logging a warning on truncation.
- L125 `check_requirements()` (function) — Check whether the ntfy adapter is installable and minimally configured.
- L138 `validate_config(config)` (function) — Validate that the configured ntfy platform has a topic set.
- L145 `is_connected(config)` (function) — Check whether ntfy is configured (env or config.yaml).
- L152 `NtfyAdapter` (class) — ntfy adapter.
- L161 `__init__(self, config: PlatformConfig)` (method)
- L186 `connect(self)` (method) — Connect to ntfy by starting the streaming subscription task.
- L205 `_run_stream(self)` (method) — Subscribe to the ntfy topic with automatic reconnection.
- L238 `_consume_stream(self, url: str, headers: Dict[str, str])` (method) — Open an HTTP streaming connection and dispatch events.
- L286 `disconnect(self)` (method) — Disconnect from ntfy.
- L308 `_on_message(self, event: Dict[str, Any])` (method) — Process an incoming ntfy message event.
- L367 `_is_duplicate(self, msg_id: str)` (method) — Return True if this message ID was already seen within the dedup window.
- L381 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Publish a message to the configured publish topic.
- L432 `send_typing(self, chat_id: str, metadata=None)` (method) — ntfy does not support typing indicators.
- L436 `get_chat_info(self, chat_id: str)` (method) — Return basic info about an ntfy topic.
- L442 `_auth_headers(self)` (method) — Build Authorization header if a token is configured.
- L452 `_env_enablement()` (function) — Seed ``PlatformConfig.extra`` from env vars during gateway config load.
- L490 `_standalone_send(pconfig, chat_id: str, message: str, *, thread_id: Optional[str]=None, media_files: Optional[List[str]]=None, force_document: bool=False)` (function) — Out-of-process publish for cron / send_message_tool fallbacks.
- L555 `register(ctx)` (function) — Plugin entry point — called by the Hermes plugin system at startup.
