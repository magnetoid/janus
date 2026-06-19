---
sidebar_position: 101
title: "ACE Playbook (self-tuning learning loop)"
description: "The one place Janus improves its own learning machinery — a red-team-gated, capped playbook of guidance the loop applies to its own prompts"
---

# ACE Playbook — the loop tunes its own prompts

Janus's self-learning loop mines memory, distills lessons, and mines skills using
**fixed** prompts written by developers. The **ACE playbook** is the one place
the loop improves *itself*: a small, curated set of learned guidance that is
prepended to the loop's own step prompts — so it gets better at *learning* over
time, not just at accumulating facts.

This is the closest Janus comes to *recursive* self-improvement — and it is
deliberately **bounded**. It is **off by default** and admits guidance only
through an adversarial gate, capped so it can never bloat or collapse.

## How it works (ACE: Generator → Reflector → Curator)

- **Generator** — in the offline sleep cycle, `propose()` reads the loop's recent
  activity and suggests a few short, concrete pieces of guidance (e.g. *"when
  mining memory, capture tool quirks AND versions"*), scoped to a loop step
  (`memory`, `lessons`, `skills`, `outcomes`, or `general`).
- **Reflector** — every proposal must survive the
  [dialectic red-team gate](deliberation.md) (advocate / skeptic / arbiter).
  Admission **fails closed**: if the reflector can't run, nothing is added.
- **Curator** — surviving guidance is merged into the playbook, **deduped**, and
  **pruned by score** to a hard cap (`learning.playbook.max_entries`). It is
  never collapsed into a lossy summary — each bullet stays discrete (ACE's
  anti-brevity rule).

At learning time, `augment_system()` prepends the relevant scope's guidance to
the step's system prompt (currently memory mining and lesson distillation). No
token is spent and nothing changes when the playbook is empty or disabled.

## Safety gates

The playbook edits the loop's own prompts, so it is conservative by design:

- **Off by default** (`learning.playbook.enabled`).
- **Fails closed** — no entry without a passing red-team verdict.
- **Capped** — bounded size prevents prompt bloat and context collapse.
- **Best-effort** — never raises into the agent loop; curation runs offline.

## Use it

```bash
janus config set learning.playbook.enabled true
janus learning playbook        # inspect the guidance the loop has learned
```

Guidance accrues during the offline sleep cycle (`janus sleep --now` to trigger
one). Status and per-scope counts are also shown on the dashboard's **Learning**
page.

## Config reference

```yaml
learning:
  playbook:
    enabled: false
    max_entries: 40
```
