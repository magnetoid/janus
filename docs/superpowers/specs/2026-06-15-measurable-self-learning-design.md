# Measurable Self-Improvement — Design Spec

**Date:** 2026-06-15
**Status:** Approved (brainstorming) — pending implementation plan
**Owner:** Janus / Cloud Industry

## Goal

Make Janus a *measurably* self-improving agent: every learning write it makes
(memory fact, skill, lesson, playbook entry) becomes provable — a trustworthy,
game-resistant eval curve trends up over real use, and any learning feature that
does not move the curve is rejected.

This is **Approach C (hybrid)**: a thin longitudinal measurement spine built on
the existing `agent/evals.py` harness, shipped together with one paired learning
feature (write-time memory reconciliation) so capability and proof arrive
together.

## Success criteria

1. A **learning curve** exists: suite pass-rate over time, persisted and graphed,
   derived from deterministic checks (not LLM judgment).
2. The benchmark is **self-growing**: agent failures generate candidate eval
   pins (quarantined, user-reviewed) so the suite grows to cover exactly what the
   agent should have learned.
3. Every learning feature has an **A/B delta**: suite pass-rate with the feature
   ON vs OFF, so improvement is *attributable*, not assumed.
4. The first paired feature (write-time memory reconciliation) is validated by
   dedicated seeded-memory reconciliation evals (a constructed contradiction the
   reconcile must resolve), unit tests of each decision, and a token-savings
   measurement — not merely assumed.

## Constraints (locked during brainstorming)

- **Success = measurable self-improvement** — trustworthy, instrumented, not
  vibes. The central risk to defend against is *self-measurement that trends up
  while quality degrades* (model collapse / reward hacking; RAGEN 2504.20073).
- **No fine-tuning** — hosted models only; learn at the memory / skill / lesson /
  retrieval / orchestration level. No training infra, no GPUs.
- Must honor existing loop invariants: best-effort (never raises), injectable
  `llm_caller`, config-gated default-off, prompt-cache safe.
- Build on what exists. `agent/evals.py` is the measurement substrate — extend,
  do not duplicate.

## Existing substrate (reused, not rebuilt)

- `agent/evals.py` — replayable, **hermetic**, **deterministic** eval harness.
  `EvalSpec` (prompt + checks), `run_evals(specs, agent_runner=…)` with an
  **injectable runner**, deterministic check types (`contains`, `not_contains`,
  `regex`, `min_length`, `max_length`, `tool_called`, `tool_not_called`),
  results appended to `$JANUS_HOME/evals/results/<ts>.jsonl`. Specs opt into
  `use_memory: true` when the eval is *about* memory behavior.
- `agent/outcome_tracker.py` — Tier 1 `learning_metrics()` (forward/backward
  transfer, forgetting, **diversity/entropy** collapse early-warning).
- `agent/lessons.py` — Tier 1 Reflexion write-back (failure → lesson).
- `agent/memory_gardener.py` — contradiction reconciliation (currently
  weekly-sleep only).
- `agent/memory_miner.py` — session-end fact distillation.

## Architecture

A closed loop with three spine components and one paired feature.

### Component 1 — Longitudinal eval runner (spine)

**New:** `agent/eval_trend.py`.

- `run_trend(specs=None, agent_runner=None, save=True) -> dict` — calls
  `run_evals`, then appends a compact record to `$JANUS_HOME/evals/trend.jsonl`:
  `{ts, pass_rate, total, passed, per_eval: {name: bool}, suite_hash}`.
  `suite_hash` is a stable hash of the loaded spec set so curve points are only
  compared across the same suite version.
- `learning_curve(window=None) -> dict` — reads `trend.jsonl`, returns the
  pass-rate time series plus **per-eval trajectories**: which evals flipped
  `fail→pass` (learned) and `pass→fail` (regressed/forgot) between the first and
  latest run of the current `suite_hash`.
