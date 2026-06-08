---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/memory/holographic/store.py

Symbols in `plugins/memory/holographic/store.py`.

- L94 `_clamp_trust(value: float)` (function)
- L98 `MemoryStore` (class) — SQLite-backed fact store with entity resolution and trust scoring.
- L101 `__init__(self, db_path: 'str | Path | None'=None, default_trust: float=0.5, hrr_dim: int=1024)` (method)
- L128 `_init_db(self)` (method) — Create tables, indexes, and triggers if they do not exist. Enable WAL mode.
- L146 `add_fact(self, content: str, category: str='general', tags: str='')` (method) — Insert a fact and return its fact_id.
- L191 `search_facts(self, query: str, category: str | None=None, min_trust: float=0.3, limit: int=10)` (method) — Full-text search over facts using FTS5.
- L242 `update_fact(self, fact_id: int, content: str | None=None, trust_delta: float | None=None, tags: str | None=None, category: str | None=None)` (method) — Partially update a fact. Trust is clamped to [0, 1].
- L306 `remove_fact(self, fact_id: int)` (method) — Delete a fact and its entity links. Returns True if the row existed.
- L323 `list_facts(self, category: str | None=None, min_trust: float=0.0, limit: int=50)` (method) — Browse facts ordered by trust_score descending.
- L353 `record_feedback(self, fact_id: int, helpful: bool)` (method) — Record user feedback and adjust trust asymmetrically.
- L398 `_extract_entities(self, text: str)` (method) — Extract entity candidates from text using simple regex rules.
- L433 `_resolve_entity(self, name: str)` (method) — Find an existing entity by name or alias (case-insensitive) or create one.
- L463 `_link_fact_entity(self, fact_id: int, entity_id: int)` (method) — Insert into fact_entities, silently ignore if the link already exists.
- L474 `_compute_hrr_vector(self, fact_id: int, content: str)` (method) — Compute and store HRR vector for a fact. No-op if numpy unavailable.
- L498 `_rebuild_bank(self, category: str)` (method) — Full rebuild of a category's memory bank from all its fact vectors.
- L536 `rebuild_all_vectors(self, dim: int | None=None)` (method) — Recompute all HRR vectors + banks from text. For recovery/migration.
- L566 `_row_to_dict(self, row: sqlite3.Row)` (method) — Convert a sqlite3.Row to a plain dict.
- L570 `close(self)` (method) — Close the database connection.
- L574 `__enter__(self)` (method)
- L577 `__exit__(self, *_: object)` (method)
