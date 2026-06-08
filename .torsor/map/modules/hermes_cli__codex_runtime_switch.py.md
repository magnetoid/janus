---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/codex_runtime_switch.py

Symbols in `hermes_cli/codex_runtime_switch.py`.

- L27 `CodexRuntimeStatus` (class) — Result of a /codex-runtime invocation. Callers render this however
- L40 `parse_args(arg_string: str)` (function) — Parse the slash-command argument string. Returns (value, errors).
- L62 `get_current_runtime(config: dict)` (function) — Read the current `model.openai_runtime` value from a config dict.
- L76 `set_runtime(config: dict, new_value: str)` (function) — Mutate the config dict in place to persist the new runtime value.
- L90 `check_codex_binary_ok()` (function) — Best-effort verification that codex CLI is installed at acceptable
- L101 `apply(config: dict, new_value: Optional[str], *, persist_callback=None)` (function) — Top-level entry point used by both CLI and gateway handlers.
