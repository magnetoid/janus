---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/bedrock_adapter.py

Symbols in `agent/bedrock_adapter.py`.

- L61 `_require_boto3()` (function) — Import boto3, raising a clear error if not installed.
- L74 `_get_bedrock_runtime_client(region: str)` (function) — Get or create a cached ``bedrock-runtime`` client for the given region.
- L87 `_get_bedrock_control_client(region: str)` (function) — Get or create a cached ``bedrock`` control-plane client for model discovery.
- L97 `reset_client_cache()` (function) — Clear cached boto3 clients. Used in tests and profile switches.
- L103 `invalidate_runtime_client(region: str)` (function) — Evict the cached ``bedrock-runtime`` client for a single region.
- L145 `_traceback_frames_modules(exc: BaseException)` (function) — Yield ``__name__``-style module strings for each frame in exc's traceback.
- L155 `is_stale_connection_error(exc: BaseException)` (function) — Return True if ``exc`` indicates a dead/stale Bedrock HTTP connection.
- L231 `resolve_aws_auth_env_var(env: Optional[Dict[str, str]]=None)` (function) — Return the name of the AWS auth source that is active, or None.
- L273 `has_aws_credentials(env: Optional[Dict[str, str]]=None)` (function) — Return True if any AWS credential source is detected.
- L304 `resolve_bedrock_region(env: Optional[Dict[str, str]]=None)` (function) — Resolve the AWS region for Bedrock API calls.
- L335 `bedrock_model_ids_or_none()` (function) — Live-discover Bedrock model IDs for the active region.
- L374 `_model_supports_tool_use(model_id: str)` (function) — Return True if the model is expected to support tool/function calling.
- L384 `is_anthropic_bedrock_model(model_id: str)` (function) — Return True if the model is an Anthropic Claude model on Bedrock.
- L410 `convert_tools_to_converse(tools: List[Dict])` (function) — Convert OpenAI-format tool definitions to Bedrock Converse ``toolConfig``.
- L441 `_convert_content_to_converse(content)` (function) — Convert OpenAI message content (string or list) to Converse content blocks.
- L493 `convert_messages_to_converse(messages: List[Dict])` (function) — Convert OpenAI-format messages to Bedrock Converse format.
- L616 `_converse_stop_reason_to_openai(stop_reason: str)` (function) — Map Bedrock Converse stop reasons to OpenAI finish_reason values.
- L629 `normalize_converse_response(response: Dict)` (function) — Convert a Bedrock Converse API response to an OpenAI-compatible object.
- L709 `normalize_converse_stream_events(event_stream)` (function) — Consume a Bedrock ConverseStream event stream and build an OpenAI-compatible response.
- L725 `stream_converse_with_callbacks(event_stream, on_text_delta=None, on_tool_start=None, on_reasoning_delta=None, on_interrupt_check=None)` (function) — Process a Bedrock ConverseStream event stream with real-time callbacks.
- L876 `build_converse_kwargs(model: str, messages: List[Dict], tools: Optional[List[Dict]]=None, max_tokens: int=4096, temperature: Optional[float]=None, top_p: Optional[float]=None, stop_sequences: Optional[List[str]]=None, guardrail_config: Optional[Dict]=None)` (function) — Build kwargs for ``bedrock-runtime.converse()`` or ``converse_stream()``.
- L934 `call_converse(region: str, model: str, messages: List[Dict], tools: Optional[List[Dict]]=None, max_tokens: int=4096, temperature: Optional[float]=None, top_p: Optional[float]=None, stop_sequences: Optional[List[str]]=None, guardrail_config: Optional[Dict]=None)` (function) — Call Bedrock Converse API (non-streaming) and return an OpenAI-compatible response.
- L975 `call_converse_stream(region: str, model: str, messages: List[Dict], tools: Optional[List[Dict]]=None, max_tokens: int=4096, temperature: Optional[float]=None, top_p: Optional[float]=None, stop_sequences: Optional[List[str]]=None, guardrail_config: Optional[Dict]=None)` (function) — Call Bedrock ConverseStream API and return an OpenAI-compatible response.
- L1025 `reset_discovery_cache()` (function) — Clear the model discovery cache. Used in tests.
- L1030 `discover_bedrock_models(region: str, provider_filter: Optional[List[str]]=None)` (function) — Discover available Bedrock foundation models and inference profiles.
- L1162 `_extract_provider_from_arn(arn: str)` (function) — Extract the model provider from a Bedrock model ARN.
- L1199 `is_context_overflow_error(error_message: str)` (function) — Return True if the error indicates the input context was too large.
- L1208 `classify_bedrock_error(error_message: str)` (function) — Classify a Bedrock error for retry/failover decisions.
- L1264 `get_bedrock_context_length(model_id: str)` (function) — Look up the context window size for a Bedrock model.
