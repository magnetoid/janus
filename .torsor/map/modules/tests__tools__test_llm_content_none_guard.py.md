---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_llm_content_none_guard.py

Symbols in `tests/tools/test_llm_content_none_guard.py`.

- L23 `_make_response(content, **msg_attrs)` (function) — Build a minimal OpenAI-compatible ChatCompletion response stub.
- L34 `_run(coro)` (function) — Run an async coroutine synchronously.
- L41 `TestMoAReferenceModelContentNone` (class) — tools/mixture_of_agents_tool.py — _query_model()
- L44 `test_none_content_raises_before_fix(self)` (method) — Demonstrate that None content from a reasoning model crashes.
- L52 `test_none_content_safe_with_or_guard(self)` (method) — The ``or ""`` guard should convert None to empty string.
- L59 `test_normal_content_unaffected(self)` (method) — Regular string content should pass through unchanged.
- L69 `TestMoAAggregatorContentNone` (class) — tools/mixture_of_agents_tool.py — _run_aggregator()
- L72 `test_none_content_raises_before_fix(self)` (method)
- L78 `test_none_content_safe_with_or_guard(self)` (method)
- L87 `TestWebToolsProcessorContentNone` (class) — tools/web_tools.py — _process_with_llm() return line
- L90 `test_none_content_raises_before_fix(self)` (method)
- L96 `test_none_content_safe_with_or_guard(self)` (method)
- L105 `TestWebToolsSynthesisContentNone` (class) — tools/web_tools.py — synthesize_content() final_summary line
- L108 `test_none_content_raises_before_fix(self)` (method)
- L114 `test_none_content_safe_with_or_guard(self)` (method)
- L123 `TestVisionToolsContentNone` (class) — tools/vision_tools.py — analyze_image() analysis extraction
- L126 `test_none_content_raises_before_fix(self)` (method)
- L132 `test_none_content_safe_with_or_guard(self)` (method)
- L141 `TestSkillsGuardContentNone` (class) — tools/skills_guard.py — _llm_audit_skill() llm_text extraction
- L144 `test_none_content_raises_before_fix(self)` (method)
- L150 `test_none_content_safe_with_or_guard(self)` (method)
- L159 `TestSourceLinesAreGuarded` (class) — Read the actual source files and verify the fix is applied.
- L167 `_read_file(rel_path: str)` (method)
- L173 `test_mixture_of_agents_reference_model_guarded(self)` (method)
- L181 `test_web_tools_guarded(self)` (method)
- L188 `test_vision_tools_guarded(self)` (method)
- L195 `test_skills_guard_guarded(self)` (method)
- L205 `TestExtractContentOrReasoning` (class) — agent/auxiliary_client.py — extract_content_or_reasoning()
- L208 `test_normal_content_returned(self)` (method)
- L212 `test_none_content_returns_empty(self)` (method)
- L216 `test_empty_string_returns_empty(self)` (method)
- L220 `test_think_blocks_stripped_with_remaining_content(self)` (method)
- L224 `test_think_only_content_falls_back_to_reasoning_field(self)` (method) — When content is only think blocks, fall back to structured reasoning.
- L232 `test_none_content_with_reasoning_field(self)` (method) — DeepSeek-R1 pattern: content=None, reasoning='...'
- L237 `test_none_content_with_reasoning_content_field(self)` (method) — Moonshot/Novita pattern: content=None, reasoning_content='...'
- L242 `test_none_content_with_reasoning_details(self)` (method) — OpenRouter unified format: reasoning_details=[{summary: ...}]
- L249 `test_reasoning_fields_not_duplicated(self)` (method) — When reasoning and reasoning_content have the same value, don't duplicate.
- L254 `test_multiple_reasoning_sources_combined(self)` (method) — Different reasoning sources are joined with double newline.
- L265 `test_content_preferred_over_reasoning(self)` (method) — When both content and reasoning exist, content wins.
