---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/e2e/conftest.py

Symbols in `tests/e2e/conftest.py`.

- L30 `_ensure_telegram_mock()` (function) — Install mock telegram modules so TelegramAdapter can be imported.
- L59 `_ensure_discord_mock()` (function) — Install mock discord modules so DiscordAdapter can be imported.
- L91 `_ensure_slack_mock()` (function) — Install mock slack modules so SlackAdapter can be imported.
- L131 `make_source(platform: Platform, chat_id: str='e2e-chat-1', user_id: str='e2e-user-1', chat_type: str='dm')` (function)
- L141 `make_session_entry(platform: Platform, source: SessionSource=None)` (function)
- L153 `make_event(platform: Platform, text: str='/help', chat_id: str='e2e-chat-1', user_id: str='e2e-user-1', chat_type: str='dm')` (function)
- L167 `make_runner(platform: Platform, session_entry: SessionEntry=None)` (function) — Create a GatewayRunner with mocked internals for e2e testing.
- L238 `make_adapter(platform: Platform, runner=None)` (function) — Create a platform adapter wired to *runner*, with send methods mocked.
- L266 `send_and_capture(adapter, text: str, platform: Platform, **event_kwargs)` (function) — Send a message through the full e2e flow and return the send mock.
- L277 `platform(request)` (function)
- L282 `source(platform)` (function)
- L287 `session_entry(platform, source)` (function)
- L292 `runner(platform, session_entry)` (function)
- L297 `adapter(platform, runner)` (function)
- L313 `_next_message_id()` (function)
- L319 `make_fake_bot_user()` (function)
- L326 `make_fake_guild(guild_id: int=GUILD_ID, name: str='Test Server')` (function)
- L330 `make_fake_text_channel(channel_id: int=CHANNEL_ID, name: str='general', guild=None)` (function)
- L338 `make_fake_dm_channel(channel_id: int=55555)` (function)
- L347 `make_fake_thread(thread_id: int=THREAD_ID, name: str='test-thread', parent=None)` (function)
- L360 `make_discord_message(*, content: str='hello', author=None, channel=None, mentions=None, attachments=None, message_id: int=None)` (function)
- L387 `get_response_text(adapter)` (function) — Extract the response text from adapter.send() call args, or None if not called.
- L394 `_make_discord_adapter_wired(runner=None)` (function) — Create a DiscordAdapter wired to a GatewayRunner for e2e tests.
- L420 `discord_setup()` (function)
- L425 `discord_adapter(discord_setup)` (function)
- L430 `discord_runner(discord_setup)` (function)
- L435 `bot_user()` (function)
