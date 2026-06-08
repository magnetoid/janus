---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_allowed_channels.py

Symbols in `tests/gateway/test_discord_allowed_channels.py`.

- L16 `_channel_is_allowed(channel_id: str, allowed_channels_raw: str)` (function) — Replicate the channel-allow-list check from discord.py on_message.
- L26 `_channel_is_ignored(channel_id: str, ignored_channels_raw: str)` (function) — Replicate the ignored-channel check from discord.py on_message.
- L34 `_channel_is_free_response(channel_id: str, free_channels_raw: str)` (function) — Replicate the free-response-channel check from discord.py on_message.
- L42 `TestDiscordAllowedChannelsWildcard` (class) — Wildcard and channel-list behaviour for DISCORD_ALLOWED_CHANNELS.
- L45 `test_wildcard_allows_any_channel(self)` (method) — '*' should allow messages from any channel ID.
- L49 `test_wildcard_in_list_allows_any_channel(self)` (method) — '*' mixed with other entries still allows any channel.
- L53 `test_exact_match_allowed(self)` (method) — Channel ID present in the explicit list is allowed.
- L57 `test_non_matching_channel_blocked(self)` (method) — Channel ID absent from the explicit list is blocked.
- L61 `test_empty_allowlist_allows_all(self)` (method) — Empty DISCORD_ALLOWED_CHANNELS means no restriction.
- L65 `test_whitespace_only_entry_ignored(self)` (method) — Entries that are only whitespace are stripped and ignored.
- L70 `TestDiscordIgnoredChannelsWildcard` (class) — Wildcard and channel-list behaviour for DISCORD_IGNORED_CHANNELS.
- L73 `test_wildcard_silences_every_channel(self)` (method) — '*' in ignored_channels silences the bot everywhere.
- L77 `test_empty_ignored_list_silences_nothing(self)` (method)
- L80 `test_exact_match_is_ignored(self)` (method)
- L83 `test_non_match_not_ignored(self)` (method)
- L87 `TestDiscordFreeResponseChannelsWildcard` (class) — Wildcard and channel-list behaviour for DISCORD_FREE_RESPONSE_CHANNELS.
- L90 `test_wildcard_makes_every_channel_free_response(self)` (method) — '*' in free_response_channels exempts every channel from mention-required.
- L94 `test_wildcard_in_list_applies_everywhere(self)` (method)
- L97 `test_exact_match_is_free_response(self)` (method)
- L100 `test_non_match_not_free_response(self)` (method)
- L103 `test_empty_list_no_free_response(self)` (method)
