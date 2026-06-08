---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_clarify_buttons.py

Symbols in `tests/gateway/test_discord_clarify_buttons.py`.

- L39 `_make_adapter(*, allowed_users=None, allowed_roles=None)` (function)
- L48 `_clear_clarify_state()` (function)
- L56 `_make_interaction(*, user_id='42', display_name='Tester', roles=None, include_message=True)` (function) — Build a mock discord.Interaction with response.edit_message /
- L84 `TestClarifyChoiceViewConstruction` (class) — The view should build numeric buttons plus an Other button.
- L87 `test_renders_n_choice_buttons_plus_other(self)` (method)
- L107 `test_caps_at_24_choices_plus_other(self)` (method)
- L118 `test_truncates_long_choice_label(self)` (method)
- L137 `TestClarifyChoiceResolve` (class) — Clicking a numeric button should resolve the clarify entry.
- L140 `setup_method(self)` (method)
- L144 `test_choice_resolves_with_canonical_choice_text(self)` (method)
- L169 `test_choice_falls_back_to_label_text_when_entry_missing(self)` (method) — If the gateway entry vanished (race / stale view), the button's
- L187 `test_already_resolved_sends_ephemeral_reply(self)` (method)
- L205 `test_unauthorized_user_rejected(self)` (method)
- L234 `TestClarifyOtherButton` (class) — Clicking Other should flip the entry into text-capture mode.
- L237 `setup_method(self)` (method)
- L241 `test_other_flips_entry_to_awaiting_text(self)` (method)
- L270 `test_other_unauthorized_user_rejected(self)` (method)
- L293 `TestDiscordSendClarify` (class) — Verify send_clarify renders an embed and (optionally) attaches the view.
- L296 `setup_method(self)` (method)
- L300 `test_multi_choice_attaches_view(self)` (method)
- L328 `test_open_ended_omits_view(self)` (method)
- L352 `test_routes_to_thread_when_metadata_thread_id_set(self)` (method)
- L373 `test_not_connected_returns_failure(self)` (method)
- L387 `test_filters_empty_and_whitespace_choices(self)` (method)
