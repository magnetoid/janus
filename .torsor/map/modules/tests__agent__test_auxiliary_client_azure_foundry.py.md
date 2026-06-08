---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_auxiliary_client_azure_foundry.py

Symbols in `tests/agent/test_auxiliary_client_azure_foundry.py`.

- L35 `_reset_credential_cache()` (function)
- L43 `fake_azure_identity(monkeypatch)` (function) — Stand-in for azure.identity (keeps CI hermetic when the SDK is
- L69 `patch_load_config(monkeypatch)` (function) — Helper to set model_cfg seen by _try_azure_foundry.
- L84 `TestAuxAzureFoundryApiKey` (class)
- L85 `test_chat_completions_returns_plain_openai_client(self, monkeypatch, patch_load_config)` (method)
- L102 `test_codex_responses_wraps_in_codex_aux_client(self, monkeypatch, patch_load_config)` (method)
- L118 `test_no_key_returns_none(self, monkeypatch, patch_load_config)` (method)
- L132 `test_no_model_returns_none(self, monkeypatch, patch_load_config)` (method) — Azure has no fallback aux model — fail soft so the auto chain
- L154 `TestAuxAzureFoundryEntra` (class)
- L155 `test_callable_api_key_reaches_openai_constructor(self, monkeypatch, fake_azure_identity, patch_load_config)` (method) — The token provider callable must arrive at ``OpenAI(api_key=...)``
- L201 `test_codex_responses_with_entra_wraps_correctly(self, monkeypatch, fake_azure_identity, patch_load_config)` (method) — GPT-5.x deployment on Entra ID — auto-upgraded to
- L235 `test_entra_anthropic_messages_uses_bearer_hook(self, monkeypatch, fake_azure_identity, patch_load_config)` (method) — Entra ID + anthropic_messages: runtime returns a callable
- L292 `TestResolveProviderClientAzureFoundry` (class)
- L293 `test_dispatches_to_azure_branch_not_generic_api_key_path(self, monkeypatch, fake_azure_identity, patch_load_config)` (method) — End-to-end: the public ``resolve_provider_client`` entry
- L326 `test_warns_and_returns_none_on_failure(self, monkeypatch, patch_load_config, caplog)` (method) — When azure-foundry is requested but cannot be resolved
