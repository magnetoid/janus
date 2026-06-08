---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/model-providers/qwen-oauth/__init__.py

Symbols in `plugins/model-providers/qwen-oauth/__init__.py`.

- L10 `QwenProfile` (class) — Qwen Portal — message normalization, vl_high_resolution, metadata top-level.
- L13 `prepare_messages(self, messages: list[dict[str, Any]])` (method) — Normalize content to list-of-dicts format.
- L54 `build_extra_body(self, *, session_id: str | None=None, **context)` (method)
- L59 `build_api_kwargs_extras(self, *, reasoning_config: dict | None=None, qwen_session_metadata: dict | None=None, **context)` (method) — Qwen metadata goes to top-level api_kwargs, not extra_body.
