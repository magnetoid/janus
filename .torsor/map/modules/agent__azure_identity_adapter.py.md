---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/azure_identity_adapter.py

Symbols in `agent/azure_identity_adapter.py`.

- L60 `has_azure_identity_installed()` (function) — Return True if `azure-identity` can be imported right now.
- L72 `_require_azure_identity()` (function) — Import ``azure.identity``, lazy-installing it if allowed.
- L104 `reset_credential_cache()` (function) — Clear the cached ``DefaultAzureCredential``. Used by tests and
- L123 `EntraIdentityConfig` (class) — Serializable Entra ID config.
- L152 `__post_init__(self)` (method)
- L156 `to_dict(self)` (method)
- L163 `from_dict(cls, data: Optional[Dict[str, Any]], *, default_scope: Optional[str]=None)` (method)
- L174 `_build_default_credential(config: EntraIdentityConfig)` (function) — Construct a ``DefaultAzureCredential`` for ``config``.
- L194 `build_credential(config: EntraIdentityConfig)` (function) — Return the cached ``DefaultAzureCredential`` for ``config``.
- L215 `build_token_provider(scope: Optional[str]=None, *, config: Optional[EntraIdentityConfig]=None, base_url: Optional[str]=None, exclude_interactive_browser: bool=True)` (function) — Return a zero-arg callable that mints a fresh Entra bearer JWT.
- L261 `has_azure_identity_credentials(scope: Optional[str]=None, *, config: Optional[EntraIdentityConfig]=None, timeout_seconds: float=10.0, allow_install: bool=True, **overrides: Any)` (function) — Best-effort probe: can `DefaultAzureCredential` mint a token now?
- L315 `describe_active_credential(config: Optional[EntraIdentityConfig]=None, *, scope: Optional[str]=None, timeout_seconds: float=10.0, allow_install: bool=True, **overrides: Any)` (function) — Return diagnostic info about the active credential chain.
- L424 `is_token_provider(value: Any)` (function) — Return True when ``value`` is a callable Entra token provider.
- L433 `materialize_bearer_for_http(value: Any)` (function) — Return a fresh Bearer JWT for a manual HTTP request.
- L462 `build_bearer_http_client(token_provider: Callable[[], str], **httpx_kwargs: Any)` (function) — Return an ``httpx.Client`` that mints a fresh Entra bearer JWT
