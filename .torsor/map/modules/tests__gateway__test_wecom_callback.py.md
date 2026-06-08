---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_wecom_callback.py

Symbols in `tests/gateway/test_wecom_callback.py`.

- L13 `_app(name='test-app', corp_id='ww1234567890', agent_id='1000002')` (function)
- L24 `_config(apps=None)` (function)
- L31 `TestWecomCrypto` (class)
- L32 `test_roundtrip_encrypt_decrypt(self)` (method)
- L47 `test_signature_mismatch_raises(self)` (method)
- L57 `TestWecomCallbackEventConstruction` (class)
- L58 `test_build_event_extracts_text_message(self)` (method)
- L78 `test_build_event_returns_none_for_subscribe(self)` (method)
- L93 `TestWecomCallbackRouting` (class)
- L94 `test_user_app_key_scopes_across_corps(self)` (method)
- L101 `test_send_selects_correct_app_for_scoped_chat_id(self)` (method)
- L131 `test_send_falls_back_from_bare_user_id_when_unique(self)` (method)
- L156 `TestWecomCallbackSendTokenRefresh` (class)
- L158 `test_send_retries_with_fresh_token_on_errcode_40001(self)` (method) — errcode=40001 must evict the cached token, refresh, and retry once.
- L195 `test_send_retries_with_fresh_token_on_errcode_42001(self)` (method) — errcode=42001 (token expired) must also trigger the refresh-retry path.
- L228 `test_send_does_not_retry_on_non_token_errcode(self)` (method) — Errors unrelated to token validity must fail immediately without retrying.
- L251 `test_send_fails_cleanly_when_retry_also_fails(self)` (method) — If the refreshed token is also rejected, return failure without looping further.
- L280 `TestWecomCallbackPollLoop` (class)
- L282 `test_poll_loop_dispatches_handle_message(self, monkeypatch)` (method)
