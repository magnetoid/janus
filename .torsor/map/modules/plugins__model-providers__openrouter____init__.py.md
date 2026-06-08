---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/model-providers/openrouter/__init__.py

Symbols in `plugins/model-providers/openrouter/__init__.py`.

- L14 `OpenRouterProfile` (class) — OpenRouter aggregator — provider preferences, reasoning config passthrough.
- L17 `fetch_models(self, *, api_key: str | None=None, timeout: float=8.0)` (method) — Fetch from public OpenRouter catalog — no auth required.
- L42 `build_extra_body(self, *, session_id: str | None=None, **context: Any)` (method)
- L70 `build_api_kwargs_extras(self, *, reasoning_config: dict | None=None, supports_reasoning: bool=False, model: str | None=None, session_id: str | None=None, **context: Any)` (method) — OpenRouter passes the full reasoning_config dict as extra_body.reasoning.
