# Plan Mode — design spec

> Date: 2026-06-24 · Status: approved, implementing

## Problem
The agent rushes into multi-step, state-changing work without showing a plan or
getting the user's sign-off. Complements Standing Agreements (which fixes
*forgetting* commitments); Plan mode fixes *acting before alignment*.

## Behaviour
For **hard** tasks (auto-detected) the agent FIRST proposes a step-by-step plan and
**pauses** for approval before executing. Simple/mid tasks are untouched (stay
instant). A `/plan` force-flag makes the next message plan regardless of complexity.

## Components (mirrors agent/agreements.py + tools/agreements_tool.py)
1. **`agent/plan_mode.py`** — best-effort, config-gated, never raises:
   - `enabled(config)` — default on.
   - `should_plan(prompt, config, *, forced=False)` → True when `enabled` and
     (`forced` or `classify_complexity(prompt)=="hard"`). Reuses
     `agent/task_complexity.py` (free, local — no token cost).
   - `directive(config)` — static system-prompt text (empty when disabled).
   - per-session plan store: `record_plan(session, steps)`, `load_plan(session)`,
     `clear(session)`; `format_plan(steps)` → numbered list + approval prompt.
   - `/plan` force flag: `set_forced(session)`, `consume_forced(session)` (one-shot).
2. **`tools/plan_tool.py`** — `propose_plan(steps)` tool: records the plan, returns
   the formatted plan + "Reply **go** to approve, or tell me what to change." The
   agent presents it and yields the turn (same flow as the clarify gateway). On
   approval the agent executes and may seed the `todo` list from the steps.
   Registered in the `memory` toolset + `_JANUS_CORE_TOOLS`.
3. **Directive** injected into the **stable** system-prompt part
   (`agent/system_prompt.py`), config-gated → cache-safe (set once at session start,
   never rebuilt mid-conversation).
4. **Config** `plan_mode: {enabled: true, min_complexity: "hard"}`.
5. **`/plan` command** in `COMMAND_REGISTRY` (+ CLI/gateway handlers): sets the
   force flag so the next task plans even if not hard.

## Invariants
- **Cache-safe**: directive is static in the stable part; plan output is an appended
  message. No mid-conversation system-prompt/toolset mutation.
- **Best-effort**: every function wrapped; never breaks the loop.
- **YAGNI**: no plan-editing UI (reply in natural language → re-propose), no
  cross-session plan persistence, no extra approval data structure.

## Testing
Unit-level (like agreements): `should_plan` gating (enabled+hard, forced override,
disabled), directive on/off, `propose_plan` records/formats, force-flag one-shot,
tool exposure in toolset + core. Plus a real prompt-build test stays green.
