"""Tests for agentic RAG over a corpus (agent/corpus_rag.py)."""
import pytest

from agent import corpus_rag as cr


@pytest.fixture
def corpus(tmp_path):
    (tmp_path / "a.py").write_text(
        "def deploy_staging():\n    run_tests()\n    push_to_staging()\n", encoding="utf-8")
    (tmp_path / "notes.md").write_text(
        "# Notes\n\nThe database is postgres 16 on the staging server.\n", encoding="utf-8")
    (tmp_path / "skip.bin").write_text("binary-ish not indexed", encoding="utf-8")
    sub = tmp_path / "node_modules"; sub.mkdir()
    (sub / "junk.py").write_text("deploy deploy deploy", encoding="utf-8")  # skipped dir
    return tmp_path


def test_search_finds_relevant_chunk_with_citation(corpus):
    hits = cr.search_corpus("how to deploy staging", root=corpus)
    assert hits
    top = hits[0]
    assert top["file"] == "a.py" and top["line"] == 1
    assert "deploy_staging" in top["snippet"]


def test_search_matches_markdown(corpus):
    hits = cr.search_corpus("postgres database server", root=corpus)
    assert any(h["file"] == "notes.md" for h in hits)


def test_search_skips_ignored_dirs_and_extensions(corpus):
    hits = cr.search_corpus("deploy", root=corpus)
    files = {h["file"] for h in hits}
    assert not any("node_modules" in f for f in files)   # skipped dir
    assert not any(f.endswith(".bin") for f in files)     # non-text ext


def test_search_empty_query_or_no_match(corpus):
    assert cr.search_corpus("   ", root=corpus) == []
    assert cr.search_corpus("quantumchromodynamics", root=corpus) == []


def test_register_list_remove(tmp_path, monkeypatch):
    monkeypatch.setenv("JANUS_HOME", str(tmp_path / ".janus"))
    corpus_dir = tmp_path / "repo"; corpus_dir.mkdir()
    res = cr.register_corpus("My Repo", str(corpus_dir))
    assert res["ok"] and res["name"] == "my-repo"
    assert cr.load_corpora()["my-repo"] == str(corpus_dir.resolve())
    assert cr.remove_corpus("my-repo") is True
    assert cr.load_corpora() == {}


def test_register_rejects_nonexistent_dir(tmp_path, monkeypatch):
    monkeypatch.setenv("JANUS_HOME", str(tmp_path / ".janus"))
    res = cr.register_corpus("x", str(tmp_path / "nope"))
    assert res["ok"] is False


def test_search_by_registered_name(tmp_path, monkeypatch, corpus):
    monkeypatch.setenv("JANUS_HOME", str(tmp_path / ".janus"))
    cr.register_corpus("code", str(corpus))
    hits = cr.search_corpus("deploy staging", corpus="code")
    assert any(h["file"] == "a.py" for h in hits)
