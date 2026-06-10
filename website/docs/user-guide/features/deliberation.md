---
sidebar_position: 5
title: "Dialectic Deliberation"
description: "Two-headed adversarial reasoning — an on-demand deliberate tool, and an opt-in red-team gate on the self-learning loop"
---

# Dialectic Deliberation

Janus is the two-faced god, and this feature makes that literal: stage the strongest honest disagreement about a question or a learned artifact, then let an arbiter rule on the stronger **argument** — never the majority.

It complements the other deliberate-spend reasoning tools:

| Tool | Shape | Catches |
| --- | --- | --- |
| `mixture_of_agents` | **Breadth** — many models, one pass, aggregate | Single-model blind spots, by averaging |
| `deep_reason` | **Depth** — one model, critique-and-retry | First-pass sloppiness |
| `deliberate` | **Opposition** — advocate vs opponent, arbiter rules | **False consensus** — confident answers that collapse under a real adversary |

Averaging correlated witnesses (models trained on overlapping data agree for reasons unrelated to truth) makes you *feel* certain without being right. Opposition is the corrective: a conclusion that survives a genuine adversary is load-bearing.

The full design rationale lives in `plans/dialectic-learning-gate.md` in the repo.

## The `deliberate` tool (on demand)

Enable the `moa` toolset (`janus tools` — it's off by default), then ask in any chat:

> "Use the deliberate tool: should we migrate the gateway to async-only?"

Three auxiliary-model calls run:

1. **Advocate** — commits to the strongest defensible answer, no hedging.
2. **Opponent** — argues the strongest *honest* counter-case: a different answer, a framing under which the answer flips, or the sharpest objection. If the advocate is simply right, it formally `CONCEDE`s.
3. **Synthesizer** — rules on the stronger argument and emits a structured verdict.

Reading the verdict:

- **`answer`** — the synthesis. When **`frame_dependent: true`**, the answer states *both frames and what each depends on*. This is the glass-half-full case: when both framings are honestly valid, reporting frame-dependence **is** the truthful answer — not a failure to decide.
- **`crux`** — the single load-bearing consideration. If the crux looks wrong to you, distrust the whole verdict.
- **`dissent`** — the strongest objection that *survived*. Your residual risk; read it even when you accept the answer.
- **`conceded: true`** — the opponent found no honest counter-case. The most trustworthy verdicts.

Use it for judgment calls, contested claims, and decisions where a wrong confident answer is costly. Don't use it for lookups or arithmetic — the opponent will just concede and you've spent three calls.

### Putting the heads on different models

Two calls to the same model share blind spots. Pin the stances to different model families via the standard [auxiliary model](/user-guide/configuration) machinery:

```yaml
auxiliary:
  dialectic_skeptic: {provider: openrouter, model: qwen3-coder}
  dialectic_arbiter: {provider: anthropic, model: claude-sonnet-4-6}
  # dialectic_advocate falls back to your default auxiliary model
```

## The learning red-team gate (opt-in)

The self-learning loop is single-witness by default: one LLM pass decides what becomes a permanent memory, a skill draft, or a success label — and whatever gets in **compounds** across every future session. The gate makes admission adversarial.

It is **off by default** — a feature to test and validate, not permanent behavior:

```yaml
# config.yaml
memory:
  session_mining: true        # the gate filters what mining produces,
skills:
  session_mining: true        # so mining itself must be on
learning:
  track_outcomes: true
  dialectic:
    enabled: true             # ← master switch
    memory: true              # per-path toggles (these are the defaults)
    skills: true
    outcomes: true
```

With it on, at session end:

- **Mined facts** must survive a batched advocate → skeptic → arbiter exchange before reaching the memory store. The skeptic checks for the classic failure: a session-scoped instruction ("use port 8080 *for this demo*") phrased as a permanent fact. The arbiter can also **revise** — narrow an overbroad claim instead of dropping it. Rejected facts are never silently destroyed: they're logged with the skeptic's objection (`janus logs`, grep `red-team rejected fact`).
- **Skill drafts** are all still written to `~/.janus/skills/.drafts/` — drafts are *your* review quarantine — but rejected ones carry the objection as a flag. Read the flag first when reviewing.
- **Session outcomes** are labeled by a quorum of two opposed judges (charitable: "did it materially advance the goal?" vs strict: "fully done, no unresolved errors?"). Only agreement produces a label; disagreement records honestly as "unclear" instead of one judge's coin flip polluting skill success-rate trajectories.

**Cost is bounded by design:** all of a session's facts ride in 3 batched calls (not 3 per fact), outcomes cost 2, everything runs on auxiliary models, and it all happens post-session — the live conversation's prompt cache is never touched. Infrastructure errors always fail open to today's behavior; a real arbiter rejection is never overridden.

### Validating it

Watch two signals during the trial period:

1. **Wrong rejections** — good facts being blocked means the skeptic prompt is too aggressive.
2. **Contested rate** on outcomes — expect roughly 10–25%; above ~40% means the strict judge is too harsh.

`janus evals init` scaffolds a validation suite (see [Evals](/user-guide/features/evals)) including the frame-dependence pair: a question that *should* flag `frame_dependent` and one that shouldn't. Run the eval suite before enabling the gate and again after a week — that diff is your evidence.
