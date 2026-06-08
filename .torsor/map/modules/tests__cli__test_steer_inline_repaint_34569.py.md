---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_steer_inline_repaint_34569.py

Symbols in `tests/cli/test_steer_inline_repaint_34569.py`.

- L28 `_load_handle_enter_node()` (function) — Extract the ``handle_enter`` nested function node from cli.py.
- L42 `_is_buffer_reset(node: ast.stmt)` (function) — True if the statement is ``...current_buffer.reset(...)``.
- L53 `_is_invalidate(node: ast.stmt)` (function) — True if the statement is ``event.app.invalidate()``.
- L64 `_collect_reset_blocks(func: ast.FunctionDef)` (function) — Find every statement sequence (a block body/orelse/finalbody) within
- L78 `test_inline_command_reset_branches_invalidate()` (function) — Every handle_enter branch that resets the buffer and then returns must
