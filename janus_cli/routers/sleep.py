from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/sleep")
async def get_sleep_status():
    from agent import sleep as sl
    state = sl.load_sleep_state()
    return {
        "paused": bool(state.get("paused")),
        "last_run": state.get("last_run"),
        "last_report": state.get("last_report"),
    }

@router.put("/api/sleep/paused")
async def set_sleep_paused(body: web_server_mod.SleepPause):
    from agent import sleep as sl
    state = sl.load_sleep_state()
    state["paused"] = bool(body.paused)
    sl.save_sleep_state(state)
    return {"ok": True, "paused": bool(body.paused)}

