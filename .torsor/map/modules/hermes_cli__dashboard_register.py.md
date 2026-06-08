---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/dashboard_register.py

Symbols in `hermes_cli/dashboard_register.py`.

- L60 `_generate_dashboard_name()` (function) — Return a human-readable ``adjective_noun`` name (Docker-style).
- L65 `_resolve_portal_base_url(override: Optional[str]=None)` (function) — Resolve the portal base URL for the registration request.
- L93 `_register_self_hosted_client(*, access_token: str, portal_base_url: str, name: str, custom_redirect_uri: Optional[str], timeout: float=15.0)` (function) — POST to the portal's self-hosted-client endpoint and return the JSON body.
- L162 `_print_post_register_hint(*, client_id: str, portal_base_url: str, custom_redirect_uri: Optional[str], wrote_portal_url: bool)` (function) — Print the success summary + the gate-engagement caveat.
- L209 `cmd_dashboard_register(args)` (function) — Register a self-hosted dashboard OAuth client with Nous Portal.
