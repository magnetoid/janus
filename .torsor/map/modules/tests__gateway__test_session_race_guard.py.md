---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session_race_guard.py

Symbols in `tests/gateway/test_session_race_guard.py`.

- L22 `_FakeAdapter` (class) — Minimal adapter stub for testing.
- L25 `__init__(self)` (method)
- L30 `send(self, chat_id, text, **kwargs)` (method)
- L33 `interrupt_session_activity(self, session_key, chat_id)` (method)
- L40 `_make_runner()` (function)
- L70 `_make_event(text='hello', chat_id='12345')` (function)
- L82 `test_sentinel_placed_before_agent_setup()` (function) — After passing the 'not running' guard, the sentinel must be
- L110 `test_sentinel_cleaned_up_after_handler_returns()` (function) — If _handle_message_with_agent returns normally, the sentinel
- L132 `test_sentinel_cleaned_up_on_exception()` (function) — If _handle_message_with_agent raises, the sentinel must still
- L155 `test_second_message_during_sentinel_queued_not_duplicate()` (function) — While the sentinel is set (agent setup in progress), a second
- L196 `test_merge_pending_message_event_merges_text_and_photo_followups()` (function)
- L229 `test_merge_pending_message_event_promotes_document_followups_over_text()` (function)
- L263 `test_recent_telegram_text_followup_is_queued_without_interrupt()` (function)
- L283 `test_recent_telegram_followups_append_in_pending_queue()` (function)
- L307 `test_command_messages_do_not_leave_sentinel()` (function) — Slash commands (/help, /status, etc.) return early from
- L334 `test_start_command_is_noop_and_does_not_show_help()` (function) — Telegram /start is a platform ping; it must not dump /help output.
- L350 `test_start_command_is_noop_during_active_session()` (function) — A mid-run /start must not interrupt the active agent or show commands.
- L379 `test_active_session_bypass_commands_dispatch_without_interrupt(command_text, handler_attr, handler_result)` (function) — Gateway-handled bypass commands must return directly while an agent runs.
- L405 `test_stop_during_sentinel_force_cleans_session()` (function) — If /stop arrives while the sentinel is set (agent still starting),
- L446 `test_stop_hard_kills_running_agent()` (function) — When /stop arrives while a real agent is running, it must:
- L489 `test_stop_clears_pending_messages()` (function) — When /stop hard-kills a running agent, any pending messages
- L520 `test_shutdown_skips_sentinel()` (function) — During gateway shutdown, sentinel entries in _running_agents
