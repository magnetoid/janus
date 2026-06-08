---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_unknown_command.py

Symbols in `tests/gateway/test_unknown_command.py`.

- L19 `_make_source()` (function)
- L29 `_make_event(text: str)` (function)
- L33 `_make_runner()` (function)
- L83 `test_unknown_slash_command_returns_guidance(monkeypatch)` (function) — A genuinely unknown /foobar should return user-facing guidance, not
- L111 `test_unknown_slash_command_underscored_form_also_guarded(monkeypatch)` (function) — Telegram may send /foo_bar — same guard must trigger for underscored
- L136 `test_known_slash_command_not_flagged_as_unknown(monkeypatch)` (function) — A real built-in like /status must NOT hit the unknown-command guard.
- L150 `test_underscored_alias_for_hyphenated_builtin_not_flagged(monkeypatch)` (function) — Telegram autocomplete sends /reload_mcp for the /reload-mcp built-in.
- L178 `test_command_hook_can_deny_before_dispatch(monkeypatch)` (function) — A handler returning {"decision": "deny"} blocks a slash command early.
- L207 `test_command_hook_deny_without_message_uses_default(monkeypatch)` (function) — A deny decision with no message falls back to a generic blocked string.
- L228 `test_command_hook_can_mark_command_as_handled(monkeypatch)` (function) — A handled decision short-circuits dispatch cleanly with a custom reply.
- L250 `test_command_hook_allow_decision_is_passthrough(monkeypatch)` (function) — A handler returning {"decision": "allow"} must NOT prevent normal dispatch.
- L271 `test_command_hook_non_dict_return_values_ignored(monkeypatch)` (function) — Hook return values that aren't dicts must not break dispatch.
- L291 `test_command_hook_fires_for_plugin_registered_command(monkeypatch)` (function) — Plugin-registered slash commands should also trigger command:<name> hooks.
- L327 `test_command_hook_rewrite_routes_to_plugin(monkeypatch)` (function) — A rewrite decision should re-resolve the command and route to the new one.
