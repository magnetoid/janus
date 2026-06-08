---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_azure_foundry_entra.py

Symbols in `tests/hermes_cli/test_azure_foundry_entra.py`.

- L32 `_reset_credential_cache()` (function)
- L40 `fake_azure_identity(monkeypatch)` (function) — Identical fake to test_azure_identity_adapter — keeps Azure SDK
- L72 `TestResolveAzureFoundryRuntimeEntra` (class)
- L73 `test_returns_callable_api_key_for_entra(self, fake_azure_identity)` (method)
- L91 `test_entra_inherits_codex_responses_for_gpt5_family(self, fake_azure_identity)` (method) — GPT-5.x / o-series / codex models on Azure are Responses-API-only.
- L112 `test_entra_propagates_scope_only(self, fake_azure_identity)` (method) — ``model.entra.scope`` is the only Hermes-managed Azure SDK
- L144 `test_entra_default_scope_when_unset(self, fake_azure_identity)` (method) — When ``model.entra.scope`` is not set, the runtime resolves
- L165 `test_entra_scope_override_wins(self, fake_azure_identity)` (method) — Users on sovereign clouds / unusual tenants can set
- L186 `test_entra_with_anthropic_messages_is_supported(self, fake_azure_identity)` (method) — Entra ID now works for both OpenAI-style and Anthropic-style
- L213 `test_entra_with_explicit_api_key_uses_string_escape_hatch(self, fake_azure_identity)` (method) — Passing --api-key on the CLI overrides the entra path so a
- L232 `test_entra_runtime_dict_keeps_only_scope_override(self, fake_azure_identity)` (method)
- L255 `TestResolveAzureFoundryRuntimeApiKey` (class)
- L256 `test_default_auth_mode_uses_static_key(self, monkeypatch)` (method)
- L271 `test_explicit_auth_mode_api_key(self, monkeypatch)` (method)
- L286 `test_anthropic_messages_strips_v1_suffix(self, monkeypatch)` (method)
- L299 `test_missing_api_key_raises_with_entra_hint(self, monkeypatch)` (method)
- L323 `TestAzureFoundryAuthStatus` (class)
- L324 `test_entra_status_does_not_mint_token(self, monkeypatch, tmp_path)` (method) — Structural check — must return logged_in=True based on
- L352 `test_entra_status_reports_missing_package(self, monkeypatch)` (method)
- L373 `test_api_key_status_uses_env_var(self, monkeypatch)` (method)
- L390 `test_api_key_status_false_when_missing(self, monkeypatch)` (method)
