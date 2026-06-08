---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/gemini_native_adapter.py

Symbols in `agent/gemini_native_adapter.py`.

- L44 `is_native_gemini_base_url(base_url: str)` (function) — Return True when the endpoint speaks Gemini's native REST API.
- L54 `probe_gemini_tier(api_key: str, base_url: str=DEFAULT_GEMINI_BASE_URL, *, model: str='gemini-2.5-flash', timeout: float=10.0)` (function) — Probe a Google AI Studio API key and return its tier.
- L128 `is_free_tier_quota_error(error_message: str)` (function) — Return True when a Gemini 429 message indicates free-tier exhaustion.
- L145 `GeminiAPIError` (class) — Error shape compatible with Hermes retry/error classification.
- L148 `__init__(self, message: str, *, code: str='gemini_api_error', status_code: Optional[int]=None, response: Optional[httpx.Response]=None, retry_after: Optional[float]=None, details: Optional[Dict[str, Any]]=None)` (method)
- L166 `_coerce_content_to_text(content: Any)` (function)
- L184 `_extract_multimodal_parts(content: Any)` (function)
- L222 `_tool_call_extra_signature(tool_call: Dict[str, Any])` (function)
- L235 `_translate_tool_call_to_gemini(tool_call: Dict[str, Any])` (function)
- L257 `_translate_tool_result_to_gemini(message: Dict[str, Any], tool_name_by_call_id: Optional[Dict[str, str]]=None)` (function)
- L283 `_build_gemini_contents(messages: List[Dict[str, Any]])` (function)
- L337 `_translate_tools_to_gemini(tools: Any)` (function)
- L361 `_translate_tool_choice_to_gemini(tool_choice: Any)` (function)
- L379 `_normalize_thinking_config(config: Any)` (function)
- L395 `build_gemini_request(*, messages: List[Dict[str, Any]], tools: Any=None, tool_choice: Any=None, temperature: Optional[float]=None, max_tokens: Optional[int]=None, top_p: Optional[float]=None, stop: Any=None, thinking_config: Any=None)` (function)
- L449 `_map_gemini_finish_reason(reason: str)` (function)
- L460 `_tool_call_extra_from_part(part: Dict[str, Any])` (function)
- L467 `_empty_response(model: str)` (function)
- L493 `translate_gemini_response(resp: Dict[str, Any], model: str)` (function)
- L562 `_GeminiStreamChunk` (class)
- L566 `_make_stream_chunk(*, model: str, content: str='', tool_call_delta: Optional[Dict[str, Any]]=None, finish_reason: Optional[str]=None, reasoning: str='')` (function)
- L612 `_iter_sse_events(response: httpx.Response)` (function)
- L637 `translate_stream_event(event: Dict[str, Any], model: str, tool_call_indices: Dict[str, Dict[str, Any]])` (function)
- L719 `gemini_http_error(response: httpx.Response)` (function)
- L798 `_GeminiChatCompletions` (class)
- L799 `__init__(self, client: 'GeminiNativeClient')` (method)
- L802 `create(self, **kwargs: Any)` (method)
- L806 `_AsyncGeminiChatCompletions` (class)
- L807 `__init__(self, client: 'AsyncGeminiNativeClient')` (method)
- L810 `create(self, **kwargs: Any)` (method)
- L814 `_GeminiChatNamespace` (class)
- L815 `__init__(self, client: 'GeminiNativeClient')` (method)
- L819 `_AsyncGeminiChatNamespace` (class)
- L820 `__init__(self, client: 'AsyncGeminiNativeClient')` (method)
- L824 `GeminiNativeClient` (class) — Minimal OpenAI-SDK-compatible facade over Gemini's native REST API.
- L827 `__init__(self, *, api_key: str, base_url: Optional[str]=None, default_headers: Optional[Dict[str, str]]=None, timeout: Any=None, http_client: Optional[httpx.Client]=None, **_: Any)` (method)
- L856 `close(self)` (method)
- L863 `__enter__(self)` (method)
- L866 `__exit__(self, exc_type, exc_val, exc_tb)` (method)
- L869 `_headers(self)` (method)
- L880 `_advance_stream_iterator(iterator: Iterator[_GeminiStreamChunk])` (method)
- L886 `_create_chat_completion(self, *, model: str='gemini-2.5-flash', messages: Optional[List[Dict[str, Any]]]=None, stream: bool=False, tools: Any=None, tool_choice: Any=None, temperature: Optional[float]=None, max_tokens: Optional[int]=None, top_p: Optional[float]=None, stop: Any=None, extra_body: Optional[Dict[str, Any]]=None, timeout: Any=None, **_: Any)` (method)
- L935 `_stream_completion(self, *, model: str, request: Dict[str, Any], timeout: Any=None)` (method)
- L959 `AsyncGeminiNativeClient` (class) — Async wrapper used by auxiliary_client for native Gemini calls.
- L962 `__init__(self, sync_client: GeminiNativeClient)` (method)
- L974 `_create_chat_completion(self, **kwargs: Any)` (method)
- L989 `close(self)` (method)
