---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/todo_tool.py

Symbols in `tools/todo_tool.py`.

- L25 `TodoStore` (class) — In-memory todo list. One instance per AIAgent (one per session).
- L35 `__init__(self)` (method)
- L38 `write(self, todos: List[Dict[str, Any]], merge: bool=False)` (method) — Write todos. Returns the full current list after writing.
- L82 `read(self)` (method) — Return a copy of the current list.
- L86 `has_items(self)` (method) — Check if there are any items in the list.
- L90 `format_for_injection(self)` (method) — Render the todo list for post-compression injection.
- L125 `_validate(item: Dict[str, Any])` (method) — Validate and normalize a todo item.
- L147 `_dedupe_by_id(todos: List[Dict[str, Any]])` (method) — Collapse duplicate ids, keeping the last occurrence in its position.
- L156 `todo_tool(todos: Optional[List[Dict[str, Any]]]=None, merge: bool=False, store: Optional[TodoStore]=None)` (function) — Single entry point for the todo tool. Reads or writes depending on params.
- L198 `check_todo_requirements()` (function) — Todo tool has no external requirements -- always available.
