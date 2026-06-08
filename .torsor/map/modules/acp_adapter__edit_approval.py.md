---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# acp_adapter/edit_approval.py

Symbols in `acp_adapter/edit_approval.py`.

- L25 `EditProposal` (class) — A proposed single-file edit that can be shown to an ACP client.
- L50 `set_edit_approval_requester(requester: EditApprovalRequester | None)` (function) — Bind an ACP edit approval requester for the current context.
- L56 `reset_edit_approval_requester(token: Token)` (function) — Restore a previous edit approval requester binding.
- L62 `clear_edit_approval_requester()` (function) — Clear the current requester; primarily used by tests.
- L68 `get_edit_approval_requester()` (function)
- L72 `_read_text_if_exists(path: str)` (function)
- L81 `_proposal_for_write_file(arguments: dict[str, Any])` (function)
- L97 `_proposal_for_patch_replace(arguments: dict[str, Any])` (function)
- L130 `build_edit_proposal(tool_name: str, arguments: dict[str, Any])` (function) — Return an edit proposal for supported file mutation calls.
- L140 `_is_sensitive_auto_approve_path(path: str)` (function)
- L148 `should_auto_approve_edit(proposal: EditProposal, policy: str, cwd: str | None=None)` (function) — Return whether an ACP edit proposal may bypass the prompt for this session.
- L181 `maybe_require_edit_approval(tool_name: str, arguments: dict[str, Any])` (function) — Run ACP edit approval if bound.
- L212 `build_acp_edit_tool_call(proposal: EditProposal)` (function) — Build the ToolCallUpdate payload for ACP request_permission.
- L234 `make_acp_edit_approval_requester(request_permission_fn: Callable, loop: asyncio.AbstractEventLoop, session_id: str, timeout: float=60.0, auto_approve_getter: Callable[[], tuple[str, str | None]] | None=None)` (function) — Return a sync requester that bridges edit proposals to ACP permissions.
