---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_internal_event_bypass_pairing.py

Symbols in `tests/gateway/test_internal_event_bypass_pairing.py`.

- L26 `_FakeRegistry` (class) — Return pre-canned sessions, then None once exhausted.
- L29 `__init__(self, sessions)` (method)
- L33 `get(self, session_id)` (method)
- L38 `is_completion_consumed(self, session_id)` (method)
- L42 `_build_runner(monkeypatch, tmp_path)` (function) — Create a GatewayRunner with notifications set to 'all'.
- L59 `_watcher_dict_with_notify()` (function)
- L76 `test_notify_on_complete_sets_internal_flag(monkeypatch, tmp_path)` (function) — Synthetic completion event must have internal=True.
- L103 `test_internal_event_bypasses_authorization(monkeypatch, tmp_path)` (function) — An internal event should skip _is_user_authorized entirely.
- L152 `test_internal_event_does_not_trigger_pairing(monkeypatch, tmp_path)` (function) — An internal event with no user_id must not generate a pairing code.
- L203 `test_notify_on_complete_preserves_user_identity(monkeypatch, tmp_path)` (function) — Synthetic completion event should carry user_id and user_name from the watcher.
- L234 `test_notify_on_complete_uses_session_store_origin_for_group_topic(monkeypatch, tmp_path)` (function)
- L287 `test_none_user_id_skips_pairing(monkeypatch, tmp_path)` (function) — A non-internal event with user_id=None should be silently dropped.
- L318 `test_none_user_id_does_not_generate_pairing_code(monkeypatch, tmp_path)` (function) — A message with user_id=None must never call generate_code.
- L355 `test_non_internal_event_without_user_triggers_pairing(monkeypatch, tmp_path)` (function) — Verify the normal (non-internal) path still triggers pairing for unknown users.
