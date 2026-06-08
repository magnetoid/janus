---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/memory/holographic/holographic.py

Symbols in `plugins/memory/holographic/holographic.py`.

- L38 `_require_numpy()` (function)
- L43 `encode_atom(word: str, dim: int=1024)` (function) — Deterministic phase vector via SHA-256 counter blocks.
- L70 `bind(a: 'np.ndarray', b: 'np.ndarray')` (function) — Circular convolution = element-wise phase addition.
- L80 `unbind(memory: 'np.ndarray', key: 'np.ndarray')` (function) — Circular correlation = element-wise phase subtraction.
- L90 `bundle(*vectors: 'np.ndarray')` (function) — Superposition via circular mean of complex exponentials.
- L101 `similarity(a: 'np.ndarray', b: 'np.ndarray')` (function) — Phase cosine similarity. Range [-1, 1].
- L111 `encode_text(text: str, dim: int=1024)` (function) — Bag-of-words: bundle of atom vectors for each token.
- L135 `encode_fact(content: str, entities: list[str], dim: int=1024)` (function) — Structured encoding: content bound to ROLE_CONTENT, each entity bound to ROLE_ENTITY, all bundled.
- L163 `phases_to_bytes(phases: 'np.ndarray')` (function) — Serialize phase vector to bytes. float64 tobytes — 8 KB at dim=1024.
- L169 `bytes_to_phases(data: bytes)` (function) — Deserialize bytes back to phase vector. Inverse of phases_to_bytes.
- L179 `snr_estimate(dim: int, n_items: int)` (function) — Signal-to-noise ratio estimate for holographic storage.
