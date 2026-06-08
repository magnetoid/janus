---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_tool_token_estimation.py

Symbols in `tests/hermes_cli/test_tool_token_estimation.py`.

- L20 `test_estimate_tool_tokens_returns_positive_counts()` (function) — _estimate_tool_tokens should return a non-empty dict with positive values.
- L39 `test_estimate_tool_tokens_is_cached()` (function) — Second call should return the same cached dict object.
- L50 `test_estimate_tool_tokens_returns_empty_when_tiktoken_unavailable(monkeypatch)` (function) — Graceful degradation when tiktoken cannot be imported.
- L74 `test_estimate_tool_tokens_covers_known_tools()` (function) — Should include schemas for well-known tools like terminal, web_search.
- L89 `test_prompt_toolset_checklist_passes_status_fn(monkeypatch)` (function) — _prompt_toolset_checklist should pass a status_fn to curses_checklist.
- L111 `test_status_fn_returns_formatted_token_count(monkeypatch)` (function) — The status_fn should return a human-readable token count string.
- L139 `test_status_fn_deduplicates_overlapping_tools(monkeypatch)` (function) — When toolsets overlap (browser includes web_search), tokens should not double-count.
- L190 `test_status_fn_empty_selection()` (function) — Status function with no tools selected should return ~0 tokens.
- L220 `test_curses_checklist_numbered_fallback_shows_status(monkeypatch, capsys)` (function) — The numbered fallback should print the status_fn output.
- L243 `test_curses_checklist_numbered_fallback_without_status(monkeypatch, capsys)` (function) — The numbered fallback should work fine without status_fn.
- L264 `test_registry_get_schema_returns_schema()` (function) — registry.get_schema() should return a tool's schema dict.
- L278 `test_registry_get_schema_returns_none_for_unknown()` (function) — registry.get_schema() should return None for unknown tools.
