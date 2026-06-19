from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/learning/stats")
async def get_learning_stats():
    try:
        from agent import outcome_tracker as ot
        from agent import persona_optimizer as po

        stats = ot.skill_stats()
        ranked = sorted(stats.items(),
                        key=lambda kv: (kv[1].get("success_rate") or 0, kv[1]["uses"]),
                        reverse=True)
        try:
            from agent import lessons as _lessons
            lessons_stat = _lessons.stats()
        except Exception:
            lessons_stat = {"total": 0, "by_task_type": {}}
        try:
            from agent import eval_trend as _et
            from agent.evals import evals_dir as _evals_dir
            curve = _et.learning_curve()
            drafts = list((_evals_dir() / ".drafts").glob("*.yaml"))
            curve["draft_pins"] = len(drafts)
        except Exception:
            curve = {"points": [], "learned": [], "regressed": [], "draft_pins": 0}
        try:
            from agent import playbook as _pb
            playbook = {"enabled": _pb.enabled(), **_pb.stats()}
        except Exception:
            playbook = {"enabled": False, "total": 0, "by_scope": {}}
        try:
            from agent.model_routing import _consensus_config, enabled as _consensus_enabled
            _cc = _consensus_config()
            _tiers = _cc.get("model_tiers", {}) or {}
            consensus = {
                "enabled": _consensus_enabled(),
                "tiers": {k: (_tiers.get(k, {}) or {}).get("model", "") for k in ("cheap", "mid", "smart")},
                "ensemble": bool((_cc.get("ensemble", {}) or {}).get("enabled")),
            }
        except Exception:
            consensus = {"enabled": False, "tiers": {}, "ensemble": False}
        return {
            "overall": ot.overall_stats(),
            "recent_success_rate": ot.recent_success_rate(20),
            "skills": [{"name": n, **s} for n, s in ranked],
            "personas": po.persona_stats(),
            "metrics": ot.learning_metrics(),
            "lessons": lessons_stat,
            "curve": curve,
            "playbook": playbook,
            "consensus": consensus,
        }
    except Exception as exc:
        raise web_server_mod.HTTPException(status_code=500, detail=f"learning stats unavailable: {exc}")


class _ToggleBody(BaseModel):
    enabled: bool


def _set_flag(dotted_key: str, enabled: bool) -> Dict[str, Any]:
    try:
        from janus_cli.config import set_config_value
        set_config_value(dotted_key, "true" if enabled else "false")
        return {"ok": True, "enabled": enabled}
    except Exception as exc:
        raise web_server_mod.HTTPException(status_code=500, detail=f"could not set {dotted_key}: {exc}")


@router.put("/api/learning/consensus/enabled")
async def set_consensus_enabled(body: _ToggleBody):
    return _set_flag("consensus.enabled", body.enabled)


@router.put("/api/learning/playbook/enabled")
async def set_playbook_enabled(body: _ToggleBody):
    return _set_flag("learning.playbook.enabled", body.enabled)

