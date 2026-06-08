---
type: decision
status: accepted
tags:
- adr
links: []
created: '2026-06-08T02:34:30'
updated: '2026-06-08T02:34:30'
rules:
- kind: forbid_pattern
  target: Nous Research
  scope: '*.py'
  message: "Company brand 'Nous Research' must be 'Imba Labs' \u2014 see ADR brand-taxonomy"
  severity: warning
---

# ADR 0003: Brand taxonomy: Imba Labs (company) + Janus (agent)

## Context
Extends ADR 0002. User clarified the rebrand has two brand axes: the COMPANY 'Nous Research' becomes 'Imba Labs', and the AGENT 'Hermes Agent' becomes 'Janus'. Both source brands are overloaded with real external products/services that must NOT be renamed or live integrations break: on the Hermes side — the Nous 'Hermes' LLM model family (hermes-3-405b, hermes-3-70b, Hermes-4-70B, nous-hermes-*); on the Nous side — 'Nous Portal' (real inference service), the 'nous' provider slug, the nousresearch.com domain (incl portal./api. subdomains), and the NousResearch GitHub org handle. Surface scale: ~674 NousResearch, 538 Nous Portal, 530 'nous' slug, 433 nousresearch.com, 197 'Nous Research', plus ~2873 files containing 'hermes'.

## Decision
Rename only unambiguous BRAND/IDENTITY tokens, case-preserving, with real products PROTECTED: (a) Agent: hermes→janus for python modules, env vars (HERMES_*), config dir (~/.hermes), package, CLI entries, and 'Hermes Agent'/'Hermes' brand prose — PROTECT hermes-N / nous-hermes model IDs. (b) Company: 'Nous Research'/'Nous research' → 'Imba Labs' — PROTECT 'Nous Portal' product name, the 'nous' provider slug, nousresearch.com domains, and the NousResearch GitHub org. Service/URL/domain/repo repointing (e.g. hermes-agent.nousresearch.com docs URL, github.com/NousResearch/hermes-agent) is deferred until the user provides Imba Labs' own domain/org/repo — renaming them now would only create dead links.

## Consequences
Brand-complete in code and prose while keeping every live integration (Nous Portal, provider slug, model catalog, update-check) functional. A follow-up pass repoints domains/URLs/repo once Imba Labs infra exists.
