---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_connect.py

Symbols in `tests/gateway/test_discord_connect.py`.

- L12 `_FakeAllowedMentions` (class) — Stand-in for ``discord.AllowedMentions`` — exposes the same four
- L17 `__init__(self, *, everyone=True, roles=True, users=True, replied_user=True)` (method)
- L24 `_ensure_discord_mock()` (function) — Install (or augment) a mock ``discord`` module.
- L75 `_speed_up_command_sync_mutation_pacing(monkeypatch)` (function)
- L83 `FakeTree` (class)
- L84 `__init__(self)` (method)
- L89 `command(self, *args, **kwargs)` (method)
- L92 `get_commands(self, *args, **kwargs)` (method)
- L96 `FakeBot` (class)
- L97 `__init__(self, *, intents, proxy=None, allowed_mentions=None, **_)` (method)
- L110 `event(self, fn)` (method)
- L114 `start(self, token)` (method)
- L118 `close(self)` (method)
- L122 `SlowSyncTree` (class)
- L123 `__init__(self)` (method)
- L136 `SlowSyncBot` (class)
- L137 `__init__(self, *, intents, proxy=None)` (method)
- L151 `test_connect_only_requests_members_intent_when_needed(monkeypatch, allowed_users, expected_members_intent)` (function)
- L186 `test_reconnect_closes_previous_client_to_prevent_zombie_websocket(monkeypatch)` (function) — Regression for #18187: calling connect() twice without disconnect() in
- L249 `test_connect_releases_token_lock_on_timeout(monkeypatch)` (function)
- L283 `test_connect_does_not_wait_for_slash_sync(monkeypatch)` (function)
- L317 `test_connect_respects_slash_commands_opt_out(monkeypatch)` (function)
- L350 `test_safe_sync_slash_commands_only_mutates_diffs()` (function)
- L461 `test_safe_sync_slash_commands_recreates_metadata_only_diffs()` (function)
- L537 `test_post_connect_initialization_skips_sync_when_policy_off(monkeypatch)` (function)
- L550 `test_post_connect_initialization_skips_same_fingerprint_after_success(tmp_path, monkeypatch)` (function)
- L587 `test_post_connect_initialization_respects_discord_retry_after(tmp_path, monkeypatch)` (function)
- L627 `test_post_connect_initialization_reraises_non_rate_limit_exceptions(tmp_path, monkeypatch)` (function) — Arbitrary failures during sync must surface, not be swallowed as rate-limits.
- L669 `test_safe_sync_slash_commands_paces_mutation_writes(monkeypatch)` (function)
- L727 `test_safe_sync_reads_permission_attrs_from_existing_command()` (function) — Regression: AppCommand.to_dict() in discord.py does NOT include
- L823 `test_safe_sync_detects_contexts_drift()` (function) — Regression: contexts and integration_types must be canonicalized
