---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_auth_manual_paste.py

Symbols in `tests/hermes_cli/test_auth_manual_paste.py`.

- L53 `test_is_remote_session_detects_known_remote_envvar(monkeypatch, envvar)` (function) — Each documented remote-console env var must trip the check.
- L75 `test_is_remote_session_false_when_no_remote_envvars(monkeypatch)` (function)
- L95 `test_parse_full_callback_url()` (function)
- L107 `test_parse_callback_url_https_and_extra_params()` (function)
- L115 `test_parse_bare_query_string_with_leading_question_mark()` (function)
- L121 `test_parse_bare_query_fragment_no_question_mark()` (function)
- L127 `test_parse_bare_opaque_code_value()` (function) — Some users only copy the ``code`` value itself.
- L134 `test_parse_callback_with_error_field()` (function)
- L144 `test_parse_empty_input_returns_all_none()` (function)
- L154 `test_parse_whitespace_only_returns_all_none()` (function)
- L159 `test_parse_malformed_url_does_not_crash()` (function)
- L171 `test_prompt_reads_stdin_and_parses(monkeypatch)` (function)
- L188 `test_prompt_eof_returns_all_none(monkeypatch)` (function)
- L200 `test_prompt_keyboard_interrupt_returns_all_none(monkeypatch)` (function)
- L217 `_StubTokenResponse` (class)
- L220 `__init__(self, payload)` (method)
- L224 `json(self)` (method)
- L228 `test_xai_loopback_login_manual_paste_skips_http_server(monkeypatch)` (function) — ``manual_paste=True`` must NOT bind a loopback HTTP server.
- L304 `test_xai_loopback_login_manual_paste_state_mismatch_raises(monkeypatch)` (function) — A pasted callback with the wrong state must still be rejected.
- L333 `test_xai_loopback_login_manual_paste_bare_code_succeeds(monkeypatch)` (function) — Bare-code paste (state=None) must complete login under manual_paste.
- L381 `test_xai_loopback_login_loopback_path_rejects_missing_state(monkeypatch)` (function) — Loopback (manual_paste=False) must NOT accept ``state=None``.
- L434 `test_xai_loopback_login_manual_paste_missing_code_raises(monkeypatch)` (function) — Empty paste must surface as ``xai_code_missing``, not crash.
- L467 `test_xai_loopback_login_timeout_falls_back_to_manual_paste(monkeypatch)` (function) — Loopback timeout should offer the existing manual-paste path.
- L561 `test_xai_loopback_login_timeout_noninteractive_reraises(monkeypatch)` (function) — Non-interactive stdin must keep the original timeout error.
- L629 `test_ssh_hint_mentions_manual_paste_for_non_ssh_remotes(monkeypatch)` (function) — Users on Cloud Shell / Codespaces have no real SSH client; the
