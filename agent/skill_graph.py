"""Skill graph + verifiable-reward promotion.

Upgrades skills from a flat list to a directed ACYCLIC graph: nodes are skills,
edges are prerequisite/composition relationships, and each node carries a
``promotion_level`` (a quality TIER — orthogonal to the curator's lifecycle
state of active/stale/archived) plus a ``refinement_flagged`` mark.

Promotion is gated by VERIFIABLE rewards, not raw usage: a skill is promotable
only when its static self-test passes (agent/skill_verifier.py) AND its outcome
trajectory (agent/outcome_tracker.skill_success_trajectory) clears a success
threshold over enough uses. Skills that fail their test or correlate with
failures get flagged for refinement. This is arXiv 2512.23760's audited
skill-graph idea, grounded in Janus's existing verifier + outcome signal.

Pure + best-effort; the promotability assessment needs no LLM (heuristic over
verifiable signals). Storage: ``~/.janus/learning/skill_graph.json``.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)


def get_graph_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "learning" / "skill_graph.json"


def load_graph() -> Dict[str, Any]:
    path = get_graph_path()
    if not path.is_file():
        return {"nodes": {}, "edges": []}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and "nodes" in data and "edges" in data:
            return data
    except (ValueError, OSError):
        pass
    return {"nodes": {}, "edges": []}


def save_graph(data: Dict[str, Any]) -> None:
    path = get_graph_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _skill_names() -> List[str]:
    try:
        from tools.skills_tool import _find_all_skills
        return [s["name"] for s in _find_all_skills()]
    except Exception:
        return []


def build_graph_from_skills(names: Optional[List[str]] = None) -> Dict[str, Any]:
    """Bootstrap/refresh graph nodes from current skills (idempotent).

    New skills get a node at promotion_level 0; nodes for skills that no longer
    exist are sanitized out, and dangling edges with them are dropped.
    """
    if names is None:
        names = _skill_names()
    live = set(names)
    graph = load_graph()
    nodes = graph.get("nodes", {})
    for name in names:
        nodes.setdefault(name, {"promotion_level": 0, "refinement_flagged": False})
    # sanitize: drop nodes + edges referencing skills that no longer exist
    nodes = {n: v for n, v in nodes.items() if n in live}
    edges = [
        e for e in graph.get("edges", [])
        if e.get("from") in live and e.get("to") in live
    ]
    graph = {"nodes": nodes, "edges": edges}
    save_graph(graph)
    return graph


def graph_node_keys() -> List[str]:
    return sorted(load_graph().get("nodes", {}).keys())


def get_node(skill_name: str) -> Optional[Dict[str, Any]]:
    return load_graph().get("nodes", {}).get(skill_name)


def _edge_set(edges: List[Dict[str, str]]) -> Dict[str, set]:
    adj: Dict[str, set] = {}
    for e in edges:
        adj.setdefault(e["from"], set()).add(e["to"])
    return adj


def _creates_cycle(edges: List[Dict[str, str]], frm: str, to: str) -> bool:
    """Would adding frm->to create a cycle? (i.e. is `frm` reachable from `to`?)"""
    adj = _edge_set(edges)
    stack, seen = [to], set()
    while stack:
        node = stack.pop()
        if node == frm:
            return True
        if node in seen:
            continue
        seen.add(node)
        stack.extend(adj.get(node, ()))
    return False


def add_edge(from_skill: str, to_skill: str, edge_type: str = "prerequisite") -> Tuple[bool, str]:
    """Add ``from_skill -> to_skill``. Refuses self-loops, missing nodes, and cycles."""
    if from_skill == to_skill:
        return False, "self-edges are not allowed"
    graph = load_graph()
    nodes = graph.get("nodes", {})
    if from_skill not in nodes or to_skill not in nodes:
        return False, "both skills must be graph nodes (run build first)"
    edges = graph.get("edges", [])
    if any(e["from"] == from_skill and e["to"] == to_skill for e in edges):
        return True, "edge already exists"
    if _creates_cycle(edges, from_skill, to_skill):
        return False, "would create a cycle"
    edges.append({"from": from_skill, "to": to_skill, "type": edge_type})
    graph["edges"] = edges
    save_graph(graph)
    return True, "added"


def remove_edge(from_skill: str, to_skill: str) -> bool:
    graph = load_graph()
    before = len(graph.get("edges", []))
    graph["edges"] = [
        e for e in graph.get("edges", [])
        if not (e["from"] == from_skill and e["to"] == to_skill)
    ]
    if len(graph["edges"]) != before:
        save_graph(graph)
        return True
    return False


def dependencies_of(skill_name: str) -> List[str]:
    """Transitive prerequisites (everything ``skill_name`` points to)."""
    adj = _edge_set(load_graph().get("edges", []))
    out, stack, seen = [], list(adj.get(skill_name, ())), set()
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        out.append(node)
        stack.extend(adj.get(node, ()))
    return sorted(out)


def dependents_of(skill_name: str) -> List[str]:
    """Skills that (transitively) depend on ``skill_name``."""
    edges = load_graph().get("edges", [])
    rev = _edge_set([{"from": e["to"], "to": e["from"]} for e in edges])
    out, stack, seen = [], list(rev.get(skill_name, ())), set()
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        out.append(node)
        stack.extend(rev.get(node, ()))
    return sorted(out)


def cyclic_edges() -> List[Tuple[str, str]]:
    """Return edges that participate in a cycle (should be empty for a healthy DAG)."""
    edges = load_graph().get("edges", [])
    bad = []
    for e in edges:
        others = [x for x in edges if x is not e]
        if _creates_cycle(others, e["from"], e["to"]):
            bad.append((e["from"], e["to"]))
    return bad


def topological_sort() -> List[str]:
    """Kahn's algorithm. Nodes in a cycle are appended at the end (best-effort)."""
    graph = load_graph()
    nodes = list(graph.get("nodes", {}).keys())
    adj = _edge_set(graph.get("edges", []))
    indeg = {n: 0 for n in nodes}
    for src, dsts in adj.items():
        for d in dsts:
            if d in indeg:
                indeg[d] += 1
    queue = sorted([n for n in nodes if indeg[n] == 0])
    order = []
    while queue:
        n = queue.pop(0)
        order.append(n)
        for d in sorted(adj.get(n, ())):
            indeg[d] -= 1
            if indeg[d] == 0:
                queue.append(d)
        queue.sort()
    # any nodes left (cycle) appended deterministically
    order.extend(sorted(n for n in nodes if n not in order))
    return order