- `maybe_run_trend(...)` — schedule gate (interval + enabled), mirroring
  `sleep.maybe_run_sleep`. Wired into the sleep cycle and/or gateway cron.
- Gated by `evals.trend.enabled` (default false), `evals.trend.interval_hours`.

### Component 2 — Failure → regression-pin generator (self-growing benchmark)

**New:** `agent/eval_miner.py`.

- `draft_eval_from_failure(messages, lesson=None, *, llm_caller=None, …) ->
  Optional[EvalSpec]` — from a failed transcript (and its Tier 1 lesson), draft
  an `EvalSpec`: a prompt that re-creates the situation + **deterministic checks**
  capturing "next time this should happen." Best-effort, injectable, never raises.
- `write_eval_draft(spec, drafts_dir=None) -> Path` — writes YAML to
  `$JANUS_HOME/evals/.drafts/` (auto-suffix on name clash), **never** to the live
  suite. The `.drafts/` directory is excluded from `load_eval_specs` (which
  already skips dotfiles; `.drafts` is a dot-dir under `evals/` and not globbed).
- Hooked into `agent/auto_mine.py` alongside the Tier 1 lesson write, on a
  classified failure, gated by `evals.autopin` (default false).
- **Anti-gaming:** drafts are user-reviewed before being moved into the live
  suite — the agent cannot inflate its own curve.

### Component 3 — A/B feature gate (trustworthy attribution)

**New:** `compare_feature(flag, specs=None, agent_runner=None) -> dict` in
`agent/eval_trend.py`.

- Runs the suite twice — once with the named learning flag forced ON, once OFF —
  via a config override threaded into the (hermetic) runner. Returns
  `{flag, pass_rate_on, pass_rate_off, delta, per_eval_delta}`.
- A feature is "real" only if `delta` clears a small noise threshold.
- Two flag classes: **inference-time** flags (e.g. lesson injection, future ACE
  playbook, adaptive dialectic) flip agent behavior within the hermetic run and
  A/B cleanly against the generic suite. **Write-time** flags (memory
  reconciliation) change what gets *written*, so their A/B uses purpose-built
  **seeded-memory** eval scenarios: pre-seed a contradictory memory state, run
  the mining step with the flag ON vs OFF, then a `use_memory` eval whose correct
  answer depends on the stale fact being reconciled away. The gate is the same;
  the eval scenario is what differs.
- Exposed via `janus evals ab <flag>` and surfaced on the dashboard.

### Component 4 — Paired feature: write-time memory reconciliation

**Modified:** `agent/memory_miner.py` (+ reuse `agent/memory_gardener.py`).

- Promote reconciliation from weekly-sleep-only to a **write-time** decision. For
  each candidate fact, classify against existing memory: `ADD` (new), `UPDATE`
  (supersedes an existing fact — replace it), `DELETE` (contradicts an existing
  fact — remove the stale one), `NOOP` (already known, skip).
- Implemented as `reconcile_candidate(candidate, existing, *, llm_caller=…) ->
  {action, target_index?, revised?}`; `mine_session_memory` applies the action
  via the existing `MemoryStore` add/replace/remove API.
- Gated by `memory.write_time_reconcile` (default false). When off, current
  add-only behavior is unchanged.
- **Why first:** biggest quality + token win (kills stale-memory rot, Mem0
  reports >90% token savings vs full-context), and the cleanest target for a
  seeded-memory A/B scenario, so the spine proves a real feature immediately.

### Component 5 — Dashboard surface

**Modified:** `janus_cli/routers/learning.py` + `web/src/pages/LearningPage.tsx`.

- Extend `/api/learning/stats` (or a new `/api/learning/curve`) with the learning
  curve series, per-eval flip status, and A/B deltas for enabled features.
- LearningPage gains a "Learning curve" card (pass-rate sparkline over time),
  a per-eval flip list (learned / regressed), and pending draft-pin count.

