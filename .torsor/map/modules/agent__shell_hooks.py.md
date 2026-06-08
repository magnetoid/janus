---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/shell_hooks.py

Symbols in `agent/shell_hooks.py`.

- L107 `ShellHookSpec` (class) — Parsed and validated representation of a single ``hooks:`` entry.
- L116 `__post_init__(self)` (method)
- L133 `matches_tool(self, tool_name: Optional[str])` (method)
- L149 `register_from_config(cfg: Optional[Dict[str, Any]], *, accept_hooks: bool=False)` (function) — Register every configured shell hook on the plugin manager.
- L224 `iter_configured_hooks(cfg: Optional[Dict[str, Any]])` (function) — Return the parsed ``ShellHookSpec`` entries from config without
- L232 `reset_for_tests()` (function) — Clear the idempotence set.  Test-only helper.
- L242 `_parse_hooks_block(hooks_cfg: Any)` (function) — Normalise the ``hooks:`` dict into a flat list of ``ShellHookSpec``.
- L290 `_parse_single_entry(event: str, index: int, raw: Any)` (function)
- L364 `_spawn(spec: ShellHookSpec, stdin_json: str)` (function) — Run ``spec.command`` as a subprocess with ``stdin_json`` on stdin.
- L422 `_make_callback(spec: ShellHookSpec)` (function) — Build the closure that ``invoke_hook()`` will call per firing.
- L466 `_serialize_payload(event: str, kwargs: Dict[str, Any])` (function) — Render the stdin JSON payload.  Unserialisable values are
- L485 `_block_message(primary: Any, secondary: Any)` (function) — Return a validated string block message, falling back to the default.
- L496 `_parse_response(event: str, stdout: str)` (function) — Translate stdout JSON into a Hermes wire-shape dict.
- L546 `allowlist_path()` (function) — Path to the per-user shell-hook allowlist file.
- L551 `load_allowlist()` (function) — Return the parsed allowlist, or an empty skeleton if absent.
- L565 `save_allowlist(data: Dict[str, Any])` (function) — Atomically persist the allowlist via per-process ``mkstemp`` +
- L597 `_is_allowlisted(event: str, command: str)` (function)
- L608 `_locked_update_approvals()` (function) — Serialise read-modify-write on the allowlist across processes.
- L641 `_prompt_and_record(event: str, command: str, *, accept_hooks: bool)` (function) — Decide whether to approve an unseen ``(event, command)`` pair.
- L679 `_record_approval(event: str, command: str)` (function)
- L697 `_utc_now_iso()` (function)
- L701 `revoke(command: str)` (function) — Remove every allowlist entry matching ``command``.
- L726 `_command_script_path(command: str)` (function) — Return the script path from ``command`` for doctor / drift checks.
- L753 `_resolve_effective_accept(cfg: Dict[str, Any], accept_hooks_arg: bool)` (function) — Combine all three opt-in channels into a single boolean.
- L780 `allowlist_entry_for(event: str, command: str)` (function) — Return the allowlist record for this pair, if any.
- L792 `script_mtime_iso(command: str)` (function) — ISO-8601 mtime of the resolved script path, or ``None`` if the
- L807 `script_is_executable(command: str)` (function) — Return ``True`` iff ``command`` is runnable as configured.
- L830 `run_once(spec: ShellHookSpec, kwargs: Dict[str, Any])` (function) — Fire a single shell-hook invocation with a synthetic payload.
