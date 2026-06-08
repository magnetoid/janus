---
type: decision
status: accepted
tags:
- adr
links: []
created: '2026-06-08T02:05:59'
updated: '2026-06-08T02:05:59'
rules:
- kind: forbid_pattern
  target: Hermes Agent
  scope: '*.py'
  message: "Brand string 'Hermes Agent' must be 'Janus' \u2014 see ADR rebrand-hermes-agent-janus"
  severity: warning
---

# ADR 0002: Rebrand Hermes Agent → Janus (project-wide)

## Context
Project goal: rename the agent from "Hermes Agent" (Nous Research) to "Janus" everywhere, and build a "best of both" combining Hermes and OpenClaw. This is a ~2026-file repo with ~4,500 references to "hermes" across 3 distinct layers: (1) user-facing display branding — safe; (2) hard runtime identity — `~/.hermes` config dir, `HERMES_HOME` env var, `get_hermes_home()`, the `hermes-agent` package, `hermes`/`hermes-agent`/`hermes-acp` CLI entry points, and python modules `hermes_cli`/`hermes_constants`/`hermes_state` — breaking these orphans every existing install's data; (3) docs/metadata + external URLs (hermes-agent.nousresearch.com, github.com/NousResearch). The repo is NOT under version control, so a blind global sed has no undo.

## Decision
Do the rebrand as a STAGED, case-preserving, scripted rename on top of git — never a naive `sed s/hermes/janus/g`. Stages: (0) git init as a safety net before any mass edit; (1) user-facing display branding (skin_engine default branding, banner, welcome/goodbye/response_label) — what makes it "named Janus"; (2) docs/README/metadata; (3) runtime identity rename WITH back-compat shims: introduce JANUS_HOME but keep reading HERMES_HOME as a fallback, add a `janus` CLI entry alongside `hermes`, migrate `~/.hermes`→`~/.janus` with a one-time migration. EXCLUDE from replacement: external URLs, the OpenClaw→Hermes migration code paths, and third-party identifiers. Preserve case variants (Hermes/hermes/HERMES). Verify with scripts/run_tests.sh between stages.

## Consequences
Slower than a one-line sed, but reversible and non-breaking. Existing installs keep working via back-compat shims during the identity rename. The drift rule below flags any reintroduction of the "Hermes Agent" brand string in new Python code; until the rename completes it will also flag remaining occurrences, which is the desired progress signal.
