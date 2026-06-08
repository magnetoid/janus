---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_content_none_guard.py

Symbols in `tests/tools/test_browser_content_none_guard.py`.

- L18 `_make_response(content)` (function) — Build a minimal OpenAI-compatible ChatCompletion response stub.
- L27 `TestExtractRelevantContentNoneGuard` (class) — tools/browser_tool.py — _extract_relevant_content()
- L30 `test_none_content_falls_back_to_truncated(self)` (method) — When LLM returns None content, should fall back to truncated snapshot.
- L41 `test_normal_content_returned(self)` (method) — Normal string content should pass through.
- L50 `test_empty_string_content_falls_back(self)` (method) — Empty string content should also fall back to truncated.
- L63 `TestBrowserVisionNoneGuard` (class) — tools/browser_tool.py — browser_vision() analysis extraction
- L66 `test_none_content_produces_fallback_message(self)` (method) — When LLM returns None content, analysis should have a fallback message.
- L74 `test_normal_content_passes_through(self)` (method) — Normal analysis content should pass through unchanged.
- L85 `TestBrowserSourceLinesAreGuarded` (class) — Verify the actual source file has the fix applied.
- L89 `_read_file()` (method)
- L95 `test_extract_relevant_content_guarded(self)` (method)
- L103 `test_browser_vision_guarded(self)` (method)
