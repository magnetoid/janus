---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/subdirectory_hints.py

Symbols in `agent/subdirectory_hints.py`.

- L49 `_is_ancestor_or_same(a: Path, b: Path)` (function) — Check if *a* is the same as or an ancestor of *b* (parent directory check).
- L57 `SubdirectoryHintTracker` (class) — Track which directories the agent visits and load hints on first access.
- L70 `__init__(self, working_dir: Optional[str]=None)` (method)
- L76 `check_tool_call(self, tool_name: str, tool_args: Dict[str, Any])` (method) — Check tool call arguments for new directories and load any hint files.
- L100 `_extract_directories(self, tool_name: str, args: Dict[str, Any])` (method) — Extract directory paths from tool call arguments.
- L120 `_add_path_candidate(self, raw_path: str, candidates: Set[Path])` (method) — Resolve a raw path and add its directory + ancestors to candidates.
- L150 `_extract_paths_from_command(self, cmd: str, candidates: Set[Path])` (method) — Extract path-like tokens from a shell command string.
- L169 `_is_valid_subdir(self, path: Path)` (method) — Check if path is a valid directory to scan for hints.
- L198 `_load_hints_for_directory(self, directory: Path)` (method) — Load hint files from a directory. Returns formatted text or None.
