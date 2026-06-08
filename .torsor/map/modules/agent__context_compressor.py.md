---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/context_compressor.py

Symbols in `agent/context_compressor.py`.

- L118 `_dedupe_append(items: list[str], value: str, *, limit: int)` (function)
- L124 `_extract_tool_call_name_and_args(tool_call: Any)` (function) — Return a best-effort ``(name, arguments)`` pair for dict/object tool calls.
- L136 `_extract_tool_call_id(tool_call: Any)` (function)
- L142 `_collect_path_mentions(text: str, relevant_files: list[str], *, limit: int=12)` (function)
- L147 `_content_length_for_budget(raw_content: Any)` (function) — Return the effective char-length of a message's content for token budgeting.
- L180 `_content_text_for_contains(content: Any)` (function) — Return a best-effort text view of message content.
- L203 `_append_text_to_content(content: Any, text: str, *, prepend: bool=False)` (function) — Append or prepend plain text to message content safely.
- L221 `_strip_image_parts_from_parts(parts: Any)` (function) — Strip image parts from an OpenAI-style content-parts list.
- L246 `_truncate_tool_call_args_json(args: str, head_chars: int=200)` (function) — Shrink long string values inside a tool-call arguments JSON blob while
- L295 `_is_image_part(part: Any)` (function) — True if ``part`` is a multimodal image content block.
- L308 `_content_has_images(content: Any)` (function) — True if a message's ``content`` is a multimodal list with image parts.
- L315 `_strip_images_from_content(content: Any)` (function) — Return a copy of ``content`` with every image part replaced by a
- L343 `_strip_historical_media(messages: List[Dict[str, Any]])` (function) — Replace image parts in older messages with placeholder text.
- L400 `_summarize_tool_result(tool_name: str, tool_args: str, tool_content: str)` (function) — Create an informative 1-line summary of a tool call + result.
- L522 `ContextCompressor` (class) — Default context engine — compresses conversation context via lossy summarization.
- L534 `name(self)` (method)
- L537 `on_session_reset(self)` (method) — Reset all per-session state for /new or /reset.
- L556 `update_model(self, model: str, context_length: int, base_url: str='', api_key: Any='', provider: str='', api_mode: str='')` (method) — Update model info after a model switch or fallback activation.
- L584 `__init__(self, model: str, threshold_percent: float=0.5, protect_first_n: int=3, protect_last_n: int=20, summary_target_ratio: float=0.2, quiet_mode: bool=False, summary_model_override: str=None, base_url: str='', api_key: str='', config_context_length: int | None=None, provider: str='', api_mode: str='', abort_on_summary_failure: bool=False)` (method)
- L684 `update_from_response(self, usage: Dict[str, Any])` (method) — Update tracked token usage from API response.
- L698 `should_defer_preflight_to_real_usage(self, rough_tokens: int)` (method) — Return True when a high rough preflight estimate is known-noisy.
- L728 `should_compress(self, prompt_tokens: int=None)` (method) — Check if context exceeds the compression threshold.
- L754 `_prune_old_tool_results(self, messages: List[Dict[str, Any]], protect_tail_count: int, protect_tail_tokens: int | None=None)` (method) — Replace old tool result contents with informative 1-line summaries.
- L926 `_compute_summary_budget(self, turns_to_summarize: List[Dict[str, Any]])` (method) — Scale summary token budget with the amount of content being compressed.
- L946 `_serialize_for_summary(self, turns: List[Dict[str, Any]])` (method) — Serialize conversation turns into labeled text for the summarizer.
- L1001 `_build_static_fallback_summary(self, turns_to_summarize: List[Dict[str, Any]], reason: str | None=None)` (method) — Build a deterministic handoff when the LLM summarizer is unavailable.
- L1190 `_fallback_to_main_for_compression(self, e: Exception, reason: str)` (method) — Switch from a separate ``summary_model`` back to the main model.
- L1217 `_generate_summary(self, turns_to_summarize: List[Dict[str, Any]], focus_topic: Optional[str]=None)` (method) — Generate a structured summary of conversation turns.
- L1549 `_strip_summary_prefix(summary: str)` (method) — Return summary body without the current, legacy, or any historical
- L1565 `_with_summary_prefix(cls, summary: str)` (method) — Normalize summary text to the current compaction handoff format.
- L1571 `_is_context_summary_content(content: Any)` (method)
- L1578 `_find_latest_context_summary(cls, messages: List[Dict[str, Any]], start: int, end: int)` (method) — Find the newest handoff summary inside a compression window.
- L1596 `_get_tool_call_id(tc)` (method) — Extract the call ID from a tool_call entry (dict or SimpleNamespace).
- L1602 `_sanitize_tool_pairs(self, messages: List[Dict[str, Any]])` (method) — Fix orphaned tool_call / tool_result pairs after compression.
- L1662 `_align_boundary_forward(self, messages: List[Dict[str, Any]], idx: int)` (method) — Push a compress-start boundary forward past any orphan tool results.
- L1672 `_protect_head_size(self, messages: List[Dict[str, Any]])` (method) — Total count of head messages to protect.
- L1692 `_align_boundary_backward(self, messages: List[Dict[str, Any]], idx: int)` (method) — Pull a compress-end boundary backward to avoid splitting a
- L1720 `_find_last_user_message_idx(self, messages: List[Dict[str, Any]], head_end: int)` (method) — Return the index of the last user-role message at or after *head_end*, or -1.
- L1729 `_ensure_last_user_message_in_tail(self, messages: List[Dict[str, Any]], cut_idx: int, head_end: int)` (method) — Guarantee the most recent user message is in the protected tail.
- L1776 `_find_tail_cut_by_tokens(self, messages: List[Dict[str, Any]], head_end: int, token_budget: int | None=None)` (method) — Walk backward from the end of messages, accumulating tokens until
- L1843 `has_content_to_compress(self, messages: List[Dict[str, Any]])` (method) — Return True if there is a non-empty middle region to compact.
- L1858 `compress(self, messages: List[Dict[str, Any]], current_tokens: int=None, focus_topic: str=None, force: bool=False)` (method) — Compress conversation messages by summarizing middle turns.
