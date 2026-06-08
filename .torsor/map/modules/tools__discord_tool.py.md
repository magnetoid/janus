---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/discord_tool.py

Symbols in `tools/discord_tool.py`.

- L53 `_get_bot_token()` (function) — Resolve the Discord bot token from environment.
- L58 `_discord_request(method: str, path: str, token: str, params: Optional[Dict[str, str]]=None, body: Optional[Dict[str, Any]]=None, timeout: int=15)` (function) — Make a request to the Discord REST API.
- L100 `DiscordAPIError` (class) — Raised when a Discord API call fails.
- L102 `__init__(self, status: int, body: str)` (method)
- L126 `_channel_type_name(type_id: int)` (function)
- L138 `_detect_capabilities(token: str, *, force: bool=False)` (function) — Detect the bot's app-wide capabilities via GET /applications/@me.
- L179 `_reset_capability_cache()` (function) — Test hook: clear the detection cache.
- L189 `_list_guilds(token: str, **_kwargs: Any)` (function) — List all guilds the bot is a member of.
- L204 `_server_info(token: str, guild_id: str, **_kwargs: Any)` (function) — Get detailed information about a guild.
- L222 `_list_channels(token: str, guild_id: str, **_kwargs: Any)` (function) — List all channels in a guild, organized by category.
- L277 `_channel_info(token: str, channel_id: str, **_kwargs: Any)` (function) — Get detailed info about a specific channel.
- L294 `_list_roles(token: str, guild_id: str, **_kwargs: Any)` (function) — List all roles in a guild.
- L312 `_member_info(token: str, guild_id: str, user_id: str, **_kwargs: Any)` (function) — Get info about a specific guild member.
- L329 `_search_members(token: str, guild_id: str, query: str, limit: int=20, **_kwargs: Any)` (function) — Search for guild members by name.
- L351 `_fetch_messages(token: str, channel_id: str, limit: int=50, before: Optional[str]=None, after: Optional[str]=None, **_kwargs: Any)` (function) — Fetch recent messages from a channel.
- L394 `_list_pins(token: str, channel_id: str, **_kwargs: Any)` (function) — List pinned messages in a channel.
- L409 `_pin_message(token: str, channel_id: str, message_id: str, **_kwargs: Any)` (function) — Pin a message in a channel.
- L415 `_unpin_message(token: str, channel_id: str, message_id: str, **_kwargs: Any)` (function) — Unpin a message from a channel.
- L421 `_delete_message(token: str, channel_id: str, message_id: str, **_kwargs: Any)` (function) — Delete a message from a channel or thread.
- L427 `_create_thread(token: str, channel_id: str, name: str, message_id: Optional[str]=None, auto_archive_duration: int=1440, **_kwargs: Any)` (function) — Create a thread in a channel.
- L457 `_add_role(token: str, guild_id: str, user_id: str, role_id: str, **_kwargs: Any)` (function) — Add a role to a guild member.
- L463 `_remove_role(token: str, guild_id: str, user_id: str, role_id: str, **_kwargs: Any)` (function) — Remove a role from a guild member.
- L544 `_load_allowed_actions_config()` (function) — Read ``discord.server_actions`` from user config.
- L585 `_available_actions(caps: Dict[str, Any], allowlist: Optional[List[str]])` (function) — Compute the visible action list from intents + config allowlist.
- L609 `_build_schema(actions: List[str], caps: Optional[Dict[str, Any]]=None, tool_name: str='discord')` (function) — Build the tool schema for the given filtered action list.
- L728 `_get_dynamic_schema(action_subset: Dict[str, Any], tool_name: str)` (function) — Build a dynamic schema for *action_subset* filtered by intents + config.
- L744 `get_dynamic_schema_core()` (function)
- L748 `get_dynamic_schema_admin()` (function)
- L752 `get_dynamic_schema()` (function) — Backward-compat wrapper — returns core schema.
- L805 `_enrich_403(action: str, body: str)` (function) — Return a user-friendly guidance string for a 403 on ``action``.
- L818 `check_discord_tool_requirements()` (function) — Tool is available only when a Discord bot token is configured.
- L827 `_run_discord_action(action: str, valid_actions: Dict[str, Any], tool_label: str, guild_id: str='', channel_id: str='', user_id: str='', role_id: str='', message_id: str='', query: str='', name: str='', limit: int=50, before: str='', after: str='', auto_archive_duration: int=1440)` (function) — Shared handler logic for both discord tools.
- L908 `discord_core(action: str, **kwargs)` (function) — Execute a core Discord action (fetch_messages, search_members, create_thread).
- L913 `discord_admin_handler(action: str, **kwargs)` (function) — Execute a Discord admin action (server management).
- L929 `_make_handler(handler_fn)` (function) — Create a registry-compatible handler lambda for a discord handler.
