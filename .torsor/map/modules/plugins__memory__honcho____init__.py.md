---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/memory/honcho/__init__.py

Symbols in `plugins/memory/honcho/__init__.py`.

- L191 `HonchoMemoryProvider` (class) — Honcho AI-native memory with dialectic Q&A and persistent user modeling.
- L194 `__init__(self)` (method)
- L239 `name(self)` (method)
- L242 `is_available(self)` (method) — Check if Honcho is configured. No network calls.
- L252 `save_config(self, values, hermes_home)` (method) — Write config to $HERMES_HOME/honcho.json (Honcho SDK native format).
- L268 `get_config_schema(self)` (method)
- L274 `post_setup(self, hermes_home: str, config: dict)` (method) — Run the full Honcho setup wizard after provider selection.
- L280 `initialize(self, session_id: str, **kwargs)` (method) — Initialize Honcho session manager.
- L357 `_resolve_session_key(self, cfg, session_id: str, **kwargs)` (method) — Resolve the Honcho session key without touching the network.
- L371 `_start_session_init_background(self, *, wait_timeout: float=0.0)` (method) — Start Honcho session initialization in a daemon thread.
- L417 `_do_session_init(self, cfg, session_id: str, **kwargs)` (method) — Shared session initialization logic for both eager and lazy paths.
- L504 `_ensure_session(self)` (method) — Lazily initialize the Honcho session (for tools-only mode).
- L534 `_session_ready(self)` (method) — Return whether a manager/session key can be used safely.
- L549 `_format_first_turn_context(self, ctx: dict)` (method) — Format the prefetch context dict into a readable system prompt block.
- L578 `system_prompt_block(self)` (method) — Return system prompt text, adapted by recall_mode.
- L622 `prefetch(self, query: str, *, session_id: str='')` (method) — Return base context (representation + card) plus dialectic supplement.
- L767 `_truncate_to_budget(self, text: str)` (method) — Truncate text to fit within context_tokens budget if set.
- L781 `queue_prefetch(self, query: str, *, session_id: str='')` (method) — Fire background prefetch threads for the upcoming turn.
- L891 `_thread_is_live(self)` (method) — Thread-alive guard that treats threads older than the stale
- L906 `_effective_cadence(self)` (method) — Cadence plus empty-streak backoff, capped at _BACKOFF_MAX × base.
- L914 `liveness_snapshot(self)` (method) — In-process snapshot of dialectic liveness state for diagnostics.
- L933 `_apply_reasoning_heuristic(self, base: str, query: str)` (method) — Scale `base` up by query length, clamped at reasoning_level_cap.
- L953 `_resolve_pass_level(self, pass_idx: int, query: str='')` (method) — Resolve reasoning level for a given pass index.
- L971 `_build_dialectic_prompt(self, pass_idx: int, prior_results: list[str], is_cold: bool)` (method) — Build the prompt for a given dialectic pass.
- L1011 `_signal_sufficient(result: str)` (method) — Check if a dialectic pass returned enough signal to skip further passes.
- L1030 `_run_dialectic_depth(self, query: str)` (method) — Execute up to dialecticDepth .chat() calls with conditional bail-out.
- L1082 `_is_trivial_prompt(cls, text: str)` (method) — Return True if the prompt is too trivial to warrant context injection.
- L1095 `on_turn_start(self, turn_number: int, message: str, **kwargs)` (method) — Track turn count for cadence and injection_frequency logic.
- L1100 `_chunk_message(content: str, limit: int)` (method) — Split content into chunks that fit within the Honcho message limit.
- L1144 `_empty_profile_hint(self, peer: str)` (method) — Build a diagnostic hint when honcho_profile returns an empty card.
- L1201 `sync_turn(self, user_content: str, assistant_content: str, *, session_id: str='')` (method) — Record the conversation turn in Honcho (non-blocking).
- L1237 `on_memory_write(self, action: str, target: str, content: str, metadata: Optional[Dict[str, Any]]=None)` (method) — Mirror built-in user profile writes as Honcho conclusions.
- L1270 `on_session_end(self, messages: List[Dict[str, Any]])` (method) — Flush all pending messages to Honcho on session end.
- L1286 `get_tool_schemas(self)` (method) — Return tool schemas, respecting recall_mode.
- L1297 `handle_tool_call(self, tool_name: str, args: dict, **kwargs)` (method) — Handle a Honcho tool call, with lazy session init for tools-only mode.
- L1401 `shutdown(self)` (method)
- L1417 `register(ctx)` (function) — Register Honcho as a memory provider plugin.
