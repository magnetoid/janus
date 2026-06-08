---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/plugin_llm.py

Symbols in `agent/plugin_llm.py`.

- L78 `PluginLlmTextInput` (class) — Text block in a structured input list.
- L86 `PluginLlmImageInput` (class) — Image block in a structured input list.
- L115 `PluginLlmUsage` (class) — Token + cost usage for a completion. All fields optional — providers
- L128 `PluginLlmCompleteResult` (class) — Result of :meth:`PluginLlm.complete`.
- L140 `PluginLlmStructuredResult` (class) — Result of :meth:`PluginLlm.complete_structured`.
- L164 `_TrustPolicy` (class) — Resolved trust gate for one plugin's LLM access.
- L178 `_normalize_ref(raw: str)` (function) — Lower-case + strip whitespace. Used for allowlist matching.
- L183 `_coerce_allowlist(raw: Any)` (function) — Coerce a YAML list into ``(frozenset_or_None, allow_any)``.
- L202 `_resolve_trust_policy(plugin_id: str)` (function) — Read ``plugins.entries.<plugin_id>.llm`` from config.yaml.
- L249 `PluginLlmTrustError` (class) — Raised when a plugin attempts an LLM override without trust.
- L253 `_check_overrides(policy: _TrustPolicy, *, requested_provider: Optional[str], requested_model: Optional[str], requested_agent_id: Optional[str], requested_profile: Optional[str])` (function) — Apply the trust gate. Returns the validated overrides as
- L337 `_normalize_input_block(block: PluginLlmInput)` (function) — Coerce a structured input block to a plain dict the message
- L374 `_build_structured_messages(*, instructions: str, inputs: Sequence[PluginLlmInput], json_mode: bool, json_schema: Optional[Any], schema_name: Optional[str], system_prompt: Optional[str])` (function) — Build the OpenAI-style messages list for a structured call.
- L447 `_strip_code_fences(text: str)` (function) — Pull the first fenced code block out of ``text`` if any. Returns
- L456 `_parse_structured_text(*, text: str, json_mode: bool, json_schema: Optional[Any])` (function) — Return ``(parsed, content_type)``. ``content_type`` is ``"json"``
- L492 `_extract_usage(response: Any)` (function) — Pull token usage out of an OpenAI-shaped response object.
- L520 `_extract_text(response: Any)` (function) — Pull the assistant text out of an OpenAI-shaped response object.
- L543 `_resolve_attribution(*, provider_override: Optional[str], model_override: Optional[str], response: Any)` (function) — Decide what to record as ``result.provider`` / ``result.model``.
- L598 `PluginLlm` (class) — Host-owned LLM access for one trusted plugin.
- L607 `__init__(self, *, plugin_id: str, policy_loader: Optional[Callable[[str], _TrustPolicy]]=None, sync_caller: Optional[Callable[..., Any]]=None, async_caller: Optional[Callable[..., Awaitable[Any]]]=None)` (method)
- L622 `complete(self, messages: List[Dict[str, Any]], *, provider: Optional[str]=None, model: Optional[str]=None, temperature: Optional[float]=None, max_tokens: Optional[int]=None, timeout: Optional[float]=None, agent_id: Optional[str]=None, profile: Optional[str]=None, purpose: Optional[str]=None)` (method) — Run a host-owned chat completion against the user's active model.
- L683 `complete_structured(self, *, instructions: str, input: Sequence[PluginLlmInput], json_schema: Optional[Any]=None, json_mode: bool=False, schema_name: Optional[str]=None, system_prompt: Optional[str]=None, provider: Optional[str]=None, model: Optional[str]=None, temperature: Optional[float]=None, max_tokens: Optional[int]=None, timeout: Optional[float]=None, agent_id: Optional[str]=None, profile: Optional[str]=None, purpose: Optional[str]=None)` (method) — Run a bounded host-owned structured completion.
- L777 `acomplete(self, messages: List[Dict[str, Any]], *, provider: Optional[str]=None, model: Optional[str]=None, temperature: Optional[float]=None, max_tokens: Optional[int]=None, timeout: Optional[float]=None, agent_id: Optional[str]=None, profile: Optional[str]=None, purpose: Optional[str]=None)` (method) — Async sibling of :meth:`complete`.
- L823 `acomplete_structured(self, *, instructions: str, input: Sequence[PluginLlmInput], json_schema: Optional[Any]=None, json_mode: bool=False, schema_name: Optional[str]=None, system_prompt: Optional[str]=None, provider: Optional[str]=None, model: Optional[str]=None, temperature: Optional[float]=None, max_tokens: Optional[int]=None, timeout: Optional[float]=None, agent_id: Optional[str]=None, profile: Optional[str]=None, purpose: Optional[str]=None)` (method) — Async sibling of :meth:`complete_structured`.
- L898 `_json_response_format(*, json_mode: bool, json_schema: Optional[Any])` (method) — Build the ``extra_body.response_format`` payload for the
- L919 `_invoke_sync(self, *, messages: List[Dict[str, Any]], provider_override: Optional[str], model_override: Optional[str], profile_override: Optional[str], temperature: Optional[float], max_tokens: Optional[int], timeout: Optional[float], extra_body: Optional[Dict[str, Any]]=None)` (method) — Invoke the host's ``call_llm``. Lazy-imports
- L966 `_invoke_async(self, *, messages: List[Dict[str, Any]], provider_override: Optional[str], model_override: Optional[str], profile_override: Optional[str], temperature: Optional[float], max_tokens: Optional[int], timeout: Optional[float], extra_body: Optional[Dict[str, Any]]=None)` (method)
- L1016 `make_plugin_llm_for_test(*, plugin_id: str, policy: _TrustPolicy, sync_caller: Optional[Callable[..., Any]]=None, async_caller: Optional[Callable[..., Awaitable[Any]]]=None)` (function) — Construct a :class:`PluginLlm` with an injected policy and caller.
