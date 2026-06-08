---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_fresh_reset_skill_injection.py

Symbols in `tests/gateway/test_fresh_reset_skill_injection.py`.

- L33 `_make_store(tmp_path)` (function)
- L37 `_make_source(chat_id='123', user_id='u1')` (function)
- L45 `_is_new_session(entry)` (function) — Mirror of the predicate in ``_handle_message_with_agent``.
- L62 `TestResetSessionStampsFreshReset` (class)
- L63 `test_reset_session_sets_is_fresh_reset_true(self, tmp_path)` (method)
- L74 `test_reset_session_unknown_key_returns_none(self, tmp_path)` (method)
- L78 `test_fresh_session_does_not_have_is_fresh_reset(self, tmp_path)` (method) — A vanilla first-time session should not carry the flag.
- L89 `TestIsNewSessionSurvivesUpdatedAtBump` (class)
- L90 `test_is_new_session_true_after_reset_then_next_message(self, tmp_path)` (method) — The actual bug: _is_new_session was False on message after /reset.
- L107 `test_flag_consumed_after_first_read(self, tmp_path)` (method) — After the message handler consumes is_fresh_reset, the NEXT
- L132 `TestVanillaBehaviorUnaffected` (class)
- L133 `test_ongoing_session_not_flagged_as_new(self, tmp_path)` (method)
- L144 `test_idle_auto_reset_does_not_set_is_fresh_reset(self, tmp_path)` (method) — Idle/daily auto-resets use was_auto_reset — confirm they do NOT
- L174 `TestPersistence` (class)
- L175 `test_is_fresh_reset_survives_to_dict_from_dict(self, tmp_path)` (method) — Protect against the gateway restarting between /reset and the
- L189 `test_default_false_when_missing_from_dict(self, tmp_path)` (method) — Older sessions.json files written before this field existed must