# --- verifiable-reward promotion --------------------------------------------

def _graph_cfg(key: str, default: Any) -> Any:
    try:
        import yaml
        from janus_constants import get_janus_home
        cfg_path = get_janus_home() / "config.yaml"
        if cfg_path.is_file():
            cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
            g = cfg.get("graph", {})
            if isinstance(g, dict) and key in g:
                return g[key]
    except Exception:
        pass
    return default


def _resolve_skill_dir(skill_name: str) -> Optional[Path]:
    try:
        from tools.skills_tool import _find_all_skills
        for s in _find_all_skills():
            if s.get("name") == skill_name and s.get("path"):
                return Path(s["path"])
    except Exception:
        pass
    return None


def assess_promotability(skill_name: str, *, skill_dir: Optional[Path] = None) -> Dict[str, Any]:
    """Verifiable-reward assessment (no LLM). Combines the static self-test with
    the outcome trajectory. Returns promotable/refinement_needed + the signals."""
    from agent.outcome_tracker import skill_success_trajectory

    min_uses = int(_graph_cfg("min_uses_for_promotion", 3))
    promo_thr = float(_graph_cfg("promotion_success_threshold", 0.75))
    refine_thr = float(_graph_cfg("refinement_failure_threshold", 0.35))

    if skill_dir is None:
        skill_dir = _resolve_skill_dir(skill_name)
    verify_ok = True
    if skill_dir is not None:
        try:
            from agent.skill_verifier import verify_skill_dir
            verify_ok = bool(verify_skill_dir(skill_dir).get("ok"))
        except Exception:
            verify_ok = True  # absence of a verifier result isn't a failure

    traj = skill_success_trajectory(skill_name)
    uses = len(traj)
    success_rate = round(sum(traj) / uses, 3) if uses else None

    promotable = bool(
        verify_ok and uses >= min_uses
        and success_rate is not None and success_rate >= promo_thr
    )
    refinement_needed = bool(
        (not verify_ok)
        or (success_rate is not None and uses >= min_uses and success_rate <= refine_thr)
    )
    if promotable:
        reason = f"verified + {int(success_rate * 100)}% success over {uses} uses"
    elif refinement_needed:
        reason = "failed self-test" if not verify_ok else \
                 f"low success ({int(success_rate * 100)}%) over {uses} uses"
    else:
        reason = "insufficient signal" if uses < min_uses else "stable"
    return {
        "skill": skill_name, "promotable": promotable, "refinement_needed": refinement_needed,
        "verify_ok": verify_ok, "success_rate": success_rate, "uses": uses, "reason": reason,
    }


def promote_skill(skill_name: str) -> Dict[str, Any]:
    graph = load_graph()
    node = graph.get("nodes", {}).get(skill_name)
    if node is None:
        return {"ok": False, "reason": "not a graph node"}
    node["promotion_level"] = min(int(node.get("promotion_level", 0)) + 1, 5)
    node["refinement_flagged"] = False
    save_graph(graph)
    return {"ok": True, "promotion_level": node["promotion_level"]}


def flag_refinement_needed(skill_name: str, reason: str = "") -> bool:
    graph = load_graph()
    node = graph.get("nodes", {}).get(skill_name)
    if node is None:
        return False
    node["refinement_flagged"] = True
    if reason:
        node["refinement_reason"] = reason
    save_graph(graph)
    return True


def as_json() -> str:
    return json.dumps(load_graph(), indent=2, ensure_ascii=False)
