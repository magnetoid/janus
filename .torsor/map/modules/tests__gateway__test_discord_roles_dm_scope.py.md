---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_roles_dm_scope.py

Symbols in `tests/gateway/test_discord_roles_dm_scope.py`.

- L25 `_set_dm_role_auth_guild(monkeypatch, guild_id=None)` (function) — Stub ``hermes_cli.config.read_raw_config`` so ``_read_dm_role_auth_guild``
- L36 `_make_adapter(allowed_users=None, allowed_roles=None, guilds=None)` (function) — Build a minimal DiscordAdapter without running __init__.
- L52 `_role(role_id)` (function)
- L56 `_guild_with_member(guild_id, member_id, role_ids)` (function) — Build a fake guild that holds one member with the given roles.
- L76 `test_dm_rejects_role_held_in_other_guild(monkeypatch)` (function) — A user with an allowed role in a DIFFERENT guild must NOT pass a DM.
- L103 `test_dm_role_auth_requires_explicit_guild_optin(monkeypatch)` (function) — With dm_role_auth_guild set, only that specific guild counts.
- L127 `test_dm_role_auth_optin_rejects_when_not_member(monkeypatch)` (function) — dm_role_auth_guild set but user isn't a member → reject.
- L155 `test_guild_message_role_check_scoped_to_originating_guild(monkeypatch)` (function) — A user with the role in a DIFFERENT guild than the message origin
- L183 `test_guild_message_role_check_allows_when_role_in_same_guild(monkeypatch)` (function) — Positive path: user has the role IN the message's guild → allowed.
- L205 `test_guild_message_rejects_author_roles_from_different_guild(monkeypatch)` (function) — If an author Member object comes from a different guild than the
- L240 `test_user_id_allowlist_works_in_dm()` (function)
- L248 `test_user_id_allowlist_works_in_guild()` (function)
- L259 `test_empty_allowlists_allow_everyone()` (function)
- L273 `test_slash_authorization_rejects_cross_guild_role_dm(monkeypatch)` (function) — Slash interaction in a DM must not be authorized by a role held in
- L303 `test_slash_authorization_rejects_cross_guild_role_in_guild(monkeypatch)` (function) — Slash in guild B must not be authorized by a role held in guild A.
- L331 `test_slash_authorization_allows_in_scope_guild_role(monkeypatch)` (function) — Positive control: slash in guild B, user has role in guild B → allowed.
