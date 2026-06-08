---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/runtime_provider.py

Symbols in `hermes_cli/runtime_provider.py`.

- L37 `_normalize_custom_provider_name(value: str)` (function)
- L41 `_loopback_hostname(host: str)` (function)
- L46 `_config_base_url_trustworthy_for_bare_custom(cfg_base_url: str, cfg_provider: str)` (function) — Decide whether ``model.base_url`` may back bare ``custom`` runtime resolution.
- L76 `_detect_api_mode_for_url(base_url: str)` (function) — Auto-detect api_mode from the resolved base URL.
- L103 `_host_derived_api_key(base_url: str)` (function) — Look up `<VENDOR>_API_KEY` in the env, derived from the base URL host.
- L160 `_auto_detect_local_model(base_url: str)` (function) — Query a local server for its model name when only one model is loaded.
- L183 `_get_model_config()` (function)
- L205 `_provider_supports_explicit_api_mode(provider: Optional[str], configured_provider: Optional[str]=None)` (function) — Check whether a persisted api_mode should be honored for a given provider.
- L222 `_copilot_runtime_api_mode(model_cfg: Dict[str, Any], api_key: str)` (function)
- L254 `_parse_api_mode(raw: Any)` (function) — Validate an api_mode value from config. Returns None if invalid.
- L263 `_maybe_apply_codex_app_server_runtime(*, provider: str, api_mode: str, model_cfg: Optional[Dict[str, Any]])` (function) — Optional opt-in: rewrite api_mode → "codex_app_server" for OpenAI/Codex
- L289 `_resolve_runtime_from_pool_entry(*, provider: str, entry: PooledCredential, requested_provider: str, model_cfg: Optional[Dict[str, Any]]=None, pool: Optional[CredentialPool]=None, target_model: Optional[str]=None)` (function)
- L426 `resolve_requested_provider(requested: Optional[str]=None)` (function) — Resolve provider request from explicit arg, config, then env.
- L445 `_try_resolve_from_custom_pool(base_url: str, provider_label: str, api_mode_override: Optional[str]=None, provider_name: Optional[str]=None)` (function) — Check if a credential pool exists for a custom endpoint and return a runtime dict if so.
- L477 `_lift_max_output_tokens(entry: Dict[str, Any], result: Dict[str, Any])` (function) — Propagate a per-provider output cap onto the resolved runtime dict.
- L492 `_get_named_custom_provider(requested_provider: str)` (function)
- L637 `_custom_provider_request_overrides(custom_provider: Dict[str, Any])` (function)
- L644 `_resolve_named_custom_runtime(*, requested_provider: str, explicit_api_key: Optional[str]=None, explicit_base_url: Optional[str]=None)` (function)
- L767 `_resolve_openrouter_runtime(*, requested_provider: str, explicit_api_key: Optional[str]=None, explicit_base_url: Optional[str]=None)` (function)
- L907 `_resolve_azure_foundry_runtime(*, requested_provider: str, model_cfg: Dict[str, Any], explicit_api_key: Optional[str]=None, explicit_base_url: Optional[str]=None, target_model: Optional[str]=None)` (function) — Resolve an Azure Foundry runtime entry.
- L1076 `_resolve_explicit_runtime(*, provider: str, requested_provider: str, model_cfg: Dict[str, Any], explicit_api_key: Optional[str]=None, explicit_base_url: Optional[str]=None)` (function)
- L1228 `resolve_runtime_provider(*, requested: Optional[str]=None, explicit_api_key: Optional[str]=None, explicit_base_url: Optional[str]=None, target_model: Optional[str]=None)` (function) — Resolve runtime provider credentials for agent execution.
- L1691 `format_runtime_provider_error(error: Exception)` (function)
