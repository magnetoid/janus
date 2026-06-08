---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/api_server.py

Symbols in `gateway/platforms/api_server.py`.

- L74 `_coerce_port(value: Any, default: int=DEFAULT_PORT)` (function) — Parse a listen port without letting malformed env/config values crash startup.
- L86 `_coerce_request_bool(value: Any, default: bool=False)` (function) — Normalize boolean-like API payload values.
- L111 `_normalize_chat_content(content: Any, *, _max_depth: int=10, _depth: int=0)` (function) — Normalize OpenAI chat message content into a plain text string.
- L178 `_normalize_multimodal_content(content: Any)` (function) — Validate and normalize multimodal content for the API server.
- L296 `_content_has_visible_payload(content: Any)` (function) — True when content has any text or image attachment.  Used to reject empty turns.
- L311 `_multimodal_validation_error(exc: ValueError, *, param: str)` (function) — Translate a ``_normalize_multimodal_content`` ValueError into a 400 response.
- L323 `_session_chat_user_message(body: Dict[str, Any], *, param: str='message')` (function) — Parse and normalize session chat ``message`` / ``input`` like chat completions.
- L337 `check_api_server_requirements()` (function) — Check if API server dependencies are available.
- L342 `ResponseStore` (class) — SQLite-backed LRU store for Responses API state.
- L354 `__init__(self, max_size: int=MAX_STORED_RESPONSES, db_path: str=None)` (method)
- L395 `_tighten_file_permissions(self)` (method) — Force owner-only permissions on the DB and SQLite sidecars.
- L414 `get(self, response_id: str)` (method) — Retrieve a stored response by ID (updates access time for LRU).
- L440 `put(self, response_id: str, data: Dict[str, Any])` (method) — Store a response, evicting the oldest if at capacity.
- L471 `delete(self, response_id: str)` (method) — Remove a response from the store. Returns True if found and deleted.
- L483 `get_conversation(self, name: str)` (method) — Get the latest response_id for a conversation name.
- L490 `set_conversation(self, name: str, response_id: str)` (method) — Map a conversation name to its latest response_id.
- L498 `close(self)` (method) — Close the database connection.
- L505 `__len__(self)` (method)
- L545 `_openai_error(message: str, err_type: str='invalid_request_error', param: str=None, code: str=None)` (function) — OpenAI-style error envelope.
- L596 `_IdempotencyCache` (class) — In-memory idempotency cache with TTL and basic LRU semantics.
- L598 `__init__(self, max_items: int=1000, ttl_seconds: int=300)` (method)
- L605 `_purge(self)` (method)
- L613 `get_or_set(self, key: str, fingerprint: str, compute_coro)` (method)
- L644 `_make_request_fingerprint(body: Dict[str, Any], keys: List[str])` (function)
- L650 `_derive_chat_session_id(system_prompt: Optional[str], first_user_message: str)` (function) — Derive a stable session ID from the conversation's first user message.
- L705 `APIServerAdapter` (class) — OpenAI-compatible HTTP API server adapter.
- L713 `__init__(self, config: PlatformConfig)` (method)
- L748 `_parse_cors_origins(value: Any)` (method) — Normalize configured CORS origins into a stable tuple.
- L763 `_resolve_model_name(explicit: str)` (method) — Derive the advertised model name for /v1/models.
- L782 `_cors_headers_for_origin(self, origin: str)` (method) — Return CORS headers for an allowed browser origin.
- L802 `_origin_allowed(self, origin: str)` (method) — Allow non-browser clients and explicitly configured browser origins.
- L813 `_clean_log_value(value: Any, *, max_len: int=200)` (method) — Sanitize request metadata before it reaches security logs.
- L820 `_request_audit_context(self, request: 'web.Request')` (method) — Return non-secret source metadata for security/audit warnings.
- L840 `_request_audit_log_suffix(self, request: 'web.Request')` (method)
- L845 `_cron_origin_from_request(self, request: 'web.Request')` (method) — Persist safe API source metadata on cron jobs created over HTTP.
- L868 `_check_auth(self, request: 'web.Request')` (method) — Validate Bearer token from Authorization header.
- L907 `_parse_session_key_header(self, request: 'web.Request')` (method) — Extract and validate the ``X-Hermes-Session-Key`` header.
- L963 `_ensure_session_db(self)` (method) — Lazily initialise and return the shared SessionDB instance.
- L981 `_create_agent(self, ephemeral_system_prompt: Optional[str]=None, session_id: Optional[str]=None, stream_delta_callback=None, tool_progress_callback=None, tool_start_callback=None, tool_complete_callback=None, gateway_session_key: Optional[str]=None)` (method) — Create an AIAgent instance using the gateway's runtime config.
- L1048 `_handle_health(self, request: 'web.Request')` (method) — GET /health — simple health check.
- L1052 `_handle_health_detailed(self, request: 'web.Request')` (method) — GET /health/detailed — rich status for cross-container dashboard probing.
- L1073 `_handle_models(self, request: 'web.Request')` (method) — GET /v1/models — return hermes-agent as an available model.
- L1094 `_handle_capabilities(self, request: 'web.Request')` (method) — GET /v1/capabilities — advertise the stable API surface.
- L1174 `_handle_skills(self, request: 'web.Request')` (method) — GET /v1/skills — list installed skills visible to the API-server agent.
- L1205 `_handle_toolsets(self, request: 'web.Request')` (method) — GET /v1/toolsets — list toolsets and their resolved tools.
- L1266 `_parse_nonnegative_int(value: Any, default: int, maximum: int)` (method)
- L1276 `_session_response(session: Dict[str, Any])` (method) — Return a stable, client-safe session representation.
- L1294 `_message_response(message: Dict[str, Any])` (method)
- L1302 `_read_json_body(self, request: 'web.Request')` (method)
- L1311 `_get_existing_session_or_404(self, session_id: str)` (method)
- L1320 `_conversation_history_for_session(self, session_id: str)` (method)
- L1330 `_handle_list_sessions(self, request: 'web.Request')` (method) — GET /api/sessions — list persisted Hermes sessions.
- L1359 `_handle_create_session(self, request: 'web.Request')` (method) — POST /api/sessions — create an empty Hermes session row.
- L1396 `_handle_get_session(self, request: 'web.Request')` (method) — GET /api/sessions/{session_id}.
- L1406 `_handle_patch_session(self, request: 'web.Request')` (method) — PATCH /api/sessions/{session_id} — update client-safe session metadata.
- L1434 `_handle_delete_session(self, request: 'web.Request')` (method) — DELETE /api/sessions/{session_id}.
- L1447 `_handle_session_messages(self, request: 'web.Request')` (method) — GET /api/sessions/{session_id}/messages.
- L1464 `_handle_fork_session(self, request: 'web.Request')` (method) — POST /api/sessions/{session_id}/fork — branch via current SessionDB primitives.
- L1511 `_handle_session_chat(self, request: 'web.Request')` (method) — POST /api/sessions/{session_id}/chat — one synchronous agent turn.
- L1555 `_handle_session_chat_stream(self, request: 'web.Request')` (method) — POST /api/sessions/{session_id}/chat/stream — SSE wrapper over _run_agent.
- L1696 `_handle_chat_completions(self, request: 'web.Request')` (method) — POST /v1/chat/completions — OpenAI Chat Completions format.
- L2017 `_write_sse_chat_completion(self, request: 'web.Request', completion_id: str, model: str, created: int, stream_q, agent_task, agent_ref=None, session_id: str=None, gateway_session_key: str=None)` (method) — Write real streaming SSE from agent's stream_delta_callback queue.
- L2169 `_write_sse_responses(self, request: 'web.Request', response_id: str, model: str, created_at: int, stream_q, agent_task, agent_ref, conversation_history: List[Dict[str, str]], user_message: str, instructions: Optional[str], conversation: Optional[str], store: bool, session_id: str, gateway_session_key: Optional[str]=None)` (method) — Write an SSE stream for POST /v1/responses (OpenAI Responses API).
- L2765 `_handle_responses(self, request: 'web.Request')` (method) — POST /v1/responses — OpenAI Responses API format.
- L3049 `_handle_get_response(self, request: 'web.Request')` (method) — GET /v1/responses/{response_id} — retrieve a stored response.
- L3062 `_handle_delete_response(self, request: 'web.Request')` (method) — DELETE /v1/responses/{response_id} — delete a stored response.
- L3090 `_check_jobs_available()` (method) — Return error response if cron module isn't available.
- L3098 `_check_job_id(self, request: 'web.Request')` (method) — Validate and extract job_id. Returns (job_id, error_response).
- L3112 `_handle_list_jobs(self, request: 'web.Request')` (method) — GET /api/jobs — list all cron jobs.
- L3127 `_handle_create_job(self, request: 'web.Request')` (method) — POST /api/jobs — create a new cron job.
- L3180 `_handle_get_job(self, request: 'web.Request')` (method) — GET /api/jobs/{job_id} — get a single cron job.
- L3199 `_handle_update_job(self, request: 'web.Request')` (method) — PATCH /api/jobs/{job_id} — update a cron job.
- L3236 `_handle_delete_job(self, request: 'web.Request')` (method) — DELETE /api/jobs/{job_id} — delete a cron job.
- L3255 `_handle_pause_job(self, request: 'web.Request')` (method) — POST /api/jobs/{job_id}/pause — pause a cron job.
- L3274 `_handle_resume_job(self, request: 'web.Request')` (method) — POST /api/jobs/{job_id}/resume — resume a paused cron job.
- L3293 `_handle_run_job(self, request: 'web.Request')` (method) — POST /api/jobs/{job_id}/run — trigger immediate execution.
- L3317 `_build_response_conversation_history(conversation_history: List[Dict[str, Any]], user_message: Any, result: Dict[str, Any], final_response: Any)` (method) — Build the stored Responses transcript without duplicating history.
- L3348 `_response_messages_turn_start_index(conversation_history: List[Dict[str, Any]], user_message: Any, result: Dict[str, Any])` (method) — Detect transcript-shaped result["messages"] and return turn start.
- L3368 `_turn_transcript_messages(cls, conversation_history: List[Dict[str, Any]], user_message: Any, result: Dict[str, Any])` (method) — Return this turn's assistant/tool messages in client-safe shape.
- L3406 `_extract_output_items(result: Dict[str, Any], start_index: int=0)` (method) — Build the output item array from the agent's messages.
- L3459 `_run_agent(self, user_message: str, conversation_history: List[Dict[str, str]], ephemeral_system_prompt: Optional[str]=None, session_id: Optional[str]=None, stream_delta_callback=None, tool_progress_callback=None, tool_start_callback=None, tool_complete_callback=None, agent_ref: Optional[list]=None, gateway_session_key: Optional[str]=None)` (method) — Create an agent and run a conversation in a thread executor.
- L3526 `_set_run_status(self, run_id: str, status: str, **fields: Any)` (method) — Update pollable run status without exposing private agent objects.
- L3541 `_make_run_event_callback(self, run_id: str, loop: 'asyncio.AbstractEventLoop')` (method) — Return a tool_progress_callback that pushes structured events to the run's SSE queue.
- L3587 `_handle_runs(self, request: 'web.Request')` (method) — POST /v1/runs — start an agent run, return run_id immediately.
- L3883 `_handle_get_run(self, request: 'web.Request')` (method) — GET /v1/runs/{run_id} — return pollable run status for external UIs.
- L3898 `_handle_run_events(self, request: 'web.Request')` (method) — GET /v1/runs/{run_id}/events — SSE stream of structured agent lifecycle events.
- L3948 `_handle_run_approval(self, request: 'web.Request')` (method) — POST /v1/runs/{run_id}/approval — resolve a pending run approval.
- L4036 `_handle_stop_run(self, request: 'web.Request')` (method) — POST /v1/runs/{run_id}/stop — interrupt a running agent.
- L4076 `_sweep_orphaned_runs(self)` (method) — Periodically clean up run streams that were never consumed.
- L4115 `connect(self)` (method) — Start the aiohttp web server.
- L4230 `disconnect(self)` (method) — Stop the aiohttp web server and release all owned resources.
- L4259 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Not used — HTTP request/response cycle handles delivery directly.
- L4271 `get_chat_info(self, chat_id: str)` (method) — Return basic info about the API server.
