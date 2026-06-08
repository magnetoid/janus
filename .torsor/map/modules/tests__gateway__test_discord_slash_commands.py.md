---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_slash_commands.py

Symbols in `tests/gateway/test_discord_slash_commands.py`.

- L12 `_ensure_discord_mock()` (function)
- L81 `FakeTree` (class)
- L82 `__init__(self)` (method)
- L85 `command(self, *, name, description)` (method)
- L92 `add_command(self, cmd)` (method)
- L95 `get_commands(self)` (method)
- L100 `adapter()` (function)
- L123 `test_registers_native_thread_slash_command(adapter)` (function)
- L145 `test_registers_native_restart_slash_command(adapter)` (function)
- L167 `test_auto_registers_missing_gateway_commands(adapter)` (function) — Commands in COMMAND_REGISTRY that aren't explicitly registered should
- L183 `test_auto_registered_command_dispatches_correctly(adapter)` (function) — Auto-registered commands should dispatch via _run_simple_slash.
- L197 `test_auto_registered_command_with_args(adapter)` (function) — Auto-registered commands with args_hint should accept an optional args param.
- L213 `test_auto_registers_plugin_commands_for_discord(adapter)` (function) — Plugin slash commands should appear as native Discord app commands.
- L242 `test_auto_registered_plugin_command_without_args_hint(adapter)` (function) — Plugin commands without args_hint should register as parameterless.
- L267 `test_plugin_command_name_conflict_skipped(adapter)` (function) — A plugin command that collides with a built-in must not override it.
- L301 `test_handle_thread_create_slash_reports_success(adapter)` (function)
- L330 `test_handle_thread_create_slash_dispatches_session_when_message_provided(adapter)` (function) — When a message is given, _dispatch_thread_session should be called.
- L353 `test_handle_thread_create_slash_no_dispatch_without_message(adapter)` (function) — Without a message, no session dispatch should occur.
- L374 `test_handle_thread_create_slash_falls_back_to_seed_message(adapter)` (function)
- L402 `test_handle_thread_create_slash_reports_failure(adapter)` (function)
- L430 `test_dispatch_thread_session_builds_thread_event(adapter)` (function) — Dispatched event should have chat_type=thread and chat_id=thread_id.
- L460 `test_build_slash_event_preserves_thread_context(adapter)` (function)
- L476 `test_build_slash_event_uses_group_context_for_channels(adapter)` (function)
- L497 `test_auto_create_thread_uses_message_content_as_name(adapter)` (function)
- L516 `test_auto_create_thread_strips_mention_syntax_from_name(adapter)` (function) — Thread names must not contain raw <@id>, <@&id>, or <#id> markers.
- L540 `test_auto_create_thread_falls_back_to_hermes_when_only_mentions(adapter)` (function) — If a message contains only mention syntax, the stripped content is
- L558 `test_auto_create_thread_truncates_long_names(adapter)` (function)
- L577 `test_auto_create_thread_falls_back_to_seed_message(adapter)` (function)
- L598 `test_auto_create_thread_returns_none_when_direct_and_fallback_fail(adapter)` (function)
- L618 `_FakeTextChannel` (class) — A channel that is NOT a discord.Thread or discord.DMChannel.
- L621 `__init__(self, channel_id=100, name='general', guild_name='TestGuild')` (method)
- L627 `history(self, *args, **kwargs)` (method)
- L635 `_FakeThreadChannel` (class) — isinstance(ch, discord.Thread) → True.
- L638 `__init__(self, channel_id=200, name='existing-thread', guild_name='TestGuild', parent_id=100)` (method)
- L646 `history(self, *args, **kwargs)` (method)
- L654 `_fake_message(channel, *, content='Hello', author_id=42, display_name='Jezza')` (function)
- L668 `test_auto_thread_creates_thread_and_redirects(adapter, monkeypatch)` (function) — When DISCORD_AUTO_THREAD=true, a new thread is created and the event routes there.
- L696 `test_auto_thread_enabled_by_default_slash_commands(adapter, monkeypatch)` (function) — Without DISCORD_AUTO_THREAD env var, auto-threading is enabled (default: true).
- L722 `test_auto_thread_can_be_disabled(adapter, monkeypatch)` (function) — Setting DISCORD_AUTO_THREAD=false keeps messages in the channel.
- L746 `test_auto_thread_skips_threads_and_dms(adapter, monkeypatch)` (function) — Auto-thread should not create threads inside existing threads.
- L772 `test_discord_auto_thread_config_bridge(monkeypatch, tmp_path)` (function) — discord.auto_thread in config.yaml should be bridged to DISCORD_AUTO_THREAD env var.
- L801 `test_register_skill_command_is_flat_not_nested(adapter)` (function) — _register_skill_group should register a single flat ``/skill`` command.
- L839 `test_register_skill_command_empty_skills_no_command(adapter)` (function) — No /skill command should be registered when there are zero skills.
- L851 `test_register_skill_command_callback_dispatches_by_name(adapter)` (function) — The /skill callback should look up the skill by ``name`` and
- L892 `test_register_skill_command_handles_unknown_skill_gracefully(adapter)` (function) — Passing a name that isn't a registered skill should respond with
- L922 `test_register_skill_command_payload_fits_discord_8kb_limit(adapter)` (function) — The /skill command registration payload must stay under Discord's
- L967 `test_register_skill_command_autocomplete_filters_by_name_and_description(adapter)` (function) — The autocomplete callback should match on both skill name and
