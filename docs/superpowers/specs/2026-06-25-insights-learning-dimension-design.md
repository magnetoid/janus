# Design: `janus insights` — Learning Dimension ("Janus Insights" v1)

> **Status:** Approved design (Approach A + sleep-log append), pre-implementation.
> **Date:** 2026-06-25
> **Author:** design via brainstorming; metrics verified against the working tree.

## Problem

Janus's headline differentiator is a **closed learning loop** — mining, reflexion, dialectic admission gates, the ACE playbook, eval regression pinning. But the payoff is currently **asserted, never measured**. Two independent strategic docs name observability the #1 credibility gap, and a source audit confirmed there is no machine-readable export and no surfaced "is the loop working?" view.

The existing `agent/insights.py` (`InsightsEngine`, ~39 KB) already does **usage** analytics — tokens, cost, model/platform breakdown, which tools and skills were *invoked*, activity patterns, top sessions — rendered to terminal and gateway. It reads only `SessionDB` (SQLite). It does **not** read the learning stores and so says nothing about whether the agent is *improving*.

## Goal

Add a **Learning dimension** to the insights surface that answers "is the loop actually working?", exposed in one pass as **both** a human-readable terminal report **and** a `--json` export from the same computed object. Out of scope for v1: OTLP/Prometheus exporters, a `/metrics` HTTP endpoint, the hosted dashboard (these are follow-ons that consume the v1 JSON).

## Non-goals (v1)

- No new network surface or daemon. No OpenTelemetry/Prometheus dependency.
- No changes to `InsightsEngine`'s existing usage analytics behavior.
- No new top-level command; reuse the existing `insights` command/slash/gateway plumbing.

## Architecture — Approach A: standalone aggregator, composed at the edge

A new module **`agent/learning_insights.py`** owns the learning metrics. It is composed into the `insights` command alongside the existing usage report, rather than bolted into the SQLite-bound `InsightsEngine`.

```
insights command/slash handler
   ├─ InsightsEngine(db).generate(days, source)      → usage report   (unchanged)
   └─ learning_insights.generate_learning_report(...) → learning report (new)
        reads file-based learning stores in get_janus_home()
```

**Rationale:** `InsightsEngine` is bound to `db._conn`; the learning data is file-based JSON/JSONL in `janus_home`. Mixing data sources into a 39 KB SQLite-bound class bloats it and risks the working usage analytics. A separate, pure aggregator keeps each unit independently testable and leaves `InsightsEngine` untouched.

*Rejected:* (B) extend `InsightsEngine` directly — couples two data sources, regression risk; (C) a new `janus learning insights` command — splits "insights" across two surfaces, more wiring, no gain.

## Module contract

```python
# agent/learning_insights.py
def generate_learning_report(
    *, home: Path | None = None, days: int = 30,
) -> dict:
    """Aggregate the learning-loop metrics into a report dict.

    Pure, best-effort, NEVER raises. Paths injectable via `home` (defaults to
    get_janus_home()). Each metric is independently guarded — a missing or
    unreadable store yields an empty/null series, not an exception. Honors the
    same config gate as the rest of the learning loop where applicable.
    """
```

Matches the established learning-module pattern (pure, injectable, config-gated, best-effort, never-raises) so it is unit-testable against a temp `JANUS_HOME` with no model calls.

## Data sources & metrics (all verified to exist)

| Metric (report key) | Source module / store | Computation |
|---|---|---|
| `eval.pass_rate_trend` | `eval_trend.trend_path()` → `evals/trend.jsonl` (`{ts, pass_rate, passed, total, per_eval{}}`) | time-ordered `(ts, pass_rate)` points; latest, delta vs first-in-window |
| `eval.per_eval_latest` | same | per-eval passed/total from the latest record |
| `outcomes.success_rate` | `outcome_tracker.load()` → `learning/outcomes.json` (`{success, skills[], persona, ts}`) | overall + windowed success rate within `days`; trend points |
| `outcomes.by_skill` | `outcome_tracker.skill_success_trajectory()` (exists) | per-skill recent success ratio |
| `outcomes.by_persona` | same store, group by `persona` | per-persona success rate |
| `mining.yield_trend` | **new** `learning/sleep_log.jsonl` (see below) | per-cycle `graduated_facts`/`graduated_skills`/`lessons`/`pruned` over time |
| `knowledge.counts` | `lessons.get_lessons_path()`, `playbook.get_playbook_path()`, `skills/`, `skills/.drafts/` | point-in-time sizes: lessons, playbook entries, active skills, **quarantined drafts** (graduation backlog) |

