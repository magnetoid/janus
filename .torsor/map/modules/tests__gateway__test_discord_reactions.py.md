---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_reactions.py

Symbols in `tests/gateway/test_discord_reactions.py`.

- L15 `_ensure_discord_mock()` (function)
- L46 `FakeTree` (class)
- L47 `__init__(self)` (method)
- L50 `command(self, *, name, description)` (method)
- L59 `adapter()` (function)
- L71 `_make_event(message_id: str, raw_message)` (function)
- L88 `test_process_message_background_adds_and_swaps_reactions(adapter)` (function)
- L114 `test_interaction_backed_events_do_not_attempt_reactions(adapter)` (function)
- L150 `test_reaction_helper_failures_do_not_break_message_flow(adapter)` (function)
- L174 `test_reactions_disabled_via_env(adapter, monkeypatch)` (function) — When DISCORD_REACTIONS=false, no reactions should be added.
- L204 `test_reactions_disabled_via_env_zero(adapter, monkeypatch)` (function) — DISCORD_REACTIONS=0 should also disable reactions.
- L222 `test_reactions_enabled_by_default(adapter, monkeypatch)` (function) — When DISCORD_REACTIONS is unset, reactions should still work (default: true).
- L238 `test_on_processing_complete_cancelled_removes_eyes_without_terminal_reaction(adapter)` (function)
