---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_web_oauth_dispatch.py

Symbols in `tests/hermes_cli/test_web_oauth_dispatch.py`.

- L37 `_fake_nous_device_data()` (function)
- L50 `_invoke_scope_refusal()` (function)
- L63 `test_minimax_login_does_not_launch_anthropic_flow()` (function) — Click 'Login' on MiniMax → MUST NOT return claude.ai auth_url.
- L103 `test_nous_dashboard_device_flow_ignores_legacy_scope_override(monkeypatch)` (function)
- L130 `test_nous_dashboard_device_flow_does_not_retry_legacy_scope_on_invoke_refusal(monkeypatch)` (function)
- L149 `test_codex_dashboard_worker_persists_runtime_provider(tmp_path, monkeypatch)` (function)
- L210 `test_nous_dashboard_poller_preserves_effective_scope_when_token_omits_scope(monkeypatch)` (function)
- L260 `test_minimax_dashboard_poller_accepts_absolute_ms_expired_in()` (function) — Dashboard MiniMax completion must accept unix-ms token expiry values.
- L307 `test_anthropic_pkce_branch_still_works()` (function) — Sanity: the dispatcher tightening doesn't break the legitimate Anthropic PKCE path.
- L330 `test_xai_oauth_listed_as_loopback_flow()` (function) — xAI Grok OAuth must surface in the catalog as a first-class loopback flow.
- L340 `test_xai_loopback_start_returns_authorize_url(monkeypatch)` (function) — Start MUST bind the loopback listener and hand back an xAI authorize URL.
- L392 `test_xai_loopback_worker_persists_tokens_on_success(monkeypatch)` (function) — The worker exchanges the callback code and marks the session approved.
- L448 `test_xai_loopback_worker_fails_on_state_mismatch(monkeypatch)` (function) — A mismatched OAuth state must fail the session, not persist tokens.
- L492 `test_xai_loopback_worker_skips_persist_when_cancelled(monkeypatch)` (function) — If the session is cancelled while waiting, the worker must not persist.
- L536 `test_cancel_loopback_session_shuts_down_callback_server()` (function) — Cancelling a loopback session must free the bound callback port now.
- L582 `test_unknown_pkce_provider_rejected_cleanly()` (function) — A future PKCE provider without an explicit branch must NOT silently route to Anthropic.
