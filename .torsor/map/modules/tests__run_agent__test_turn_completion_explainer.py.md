---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_turn_completion_explainer.py

Symbols in `tests/run_agent/test_turn_completion_explainer.py`.

- L31 `_mock_response(content='Hello', finish_reason='stop', tool_calls=None)` (function)
- L37 `_make_agent(max_iterations: int=10, config: dict | None=None)` (function)
- L66 `test_explanation_quiet_for_normal_text_response()` (function) — A healthy text_response exit must NOT produce any explanation.
- L74 `test_explanation_quiet_for_empty_reason()` (function)
- L81 `test_explanation_for_empty_response_exhausted()` (function)
- L88 `test_explanation_for_partial_stream_recovery()` (function)
- L94 `test_explanation_for_max_iterations_reached_prefix_match()` (function) — ``max_iterations_reached(...)`` carries a parenthetical suffix.
- L102 `test_explanation_for_all_retries_exhausted()` (function)
- L112 `test_explainer_enabled_by_default()` (function)
- L120 `test_explainer_disabled_via_env()` (function)
- L128 `test_explainer_disabled_via_config()` (function)
- L142 `test_run_conversation_empty_exhausted_surfaces_explanation()` (function) — Four empty responses in a row should exhaust retries and the final
- L165 `test_run_conversation_normal_reply_stays_quiet()` (function) — A normal short reply like 'Done.' must NOT get an explainer footer.
