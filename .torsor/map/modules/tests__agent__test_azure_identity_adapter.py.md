---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_azure_identity_adapter.py

Symbols in `tests/agent/test_azure_identity_adapter.py`.

- L33 `_reset_adapter_cache()` (function)
- L45 `TestEntraScopeConstant` (class) — Pin the Microsoft-documented Foundry inference scope.
- L62 `test_default_scope_matches_microsoft_documentation(self)` (method)
- L72 `TestMaterializeBearerForHttp` (class) — The only helper that mints a real bearer JWT — must call the
- L76 `test_callable_is_invoked_and_returns_token(self)` (method)
- L88 `test_string_passes_through(self)` (method)
- L92 `test_callable_returning_empty_raises(self)` (method)
- L97 `test_empty_string_raises(self)` (method)
- L110 `TestBuildBearerHttpClient` (class) — ``build_bearer_http_client`` returns an ``httpx.Client`` whose
- L116 `test_returns_httpx_client_with_request_hook(self)` (method)
- L128 `test_hook_overrides_authorization_header(self)` (method)
- L167 `test_hook_strips_auth_headers_and_warns_when_token_provider_fails(self, caplog)` (method) — When the token provider fails (chain exhausted, IMDS down, az
- L210 `test_rejects_non_callable_provider(self)` (method)
- L217 `test_forwards_httpx_kwargs(self)` (method)
- L231 `TestIsTokenProvider` (class)
- L232 `test_callable_is_token_provider(self)` (method)
- L236 `test_string_is_not_token_provider(self)` (method)
- L249 `TestEntraIdentityConfig` (class) — The serializable config that crosses multiprocessing boundaries —
- L253 `test_to_dict_round_trip(self)` (method)
- L262 `test_from_dict_handles_empty_strings(self)` (method)
- L271 `test_from_dict_ignores_legacy_identity_keys(self)` (method) — Old config.yaml that still has model.entra.client_id /
- L286 `test_constructor_normalizes_empty_scope(self)` (method)
- L291 `test_from_dict_default_scope_override(self)` (method)
- L299 `test_dataclass_is_frozen(self)` (method)
- L312 `_FakeAzureIdentity` (class) — Stand-in for the ``azure.identity`` module.
- L319 `__init__(self)` (method)
- L324 `DefaultAzureCredential(self, **kwargs)` (method)
- L332 `get_bearer_token_provider(self, credential, scope)` (method)
- L339 `fake_azure_identity(monkeypatch)` (function) — Install a fake azure.identity into sys.modules and stub the
- L360 `TestBuildCredential` (class)
- L361 `test_default_kwargs_are_minimal(self, fake_azure_identity)` (method) — SDK default for ``exclude_interactive_browser_credential`` is
- L375 `test_interactive_browser_opt_in(self, fake_azure_identity)` (method) — When the user explicitly sets
- L385 `test_credential_is_cached_per_config(self, fake_azure_identity)` (method)
- L393 `test_distinct_configs_get_distinct_credentials(self, fake_azure_identity)` (method)
- L400 `test_reset_cache_invalidates(self, fake_azure_identity)` (method)
- L413 `TestBuildTokenProvider` (class)
- L414 `test_returns_callable_for_scope(self, fake_azure_identity)` (method)
- L421 `test_falls_back_to_default_scope_when_unspecified(self, fake_azure_identity)` (method) — When neither ``scope`` nor ``config`` is provided,
- L433 `test_explicit_scope_wins_over_base_url(self, fake_azure_identity)` (method)
- L441 `test_config_object_wins_over_kwargs(self, fake_azure_identity)` (method)
- L457 `TestRequireAzureIdentityMissing` (class)
- L458 `test_clear_error_when_lazy_install_disabled(self, monkeypatch)` (method) — When azure-identity isn't importable AND lazy installs are
- L499 `TestHasAzureIdentityCredentials` (class)
- L500 `test_returns_false_when_package_missing_and_install_disabled(self, monkeypatch)` (method)
- L507 `test_lazy_install_triggered_when_package_missing(self, monkeypatch)` (method) — With allow_install=True (default), the probe must trigger the
- L548 `test_returns_true_on_successful_token_mint(self, fake_azure_identity)` (method)
- L552 `test_returns_false_when_get_token_raises(self, monkeypatch)` (method)
- L565 `test_returns_false_on_timeout(self, monkeypatch)` (method) — Slow IMDS / network must time out, not hang the caller.
- L596 `TestDescribeActiveCredential` (class)
- L597 `test_reports_not_installed(self, monkeypatch)` (method)
- L607 `test_reports_install_failure(self, monkeypatch)` (method) — When lazy install is allowed but fails (e.g. lazy installs
- L624 `test_reports_env_sources_for_managed_identity(self, fake_azure_identity, monkeypatch)` (method)
- L632 `test_reports_env_sources_for_workload_identity(self, fake_azure_identity, monkeypatch)` (method)
- L639 `test_reports_env_sources_for_service_principal(self, fake_azure_identity, monkeypatch)` (method)
- L648 `test_reports_error_on_chain_failure(self, monkeypatch)` (method)
