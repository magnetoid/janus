---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/delegate_tool.py

Symbols in `tools/delegate_tool.py`.

- L73 `_subagent_auto_deny(command: str, description: str, **kwargs)` (function) — Auto-deny dangerous commands in subagent threads (safe default).
- L87 `_subagent_auto_approve(command: str, description: str, **kwargs)` (function) — Auto-approve dangerous commands in subagent threads (opt-in YOLO).
- L100 `_get_subagent_approval_callback()` (function) — Return the callback to install into subagent worker threads.
- L160 `set_spawn_paused(paused: bool)` (function) — Globally block/unblock new delegate_task spawns.
- L172 `is_spawn_paused()` (function)
- L177 `_register_subagent(record: Dict[str, Any])` (function)
- L185 `_unregister_subagent(subagent_id: str)` (function)
- L190 `interrupt_subagent(subagent_id: str)` (function) — Request that a single running subagent stop at its next iteration boundary.
- L213 `list_active_subagents()` (function) — Snapshot of the currently running subagent tree.
- L226 `_extract_output_tail(result: Dict[str, Any], *, max_entries: int=12, max_chars: int=8000)` (function) — Pull the last N tool-call results from a child's conversation.
- L281 `_stringify_tool_content(content: Any)` (function) — Return a stable text representation for tool-result content.
- L309 `_looks_like_error_output(content: Any)` (function) — Conservative stderr/error detector for tool-result previews.
- L345 `_normalize_role(r: Optional[str])` (function) — Normalise a caller-provided role to 'leaf' or 'orchestrator'.
- L362 `_get_max_concurrent_children()` (function) — Read delegation.max_concurrent_children from config, falling back to
- L400 `_get_child_timeout()` (function) — Read delegation.child_timeout_seconds from config.
- L427 `_get_max_spawn_depth()` (function) — Read delegation.max_spawn_depth from config, floored at 1 (no ceiling).
- L466 `_get_orchestrator_enabled()` (function) — Global kill switch for the orchestrator role.
- L483 `_get_inherit_mcp_toolsets()` (function) — Whether narrowed child toolsets should keep the parent's MCP toolsets.
- L489 `_is_mcp_toolset_name(name: str)` (function) — Return True for canonical MCP toolsets and their registered aliases.
- L504 `_expand_parent_toolsets(parent_toolsets: set)` (function) — Expand composite toolsets so individual toolset names are recognized.
- L535 `_preserve_parent_mcp_toolsets(child_toolsets: List[str], parent_toolsets: set[str])` (function) — Append any parent MCP toolsets that are missing from a narrowed child.
- L566 `DelegateEvent` (class) — Formal event types emitted during delegation progress.
- L598 `check_delegate_requirements()` (function) — Delegation has no external requirements -- always available.
- L603 `_build_child_system_prompt(goal: str, context: Optional[str]=None, *, workspace_path: Optional[str]=None, role: str='leaf', max_spawn_depth: int=2, child_depth: int=1)` (function) — Build a focused system prompt for a child agent.
- L679 `_resolve_workspace_hint(parent_agent)` (function) — Best-effort local workspace hint for child prompts.
- L706 `_strip_blocked_tools(toolsets: List[str])` (function) — Remove toolsets that contain only blocked tools.
- L717 `_build_child_progress_callback(task_index: int, goal: str, parent_agent, task_count: int=1, *, subagent_id: Optional[str]=None, parent_id: Optional[str]=None, depth: Optional[int]=None, model: Optional[str]=None, toolsets: Optional[List[str]]=None)` (function) — Build a callback that relays child agent tool calls to the parent display.
- L904 `_build_child_agent(task_index: int, goal: str, context: Optional[str], toolsets: Optional[List[str]], model: Optional[str], max_iterations: int, task_count: int, parent_agent, override_provider: Optional[str]=None, override_base_url: Optional[str]=None, override_api_key: Optional[str]=None, override_api_mode: Optional[str]=None, override_acp_command: Optional[str]=None, override_acp_args: Optional[List[str]]=None, role: str='leaf')` (function) — Build a child AIAgent on the main thread (thread-safe construction).
- L1227 `_dump_subagent_timeout_diagnostic(*, child: Any, task_index: int, timeout_seconds: float, duration_seconds: float, worker_thread: Optional[threading.Thread], goal: str)` (function) — Write a structured diagnostic dump for a subagent that timed out
- L1371 `_run_single_child(task_index: int, goal: str, child=None, parent_agent=None, **_kwargs)` (function) — Run a pre-built child agent. Called from within a thread.
- L1945 `_recover_tasks_from_json_string(tasks: Any)` (function)
- L1968 `delegate_task(goal: Optional[str]=None, context: Optional[str]=None, toolsets: Optional[List[str]]=None, tasks: Optional[List[Dict[str, Any]]]=None, max_iterations: Optional[int]=None, acp_command: Optional[str]=None, acp_args: Optional[List[str]]=None, role: Optional[str]=None, parent_agent=None)` (function) — Spawn one or more child agents to handle delegated tasks.
- L2371 `_resolve_child_credential_pool(effective_provider: Optional[str], parent_agent)` (function) — Resolve a credential pool for the child agent.
- L2404 `_resolve_delegation_credentials(cfg: dict, parent_agent)` (function) — Resolve credentials for subagent delegation.
- L2518 `_load_config()` (function) — Load delegation config from CLI_CONFIG or persistent config.
- L2548 `_build_top_level_description()` (function) — Compose the delegate_task tool description with current runtime limits.
- L2646 `_build_tasks_param_description()` (function) — Compose the 'tasks' parameter description with current concurrency limit.
- L2660 `_build_role_param_description()` (function) — Compose the 'role' parameter description with current spawn-depth limit.
- L2697 `_build_dynamic_schema_overrides()` (function) — Return per-call schema overrides reflecting current config.
