---
sidebar_position: 4
title: "Evals"
description: "Replayable behavior regression checks — verify the agent actually improved after a skill, memory, or config change"
---

# Evals

`janus evals` is a behavior regression harness: a suite of recorded prompts with deterministic checks against the agent's response and tool usage. Run it before and after a change — a new skill, a memory provider swap, a model switch, enabling the [dialectic gate](/user-guide/features/deliberation) — and the diff tells you whether the agent actually got better or quietly regressed.

It closes the measurement gap in the self-learning loop: [memory mining](/user-guide/features/memory), [skill mining](/user-guide/features/skills), and the [curator](/user-guide/features/curator) all *change* the agent, but nothing verified the changes helped.

## Quick start

```bash
janus evals init      # scaffold starter specs into ~/.janus/evals/
janus evals list      # show discovered specs
janus evals run       # run the suite, exit 1 on any failure
janus evals results   # show the latest saved results
```

`init` writes a starter suite including the dialectic validation pair (see below). Edit them, add your own, re-run.

## Writing a spec

Specs are YAML files in `~/.janus/evals/` (or any path passed to `run`/`list`). One spec per file, or several under an `evals:` list:

```yaml
name: knows-test-runner
prompt: "What test runner does this project use? One sentence."
checks:
  - type: contains
    value: pytest
  - type: tool_not_called
    value: terminal
```

| Field | Default | Meaning |
| --- | --- | --- |
| `name` | required | Unique id across the suite |
| `prompt` | required | The user message sent to a fresh agent |
| `checks` | required | Non-empty list, all must pass |
| `system` | — | Custom system prompt |
| `toolsets` | configured default | Toolsets the eval agent gets (e.g. `[moa]`) |
| `model` / `provider` | configured default | Per-spec override |
| `max_iterations` | 15 | Tool-call budget |
| `use_memory` | `false` | Hermetic by default; set `true` when the eval is *about* memory |
| `use_context_files` | `false` | Same, for SOUL.md/AGENTS.md context |

**Check types:** `contains`, `not_contains`, `regex`, `min_length`, `max_length` (against the final response), `tool_called`, `tool_not_called` (against the tool-call trace). String checks are case-insensitive unless `case_sensitive: true`.

## Running

```bash
janus evals run                       # everything in ~/.janus/evals/
janus evals run path/to/specs/        # a different file or directory
janus evals run --filter dialectic    # name substring filter
janus evals run --model gpt-5.5       # same suite, different model — instant A/B
```

Each eval runs in a fresh `AIAgent` with trajectories off and (by default) memory and context files skipped, so results are reproducible. Results are appended as JSONL to `~/.janus/evals/results/<timestamp>.jsonl`; the exit code is non-zero when anything failed, so the suite drops straight into CI or a cron job.

## The workflow that matters

1. `janus evals init`, curate a handful of specs that encode what *your* agent must reliably do.
2. Run the suite to get a baseline.
3. Make the change (enable the dialectic gate, install a skill, switch models).
4. Run again. Investigate any flip — in either direction.

A failing eval is information either way: the agent regressed, or the spec encoded an assumption you've deliberately changed. Update whichever is wrong.

:::tip Don't write change-detector evals
Pin *behavior* ("the answer names pytest"), not artifacts ("the answer is exactly this sentence"). Exact-match specs break on every harmless rephrase and train you to ignore failures.
:::
