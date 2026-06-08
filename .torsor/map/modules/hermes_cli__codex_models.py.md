---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/codex_models.py

Symbols in `hermes_cli/codex_models.py`.

- L58 `_add_forward_compat_models(model_ids: List[str])` (function) — Add Clawdbot-style synthetic forward-compat Codex models.
- L82 `_fetch_models_from_api(access_token: str)` (function) — Fetch available models from the Codex API. Returns visible models sorted by priority.
- L122 `_read_default_model(codex_home: Path)` (function)
- L140 `_read_cache_models(codex_home: Path)` (function)
- L177 `get_codex_model_ids(access_token: Optional[str]=None)` (function) — Return available Codex model IDs, trying API first, then local sources.
