---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_auth_codex_provider.py

Symbols in `tests/hermes_cli/test_auth_codex_provider.py`.

- L25 `_setup_hermes_auth(hermes_home: Path, *, access_token: str='access', refresh_token: str='refresh')` (function) — Write Codex tokens into the Hermes auth store.
- L47 `_jwt_with_exp(exp_epoch: int)` (function)
- L53 `test_read_codex_tokens_success(tmp_path, monkeypatch)` (function)
- L63 `test_read_codex_tokens_missing(tmp_path, monkeypatch)` (function)
- L75 `test_resolve_codex_runtime_credentials_missing_access_token(tmp_path, monkeypatch)` (function)
- L86 `test_resolve_codex_runtime_credentials_refreshes_expiring_token(tmp_path, monkeypatch)` (function)
- L106 `test_resolve_codex_runtime_credentials_force_refresh(tmp_path, monkeypatch)` (function)
- L125 `test_resolve_codex_runtime_credentials_falls_back_to_pool_when_singleton_empty(tmp_path, monkeypatch)` (function) — Regression for #32992 — chat path returns 401 when singleton is empty but pool has creds.
- L163 `test_resolve_codex_runtime_credentials_pool_fallback_skips_exhausted(tmp_path, monkeypatch)` (function) — The pool fallback skips entries currently in an exhaustion cooldown window.
- L196 `test_resolve_codex_runtime_credentials_pool_fallback_no_usable_entry(tmp_path, monkeypatch)` (function) — When both singleton and pool are empty/unusable, the original AuthError propagates.
- L217 `test_resolve_provider_explicit_codex_does_not_fallback(monkeypatch)` (function)
- L223 `test_save_codex_tokens_roundtrip(tmp_path, monkeypatch)` (function)
- L236 `test_save_codex_tokens_syncs_credential_pool(tmp_path, monkeypatch)` (function) — Re-auth must update the credential_pool device_code entry, not just providers.
- L303 `test_save_codex_tokens_syncs_manual_device_code_entries(tmp_path, monkeypatch)` (function) — Re-auth must also refresh ``manual:device_code`` pool entries.
- L385 `test_import_codex_cli_tokens(tmp_path, monkeypatch)` (function)
- L399 `test_import_codex_cli_tokens_missing(tmp_path, monkeypatch)` (function)
- L404 `test_codex_tokens_not_written_to_shared_file(tmp_path, monkeypatch)` (function) — Verify _save_codex_tokens writes only to Hermes auth store, not ~/.codex/.
- L425 `test_resolve_returns_hermes_auth_store_source(tmp_path, monkeypatch)` (function)
- L436 `_StubHTTPResponse` (class)
- L437 `__init__(self, status_code: int, payload, headers=None)` (method)
- L443 `json(self)` (method)
- L449 `_StubHTTPClient` (class)
- L450 `__init__(self, response)` (method)
- L453 `__enter__(self)` (method)
- L456 `__exit__(self, *args)` (method)
- L459 `post(self, *args, **kwargs)` (method)
- L463 `_patch_httpx(monkeypatch, response)` (function)
- L470 `test_refresh_parses_openai_nested_error_shape_refresh_token_reused(monkeypatch)` (function) — OpenAI returns {"error": {"code": "refresh_token_reused", "message": "..."}}
- L497 `test_refresh_parses_openai_nested_error_shape_generic_code(monkeypatch)` (function) — Nested error with arbitrary code still surfaces code + message.
- L519 `test_refresh_parses_oauth_spec_flat_error_shape_invalid_grant(monkeypatch)` (function) — Fallback path: OAuth spec-shape {"error": "invalid_grant", "error_description": "..."}
- L541 `test_refresh_falls_back_to_generic_message_on_unparseable_body(monkeypatch)` (function) — No JSON body → generic 'with status 401' message; 401 always forces relogin.
- L557 `test_refresh_429_classified_as_quota_not_auth_failure(monkeypatch)` (function) — 429 from the token endpoint is a usage-quota cap, not an auth failure.
- L591 `test_refresh_429_without_retry_after_header(monkeypatch)` (function) — 429 without a Retry-After header still classifies as quota, no relogin.
- L607 `test_is_rate_limited_auth_error_distinguishes_credential_errors()` (function) — Missing/expired credentials must NOT be treated as rate-limit errors.
- L625 `test_login_openai_codex_force_new_login_skips_existing_reuse_prompt(monkeypatch)` (function)
