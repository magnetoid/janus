---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/approval.py

Symbols in `tools/approval.py`.

- L49 `_fire_approval_hook(hook_name: str, **kwargs)` (function) — Invoke a plugin lifecycle hook for the approval system.
- L77 `set_current_session_key(session_key: str)` (function) — Bind the active approval session key to the current context.
- L82 `reset_current_session_key(token: contextvars.Token[str])` (function) — Restore the prior approval session key context.
- L87 `set_current_observability_context(*, turn_id: str='', tool_call_id: str='')` (function) — Bind active tool correlation IDs to approval hooks.
- L99 `reset_current_observability_context(tokens: tuple[contextvars.Token[str], contextvars.Token[str]])` (function) — Restore prior approval hook correlation IDs.
- L108 `get_current_session_key(default: str='default')` (function) — Return the active session key, preferring context-local state.
- L123 `_get_session_platform()` (function) — Return the current gateway platform from contextvars/env fallback.
- L133 `_is_gateway_approval_context()` (function) — True when this call is inside a gateway/API session.
- L301 `_check_sudo_stdin_guard(command: str)` (function) — Detect ``sudo -S`` (stdin password) without configured SUDO_PASSWORD.
- L320 `detect_hardline_command(command: str)` (function) — Check if a command matches the unconditional hardline blocklist.
- L333 `_hardline_block_result(description: str)` (function) — Build the standard block result for a hardline match.
- L349 `_sudo_stdin_block_result(description: str)` (function) — Build the standard block result for sudo stdin guard.
- L498 `_legacy_pattern_key(pattern: str)` (function) — Reproduce the old regex-derived approval key for backwards compatibility.
- L511 `_approval_key_aliases(pattern_key: str)` (function) — Return all approval keys that should match this pattern.
- L525 `_normalize_command_for_detection(command: str)` (function) — Normalize a command string before dangerous-pattern matching.
- L547 `detect_dangerous_command(command: str)` (function) — Check if a command matches any dangerous patterns.
- L580 `_ApprovalEntry` (class) — One pending dangerous-command approval inside a gateway session.
- L584 `__init__(self, data: dict)` (method)
- L594 `register_gateway_notify(session_key: str, cb)` (function) — Register a per-session callback for sending approval requests to the user.
- L606 `unregister_gateway_notify(session_key: str)` (function) — Unregister the per-session gateway approval callback.
- L619 `resolve_gateway_approval(session_key: str, choice: str, resolve_all: bool=False)` (function) — Called by the gateway's /approve or /deny handler to unblock
- L648 `has_blocking_approval(session_key: str)` (function) — Check if a session has one or more blocking gateway approvals waiting.
- L654 `submit_pending(session_key: str, approval: dict)` (function) — Store a pending approval request for a session.
- L660 `approve_session(session_key: str, pattern_key: str)` (function) — Approve a pattern for this session only.
- L666 `enable_session_yolo(session_key: str)` (function) — Enable YOLO bypass for a single session key.
- L674 `disable_session_yolo(session_key: str)` (function) — Disable YOLO bypass for a single session key.
- L682 `clear_session(session_key: str)` (function) — Remove all approval and yolo state for a given session.
- L698 `is_session_yolo_enabled(session_key: str)` (function) — Return True when YOLO bypass is enabled for a specific session.
- L706 `is_current_session_yolo_enabled()` (function) — Return True when the active approval session has YOLO bypass enabled.
- L711 `is_approved(session_key: str, pattern_key: str)` (function) — Check if a pattern is approved (session-scoped or permanent).
- L725 `approve_permanent(pattern_key: str)` (function) — Add a pattern to the permanent allowlist.
- L731 `load_permanent(patterns: set)` (function) — Bulk-load permanent allowlist entries from config.
- L742 `load_permanent_allowlist()` (function) — Load permanently allowed command patterns from config.
- L760 `save_permanent_allowlist(patterns: set)` (function) — Save permanently allowed command patterns to config.
- L775 `prompt_dangerous_approval(command: str, description: str, timeout_seconds: int | None=None, allow_permanent: bool=True, approval_callback=None)` (function) — Prompt the user to approve a dangerous command (CLI only).
- L890 `_normalize_approval_mode(mode)` (function) — Normalize approval mode values loaded from YAML/config.
- L905 `_get_approval_config()` (function) — Read the approvals config block. Returns a dict with 'mode', 'timeout', etc.
- L916 `_get_approval_mode()` (function) — Read the approval mode from config. Returns 'manual', 'smart', or 'off'.
- L922 `_get_approval_timeout()` (function) — Read the approval timeout from config. Defaults to 60 seconds.
- L930 `_get_cron_approval_mode()` (function) — Read the cron approval mode from config. Returns 'deny' or 'approve'.
- L943 `_smart_approve(command: str, description: str)` (function) — Use the auxiliary LLM to assess risk and decide approval.
- L990 `check_dangerous_command(command: str, env_type: str, approval_callback=None)` (function) — Check if a command is dangerous and handle approval.
- L1098 `_format_tirith_description(tirith_result: dict)` (function) — Build a human-readable description from tirith findings.
- L1125 `_await_gateway_decision(session_key: str, notify_cb, approval_data: dict, *, surface: str='gateway')` (function) — Enqueue *approval_data*, notify the user, and block the calling agent
- L1226 `check_all_command_guards(command: str, env_type: str, approval_callback=None)` (function) — Run all pre-exec security checks and return a single approval decision.
- L1520 `check_execute_code_guard(code: str, env_type: str)` (function) — Approve an execute_code script before its child process is spawned.
