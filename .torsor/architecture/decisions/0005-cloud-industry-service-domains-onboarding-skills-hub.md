---
type: decision
status: accepted
tags:
- adr
links: []
created: '2026-06-15T16:37:29'
updated: '2026-06-15T16:37:29'
rules:
- kind: forbid_pattern
  target: setup.github.com
  scope: '*.py'
  message: "Broken service URL from the rebrand sweep \u2014 the onboarding host is\
    \ setup.cloud-industry.com, not the code repo. See ADR cloud-industry-service-domains"
  severity: error
- kind: forbid_pattern
  target: github.com/magnetoid/janus/api
  scope: '*.py'
  message: "github.com is the code repo, not an API host \u2014 use a cloud-industry.com\
    \ service domain. See ADR cloud-industry-service-domains"
  severity: error
---

# ADR 0005: Cloud Industry service domains (onboarding, skills hub)

## Context
The brand-rebrand sweep rewrote a protected service domain (hermes-agent.nousresearch.com) to the code-repo path github.com/magnetoid/janus, which broke two live services: the managed Telegram onboarding pairing API (originally setup.hermes-agent.nousresearch.com, a Cloudflare Worker) became https://setup.github.com/magnetoid/janus, and the curated skills index (originally hermes-agent.nousresearch.com/docs/api/skills-index.json) became github.com/magnetoid/janus/api/skills-index.json. github.com serves neither endpoint, so managed Telegram setup returned 'Could not reach the onboarding service' and the skills index 404'd. The user is standing up Cloud Industry's own services rather than depending on Nous's, and wants the brand's canonical service domains recorded so future sweeps don't re-break them. Note: the broader skills system does NOT depend on this index — it also pulls from skills.sh (~20k community skills), any GitHub repo, and direct SKILL.md URLs, plus bundled and local skills — so the curated index is an optional featured catalog.

## Decision
Cloud Industry's own services live on cloud-industry.com subdomains. Canonical service hosts: setup.cloud-industry.com (Telegram managed-onboarding pairing API; overridable via the TELEGRAM_ONBOARDING_URL env var) and skills.cloud-industry.com (curated skills index; overridable via the JANUS_SKILLS_INDEX_URL env var). SERVICE/API/script URLs must point at a real service host — NEVER at the code-hosting repo (github.com/magnetoid/janus is source, not an API). The rebrand sweep must not rewrite service domains to the repo URL; treat cloud-industry.com service hosts the way nousresearch.com service domains were protected. Until the services are built, the defaults are unreachable and the manual fallbacks apply (paste a BotFather token for Telegram; skills.sh / GitHub / local skills for the hub).

## Consequences
Managed onboarding and the curated skills index point at Cloud Industry infrastructure to be built; both degrade gracefully (manual Telegram setup; alternate skill sources) until then. Guard rules flag any reintroduction of the repo-path service URLs so this class of regression can't silently return.
