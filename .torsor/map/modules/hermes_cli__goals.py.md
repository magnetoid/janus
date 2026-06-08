---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/goals.py

Symbols in `hermes_cli/goals.py`.

- L143 `GoalState` (class) — Serializable goal state stored per session.
- L163 `to_json(self)` (method)
- L167 `from_json(cls, raw: str)` (method)
- L189 `render_subgoals_block(self)` (method) — Render the subgoals as a numbered ``- N. text`` block. Empty
- L202 `_meta_key(session_id: str)` (function)
- L209 `_get_session_db()` (function) — Return a SessionDB instance for the current HERMES_HOME.
- L239 `load_goal(session_id: str)` (function) — Load the goal for a session, or None if none exists.
- L260 `save_goal(session_id: str, state: GoalState)` (function) — Persist a goal to SessionDB. No-op if DB unavailable.
- L273 `clear_goal(session_id: str)` (function) — Mark a goal cleared in the DB (preserved for audit, status=cleared).
- L287 `_truncate(text: str, limit: int)` (function)
- L298 `_goal_judge_max_tokens()` (function) — Resolve auxiliary.goal_judge.max_tokens, falling back to the default.
- L322 `_parse_judge_response(raw: str)` (function) — Parse the judge's reply. Fail-open to ``(False, "<reason>", parse_failed)``.
- L371 `judge_goal(goal: str, last_response: str, *, timeout: float=DEFAULT_JUDGE_TIMEOUT, subgoals: Optional[List[str]]=None)` (function) — Ask the auxiliary model whether the goal is satisfied.
- L471 `GoalManager` (class) — Per-session goal state + continuation decisions.
- L488 `__init__(self, session_id: str, *, default_max_turns: int=DEFAULT_MAX_TURNS)` (method)
- L496 `state(self)` (method)
- L499 `is_active(self)` (method)
- L502 `has_goal(self)` (method)
- L505 `status_line(self)` (method)
- L522 `set(self, goal: str, *, max_turns: Optional[int]=None)` (method)
- L538 `pause(self, reason: str='user-paused')` (method)
- L546 `resume(self, *, reset_budget: bool=True)` (method)
- L556 `clear(self)` (method)
- L563 `mark_done(self, reason: str)` (method)
- L573 `add_subgoal(self, text: str)` (method) — Append a user-added criterion to the active goal. Requires
- L588 `remove_subgoal(self, index_1based: int)` (method) — Remove a subgoal by 1-based index. Returns the removed text.
- L601 `clear_subgoals(self)` (method) — Wipe all subgoals. Returns the previous count.
- L610 `render_subgoals(self)` (method) — Public helper for the /subgoal slash command.
- L620 `evaluate_after_turn(self, last_response: str, *, user_initiated: bool=True)` (method) — Run the judge and update state. Return a decision dict.
- L739 `next_continuation_prompt(self)` (method)
- L779 `run_kanban_goal_loop(*, task_id: str, goal_text: str, run_turn, task_status_fn, block_fn, max_turns: int=DEFAULT_MAX_TURNS, first_response: str='', log=None)` (function) — Drive a kanban worker through a Ralph-style goal loop.