A fact/memory count is included **only if** the memory store exposes a cheap count API at implementation time; otherwise it is omitted rather than faked. Every other numeric is derived from data that already exists, except `mining.yield_trend`, which needs the one additive write below.

## The one new write: persist sleep-cycle reports

`agent/sleep.py` already builds a per-cycle `report` dict (`graduated_facts`, `graduated_skills`, `lessons`, `pruned`, `reconciled`) and then discards it. v1 appends each completed cycle's summary as one line to **`learning/sleep_log.jsonl`**:

```json
{"ts": "...", "graduated_facts": 3, "graduated_skills": 1, "lessons": 2, "pruned": 5, "dry_run": false}
```

- Additive, best-effort, guarded (a write failure must never fail the sleep cycle).
- `dry_run` cycles are tagged so they can be excluded from yield.
- Turns mining yield from a point-in-time snapshot into a trend. If absent (no cycles logged yet), `mining.yield_trend` is an empty series and `knowledge.counts` still shows current state — graceful degradation.

## Surface / CLI integration

Reuse the existing `insights` command (`CommandDef("insights", …, args_hint="[days]")`) and its slash + gateway handlers:

- `janus insights` / `/insights` → existing usage report **plus** a new **Learning** section.
- `janus insights --json` → `{"usage": {...}, "learning": {...}}` to stdout (valid JSON, no decorative text).
- `janus insights --learning` → Learning section only; `--usage` → usage only (back-compat default = both).
- Gateway: extend the existing `format_gateway` path with a compact Learning block (respect platform length limits).

The Learning terminal block renders: eval pass-rate (latest + arrow vs. window start), session success rate (windowed), mining yield (cycle totals in window), and knowledge-base counts with the **drafts-awaiting-review** backlog called out.

## Error handling

Best-effort throughout: the command must render usage analytics even if every learning store is missing. Each metric is computed in isolation and degrades to empty/null independently. No learning-store read may raise out of `generate_learning_report`. The `--json` path emits whatever was computed (with empty sections where data is absent).

## Testing (TDD)

Unit tests against fixture stores written into a temp `JANUS_HOME` (the `_isolate_janus_home` autouse fixture), asserting **invariants, not snapshots**:

- `outcomes.success_rate == successes / total` for a hand-built outcomes file; windowing excludes out-of-range `ts`.
- eval pass-rate series preserves input time order; latest/delta computed correctly.
- `mining.yield_trend` sums per-cycle fields; `dry_run` cycles excluded.
- missing/empty/corrupt store → empty series + **no raise** (one test per store, plus an "all stores absent" smoke test).
- `--json` output parses as JSON and the Learning numbers equal what the terminal renderer is given (single source of truth).
- a `sleep.py` test: a completed cycle appends exactly one well-formed `sleep_log.jsonl` line; a write failure does not propagate.

No change-detector tests (no asserting fixed counts of catalogs/config literals).

## Implementation surface (files)

- **new** `agent/learning_insights.py` — the aggregator + a `format_learning_terminal(report)` / compact gateway formatter.
- **edit** `agent/sleep.py` — append the cycle summary to `learning/sleep_log.jsonl` (guarded).
- **edit** the `insights` command handlers in `cli.py` (slash) and `janus_cli/main.py` (CLI subcommand) — compose the learning report, add `--json` / `--learning` / `--usage` flags.
- **edit** `gateway/run.py` insights handler — append the compact Learning block.
- **new** `tests/agent/test_learning_insights.py` (+ a sleep-log test in the existing sleep tests).

## Rollout

Pure read path + one additive, guarded write. No migration, no config-version bump. `mining.yield_trend` populates from the first sleep cycle after upgrade; everything else is live immediately against existing stores.
