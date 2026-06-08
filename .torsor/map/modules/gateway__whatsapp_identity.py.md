---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/whatsapp_identity.py

Symbols in `gateway/whatsapp_identity.py`.

- L48 `normalize_whatsapp_identifier(value: str)` (function) — Strip WhatsApp JID/LID syntax down to its stable numeric identifier.
- L70 `expand_whatsapp_aliases(identifier: str)` (function) — Resolve WhatsApp phone/LID aliases via bridge session mapping files.
- L122 `canonical_whatsapp_identifier(identifier: str)` (function) — Return a stable WhatsApp sender identity across phone-JID/LID variants.
