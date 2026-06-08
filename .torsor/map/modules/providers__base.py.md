---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# providers/base.py

Symbols in `providers/base.py`.

- L24 `_profile_user_agent()` (function) — Return a ``hermes-cli/<version>`` UA string, with a stable fallback.
- L39 `ProviderProfile` (class) — Base provider profile — subclass or instantiate with overrides.
- L91 `get_hostname(self)` (method) — Return the provider's base hostname for URL-based detection.
- L104 `prepare_messages(self, messages: list[dict[str, Any]])` (method) — Provider-specific message preprocessing.
- L112 `build_extra_body(self, *, session_id: str | None=None, **context: Any)` (method) — Provider-specific extra_body fields.
- L121 `build_api_kwargs_extras(self, *, reasoning_config: dict | None=None, **context: Any)` (method) — Provider-specific kwargs split between extra_body and top-level api_kwargs.
- L141 `get_max_tokens(self, model: str | None)` (method) — Return the default max_tokens cap for *model*.
- L155 `fetch_models(self, *, api_key: str | None=None, timeout: float=8.0)` (method) — Fetch the live model list from the provider's models endpoint.
