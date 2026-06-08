---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/anthropic_adapter.py

Symbols in `agent/anthropic_adapter.py`.

- L37 `_get_anthropic_sdk()` (function) — Return the ``anthropic`` SDK module, importing lazily. None if not installed.
- L132 `_get_anthropic_max_output(model: str)` (function) — Look up the max output token limit for an Anthropic model.
- L153 `_resolve_positive_anthropic_max_tokens(value)` (function) — Return ``value`` floored to a positive int, or ``None`` if it is not a
- L179 `_resolve_anthropic_messages_max_tokens(requested, model: str, context_length: Optional[int]=None)` (function) — Resolve the ``max_tokens`` budget for an Anthropic Messages call.
- L210 `_supports_adaptive_thinking(model: str)` (function) — Return True for Claude 4.6+ models that support adaptive thinking.
- L215 `_supports_xhigh_effort(model: str)` (function) — Return True for models that accept the 'xhigh' adaptive effort level.
- L226 `_forbids_sampling_params(model: str)` (function) — Return True for models that 400 on any non-default temperature/top_p/top_k.
- L236 `_supports_fast_mode(model: str)` (function) — Return True for models that support Anthropic Fast Mode (speed=fast).
- L293 `_detect_claude_code_version()` (function) — Detect the installed Claude Code version, fall back to a static constant.
- L322 `_get_claude_code_version()` (function) — Lazily detect the installed Claude Code version when OAuth headers need it.
- L330 `_is_oauth_token(key: str)` (function) — Check if the key is an Anthropic OAuth/setup token.
- L358 `_normalize_base_url_text(base_url)` (function) — Normalize SDK/base transport URL values to a plain string for inspection.
- L369 `_is_third_party_anthropic_endpoint(base_url: str | None)` (function) — Return True for non-Anthropic endpoints using the Anthropic Messages API.
- L385 `_is_kimi_coding_endpoint(base_url: str | None)` (function) — Return True for Kimi's /coding endpoint that requires claude-code UA.
- L408 `_model_name_is_kimi_family(model: str | None)` (function)
- L420 `_is_kimi_family_endpoint(base_url: str | None, model: str | None=None)` (function) — Return True for any Kimi / Moonshot Anthropic-Messages-speaking endpoint.
- L448 `_is_deepseek_anthropic_endpoint(base_url: str | None)` (function) — Return True for DeepSeek's Anthropic-compatible endpoint.
- L475 `_requires_bearer_auth(base_url: str | None)` (function) — Return True for Anthropic-compatible providers that require Bearer auth.
- L493 `_base_url_needs_context_1m_beta(base_url: str | None)` (function) — Return True for endpoints that still gate 1M context behind a beta.
- L501 `_is_minimax_anthropic_endpoint(base_url: str | None)` (function) — Return True for MiniMax's Anthropic-compatible endpoints.
- L516 `_is_azure_anthropic_endpoint(base_url: str | None)` (function) — Return True for Azure-hosted Anthropic Messages endpoints.
- L539 `_common_betas_for_base_url(base_url: str | None, *, drop_context_1m_beta: bool=False)` (function) — Return the beta headers that are safe for the configured endpoint.
- L571 `_build_anthropic_client_with_bearer_hook(token_provider, base_url: str=None, timeout: float=None, *, drop_context_1m_beta: bool=False)` (function) — Anthropic-on-Foundry Entra ID variant of :func:`build_anthropic_client`.
- L644 `build_anthropic_client(api_key, base_url: str=None, timeout: float=None, *, drop_context_1m_beta: bool=False)` (function) — Create an Anthropic client, auto-detecting setup-tokens vs API keys.
- L764 `build_anthropic_bedrock_client(region: str)` (function) — Create an AnthropicBedrock client for Bedrock Claude models.
- L800 `_read_claude_code_credentials_from_keychain()` (function) — Read Claude Code OAuth credentials from the macOS Keychain.
- L857 `read_claude_code_credentials()` (function) — Read refreshable Claude Code OAuth credentials.
- L897 `is_claude_code_token_valid(creds: Dict[str, Any])` (function) — Check if Claude Code credentials have a non-expired access token.
- L912 `refresh_anthropic_oauth_pure(refresh_token: str, *, use_json: bool=False)` (function) — Refresh an Anthropic OAuth token without mutating local credential files.
- L976 `_refresh_oauth_token(creds: Dict[str, Any])` (function) — Attempt to refresh an expired Claude Code OAuth token.
- L997 `_write_claude_code_credentials(access_token: str, refresh_token: str, expires_at_ms: int, *, scopes: Optional[list]=None)` (function) — Write refreshed credentials back to ~/.claude/.credentials.json.
- L1065 `_resolve_claude_code_token_from_credentials(creds: Optional[Dict[str, Any]]=None)` (function) — Resolve a token from Claude Code credential files, refreshing if needed.
- L1080 `_prefer_refreshable_claude_code_token(env_token: str, creds: Optional[Dict[str, Any]])` (function) — Prefer Claude Code creds when a persisted env OAuth token would shadow refresh.
- L1102 `resolve_anthropic_token()` (function) — Resolve an Anthropic token from all available sources.
- L1146 `run_oauth_setup_token()` (function) — Run 'claude setup-token' interactively and return the resulting token.
- L1197 `_generate_pkce()` (function) — Generate PKCE code_verifier and code_challenge (S256).
- L1210 `run_hermes_oauth_login_pure()` (function) — Run Hermes-native OAuth PKCE flow and return credential state.
- L1321 `read_hermes_oauth_credentials()` (function) — Read Hermes-managed OAuth credentials from ~/.hermes/.anthropic_oauth.json.
- L1338 `_is_bedrock_model_id(model: str)` (function) — Detect AWS Bedrock model IDs that use dots as namespace separators.
- L1358 `normalize_model_name(model: str, preserve_dots: bool=False)` (function) — Normalize a model name for the Anthropic API.
- L1387 `_sanitize_tool_id(tool_id: str)` (function) — Sanitize a tool call ID for the Anthropic API.
- L1400 `_normalize_tool_input_schema(schema: Any)` (function) — Normalize tool schemas before sending them to Anthropic.
- L1441 `convert_tools_to_anthropic(tools: List[Dict])` (function) — Convert OpenAI tool definitions to Anthropic format.
- L1479 `_image_source_from_openai_url(url: str)` (function) — Convert an OpenAI-style image URL/data URL into Anthropic image source.
- L1501 `_convert_content_part_to_anthropic(part: Any)` (function) — Convert a single OpenAI-style content part to Anthropic format.
- L1526 `_to_plain_data(value: Any, *, _depth: int=0, _path: Optional[set]=None)` (function) — Recursively convert SDK objects to plain Python data structures.
- L1572 `_extract_preserved_thinking_blocks(message: Dict[str, Any])` (function) — Return Anthropic thinking blocks previously preserved on the message.
- L1589 `_convert_content_to_anthropic(content: Any)` (function) — Convert OpenAI-style multimodal content arrays to Anthropic blocks.
- L1602 `_content_parts_to_anthropic_blocks(parts: Any)` (function) — Convert OpenAI-style tool-message content parts → Anthropic tool_result inner blocks.
- L1628 `_convert_assistant_message(m: Dict[str, Any])` (function) — Convert an assistant message to Anthropic content blocks.
- L1690 `_convert_tool_message_to_result(result: List[Dict[str, Any]], m: Dict[str, Any])` (function) — Convert a tool message to an Anthropic tool_result, merging consecutive
- L1752 `_convert_user_message(content: Any)` (function) — Validate and convert a user message to anthropic format.
- L1769 `_strip_orphaned_tool_blocks(result: List[Dict[str, Any]])` (function) — Strip tool_use blocks with no matching tool_result, and vice versa.
- L1826 `_merge_consecutive_roles(result: List[Dict[str, Any]])` (function) — Merge consecutive same-role messages to enforce Anthropic alternation.
- L1878 `_manage_thinking_signatures(result: List[Dict[str, Any]], base_url: str | None, model: str | None)` (function) — Strip or preserve thinking blocks based on endpoint type.
- L1984 `_evict_old_screenshots(result: List[Dict[str, Any]])` (function) — Keep only the most recent ``_MAX_KEEP_IMAGES`` computer-use screenshots.
- L2019 `convert_messages_to_anthropic(messages: List[Dict], base_url: str | None=None, model: str | None=None)` (function) — Convert OpenAI-format messages to Anthropic format.
- L2083 `build_anthropic_kwargs(model: str, messages: List[Dict], tools: Optional[List[Dict]], max_tokens: Optional[int], reasoning_config: Optional[Dict[str, Any]], tool_choice: Optional[str]=None, is_oauth: bool=False, preserve_dots: bool=False, context_length: Optional[int]=None, base_url: str | None=None, fast_mode: bool=False, drop_context_1m_beta: bool=False)` (function) — Build kwargs for anthropic.messages.create().
