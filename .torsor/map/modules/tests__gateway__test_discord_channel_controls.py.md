---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_channel_controls.py

Symbols in `tests/gateway/test_discord_channel_controls.py`.

- L13 `_ensure_discord_mock()` (function) — Install a mock discord module when discord.py isn't available.
- L52 `FakeDMChannel` (class)
- L53 `__init__(self, channel_id: int=1, name: str='dm')` (method)
- L58 `FakeTextChannel` (class)
- L59 `__init__(self, channel_id: int=1, name: str='general', guild_name: str='Hermes Server')` (method)
- L66 `FakeThread` (class)
- L67 `__init__(self, channel_id: int=1, name: str='thread', parent=None, guild_name: str='Hermes Server')` (method)
- L77 `adapter(monkeypatch)` (function)
- L89 `make_message(*, channel, content: str, mentions=None)` (function)
- L107 `test_ignored_channel_blocks_message(adapter, monkeypatch)` (function) — Messages in ignored channels are silently dropped.
- L120 `test_ignored_channel_blocks_even_with_mention(adapter, monkeypatch)` (function) — Ignored channels take priority — even @mentions are dropped.
- L137 `test_non_ignored_channel_processes_normally(adapter, monkeypatch)` (function) — Channels not in the ignored list process normally.
- L150 `test_ignored_channels_csv_parsing(adapter, monkeypatch)` (function) — Multiple channel IDs are parsed correctly from CSV.
- L164 `test_ignored_channels_empty_string_ignores_nothing(adapter, monkeypatch)` (function) — Empty DISCORD_IGNORED_CHANNELS means nothing is ignored.
- L177 `test_ignored_channel_thread_parent_match(adapter, monkeypatch)` (function) — Thread whose parent channel is ignored should also be ignored.
- L192 `test_dms_unaffected_by_ignored_channels(adapter, monkeypatch)` (function) — DMs should never be affected by ignored_channels.
- L207 `test_no_thread_channel_skips_auto_thread(adapter, monkeypatch)` (function) — Channels in no_thread_channels should not auto-create threads.
- L227 `test_normal_channel_still_auto_threads(adapter, monkeypatch)` (function) — Channels NOT in no_thread_channels still get auto-threading.
- L248 `test_no_thread_channels_csv_parsing(adapter, monkeypatch)` (function) — Multiple no_thread channel IDs parsed from CSV.
- L267 `test_no_thread_with_auto_thread_disabled_is_noop(adapter, monkeypatch)` (function) — no_thread_channels is a no-op when auto_thread is globally disabled.
- L287 `test_config_bridges_ignored_channels(monkeypatch, tmp_path)` (function) — gateway/config.py bridges discord.ignored_channels to env var.
- L308 `test_config_bridges_no_thread_channels(monkeypatch, tmp_path)` (function) — gateway/config.py bridges discord.no_thread_channels to env var.
- L327 `test_config_env_var_takes_precedence(monkeypatch, tmp_path)` (function) — Env vars should take precedence over config.yaml values.
