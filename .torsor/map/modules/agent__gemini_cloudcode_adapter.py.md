---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/gemini_cloudcode_adapter.py

Symbols in `agent/gemini_cloudcode_adapter.py`.

- L65 `_coerce_content_to_text(content: Any)` (function) — OpenAI content may be str or a list of parts; reduce to plain text.
- L86 `_translate_tool_call_to_gemini(tool_call: Dict[str, Any])` (function) — OpenAI tool_call -> Gemini functionCall part.
- L108 `_translate_tool_result_to_gemini(message: Dict[str, Any])` (function) — OpenAI tool-role message -> Gemini functionResponse part.
- L133 `_build_gemini_contents(messages: List[Dict[str, Any]])` (function) — Convert OpenAI messages[] to Gemini contents[] + systemInstruction.
- L188 `_translate_tools_to_gemini(tools: Any)` (function) — OpenAI tools[] -> Gemini tools[].functionDeclarations[].
- L214 `_translate_tool_choice_to_gemini(tool_choice: Any)` (function) — OpenAI tool_choice -> Gemini toolConfig.functionCallingConfig.
- L238 `_normalize_thinking_config(config: Any)` (function) — Accept thinkingBudget / thinkingLevel / includeThoughts (+ snake_case).
- L255 `build_gemini_request(*, messages: List[Dict[str, Any]], tools: Any=None, tool_choice: Any=None, temperature: Optional[float]=None, max_tokens: Optional[int]=None, top_p: Optional[float]=None, stop: Any=None, thinking_config: Any=None)` (function) — Build the inner Gemini request body (goes inside ``request`` wrapper).
- L300 `wrap_code_assist_request(*, project_id: str, model: str, inner_request: Dict[str, Any], user_prompt_id: Optional[str]=None)` (function) — Wrap the inner Gemini request in the Code Assist envelope.
- L320 `_translate_gemini_response(resp: Dict[str, Any], model: str)` (function) — Non-streaming Gemini response -> OpenAI-shaped SimpleNamespace.
- L405 `_empty_response(model: str)` (function)
- L425 `_map_gemini_finish_reason(reason: str)` (function)
- L440 `_GeminiStreamChunk` (class) — Mimics an OpenAI ChatCompletionChunk with .choices[0].delta.
- L445 `_make_stream_chunk(*, model: str, content: str='', tool_call_delta: Optional[Dict[str, Any]]=None, finish_reason: Optional[str]=None, reasoning: str='')` (function)
- L487 `_iter_sse_events(response: httpx.Response)` (function) — Parse Server-Sent Events from an httpx streaming response.
- L509 `_translate_stream_event(event: Dict[str, Any], model: str, tool_call_counter: List[int])` (function) — Unwrap Code Assist envelope and emit OpenAI-shaped chunk(s).
- L578 `_GeminiChatCompletions` (class)
- L579 `__init__(self, client: 'GeminiCloudCodeClient')` (method)
- L582 `create(self, **kwargs: Any)` (method)
- L586 `_GeminiChatNamespace` (class)
- L587 `__init__(self, client: 'GeminiCloudCodeClient')` (method)
- L591 `GeminiCloudCodeClient` (class) — Minimal OpenAI-SDK-compatible facade over Code Assist v1internal.
- L594 `__init__(self, *, api_key: Optional[str]=None, base_url: Optional[str]=None, default_headers: Optional[Dict[str, str]]=None, project_id: str='', **_: Any)` (method)
- L616 `close(self)` (method)
- L624 `__enter__(self)` (method)
- L627 `__exit__(self, exc_type, exc_val, exc_tb)` (method)
- L630 `_ensure_project_context(self, access_token: str, model: str)` (method) — Lazily resolve and cache the project context for this client.
- L665 `_create_chat_completion(self, *, model: str='gemini-2.5-flash', messages: Optional[List[Dict[str, Any]]]=None, stream: bool=False, tools: Any=None, tool_choice: Any=None, temperature: Optional[float]=None, max_tokens: Optional[int]=None, top_p: Optional[float]=None, stop: Any=None, extra_body: Optional[Dict[str, Any]]=None, timeout: Any=None, **_: Any)` (method)
- L730 `_stream_completion(self, *, model: str, wrapped: Dict[str, Any], headers: Dict[str, str])` (method) — Generator that yields OpenAI-shaped streaming chunks.
- L762 `_gemini_http_error(response: httpx.Response)` (function) — Translate an httpx response into a CodeAssistError with rich metadata.
