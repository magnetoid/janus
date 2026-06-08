---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_context_engine_host_contract.py

Symbols in `tests/agent/test_context_engine_host_contract.py`.

- L35 `_bare_agent()` (function)
- L44 `test_transition_runs_full_lifecycle_in_order()` (function) — End → reset → start → carry_over, in that order, when all inputs apply.
- L72 `test_transition_passes_conversation_id_from_gateway_session_key()` (function) — on_session_start receives ``conversation_id`` from ``_gateway_session_key``.
- L93 `test_transition_skips_optional_hooks_when_engine_lacks_them()` (function) — Engines that don't implement on_session_end/carry_over still work.
- L126 `test_reset_session_state_delegates_to_transition_when_args_provided()` (function) — ``reset_session_state(previous_messages=..., old_session_id=...)`` fires full lifecycle.
- L146 `test_reset_session_state_default_call_only_resets()` (function) — Bare ``reset_session_state()`` still only resets the engine (no end/start).
- L161 `test_update_from_response_forwards_canonical_cache_buckets()` (function) — conversation_loop passes cache_read/write/reasoning tokens to engine.
- L198 `test_discover_context_engines_includes_plugin_registered_engines(monkeypatch)` (function) — Plugin-registered context engines appear in the ``hermes plugins`` picker.
- L226 `test_discover_context_engines_dedupes_by_name(monkeypatch)` (function) — Repo-shipped engine wins when name collides with a plugin-registered one.
- L251 `test_engine_collector_forwards_register_command_to_plugin_manager()` (function) — A plugin context engine can register a slash command via ``ctx.register_command``.
- L278 `test_engine_collector_rejects_builtin_command_conflicts()` (function) — Context engine cannot shadow built-in slash commands like /help.
