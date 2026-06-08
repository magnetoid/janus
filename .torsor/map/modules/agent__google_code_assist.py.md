---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/google_code_assist.py

Symbols in `agent/google_code_assist.py`.

- L68 `CodeAssistError` (class) — Exception raised by the Code Assist (``cloudcode-pa``) integration.
- L78 `__init__(self, message: str, *, code: str='code_assist_error', status_code: Optional[int]=None, response: Any=None, retry_after: Optional[float]=None, details: Optional[Dict[str, Any]]=None)` (method)
- L110 `ProjectIdRequiredError` (class)
- L111 `__init__(self, message: str='GCP project id required for this tier')` (method)
- L119 `_build_headers(access_token: str, *, user_agent_model: str='')` (function)
- L133 `_client_metadata()` (function) — Match Google's gemini-cli exactly — unrecognized metadata may be rejected.
- L142 `_post_json(url: str, body: Dict[str, Any], access_token: str, *, timeout: float=_DEFAULT_REQUEST_TIMEOUT, user_agent_model: str='')` (function)
- L182 `_is_vpc_sc_violation(body: str)` (function) — Detect a VPC Service Controls violation from a response body.
- L210 `CodeAssistProjectInfo` (class) — Result from ``load_code_assist``.
- L218 `load_code_assist(access_token: str, *, project_id: str='', user_agent_model: str='')` (function) — Call ``POST /v1internal:loadCodeAssist`` with prod → sandbox fallback.
- L260 `_parse_load_response(resp: Dict[str, Any])` (function)
- L284 `onboard_user(access_token: str, *, tier_id: str, project_id: str='', user_agent_model: str='')` (function) — Call ``POST /v1internal:onboardUser`` to provision the user.
- L341 `QuotaBucket` (class)
- L349 `retrieve_user_quota(access_token: str, *, project_id: str='', user_agent_model: str='')` (function) — Call ``POST /v1internal:retrieveUserQuota`` and parse ``buckets[]``.
- L383 `ProjectContext` (class) — Resolved state for a given OAuth session.
- L391 `resolve_project_context(access_token: str, *, configured_project_id: str='', env_project_id: str='', user_agent_model: str='')` (function) — Figure out what project id + tier to use for requests.
