---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dashboard_auth_provider_base.py

Symbols in `tests/hermes_cli/test_dashboard_auth_provider_base.py`.

- L25 `test_session_has_required_fields()` (function)
- L41 `test_login_start_has_redirect_and_state()` (function)
- L55 `test_abstract_provider_cannot_be_instantiated()` (function)
- L60 `_BrokenProvider` (class)
- L66 `test_assert_protocol_compliance_rejects_partial_impl()` (function)
- L71 `_CompliantProvider` (class)
- L75 `start_login(self, *, redirect_uri: str)` (method)
- L78 `complete_login(self, *, code, state, code_verifier, redirect_uri)` (method)
- L85 `verify_session(self, *, access_token: str)` (method)
- L88 `refresh_session(self, *, refresh_token: str)` (method)
- L95 `revoke_session(self, *, refresh_token: str)` (method)
- L99 `test_assert_protocol_compliance_accepts_full_impl()` (function)
- L104 `test_assert_protocol_compliance_rejects_missing_name_attr()` (function)
- L112 `test_assert_protocol_compliance_rejects_missing_display_name()` (function)
- L134 `_isolated_registry()` (function) — Every test starts with an empty registry and leaves it empty.
- L141 `test_registry_register_and_get()` (function)
- L147 `test_registry_get_missing_returns_none()` (function)
- L151 `test_registry_lists_in_registration_order()` (function)
- L166 `test_registry_rejects_non_compliant_provider()` (function)
- L171 `test_registry_rejects_duplicate_name()` (function)
- L177 `test_registry_clear_drops_all()` (function)
