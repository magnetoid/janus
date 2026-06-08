---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_allowed_mentions.py

Symbols in `tests/gateway/test_discord_allowed_mentions.py`.

- L16 `_FakeAllowedMentions` (class) — Stand-in for ``discord.AllowedMentions`` that exposes the same four
- L21 `__init__(self, *, everyone=True, roles=True, users=True, replied_user=True)` (method)
- L27 `__repr__(self)` (method)
- L34 `_ensure_discord_mock()` (function) — Install (or augment) a mock ``discord`` module.
- L98 `_clear_allowed_mention_env(monkeypatch)` (function)
- L103 `test_safe_defaults_block_everyone_and_roles()` (function)
- L111 `test_env_var_opts_back_into_everyone(monkeypatch)` (function)
- L121 `test_env_var_can_disable_users(monkeypatch)` (function)
- L140 `test_everyone_boolean_parsing(monkeypatch, raw, expected)` (function)
- L146 `test_all_four_knobs_together(monkeypatch)` (function)
