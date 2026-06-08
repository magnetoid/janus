---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/slash_access.py

Symbols in `gateway/slash_access.py`.

- L57 `SlashAccessPolicy` (class) — Resolved access policy for a single (platform, scope) pair.
- L69 `is_admin(self, user_id: Optional[str])` (method)
- L79 `can_run(self, user_id: Optional[str], canonical_cmd: str)` (method)
- L94 `_coerce_id_list(raw: Any)` (function) — Normalize a YAML-loaded admin/user list into a frozenset of strings.
- L117 `_coerce_command_list(raw: Any)` (function) — Normalize a slash command allowlist.
- L140 `_scope_for_chat_type(chat_type: Optional[str])` (function)
- L146 `_platform_extra(platform_config: Any)` (function) — Return the ``extra`` dict from a PlatformConfig-like object.
- L163 `_keys_for_scope(scope: str)` (function) — Return (admin_key, user_cmd_key) names for a scope.
- L170 `policy_from_extra(extra: dict, scope: str)` (function) — Build a policy from a platform's ``extra`` dict for one scope.
- L196 `policy_for_source(gateway_config: Any, source: Any)` (function) — Resolve the access policy for a SessionSource.
