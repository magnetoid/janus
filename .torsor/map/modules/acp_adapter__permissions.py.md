---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# acp_adapter/permissions.py

Symbols in `acp_adapter/permissions.py`.

- L32 `_permission_option_supports_kind(kind: str)` (function) — Return whether the installed ACP SDK accepts a permission option kind.
- L41 `_build_permission_options(*, allow_permanent: bool)` (function) — Return ACP options that match Hermes approval semantics.
- L73 `_build_permission_tool_call(command: str, description: str)` (function) — Return the ACP tool-call update attached to a permission request.
- L95 `_map_outcome_to_hermes(outcome: object, *, allowed_option_ids: set[str])` (function) — Map an ACP permission outcome into Hermes approval strings.
- L107 `make_approval_callback(request_permission_fn: Callable, loop: asyncio.AbstractEventLoop, session_id: str, timeout: float=60.0)` (function) — Return a Hermes-compatible approval callback that bridges to ACP.
