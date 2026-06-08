---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/skills/test_google_oauth_setup.py

Symbols in `tests/skills/test_google_oauth_setup.py`.

- L22 `FakeCredentials` (class)
- L23 `__init__(self, payload=None)` (method)
- L42 `to_json(self)` (method)
- L46 `FakeFlow` (class)
- L53 `__init__(self, client_secrets_file, scopes, *, redirect_uri=None, state=None, code_verifier=None, autogenerate_code_verifier=False)` (method)
- L79 `reset(cls)` (method)
- L87 `from_client_secrets_file(cls, client_secrets_file, scopes, **kwargs)` (method)
- L92 `authorization_url(self, **kwargs)` (method)
- L96 `fetch_token(self, **kwargs)` (method)
- L103 `setup_module(monkeypatch, tmp_path)` (function)
- L135 `TestGetAuthUrl` (class)
- L136 `test_persists_state_and_code_verifier_for_later_exchange(self, setup_module, capsys)` (method)
- L151 `TestExchangeAuthCode` (class)
- L152 `test_reuses_saved_pkce_material_for_plain_code(self, setup_module)` (method)
- L168 `test_extracts_code_from_redirect_url_and_checks_state(self, setup_module)` (method)
- L180 `test_passes_scopes_from_redirect_url_to_flow(self, setup_module)` (method) — Callback URL carries space-delimited scope list; Flow must receive it (not full SCOPES).
- L196 `test_rejects_state_mismatch(self, setup_module, capsys)` (method)
- L210 `test_requires_pending_auth_session(self, setup_module, capsys)` (method)
- L218 `test_keeps_pending_auth_session_when_exchange_fails(self, setup_module, capsys)` (method)
- L232 `test_accepts_narrower_scopes_with_warning(self, setup_module, capsys)` (method) — Partial scopes are accepted with a warning (gws migration: v2.0).
- L261 `TestHermesConstantsFallback` (class) — Tests for _hermes_home.py fallback when hermes_constants is unavailable.
- L269 `_load_helper(self, monkeypatch)` (method) — Load _hermes_home.py with hermes_constants blocked.
- L278 `test_fallback_uses_hermes_home_env_var(self, monkeypatch, tmp_path)` (method) — When hermes_constants is missing, HERMES_HOME comes from env var.
- L284 `test_fallback_defaults_to_dot_hermes(self, monkeypatch)` (method) — When hermes_constants is missing and HERMES_HOME unset, default to ~/.hermes.
- L290 `test_fallback_ignores_empty_hermes_home(self, monkeypatch)` (method) — Empty/whitespace HERMES_HOME is treated as unset.
- L296 `test_fallback_display_hermes_home_shortens_path(self, monkeypatch)` (method) — Fallback display_hermes_home() uses ~/ shorthand like the real one.
- L302 `test_fallback_display_hermes_home_profile_path(self, monkeypatch)` (method) — Fallback display_hermes_home() handles profile paths under ~/.
- L308 `test_fallback_display_hermes_home_custom_path(self, monkeypatch)` (method) — Fallback display_hermes_home() returns full path for non-home locations.
- L314 `test_delegates_to_hermes_constants_when_available(self)` (method) — When hermes_constants IS importable, _hermes_home delegates to it.
- L327 `_load_setup_module(monkeypatch)` (function) — Load setup.py without stubbing _ensure_deps (for install_deps tests).
- L338 `_force_deps_missing(monkeypatch)` (function) — Make `import googleapiclient` / `import google_auth_oauthlib` fail so
- L345 `TestInstallDeps` (class) — Tests for install_deps() interpreter/installer selection.
- L353 `test_returns_early_when_already_installed(self, monkeypatch)` (method) — If both libs import, no installer subprocess runs at all.
- L372 `test_uses_pip_when_available(self, monkeypatch)` (method) — When pip works, install_deps succeeds via pip and never calls uv.
- L395 `test_falls_back_to_uv_when_pip_missing(self, monkeypatch)` (method) — No pip → uv pip install --python <interpreter> is used.
- L419 `test_returns_false_when_no_pip_and_no_uv(self, monkeypatch, capsys)` (method) — No pip AND no uv → failure, with the [google] extra hint printed.
- L434 `test_returns_false_when_uv_fallback_also_fails(self, monkeypatch, capsys)` (method) — uv present but its install fails → failure surfaced (not swallowed).
