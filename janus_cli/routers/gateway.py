from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.post("/api/gateway/restart")
async def restart_gateway():
    """Kick off a ``janus gateway restart`` in the background."""
    try:
        proc = web_server_mod._spawn_janus_action(["gateway", "restart"], "gateway-restart")
    except Exception as exc:
        web_server_mod._log.exception("Failed to spawn gateway restart")
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed to restart gateway: {exc}")
    return {
        "ok": True,
        "pid": proc.pid,
        "name": "gateway-restart",
    }

@router.post("/api/gateway/start")
async def start_gateway():
    try:
        proc = web_server_mod._spawn_janus_action(["gateway", "start"], "gateway-start")
    except Exception as exc:
        web_server_mod._log.exception("Failed to spawn gateway start")
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed to start gateway: {exc}")
    return {"ok": True, "pid": proc.pid, "name": "gateway-start"}

@router.post("/api/gateway/stop")
async def stop_gateway():
    try:
        proc = web_server_mod._spawn_janus_action(["gateway", "stop"], "gateway-stop")
    except Exception as exc:
        web_server_mod._log.exception("Failed to spawn gateway stop")
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed to stop gateway: {exc}")
    return {"ok": True, "pid": proc.pid, "name": "gateway-stop"}

