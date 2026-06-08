---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session_reset_notify.py

Symbols in `tests/gateway/test_session_reset_notify.py`.

- L25 `_make_source(platform=Platform.TELEGRAM, chat_id='123', user_id='u1')` (function)
- L33 `_make_store(policy=None, tmp_path=None)` (function)
- L45 `TestShouldResetReason` (class)
- L46 `test_returns_none_when_not_expired(self, tmp_path)` (method)
- L60 `test_returns_idle_when_idle_expired(self, tmp_path)` (method)
- L74 `test_returns_daily_when_daily_boundary_crossed(self, tmp_path)` (method)
- L89 `test_returns_none_when_mode_is_none(self, tmp_path)` (method)
- L108 `TestSessionEntryReason` (class)
- L109 `test_auto_reset_reason_stored(self, tmp_path)` (method)
- L130 `test_reset_had_activity_false_when_no_tokens(self, tmp_path)` (method) — Expired session with no tokens → reset_had_activity=False.
- L147 `test_reset_had_activity_true_when_tokens_used(self, tmp_path)` (method) — Expired session with tokens → reset_had_activity=True.
- L170 `TestResetPolicyNotify` (class)
- L171 `test_notify_defaults_true(self)` (method)
- L175 `test_notify_exclude_defaults(self)` (method)
- L180 `test_from_dict_with_notify_false(self)` (method)
- L184 `test_from_dict_with_custom_excludes(self)` (method)
- L190 `test_from_dict_preserves_defaults_on_missing_keys(self)` (method)
- L195 `test_to_dict_roundtrip(self)` (method)
- L211 `TestSessionEntryAutoResetRoundtrip` (class)
- L212 `test_was_auto_reset_persists_across_roundtrip(self, tmp_path)` (method) — was_auto_reset=True survives to_dict() → from_dict() (gateway restart).
- L239 `test_reset_had_activity_persists_across_roundtrip(self, tmp_path)` (method) — reset_had_activity survives to_dict() → from_dict() (gateway restart).
- L263 `test_auto_reset_reason_none_roundtrip(self, tmp_path)` (method) — auto_reset_reason=None (no reset) survives roundtrip cleanly.
