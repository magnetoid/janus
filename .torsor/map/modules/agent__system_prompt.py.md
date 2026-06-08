---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/system_prompt.py

Symbols in `agent/system_prompt.py`.

- L47 `_ra()` (function) — Lazy reference to the ``run_agent`` module.
- L62 `build_system_prompt_parts(agent: Any, system_message: Optional[str]=None)` (function) — Assemble the system prompt as three ordered parts.
- L353 `build_system_prompt(agent: Any, system_message: Optional[str]=None)` (function) — Assemble the full system prompt from all layers.
- L372 `invalidate_system_prompt(agent: Any)` (function) — Invalidate the cached system prompt, forcing a rebuild on the next turn.
- L383 `format_tools_for_system_message(agent: Any)` (function) — Format tool definitions for the system message in the trajectory format.
