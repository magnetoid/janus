---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/runtime_footer.py

Symbols in `gateway/runtime_footer.py`.

- L35 `_home_relative_cwd(cwd: str)` (function) — Return *cwd* with ``$HOME`` collapsed to ``~``.  Empty string if unset.
- L49 `_model_short(model: Optional[str])` (function) — Drop ``vendor/`` prefix for readability (``openai/gpt-5.4`` → ``gpt-5.4``).
- L56 `resolve_footer_config(user_config: dict[str, Any] | None, platform_key: str | None=None)` (function) — Resolve effective runtime-footer config for *platform_key*.
- L91 `format_runtime_footer(*, model: Optional[str], context_tokens: int, context_length: Optional[int], cwd: Optional[str]=None, fields: Iterable[str]=_DEFAULT_FIELDS)` (function) — Render the footer line, or return "" if no fields have data.
- L125 `build_footer_line(*, user_config: dict[str, Any] | None, platform_key: str | None, model: Optional[str], context_tokens: int, context_length: Optional[int], cwd: Optional[str]=None)` (function) — Top-level entry point used by gateway/run.py.
