---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_compress_focus.py

Symbols in `tests/agent/test_compress_focus.py`.

- L12 `_make_compressor()` (function) — Create a ContextCompressor with minimal state for testing.
- L36 `test_focus_topic_injected_into_summary_prompt()` (function) — When focus_topic is provided, the LLM prompt includes focus guidance.
- L63 `test_no_focus_topic_no_injection()` (function) — Without focus_topic, the prompt doesn't contain focus guidance.
- L87 `test_compress_passes_focus_to_generate_summary()` (function) — compress() passes focus_topic through to _generate_summary.
- L118 `test_compress_none_focus_by_default()` (function) — compress() passes None focus_topic by default.
