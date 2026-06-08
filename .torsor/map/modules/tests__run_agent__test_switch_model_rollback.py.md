---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_switch_model_rollback.py

Symbols in `tests/run_agent/test_switch_model_rollback.py`.

- L23 `_make_agent_openrouter()` (function) — Agent on openrouter (openai-compatible) with sentinel client + kwargs.
- L53 `_make_agent_anthropic()` (function) — Agent on native anthropic with a sentinel anthropic client.
- L80 `test_openai_client_rebuild_failure_rolls_back_to_original_state()` (function) — When OpenAI client construction fails, every mutated field must restore.
- L113 `test_anthropic_client_rebuild_failure_rolls_back_to_original_state()` (function) — When build_anthropic_client raises, every mutated field must restore.
- L155 `test_cross_branch_anthropic_to_openai_rebuild_failure_rolls_back()` (function) — Switching from anthropic_messages to chat_completions: failure must
- L185 `test_successful_switch_still_works_after_rollback_refactor()` (function) — Sanity check: the try/except wrapper hasn't broken the happy path.
