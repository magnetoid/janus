from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/curator")
async def get_curator_status():
    try:
        from agent import curator
    except Exception as exc:
        raise web_server_mod.HTTPException(status_code=500, detail=f"Curator unavailable: {exc}")
    try:
        state = curator.load_state()
    except Exception:
        state = {}
    return {
        "enabled": web_server_mod._safe_call(curator, "is_enabled", True),
        "paused": web_server_mod._safe_call(curator, "is_paused", False),
        "interval_hours": web_server_mod._safe_call(curator, "get_interval_hours", None),
        "last_run_at": state.get("last_run_at"),
        "min_idle_hours": web_server_mod._safe_call(curator, "get_min_idle_hours", None),
        "stale_after_days": web_server_mod._safe_call(curator, "get_stale_after_days", None),
        "archive_after_days": web_server_mod._safe_call(curator, "get_archive_after_days", None),
    }

@router.put("/api/curator/paused")
async def set_curator_paused(body: web_server_mod.CuratorPause):
    from agent import curator

    curator.set_paused(bool(body.paused))
    return {"ok": True, "paused": bool(body.paused)}

@router.post("/api/curator/run")
async def run_curator():
    """Trigger a curator review now (backgrounded; tail via action status)."""
    try:
        proc = web_server_mod._spawn_janus_action(["curator", "run"], "curator-run")
    except Exception as exc:
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed to run curator: {exc}")
    return {"ok": True, "pid": proc.pid, "name": "curator-run"}

