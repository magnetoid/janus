---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/memory_tool.py

Symbols in `tools/memory_tool.py`.

- L55 `get_memory_dir()` (function) — Return the profile-scoped memories directory.
- L78 `_scan_memory_content(content: str)` (function) — Scan memory content for injection/exfil patterns. Returns error string if blocked.
- L83 `_drift_error(path: 'Path', bak_path: str)` (function) — Build the error dict returned when external drift is detected.
- L113 `MemoryStore` (class) — Bounded curated memory with file persistence. One instance per AIAgent.
- L124 `__init__(self, memory_char_limit: int=2200, user_char_limit: int=1375)` (method)
- L132 `load_from_disk(self)` (method) — Load entries from MEMORY.md and USER.md, capture system prompt snapshot.
- L173 `_sanitize_entries_for_snapshot(entries: List[str], filename: str)` (method) — Return ``entries`` with any threat-matching entry replaced by a placeholder.
- L210 `_file_lock(path: Path)` (method) — Acquire an exclusive file lock for read-modify-write safety.
- L246 `_path_for(target: str)` (method)
- L252 `_reload_target(self, target: str)` (method) — Re-read entries from disk into in-memory state.
- L270 `save_to_disk(self, target: str)` (method) — Persist entries to the appropriate file. Called after every mutation.
- L275 `_entries_for(self, target: str)` (method)
- L280 `_set_entries(self, target: str, entries: List[str])` (method)
- L286 `_char_count(self, target: str)` (method)
- L292 `_char_limit(self, target: str)` (method)
- L297 `add(self, target: str, content: str)` (method) — Append a new entry. Returns error if it would exceed the char limit.
- L347 `replace(self, target: str, old_text: str, new_content: str)` (method) — Find entry containing old_text substring, replace it with new_content.
- L407 `remove(self, target: str, old_text: str)` (method) — Remove the entry containing old_text substring.
- L443 `format_for_system_prompt(self, target: str)` (method) — Return the frozen snapshot for system prompt injection.
- L458 `_success_response(self, target: str, message: str=None)` (method)
- L475 `_render_block(self, target: str, entries: List[str])` (method) — Render a system prompt block with header and usage indicator.
- L494 `_read_file(path: Path)` (method) — Read a memory file and split into entries.
- L515 `_detect_external_drift(self, target: str)` (method) — Return a backup-path string if on-disk content shows external drift.
- L571 `_write_file(path: Path, entries: List[str])` (method) — Write entries to a memory file using atomic temp-file + rename.
- L602 `memory_tool(action: str, target: str='memory', content: str=None, old_text: str=None, store: Optional[MemoryStore]=None)` (function) — Single entry point for the memory tool. Dispatches to MemoryStore methods.
- L643 `check_memory_requirements()` (function) — Memory tool has no external requirements -- always available.
