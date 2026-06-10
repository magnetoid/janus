"""Tests for the skill graph + verifiable-reward promotion (agent/skill_graph.py)."""
import pytest

from agent import skill_graph as sg
from agent import outcome_tracker as ot


def _build(monkeypatch, names):
    monkeypatch.setattr(sg, "_skill_names", lambda: names)
    return sg.build_graph_from_skills()


def test_build_graph_from_skills_bootstraps_nodes(monkeypatch):
    _build(monkeypatch, ["a", "b", "c"])
    assert sg.graph_node_keys() == ["a", "b", "c"]
    assert sg.get_node("a") == {"promotion_level": 0, "refinement_flagged": False}


def test_build_sanitizes_dropped_skills_and_edges(monkeypatch):
    _build(monkeypatch, ["a", "b"])
    assert sg.add_edge("a", "b") == (True, "added")
    # 'b' disappears -> node + its edge sanitized out on rebuild
    _build(monkeypatch, ["a"])
    assert sg.graph_node_keys() == ["a"]
    assert sg.load_graph()["edges"] == []


def test_add_edge_rejects_self_missing_and_cycles(monkeypatch):
    _build(monkeypatch, ["a", "b", "c"])
    assert sg.add_edge("a", "a")[0] is False           # self
    assert sg.add_edge("a", "ghost")[0] is False        # missing node
    assert sg.add_edge("a", "b")[0] is True
    assert sg.add_edge("b", "c")[0] is True
    assert sg.add_edge("c", "a") == (False, "would create a cycle")  # a->b->c->a
    assert sg.cyclic_edges() == []                       # graph stayed acyclic


def test_dependencies_and_dependents(monkeypatch):
    _build(monkeypatch, ["a", "b", "c"])
    sg.add_edge("a", "b"); sg.add_edge("b", "c")
    assert sg.dependencies_of("a") == ["b", "c"]   # transitive prerequisites
    assert sg.dependents_of("c") == ["a", "b"]      # transitive dependents


def test_topological_sort(monkeypatch):
    _build(monkeypatch, ["a", "b", "c"])
    sg.add_edge("a", "b"); sg.add_edge("b", "c")
    order = sg.topological_sort()
    assert order.index("a") < order.index("b") < order.index("c")


def test_assess_promotability_heuristic(monkeypatch, tmp_path):
    _build(monkeypatch, ["deploy"])
    # a valid skill dir so verify passes
    d = tmp_path / "deploy"; d.mkdir()
    (d / "SKILL.md").write_text("---\nname: deploy\ndescription: Deploy safely.\n---\n", encoding="utf-8")
    # 4 uses, 100% success -> promotable
    for i in range(4):
        ot.record_outcome(f"s{i}", True, skills=["deploy"])
    a = sg.assess_promotability("deploy", skill_dir=d)
    assert a["promotable"] is True and a["success_rate"] == 1.0 and a["uses"] == 4


def test_assess_flags_refinement_on_low_success(monkeypatch, tmp_path):
    _build(monkeypatch, ["flaky"])
    d = tmp_path / "flaky"; d.mkdir()
    (d / "SKILL.md").write_text("---\nname: flaky\ndescription: Flaky thing.\n---\n", encoding="utf-8")
    for i in range(4):
        ot.record_outcome(f"s{i}", i == 0, skills=["flaky"])  # 25% success
    a = sg.assess_promotability("flaky", skill_dir=d)
    assert a["promotable"] is False and a["refinement_needed"] is True


def test_assess_failed_selftest_flags_refinement(monkeypatch, tmp_path):
    _build(monkeypatch, ["broken"])
    d = tmp_path / "broken"; d.mkdir()  # no SKILL.md -> verify fails
    a = sg.assess_promotability("broken", skill_dir=d)
    assert a["verify_ok"] is False and a["refinement_needed"] is True


def test_promote_and_flag(monkeypatch):
    _build(monkeypatch, ["a"])
    assert sg.promote_skill("a") == {"ok": True, "promotion_level": 1}
    assert sg.promote_skill("a")["promotion_level"] == 2
    assert sg.flag_refinement_needed("a", "needs work") is True
    assert sg.get_node("a")["refinement_flagged"] is True
    assert sg.promote_skill("ghost")["ok"] is False
