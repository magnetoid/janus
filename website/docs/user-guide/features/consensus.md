---
sidebar_position: 100
title: "Consensus / Smart Model Routing"
description: "Route each task to the right-cost model — cheap for simple work, an ensemble of top models for the hardest — to save tokens and lift quality"
---

# Consensus / Smart Model Routing

Not every task needs your most expensive model. **Consensus routing** sends each
task to the *right-cost* model: the cheapest model that can do simple work, a
strong model for hard work, and — for the genuinely hardest problems — an
**ensemble** of top models whose answers are synthesized into one. You save
tokens on easy work and get better answers on hard work.

It is **opt-in** (off by default) and **cache-safe by design**: routing decides
which model to use at *task entry* (a `consensus` tool call or a delegated
subtask), never mid-conversation — so it never breaks the prompt cache.

## How it routes

1. **Classify complexity** — a *free local heuristic* (`agent/task_complexity.py`)
   scores the prompt `simple` / `mid` / `hard` from length, keywords, and
   code/math signals. No token is spent to classify — that would defeat the
   savings. (Set `consensus.complexity_mode: "model"` to escalate only the
   ambiguous `mid` band to a cheap model.)
2. **Pick a tier** — `simple → cheap`, `mid → mid`, `hard → smart`
   (`consensus.model_tiers`). An empty tier inherits your main model.
3. **Ensemble the hardest** — when `consensus.ensemble.enabled` is on, a `hard`
   task is answered by several strong models (chosen from the
   [model-strengths KB](#) for that task category) and synthesized via the
   `mixture_of_agents` tool.

## Set it up

During the wizard:

```bash
janus setup
```

Enable consensus in the **Consensus Routing** section and set a cheap + smart
model (leave blank to inherit your main model), and the ensemble toggle.

Or by hand:

```bash
janus config set consensus.enabled true
janus config set consensus.model_tiers.cheap.model <a fast/cheap model id>
janus config set consensus.model_tiers.smart.model <a strong model id>
```

## CLI

```bash
janus consensus status          # show tiers, ensemble, on/off
janus consensus route "<text>"  # show how a prompt would route — FREE, no model call
janus consensus run "<text>"    # answer a prompt through consensus routing
```

`route` is free — it classifies and shows the chosen tier/model without calling
a model — so you can sanity-check routing before turning it loose.

## The agent tool

When enabled, the agent gets a `consensus` tool (`consensus` toolset). It can
hand a sub-question to the right-cost model itself — using a cheap model for an
easy lookup and the ensemble for a hard sub-problem — which is how the agent
saves tokens on its own multi-step work.

## Config reference

```yaml
consensus:
  enabled: false
  complexity_mode: heuristic   # heuristic (free) | model
  model_tiers:
    cheap:  { provider: "", model: "" }   # simple work
    mid:    { provider: "", model: "" }   # the default
    smart:  { provider: "", model: "" }   # hard work + ensemble members
  ensemble:
    enabled: false
    min_complexity: hard
    member_count: 3
```

Status is also surfaced on the dashboard's **Learning** page.
