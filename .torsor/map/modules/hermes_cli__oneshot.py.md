---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/oneshot.py

Symbols in `hermes_cli/oneshot.py`.

- L33 `_normalize_toolsets(toolsets: object=None)` (function)
- L51 `_validate_explicit_toolsets(toolsets: object=None)` (function)
- L125 `run_oneshot(prompt: str, model: Optional[str]=None, provider: Optional[str]=None, toolsets: object=None)` (function) — Execute a single prompt and print only the final content block.
- L229 `_create_session_db_for_oneshot()` (function) — Best-effort SessionDB for ``hermes -z`` / oneshot mode.
- L245 `_run_agent(prompt: str, model: Optional[str]=None, provider: Optional[str]=None, toolsets: object=None, use_config_toolsets: bool=True)` (function) — Build an AIAgent exactly like a normal CLI chat turn would, then
- L370 `_oneshot_clarify_callback(question: str, choices=None)` (function) — Clarify is disabled in oneshot mode — tell the agent to pick a
