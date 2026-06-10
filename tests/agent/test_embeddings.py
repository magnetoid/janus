"""Tests for the optional semantic embeddings layer (agent/embeddings.py)."""
import numpy as np
import pytest

from agent import embeddings as emb


def test_rerank_none_when_no_backend(monkeypatch):
    monkeypatch.setattr(emb, "embed", lambda texts: None)
    assert emb.rerank("q", ["a", "b"], 2) is None


def test_rerank_empty_candidates():
    assert emb.rerank("q", [], 5) == []


def test_rerank_orders_by_cosine(monkeypatch):
    # query vector points at candidate index 1 (the second candidate)
    def fake_embed(texts):
        # texts = [query, cand0, cand1, cand2]
        return np.array([
            [1.0, 0.0],   # query
            [0.0, 1.0],   # cand0 — orthogonal
            [1.0, 0.0],   # cand1 — identical to query (best)
            [0.7, 0.7],   # cand2 — middling
        ], dtype="float32")
    monkeypatch.setattr(emb, "embed", fake_embed)
    order = emb.rerank("q", ["c0", "c1", "c2"], 3)
    assert order[0] == 1            # most similar first
    assert order[-1] == 0          # orthogonal last


def test_hybrid_rerank_falls_back_to_lexical_when_unavailable(monkeypatch):
    monkeypatch.setattr(emb, "rerank", lambda q, c, n: None)
    items = [{"t": "x"}, {"t": "y"}, {"t": "z"}]
    out = emb.hybrid_rerank("q", items, 2, text_of=lambda i: i["t"])
    assert out == items[:2]          # unchanged lexical top-n


def test_hybrid_rerank_reorders_when_available(monkeypatch):
    # rerank says: candidate index 2 is best, then 0
    monkeypatch.setattr(emb, "rerank", lambda q, c, n: [2, 0])
    items = [{"t": "a"}, {"t": "b"}, {"t": "c"}]
    out = emb.hybrid_rerank("q", items, 2, text_of=lambda i: i["t"])
    assert [i["t"] for i in out] == ["c", "a"]


def test_hybrid_rerank_empty():
    assert emb.hybrid_rerank("q", [], 5, text_of=lambda i: i) == []


def test_available_is_bool():
    # Whatever the env, this must not raise and returns a bool.
    assert isinstance(emb.available(), bool)
