---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/process_bootstrap.py

Symbols in `agent/process_bootstrap.py`.

- L39 `_load_openai_cls()` (function) — Import and cache ``openai.OpenAI``.
- L48 `_OpenAIProxy` (class) — Module-level proxy that looks like ``openai.OpenAI`` but imports lazily.
- L53 `__call__(self, *args, **kwargs)` (method)
- L56 `__instancecheck__(self, obj)` (method)
- L59 `__repr__(self)` (method)
- L63 `_SafeWriter` (class) — Transparent stdio wrapper that catches OSError/ValueError from broken pipes.
- L84 `__init__(self, inner)` (method)
- L87 `write(self, data)` (method)
- L93 `flush(self)` (method)
- L99 `fileno(self)` (method)
- L102 `isatty(self)` (method)
- L108 `__getattr__(self, name)` (method)
- L112 `_get_proxy_from_env()` (function) — Read proxy URL from environment variables.
- L126 `_get_proxy_for_base_url(base_url: Optional[str])` (function) — Return an env-configured proxy unless NO_PROXY excludes this base URL.
- L145 `_install_safe_stdio()` (function) — Wrap stdout/stderr so best-effort console output cannot crash the agent.
