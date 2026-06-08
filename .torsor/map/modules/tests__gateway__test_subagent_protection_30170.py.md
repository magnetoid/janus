---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_subagent_protection_30170.py

Symbols in `tests/gateway/test_subagent_protection_30170.py`.

- L63 `_make_event(text: str='hello', chat_id: str='123')` (function)
- L78 `_make_runner()` (function)
- L96 `_make_adapter()` (function)
- L106 `_make_parent_with_subagents(*, children: int=1, with_lock: bool=True)` (function) — A MagicMock shaped like an AIAgent that currently owns *children* subagents.
- L121 `_make_parent_no_subagents()` (function) — A MagicMock shaped like an AIAgent that is NOT delegating.
- L137 `TestAgentHasActiveSubagents` (class) — The detection helper must be both precise and defensive.
- L140 `test_returns_false_for_none(self)` (method)
- L143 `test_returns_false_for_pending_sentinel(self)` (method)
- L149 `test_returns_false_when_attribute_missing(self)` (method) — Production AIAgents always have _active_children, but the helper
- L158 `test_returns_false_for_empty_list(self)` (method)
- L164 `test_returns_true_for_single_child(self)` (method)
- L170 `test_returns_true_for_many_children(self)` (method)
- L178 `test_works_without_lock(self)` (method) — ``_active_children_lock`` is optional in test stubs.
- L187 `test_rejects_truthy_non_collection_attribute(self)` (method) — The MagicMock auto-attribute regression. ``MagicMock()._active_children``
- L199 `test_accepts_list_tuple_set(self, container: Any)` (method)
- L209 `TestBusyHandlerDemotesInterruptForSubagents` (class) — The Phase-1 fix from #30170: parent.interrupt() must NOT fire when
- L214 `test_does_not_call_interrupt_when_subagents_active(self)` (method)
- L233 `test_ack_explains_the_demotion(self)` (method) — The user-visible ack must mention the subagent context AND
- L257 `test_interrupt_still_fires_when_no_subagents(self)` (method) — Regression-guard the other direction: with no subagents the
- L279 `test_queue_mode_unchanged_with_subagents(self)` (method) — Configured ``queue`` mode is already subagent-safe; the new
- L303 `test_steer_mode_still_routes_through_running_agent_steer(self)` (method) — Configured ``steer`` mode must reach ``running_agent.steer()``
- L326 `test_pending_sentinel_does_not_demote(self)` (method) — The placeholder ``_AGENT_PENDING_SENTINEL`` is not a real
