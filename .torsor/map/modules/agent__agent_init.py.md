---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/agent_init.py

Symbols in `agent/agent_init.py`.

- L62 `_ra()` (function) — Lazy reference to ``run_agent`` so callers can patch
- L71 `_build_codex_gpt55_autoraise_notice(autoraise: Dict[str, float])` (function) — Build the one-time notice shown when Codex gpt-5.5 raises compaction.
- L89 `_normalized_custom_base_url(value: Any)` (function)
- L95 `_custom_provider_model_matches(agent_model: str, entry: Dict[str, Any])` (function)
- L102 `_custom_provider_extra_body_for_agent(*, provider: str, model: str, base_url: str, custom_providers: List[Dict[str, Any]])` (function)
- L135 `_merge_custom_provider_extra_body(agent, custom_providers: List[Dict[str, Any]])` (function)
- L154 `init_agent(agent, base_url: str=None, api_key: str=None, provider: str=None, api_mode: str=None, acp_command: str=None, acp_args: list[str] | None=None, command: str=None, args: list[str] | None=None, model: str='', max_iterations: int=90, tool_delay: float=1.0, enabled_toolsets: List[str]=None, disabled_toolsets: List[str]=None, save_trajectories: bool=False, verbose_logging: bool=False, quiet_mode: bool=False, ephemeral_system_prompt: str=None, log_prefix_chars: int=100, log_prefix: str='', providers_allowed: List[str]=None, providers_ignored: List[str]=None, providers_order: List[str]=None, provider_sort: str=None, provider_require_parameters: bool=False, provider_data_collection: str=None, openrouter_min_coding_score: Optional[float]=None, session_id: str=None, tool_progress_callback: callable=None, tool_start_callback: callable=None, tool_complete_callback: callable=None, thinking_callback: callable=None, reasoning_callback: callable=None, clarify_callback: callable=None, step_callback: callable=None, stream_delta_callback: callable=None, interim_assistant_callback: callable=None, tool_gen_callback: callable=None, status_callback: callable=None, notice_callback: callable=None, notice_clear_callback: callable=None, max_tokens: int=None, reasoning_config: Dict[str, Any]=None, service_tier: str=None, request_overrides: Dict[str, Any]=None, prefill_messages: List[Dict[str, Any]]=None, platform: str=None, user_id: str=None, user_id_alt: str=None, user_name: str=None, chat_id: str=None, chat_name: str=None, chat_type: str=None, thread_id: str=None, gateway_session_key: str=None, skip_context_files: bool=False, load_soul_identity: bool=False, skip_memory: bool=False, session_db=None, parent_session_id: str=None, iteration_budget: 'IterationBudget'=None, fallback_model: Dict[str, Any]=None, credential_pool=None, checkpoints_enabled: bool=False, checkpoint_max_snapshots: int=20, checkpoint_max_total_size_mb: int=500, checkpoint_max_file_size_mb: int=10, pass_session_id: bool=False)` (function) — Initialize the AI Agent.
