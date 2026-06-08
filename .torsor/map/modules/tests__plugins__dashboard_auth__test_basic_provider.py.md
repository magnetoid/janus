---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/dashboard_auth/test_basic_provider.py

Symbols in `tests/plugins/dashboard_auth/test_basic_provider.py`.

- L25 `basic()` (function)
- L30 `_clear_basic_env(monkeypatch)` (function)
- L46 `TestPasswordHashing` (class)
- L47 `test_hash_then_verify_round_trips(self, basic)` (method)
- L52 `test_wrong_password_fails(self, basic)` (method)
- L56 `test_malformed_hash_returns_false(self, basic)` (method)
- L60 `test_two_hashes_of_same_password_differ(self, basic)` (method)
- L70 `TestProvider` (class)
- L71 `_make(self, basic, **kw)` (method)
- L80 `test_protocol_compliant(self, basic)` (method)
- L83 `test_supports_password_true(self, basic)` (method)
- L86 `test_login_mints_session(self, basic)` (method)
- L93 `test_bad_credentials_raise(self, basic)` (method)
- L99 `test_verify_round_trips_and_rejects_tamper(self, basic)` (method)
- L105 `test_access_token_not_accepted_as_refresh(self, basic)` (method)
- L114 `test_refresh_round_trips(self, basic)` (method)
- L121 `test_refresh_with_garbage_raises(self, basic)` (method)
- L126 `test_cross_secret_token_does_not_verify(self, basic)` (method)
- L132 `test_revoke_is_silent(self, basic)` (method)
- L136 `test_oauth_methods_raise_not_implemented(self, basic)` (method)
- L145 `test_construction_validates_inputs(self, basic)` (method)
- L166 `TestRegister` (class)
- L167 `test_skips_when_no_username(self, basic, monkeypatch)` (method)
- L174 `test_skips_when_username_but_no_password(self, basic, monkeypatch)` (method)
- L182 `test_registers_with_env_plaintext_password(self, basic, monkeypatch)` (method)
- L196 `test_registers_with_precomputed_hash(self, basic, monkeypatch)` (method)
- L211 `test_env_password_overrides_config(self, basic, monkeypatch)` (method)
- L231 `test_explicit_secret_makes_sessions_portable(self, basic, monkeypatch)` (method)
