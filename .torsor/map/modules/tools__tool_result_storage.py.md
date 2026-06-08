---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/tool_result_storage.py

Symbols in `tools/tool_result_storage.py`.

- L44 `_resolve_storage_dir(env)` (function) — Return the best temp-backed storage dir for this environment.
- L60 `generate_preview(content: str, max_chars: int=DEFAULT_PREVIEW_SIZE_CHARS)` (function) — Truncate at last newline within max_chars. Returns (preview, has_more).
- L71 `_heredoc_marker(content: str)` (function) — Return a heredoc delimiter that doesn't collide with content.
- L78 `_write_to_sandbox(content: str, remote_path: str, env)` (function) — Write content into the sandbox via env.execute(). Returns True on success.
- L97 `_build_persisted_message(preview: str, has_more: bool, original_size: int, file_path: str)` (function) — Build the <persisted-output> replacement block.
- L122 `maybe_persist_tool_result(content: str, tool_name: str, tool_use_id: str, env=None, config: BudgetConfig=DEFAULT_BUDGET, threshold: int | float | None=None)` (function) — Layer 2: persist oversized result into the sandbox, return preview + path.
- L181 `enforce_turn_budget(tool_messages: list[dict], env=None, config: BudgetConfig=DEFAULT_BUDGET)` (function) — Layer 3: enforce aggregate budget across all tool results in a turn.
