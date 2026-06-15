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
        return {
            "overall": ot.overall_stats(),
            "recent_success_rate": ot.recent_success_rate(20),
            "skills": [{"name": n, **s} for n, s in ranked],
            "personas": po.persona_stats(),
            "metrics": ot.learning_metrics(),
            "lessons": lessons_stat,
        }
    except Exception as exc:
        raise web_server_mod.HTTPException(status_code=500, detail=f"learning stats unavailable: {exc}")

