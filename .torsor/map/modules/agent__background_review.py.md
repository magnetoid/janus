---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/background_review.py

Symbols in `agent/background_review.py`.

- L237 `summarize_background_review_actions(review_messages: List[Dict], prior_snapshot: List[Dict])` (function) — Build the human-facing action summary for a background review pass.
- L300 `build_memory_write_metadata(agent: Any, *, write_origin: Optional[str]=None, execution_context: Optional[str]=None, task_id: Optional[str]=None, tool_call_id: Optional[str]=None)` (function) — Build provenance metadata for external memory-provider mirrors.
- L327 `_run_review_in_thread(agent: Any, messages_snapshot: List[Dict], prompt: str)` (function) — Worker function executed in the background-review daemon thread.
- L562 `spawn_background_review_thread(agent: Any, messages_snapshot: List[Dict], review_memory: bool=False, review_skills: bool=False)` (function) — Build the review thread target and prompt for a background review.