## Data flow

```
session ends ─▶ classify (Tier 1)
   ├─ failure ─▶ lesson (Tier 1) + DRAFT eval pin (eval_miner) ─▶ evals/.drafts/
   │                                          └─ user review ─▶ evals/ (live suite)
   └─ memory candidates ─▶ write-time reconcile (ADD│UPDATE│DELETE│NOOP)
sleep / cron tick ─▶ eval_trend.run_trend() ─▶ trend.jsonl ─▶ learning_curve()
feature toggle ─▶ eval_trend.compare_feature(flag) ─▶ delta ─▶ admit / reject
dashboard ◀─ curve + per-eval flips + A/B deltas + draft-pin count
```

## Trust / anti-gaming (defends the success criterion)

- **Deterministic checks** — ground-truth signal can't drift like LLM-judged
  outcome classification.
- **Quarantined auto-pins** — user review prevents the agent inflating its own
  curve with trivial evals.
- **Hermetic runs** — learning evals opt into `use_memory` explicitly, isolating
  what each eval tests.
- **Diversity/entropy monitor** (Tier 1) stays as the collapse early-warning:
  curve up + diversity down ⇒ investigate.
- **Suite-hash gating** — curve points are only compared within the same suite
  version, so adding evals doesn't create phantom regressions.

## Error handling

- Every new module best-effort, never raises (loop invariant).
- An eval that errors counts as a fail; the suite continues (existing behavior).
- A failed draft-gen yields no draft (like skill mining).
- All new paths config-gated, default-off (eval runs spend model calls).

## Testing

- `eval_trend.run_trend` / `compare_feature` — tested with a fake `agent_runner`
  (no live model), asserting curve records, flip detection, and delta math.
- `eval_miner.draft_eval_from_failure` — injected `llm_caller`, deterministic
  draft + quarantine-path assertions.
- `reconcile_candidate` — one unit test per action (ADD/UPDATE/DELETE/NOOP) with
  injected `llm_caller`; plus an integration test that `mine_session_memory`
  applies UPDATE/DELETE against a seeded `MemoryStore`.
- A seeded-memory **A/B scenario** eval (the contradictory-fact pair) exercising
  `compare_feature("memory.write_time_reconcile")` end to end with a fake runner.
- Dashboard endpoint — `TestClient` over the extended router.
- All via `scripts/run_tests.sh`.

## Config keys (new)

| key | default | purpose |
|---|---|---|
| `evals.trend.enabled` | `false` | run the suite on a schedule, record the curve |
| `evals.trend.interval_hours` | `24` | min hours between scheduled trend runs |
| `evals.autopin` | `false` | failure → draft regression-pin generation |
| `memory.write_time_reconcile` | `false` | ADD/UPDATE/DELETE/NOOP at write time |

## Scope

**In:** the measurement spine (Components 1–3), the paired feature (Component 4),
the dashboard surface (Component 5), tests, config.

**Out (deferred to later increments, each admitted via the A/B gate):** ExpeL
cross-task insight extraction, ACE-style evolving playbook, adaptive
(uncertainty-triggered) dialectic, time-weighted skill trajectories. Explicitly
not part of this spec — keeps it to a single implementation plan.

## File manifest

- New: `agent/eval_trend.py`, `agent/eval_miner.py`
- New tests: `tests/agent/test_eval_trend.py`, `tests/agent/test_eval_miner.py`,
  `tests/agent/test_memory_reconcile.py`
- Modified: `agent/memory_miner.py`, `agent/auto_mine.py`,
  `janus_cli/evals.py` (CLI: `ab`, `trend` subcommands),
  `janus_cli/routers/learning.py`, `web/src/pages/LearningPage.tsx`,
  `janus_cli/config.py` (new keys), `janus_cli/main.py` (subcommand registry if
  needed), `tests/janus_cli/test_dashboard_learning_endpoints.py`
