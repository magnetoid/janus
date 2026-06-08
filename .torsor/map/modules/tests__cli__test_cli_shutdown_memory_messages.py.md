---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_shutdown_memory_messages.py

Symbols in `tests/cli/test_cli_shutdown_memory_messages.py`.

- L23 `test_cleanup_forwards_session_messages(mock_invoke_hook)` (function) — _run_cleanup forwards a populated ``_session_messages`` list.
- L48 `test_cleanup_empty_list_still_forwarded(mock_invoke_hook)` (function) — An agent that initialised but ran no turns has an empty list.
- L70 `test_cleanup_non_list_attribute_falls_back_to_no_arg(mock_invoke_hook)` (function) — A MagicMock agent auto-synthesises ``_session_messages`` as a
- L94 `test_cleanup_provider_exception_is_swallowed(mock_invoke_hook)` (function) — A raising ``shutdown_memory_provider`` must not crash CLI exit.
