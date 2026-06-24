# Self-Challenge — design spec

> Date: 2026-06-24 · Status: approved, implementing

## Goal
During the offline sleep cycle, Janus generates verifiable practice tasks aimed at
its **known weaknesses**, attempts them in a sandbox, and turns
**deterministically-verified** successes into **quarantined skill drafts** — growing
the skill graph with self-validated procedures. No LLM-judge. Default OFF.

This is the SCA / AgentEvolver "Code-as-Task" pattern adapted to Janus's safety
model (quarantine + verifiable reward + dialectic admission gate).

## Pipeline (`agent/self_challenge.py`) — best-effort, never raises
1. **Seed** — `gap_seeker.identify_gaps()`: topics where the agent repeatedly
   struggles. (No gaps → no-op.)
2. **Generate** — `generate_challenge(gap, *, llm_caller)` → a Code-as-Task
   `{instruction, checks}` where `checks` are DETERMINISTIC assertion specs reusing
   the eval framework's check types (final_contains / tool_used / equals / regex —
   never subjective). One aux model call.
3. **Attempt** — `attempt_runner(instruction)` runs the task as a RESTRICTED
   sandboxed subagent. INJECTABLE: tests inject a fake. The production default
   (`_default_attempt_runner`) is **safe-by-default** — executing a self-generated
   task is only safe inside an isolated environment (the offline sleep cycle has no
   human to approve a shell command), so it runs ONLY when an isolated execution
   backend is configured (`terminal.backend` = docker/modal/daytona/singularity/ssh,
   or an explicit `self_challenge.sandbox`); on `local` it REFUSES (returns an empty,
   non-passing result — the round drafts nothing). Returns `{final_response,
   messages}`.
4. **Verify** — `verify_result(result, checks)` → bool. Deterministic only (the
   verifiable reward). No model call.
5. **Promote** — on PASS: draft a QUARANTINED skill from the winning trajectory
   (reuse `skill_miner` draft path → `skills/.drafts/`, tagged `source:
   self-challenge`); it then flows through the existing verifiable-reward +
   dialectic admission gate. On FAIL: record a lesson (`lessons`).
6. **Orchestrate** — `run_self_challenge(*, llm_caller, attempt_runner, config)`:
   seed → for up to `max_per_cycle` gaps: generate → attempt → verify → promote.
   Returns a report `{attempted, passed, drafted, lessons, error}`.

## Sleep integration
New gated step `maybe_run_self_challenge` called from `run_sleep_cycle` (after ACE
playbook curation), wired with the real `attempt_runner`. Capped at
`max_per_cycle`; counts added to the sleep report.

## Safety (load-bearing)
- Default **OFF** (`self_challenge.enabled`).
- **Sandboxed** attempt: the default backend executes ONLY inside an isolated
  environment (`terminal.backend` docker/modal/daytona/singularity/ssh). `sandbox:
  "auto"` defers to that backend and refuses on `local` — it never runs
  self-generated commands on the host. Approval + path-security still apply.
- **Verifiable reward only** — deterministic checks, never LLM-as-judge.
- **All output quarantined** — drafts to `.drafts/`, never auto-applied; pass the
  existing dialectic + verifiable-reward gate before promotion.
- **Capped** — `max_per_cycle`, `max_iterations`, time + token budget.
- Offline only; best-effort; never raises into the sleep cycle.

## Config
`self_challenge: {enabled: false, max_per_cycle: 2, sandbox: "auto", max_iterations: 30}`

## Reuses
gap_seeker · eval assertion checks · delegate_task + environments · skill_miner ·
skill_verifier + skill_graph · dialectic gate · sleep · lessons.

## Testing
Each stage unit-tested with an injected `llm_caller` and a FAKE `attempt_runner`
(no live model / no live sandbox in tests): generate parses the Code-as-Task; verify
runs the deterministic checks (pass + fail); promote drafts on pass / records a
lesson on fail; orchestrator caps at `max_per_cycle` and is gated; sleep step gated
+ counted; everything best-effort (never raises). Invariant-style, no snapshots.

## YAGNI cuts (v1)
No difficulty curriculum, no fine-tuning, no curiosity-driven generation
(gap-seeded only), no auto-promotion (quarantine + existing gate).
