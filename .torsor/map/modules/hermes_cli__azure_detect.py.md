---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/azure_detect.py

Symbols in `hermes_cli/azure_detect.py`.

- L66 `DetectionResult` (class) — Everything auto-detection could gather from a base URL + API key.
- L92 `_resolve_credential(api_key: Any, token_provider: Optional[Callable[[], str]]=None)` (function) — Coerce wizard inputs into a (token, mode) pair.
- L131 `_apply_auth_headers(req: urllib_request.Request, token: Optional[str], mode: str)` (function) — Attach the right auth headers to ``req`` based on credential mode.
- L148 `_http_get_json(url: str, api_key: Any, timeout: float=6.0, *, token_provider: Optional[Callable[[], str]]=None)` (function) — GET a URL with the appropriate auth headers.  Return
- L177 `_strip_trailing_v1(url: str)` (function) — Strip trailing ``/v1`` or ``/v1/`` so we can construct sub-paths.
- L182 `_looks_like_anthropic_path(url: str)` (function) — Return True when the URL's path ends in ``/anthropic`` or
- L194 `_extract_model_ids(payload: dict)` (function) — Extract a list of model IDs from an OpenAI-shaped ``/models``
- L211 `_probe_openai_models(base_url: str, api_key: Any, *, token_provider: Optional[Callable[[], str]]=None)` (function) — Probe ``<base>/models`` for an OpenAI-shaped response.
- L247 `_probe_anthropic_messages(base_url: str, api_key: Any, *, token_provider: Optional[Callable[[], str]]=None)` (function) — Send a zero-token request to ``<base>/v1/messages`` and check
- L297 `detect(base_url: str, api_key: Any='', *, token_provider: Optional[Callable[[], str]]=None)` (function) — Inspect an Azure endpoint and describe its transport + models.
- L362 `lookup_context_length(model: str, base_url: str, api_key: Any='', *, token_provider: Optional[Callable[[], str]]=None)` (function) — Thin wrapper around :func:`agent.model_metadata.get_model_context_length`
