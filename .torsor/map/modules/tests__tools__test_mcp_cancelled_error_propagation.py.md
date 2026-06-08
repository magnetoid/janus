---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_cancelled_error_propagation.py

Symbols in `tests/tools/test_mcp_cancelled_error_propagation.py`.

- L25 `_hanging_run(self, cfg)` (function) — Stand-in transport that hangs forever so we can cancel it.
- L30 `TestCancelledErrorPropagation` (class)
- L31 `test_cancelled_error_is_not_swallowed_by_except_exception(self)` (method) — CancelledError raised inside the transport call must re-raise
- L69 `test_shutdown_completes_promptly_when_task_is_cancelled(self)` (method) — ``shutdown()`` falls through to ``task.cancel()`` + ``await self._task``
