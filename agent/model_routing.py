"""Consensus model routing — pick the right-cost model per task.

Classify a prompt's complexity (agent/task_complexity) and select the model
TIER from config (``consensus.model_tiers``: cheap / mid / smart). For the
hardest tasks, when the ensemble is enabled, return a consensus plan: several
strong models (from the model-strengths KB, agent/model_strengths) whose answers
the ``mixture_of_agents`` tool synthesizes.

Every decision is made at TASK ENTRY (a consensus tool call or a delegated
subtask) — never mid-conversation — so routing never breaks the prompt cache.

Pure + best-effort; reads config but never raises.
"""
from __future__ import annotations

import logging
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

# complexity band -> tier name
_BAND_TIER = {"simple": "cheap", "mid": "mid", "hard": "smart"}
_BAND_RANK = {"simple": 0, "mid": 1, "hard": 2}


def _consensus_config(config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    if config is None:
        try:
            from janus_cli.config import load_config
            config = load_config()
        except Exception:
            return {}
    c = config.get("consensus") if isinstance(config, dict) else None
    return c if isinstance(c, dict) else {}


def enabled(config: Optional[Dict[str, Any]] = None) -> bool:
    """True when consensus routing is switched on in config."""
    return bool(_consensus_config(config).get("enabled"))


def _tier_model(cfg: Dict[str, Any], tier_name: str,
                fallback_model: str, fallback_provider: str) -> Dict[str, str]:
    tiers = cfg.get("model_tiers", {}) or {}
    t = tiers.get(tier_name, {}) if isinstance(tiers, dict) else {}
    t = t if isinstance(t, dict) else {}
    model = (str(t.get("model", "")).strip()) or fallback_model
    provider = (str(t.get("provider", "")).strip()) or fallback_provider
    return {"tier": tier_name, "provider": provider, "model": model}


def consensus_members(task: Optional[str] = None, n: int = 3,
                      available: Optional[List[str]] = None) -> List[str]:
    """Strong models to ensemble for a hard task, from the model-strengths KB."""
    try:
        from agent.model_strengths import best_models_for
        models = best_models_for(task or "general", available=available, n=max(1, n))
        return list(models)[:n]
    except Exception as exc:
        logger.debug("consensus_members failed: %s", exc)
        return []


def route(
    prompt: Any, *, task: Optional[str] = None, history_len: int = 0,
    config: Optional[Dict[str, Any]] = None,
    main_model: str = "", main_provider: str = "",
    llm_caller: Optional[Callable[..., Any]] = None,
) -> Dict[str, Any]:
    """Return a routing decision for ``prompt``.

    ``{complexity, tier, provider, model, ensemble: bool, members: [...], task}``.
    An empty tier model falls back to the agent's main model. Best-effort; never
    raises — on any failure it returns the safe main-model/mid default.
    """
    result: Dict[str, Any] = {
        "complexity": "mid", "tier": "mid",
        "provider": main_provider, "model": main_model,
        "ensemble": False, "members": [], "task": task,
    }
    try:
        from agent.task_complexity import classify_complexity
        cfg = _consensus_config(config)
        band = classify_complexity(
            prompt, history_len=history_len,
            mode=str(cfg.get("complexity_mode", "heuristic")), llm_caller=llm_caller,
        )
        result["complexity"] = band

        tier = _tier_model(cfg, _BAND_TIER.get(band, "mid"), main_model, main_provider)
        result.update(tier)

        ens = cfg.get("ensemble", {}) or {}
        if isinstance(ens, dict) and ens.get("enabled"):
            floor = _BAND_RANK.get(str(ens.get("min_complexity", "hard")), 2)
            if _BAND_RANK.get(band, 1) >= floor:
                members = consensus_members(task, n=int(ens.get("member_count", 3)))
                if members:
                    result["ensemble"] = True
                    result["members"] = members
    except Exception as exc:
        logger.debug("route failed: %s", exc)
    return result
