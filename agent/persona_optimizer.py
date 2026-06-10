"""Persona self-optimization — learn which persona correlates with success.

A/B telemetry + recommender layered on the EXISTING ``agent.personalities``
config (it does not add a parallel persona store). Each ended session's outcome
(agent/outcome_tracker.py) carries the active persona; this aggregates the
success rate per persona and recommends the strongest — the SPO-style preference
signal, reusing the same reward signal the curator uses for skills.
"""
from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

DEFAULT_PERSONA = "default"


def list_personas() -> List[str]:
    """Names of configured personas (from the existing agent.personalities map)."""
    try:
        import yaml
        from janus_constants import get_janus_home

        cfg_path = get_janus_home() / "config.yaml"
        if cfg_path.is_file():
            cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
            personas = (cfg.get("agent") or {}).get("personalities") or {}
            if isinstance(personas, dict):
                return [DEFAULT_PERSONA] + sorted(personas.keys())
    except Exception:
        pass
    return [DEFAULT_PERSONA]


def persona_stats() -> Dict[str, Dict[str, Any]]:
    """Per-persona aggregates from the outcome records: uses, successes, rate."""
    from agent.outcome_tracker import load

    agg: Dict[str, Dict[str, Any]] = {}
    for rec in load():
        persona = rec.get("persona") or DEFAULT_PERSONA
        a = agg.setdefault(persona, {"uses": 0, "successes": 0})
        a["uses"] += 1
        if rec.get("success"):
            a["successes"] += 1
    for a in agg.values():
        a["success_rate"] = round(a["successes"] / a["uses"], 3) if a["uses"] else None
    return agg


def recommend_persona(min_samples: int = 10) -> Dict[str, Any]:
    """Recommend the persona with the best success rate over a meaningful sample.

    Returns ``{"recommended": name|None, "success_rate": float|None,
    "reason": str, "ranked": [...]}``.
    """
    stats = persona_stats()
    eligible = [
        (name, s) for name, s in stats.items()
        if s["uses"] >= min_samples and s["success_rate"] is not None
    ]
    ranked = sorted(stats.items(), key=lambda kv: (kv[1]["success_rate"] or 0, kv[1]["uses"]), reverse=True)
    if not eligible:
        return {
            "recommended": None,
            "success_rate": None,
            "reason": f"insufficient data — need >= {min_samples} sessions for a persona",
            "ranked": ranked,
        }
    eligible.sort(key=lambda kv: (kv[1]["success_rate"], kv[1]["uses"]), reverse=True)
    best_name, best = eligible[0]
    return {
        "recommended": best_name,
        "success_rate": best["success_rate"],
        "reason": f"highest success rate ({int(best['success_rate'] * 100)}%) over "
                  f"{best['uses']} sessions",
        "ranked": ranked,
    }
