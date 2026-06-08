---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/channel_directory.py

Symbols in `gateway/channel_directory.py`.

- L22 `_normalize_channel_query(value: str)` (function)
- L26 `_channel_target_name(platform_name: str, channel: Dict[str, Any])` (function) — Return the human-facing target label shown to users for a channel entry.
- L36 `_session_entry_id(origin: Dict[str, Any])` (function)
- L46 `_session_entry_name(origin: Dict[str, Any])` (function)
- L60 `build_channel_directory(adapters: Dict[Any, Any])` (function) — Build a channel directory from connected platform adapters and session data.
- L112 `_build_discord(adapter)` (function) — Enumerate all text channels and forum channels the Discord bot can see.
- L149 `_build_slack(adapter)` (function) — List Slack channels the bot has joined across all workspaces.
- L211 `_build_from_sessions(platform_name: str)` (function) — Pull known channels/contacts from sessions.json origin data.
- L247 `load_directory()` (function) — Load the cached channel directory from disk.
- L258 `lookup_channel_type(platform_name: str, chat_id: str)` (function) — Return the channel ``type`` string (e.g. ``"channel"``, ``"forum"``) for *chat_id*, or *None* if unknown.
- L267 `resolve_channel_name(platform_name: str, name: str)` (function) — Resolve a human-friendly channel name to a numeric ID.
- L314 `format_directory_for_display()` (function) — Format the channel directory as a human-readable list for the model.
