---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/security/oss-forensics/scripts/evidence-store.py

Symbols in `optional-skills/security/oss-forensics/scripts/evidence-store.py`.

- L51 `_now_iso()` (function)
- L55 `_sha256(content: str)` (function)
- L59 `EvidenceStore` (class)
- L60 `__init__(self, filepath: str)` (method)
- L82 `_save(self)` (method)
- L87 `_next_id(self)` (method)
- L90 `add(self, source: str, content: str, evidence_type: str, actor: str=None, url: str=None, timestamp: str=None, ioc_type: str=None, verification: str='unverified', notes: str=None)` (method)
- L127 `list_evidence(self, filter_type: str=None, filter_actor: str=None)` (method)
- L135 `verify_integrity(self)` (method) — Re-compute SHA-256 for all entries and report mismatches.
- L149 `query(self, keyword: str)` (method) — Search for keyword in content, source, actor, or url.
- L160 `export_markdown(self)` (method)
- L191 `summary(self)` (method)
- L210 `main()` (function)
