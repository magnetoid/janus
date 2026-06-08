---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_slash_auth.py

Symbols in `tests/gateway/test_discord_slash_auth.py`.

- L29 `_ensure_discord_mock()` (function)
- L92 `_isolate_discord_env(monkeypatch)` (function)
- L105 `_stub_discord_permissions(monkeypatch)` (function) — Pin discord.Permissions to a plain stand-in so tests can assert the
- L119 `adapter()` (function)
- L129 `_make_interaction(user_id, *, channel_id=12345, guild_id=42, in_dm=False, in_thread=False, parent_channel_id=None, user=_SENTINEL)` (function) — Build a mock Discord Interaction with a still-unresponded response.
- L179 `test_no_allowlist_allows_everyone(adapter)` (function) — SECURITY-CRITICAL backwards-compat: deployments without any allowlist
- L190 `test_no_allowlist_dm_also_allowed(adapter)` (function) — Same for DMs — no allowlist means no restriction, matching on_message.
- L202 `test_allowed_user_passes(adapter)` (function)
- L210 `test_disallowed_user_rejected_with_ephemeral(adapter, caplog)` (function)
- L229 `test_role_member_passes(adapter)` (function) — A user whose Member.roles includes an allowed role passes the gate.
- L238 `test_role_non_member_rejected(adapter)` (function) — A user without any matching role is rejected even if no user allowlist.
- L252 `test_channel_not_in_allowlist_rejected(adapter, monkeypatch, caplog)` (function) — on_message blocks messages in channels not in DISCORD_ALLOWED_CHANNELS;
- L264 `test_channel_in_allowlist_passes(adapter, monkeypatch)` (function)
- L271 `test_channel_allowlist_wildcard_passes(adapter, monkeypatch)` (function) — ``*`` in DISCORD_ALLOWED_CHANNELS = allow any channel, matching on_message.
- L279 `test_channel_allowlist_does_not_apply_to_dms(adapter, monkeypatch)` (function) — DMs aren't channel-gated — they go through on_message's DM lockdown.
- L292 `test_ignored_channel_rejected(adapter, monkeypatch, caplog)` (function)
- L301 `test_ignored_channel_wildcard_blocks_all(adapter, monkeypatch)` (function)
- L313 `test_unauthorized_attempt_notifies_telegram(adapter)` (function)
- L342 `test_notify_silently_no_ops_without_runner(adapter)` (function)
- L348 `test_notify_falls_back_to_slack_if_no_telegram(adapter)` (function)
- L369 `test_visibility_hide_off_by_default_is_noop(adapter, monkeypatch)` (function) — DISCORD_HIDE_SLASH_COMMANDS unset → don't touch any command's permissions.
- L385 `test_visibility_hide_helper_zeroes_perms(adapter)` (function)
- L396 `test_visibility_hide_tolerates_unsetable_command(adapter, caplog)` (function)
- L422 `test_missing_channel_id_rejected_when_channel_policy_configured(adapter, monkeypatch)` (function) — A guild interaction without a resolvable channel id must fail
- L435 `test_missing_channel_id_allowed_when_no_channel_policy(adapter)` (function) — No DISCORD_ALLOWED_CHANNELS configured + missing channel id: still
- L443 `test_missing_user_rejected_when_allowlist_configured(adapter)` (function) — interaction.user is None with a user/role allowlist active:
- L454 `test_missing_user_allowed_when_no_allowlist_configured(adapter)` (function) — interaction.user is None but no allowlist configured: allow
- L468 `test_thread_parent_in_allowlist_passes(adapter, monkeypatch)` (function) — Thread whose parent channel is on DISCORD_ALLOWED_CHANNELS passes
- L479 `test_thread_parent_in_ignorelist_rejects(adapter, monkeypatch)` (function) — Thread whose parent channel is on DISCORD_IGNORED_CHANNELS rejects
- L490 `test_ignored_beats_allowed(adapter, monkeypatch)` (function) — Channel listed in BOTH allowed and ignored: the ignored entry wins.
- L506 `test_notify_falls_back_to_slack_on_telegram_soft_fail(adapter)` (function) — adapter.send returning SendResult(success=False) must NOT short-
- L534 `test_notify_returns_on_telegram_truthy_success(adapter)` (function) — adapter.send returning SendResult(success=True) -- or any object
- L566 `_capture_skill_registration(adapter, monkeypatch, entries)` (function) — Run ``_register_skill_group`` against a stubbed skill catalog and
- L618 `test_skill_autocomplete_returns_empty_for_unauthorized(adapter, monkeypatch)` (function) — Autocomplete must not leak the installed skill catalog to users
- L639 `test_skill_autocomplete_returns_choices_for_authorized(adapter, monkeypatch)` (function) — Sanity: an authorized user still gets the autocomplete suggestions.
- L659 `test_skill_handler_rejects_before_dispatch_for_unauthorized(adapter, monkeypatch)` (function) — The /skill handler must call _check_slash_authorization BEFORE
- L695 `test_skill_handler_known_and_unknown_produce_same_rejection(adapter, monkeypatch)` (function) — An unauthorized user probing for valid skill names must see the
- L723 `test_skill_handler_dispatches_for_authorized(adapter, monkeypatch)` (function) — Sanity: an authorized user reaches _run_simple_slash with the
