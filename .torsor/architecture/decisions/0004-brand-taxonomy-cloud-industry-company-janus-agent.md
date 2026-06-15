---
type: decision
status: accepted
tags:
- adr
links: []
created: '2026-06-15T04:00:47'
updated: '2026-06-15T04:00:47'
rules:
- kind: forbid_pattern
  target: Imba Labs
  scope: '*.py'
  message: "Interim company brand 'Imba Labs' is retired \u2014 use 'Cloud Industry'\
    \ \u2014 see ADR brand-taxonomy-cloud-industry"
  severity: warning
- kind: forbid_pattern
  target: Nous Research
  scope: '*.py'
  message: "Company brand 'Nous Research' must be 'Cloud Industry' (PROTECT: 'nous'\
    \ provider slug, Nous Portal, nousresearch.com domains, NousResearch org, @nous-research/ui\
    \ package, Nous Hermes model IDs, LICENSE original copyright) \u2014 see ADR brand-taxonomy-cloud-industry"
  severity: warning
supersedes: 0003-brand-taxonomy-imba-labs-company-janus-agent
---

# ADR 0004: Brand taxonomy: Cloud Industry (company) + Janus (agent)

## Context
Supersedes ADR 0003. The interim company brand 'Imba Labs' is retired; the company is now 'Cloud Industry'. The agent remains 'Janus' (ADR 0002, unchanged). So the two standing brand mappings are: (1) agent 'Hermes Agent'/'Hermes' brand prose → 'Janus' (enforced by ADR 0002); (2) company 'Nous Research' and the now-retired 'Imba Labs' → 'Cloud Industry'. As in ADR 0003, both source brands overlap real external products that MUST NOT be renamed or live integrations break: on the Hermes side the Nous 'Hermes' LLM model family (hermes-3-*, Hermes-4-*, nous-hermes-*); on the Nous side the 'Nous Portal' inference service, the 'nous' provider slug, the nousresearch.com domains (incl. portal./inference-api. subdomains), the NousResearch GitHub org, and the '@nous-research/ui' workspace UI package the dashboard imports from. The LICENSE must also keep its original 'Copyright ... Nous Research' line (MIT requires preserving the original copyright); only the added fork-attribution line changes from 'Imba Labs' to 'Cloud Industry'.

## Decision
Rename unambiguous COMPANY brand/identity tokens case-preserving: 'Nous Research'/'Nous research' → 'Cloud Industry', and retire the interim 'Imba Labs' → 'Cloud Industry'. PROTECT (do not change): the 'nous' provider slug, 'Nous Portal' product name, nousresearch.com domains, the NousResearch GitHub org, the '@nous-research/ui' package import path, the Nous Hermes model IDs (hermes-N / nous-hermes-*), and the LICENSE original copyright line. Agent-axis rule (Hermes → Janus) stays as ADR 0002. Domain/URL/repo repointing remains deferred until Cloud Industry provides its own domain/org/repo (renaming now would only create dead links).

## Consequences
Brand-complete for the company axis in code while keeping every live integration (Nous Portal, provider slug, model catalog, dashboard UI package, update-check) functional. Guard rules flag any reintroduction of 'Imba Labs' or company-brand 'Nous Research' in *.py. A follow-up sweep updates non-.py prose (README, AGENTS.md, plugin.yaml, LICENSE fork line, ui-tui branding) and, later, repoints domains/URLs once Cloud Industry infra exists.
