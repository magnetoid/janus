---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/memory/holographic/retrieval.py

Symbols in `plugins/memory/holographic/retrieval.py`.

- L22 `FactRetriever` (class) — Multi-strategy fact retrieval with trust-weighted scoring.
- L25 `__init__(self, store: MemoryStore, temporal_decay_half_life: int=0, fts_weight: float=0.4, jaccard_weight: float=0.3, hrr_weight: float=0.3, hrr_dim: int=1024)` (method)
- L48 `search(self, query: str, category: str | None=None, min_trust: float=0.3, limit: int=10)` (method) — Hybrid search: FTS5 candidates → Jaccard rerank → trust weighting.
- L114 `probe(self, entity: str, category: str | None=None, limit: int=10)` (method) — Compositional entity query using HRR algebra.
- L192 `related(self, entity: str, category: str | None=None, limit: int=10)` (method) — Discover facts that share structural connections with an entity.
- L260 `reason(self, entities: list[str], category: str | None=None, limit: int=10)` (method) — Multi-entity compositional query — vector-space JOIN.
- L338 `contradict(self, category: str | None=None, threshold: float=0.3, limit: int=10)` (method) — Find potentially contradictory facts via entity overlap + content divergence.
- L444 `_score_facts_by_vector(self, target_vec: 'np.ndarray', category: str | None=None, limit: int=10)` (method) — Score facts by similarity to a target vector.
- L481 `_fts_candidates(self, query: str, category: str | None, min_trust: float, limit: int)` (method) — Get raw FTS5 candidates from the store.
- L545 `_tokenize(text: str)` (method) — Simple whitespace tokenization with lowercasing.
- L561 `_jaccard_similarity(set_a: set, set_b: set)` (method) — Jaccard similarity coefficient: |A ∩ B| / |A ∪ B|.
- L569 `_temporal_decay(self, timestamp_str: str | None)` (method) — Exponential decay: 0.5^(age_days / half_life_days).
