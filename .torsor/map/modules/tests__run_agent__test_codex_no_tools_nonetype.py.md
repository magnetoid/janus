---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_codex_no_tools_nonetype.py

Symbols in `tests/run_agent/test_codex_no_tools_nonetype.py`.

- L50 `transport()` (function) — Fresh ``ResponsesApiTransport`` per test (it is stateless but
- L59 `codex_messages()` (function) — Minimal Codex-shaped chat history mirroring the #32892 reproducer:
- L68 `_build_kwargs_no_tools(transport, messages)` (function) — Exercise the real ``build_kwargs`` for the codex backend with no tools.
- L83 `test_build_kwargs_omits_tools_key_when_no_tools(transport, codex_messages)` (function) — ``build_kwargs`` must not place ``tools=None`` in the outgoing dict.
- L98 `test_build_kwargs_omits_tool_choice_and_parallel_when_no_tools(transport, codex_messages)` (function) — ``tool_choice`` / ``parallel_tool_calls`` are meaningless without
- L107 `test_build_kwargs_keeps_required_codex_fields_without_tools(transport, codex_messages)` (function) — The toolless build must still emit the non-negotiable Codex fields
- L120 `test_build_kwargs_emits_tools_when_tools_present(transport, codex_messages)` (function) — Sanity check the inverse: when tools ARE provided, they MUST appear
- L148 `test_build_kwargs_drops_empty_tools_list(transport, codex_messages)` (function) — ``tools=[]`` collapses to ``None`` inside ``_responses_tools`` —
- L167 `test_openai_sdk_raises_typeerror_on_tools_none()` (function) — Document the upstream behaviour the two defences guard against.
