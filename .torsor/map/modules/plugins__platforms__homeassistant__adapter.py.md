---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/platforms/homeassistant/adapter.py

Symbols in `plugins/platforms/homeassistant/adapter.py`.

- L42 `check_ha_requirements()` (function) — Check if Home Assistant dependencies are available and configured.
- L51 `HomeAssistantAdapter` (class) — Home Assistant WebSocket adapter.
- L65 `__init__(self, config: PlatformConfig)` (method)
- L92 `_next_id(self)` (method) — Return the next WebSocket message ID.
- L101 `connect(self)` (method) — Connect to HA WebSocket API and subscribe to events.
- L140 `_ws_connect(self)` (method) — Establish WebSocket connection and authenticate.
- L187 `_cleanup_ws(self)` (method) — Close WebSocket and session.
- L196 `disconnect(self)` (method) — Disconnect from Home Assistant.
- L217 `_listen_loop(self)` (method) — Main event loop with automatic reconnection.
- L247 `_read_events(self)` (method) — Read events from WebSocket until disconnected.
- L262 `_handle_ha_event(self, event: Dict[str, Any])` (method) — Process a state_changed event from Home Assistant.
- L321 `_format_state_change(entity_id: str, old_state: Dict[str, Any], new_state: Dict[str, Any])` (method) — Convert a state_changed event into a human-readable description.
- L386 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a notification via HA REST API (persistent_notification.create).
- L440 `send_typing(self, chat_id: str, metadata=None)` (method) — No typing indicator for Home Assistant.
- L443 `get_chat_info(self, chat_id: str)` (method) — Return basic info about the HA event channel.
- L457 `_standalone_send(pconfig, chat_id: str, message: str, *, thread_id: Optional[str]=None, media_files: Optional[list]=None, force_document: bool=False)` (function) — Send a notification via the HA ``notify.notify`` service without a
- L533 `_is_connected(config)` (function) — Home Assistant is considered connected when ``HASS_TOKEN`` is set.
- L551 `_build_adapter(config)` (function) — Factory wrapper that constructs HomeAssistantAdapter from a PlatformConfig.
- L556 `register(ctx)` (function) — Plugin entry point — called by the Hermes plugin system.
