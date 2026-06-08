---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_free_response.py

Symbols in `tests/gateway/test_discord_free_response.py`.

- L13 `_ensure_discord_mock()` (function) — Install a mock discord module when discord.py isn't available.
- L52 `FakeDMChannel` (class)
- L53 `__init__(self, channel_id: int=1, name: str='dm')` (method)
- L58 `FakeTextChannel` (class)
- L59 `__init__(self, channel_id: int=1, name: str='general', guild_name: str='Hermes Server')` (method)
- L65 `history(self, *, limit, before, after=None, oldest_first=None)` (method)
- L72 `FakeForumChannel` (class)
- L73 `__init__(self, channel_id: int=1, name: str='support-forum', guild_name: str='Hermes Server')` (method)
- L81 `FakeThread` (class)
- L82 `__init__(self, channel_id: int=1, name: str='thread', parent=None, guild_name: str='Hermes Server')` (method)
- L90 `history(self, *, limit, before, after=None, oldest_first=None)` (method)
- L98 `adapter(monkeypatch)` (function)
- L128 `make_message(*, channel, content: str, mentions=None, msg_type=None)` (function)
- L143 `make_history_message(*, author, content: str, msg_id: int, msg_type=None, attachments=None)` (function)
- L160 `FakeHistoryChannel` (class)
- L161 `__init__(self, history_messages, **kwargs)` (method)
- L165 `history(self, *, limit, before, after=None, oldest_first=None)` (method)
- L186 `test_discord_defaults_to_require_mention(adapter, monkeypatch)` (function) — Default behavior: require @mention in server channels.
- L200 `test_discord_free_response_in_server_channels(adapter, monkeypatch)` (function)
- L216 `test_discord_free_response_in_threads(adapter, monkeypatch)` (function)
- L234 `test_discord_forum_threads_are_handled_as_threads(adapter, monkeypatch)` (function)
- L254 `test_discord_can_still_require_mentions_when_enabled(adapter, monkeypatch)` (function)
- L266 `test_discord_free_response_channel_overrides_mention_requirement(adapter, monkeypatch)` (function)
- L280 `test_discord_free_response_channel_can_come_from_config_extra(adapter, monkeypatch)` (function)
- L294 `test_discord_free_response_channels_bare_int(adapter, monkeypatch)` (function)
- L306 `test_discord_free_response_channels_int_list(adapter, monkeypatch)` (function)
- L315 `test_discord_forum_parent_in_free_response_list_allows_forum_thread(adapter, monkeypatch)` (function)
- L332 `test_discord_accepts_and_strips_bot_mentions_when_required(adapter, monkeypatch)` (function)
- L351 `test_discord_dms_ignore_mention_requirement(adapter, monkeypatch)` (function)
- L366 `test_discord_auto_thread_enabled_by_default(adapter, monkeypatch)` (function) — Auto-threading should be enabled by default (DISCORD_AUTO_THREAD defaults to 'true').
- L387 `test_discord_reply_message_skips_auto_thread(adapter, monkeypatch)` (function) — Quote-replies should stay in-channel instead of trying to create a thread.
- L412 `test_discord_auto_thread_can_be_disabled(adapter, monkeypatch)` (function) — Setting auto_thread to false skips thread creation.
- L430 `test_discord_bot_thread_skips_mention_requirement(adapter, monkeypatch)` (function) — Messages in a thread the bot has participated in should not require @mention.
- L451 `test_discord_unknown_thread_still_requires_mention(adapter, monkeypatch)` (function) — Messages in a thread the bot hasn't participated in should still require @mention.
- L467 `test_discord_auto_thread_tracks_participation(adapter, monkeypatch)` (function) — Auto-created threads should be tracked for future mention-free replies.
- L483 `test_discord_thread_participation_tracked_on_dispatch(adapter, monkeypatch)` (function) — When the bot processes a message in a thread, it tracks participation.
- L497 `test_discord_voice_linked_channel_skips_mention_requirement_and_auto_thread(adapter, monkeypatch)` (function) — Active voice-linked text channels should behave like free-response channels.
- L521 `test_discord_free_response_channel_skips_auto_thread(adapter, monkeypatch)` (function) — Free-response channels should reply inline, never spawn a new thread.
- L554 `test_discord_voice_linked_parent_thread_still_requires_mention(adapter, monkeypatch)` (function) — Threads under a voice-linked channel should still require @mention.
- L571 `test_discord_thread_default_keeps_responding_after_participation(adapter, monkeypatch)` (function) — Default behavior: once the bot is in a thread, it auto-responds without @mention.
- L587 `test_discord_thread_require_mention_gates_followups(adapter, monkeypatch)` (function) — When thread_require_mention=true, even bot-participated threads need @mention.
- L603 `test_discord_thread_require_mention_still_responds_when_mentioned(adapter, monkeypatch)` (function) — thread_require_mention=true still lets explicit @mentions through in threads.
- L624 `test_discord_thread_require_mention_via_config_extra(adapter, monkeypatch)` (function) — thread_require_mention can also be set via config.extra (yaml).
- L642 `test_fetch_channel_context_stops_at_self_message_and_reverses_to_chronological_order(adapter, monkeypatch)` (function)
- L670 `test_fetch_channel_context_skips_other_bots_when_allow_bots_none(adapter, monkeypatch)` (function)
- L691 `test_fetch_channel_context_uses_cache_to_narrow_window(adapter, monkeypatch)` (function) — When _last_self_message_id is cached, the fetch passes after= to skip old messages.
- L730 `test_fetch_channel_context_cache_uses_latest_window_when_after_set(adapter, monkeypatch)` (function) — Regression: discord.py defaults oldest_first=True when after= is provided.
- L767 `test_fetch_channel_context_ignores_stale_cache(adapter, monkeypatch)` (function) — If cached ID is >= trigger ID (stale/future), fall back to cold-start scan.
- L805 `test_discord_shared_channel_backfill_prepends_context(adapter, monkeypatch)` (function)
- L829 `test_discord_per_user_channel_backfills_too(adapter, monkeypatch)` (function) — Per-user sessions also benefit from backfill: Alice's session is missing
- L855 `test_discord_participated_thread_backfills_without_mention(adapter, monkeypatch)` (function) — Known threads still need recent thread context when mention gating is bypassed.
- L876 `test_discord_dm_does_not_backfill(adapter, monkeypatch)` (function) — DMs skip backfill — every DM triggers the bot, so there's no mention gap.
- L909 `test_discord_auto_thread_skips_backfill(adapter, monkeypatch)` (function) — Auto-created threads skip backfill — the thread is brand new with no prior context.
