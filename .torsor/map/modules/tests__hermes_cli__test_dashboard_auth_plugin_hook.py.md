---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dashboard_auth_plugin_hook.py

Symbols in `tests/hermes_cli/test_dashboard_auth_plugin_hook.py`.

- L17 `_Stub` (class)
- L21 `start_login(self, *, redirect_uri)` (method)
- L24 `complete_login(self, *, code, state, code_verifier, redirect_uri)` (method)
- L27 `verify_session(self, *, access_token)` (method)
- L30 `refresh_session(self, *, refresh_token)` (method)
- L33 `revoke_session(self, *, refresh_token)` (method)
- L37 `_MinimalManager` (class) — The fixture only needs whatever PluginContext touches at register-time.
- L52 `_isolated_registry()` (function)
- L58 `_make_ctx(name: str='dashboard-auth-stub')` (function)
- L63 `test_plugin_ctx_exposes_register_dashboard_auth_provider()` (function)
- L68 `test_plugin_ctx_register_dashboard_auth_provider_happy_path()` (function)
- L76 `test_plugin_ctx_silently_ignores_non_provider(caplog)` (function) — Mirror image_gen behaviour: log warning, leave registry empty.
