from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/aspirations")
async def list_aspirations():
    from agent import aspirations as asp
    return {"aspirations": asp.load()}

@router.post("/api/aspirations")
async def add_aspiration(body: web_server_mod.AspirationCreate):
    from agent import aspirations as asp
    goal = (body.goal or "").strip()
    if not goal:
        raise web_server_mod.HTTPException(status_code=400, detail="goal is required")
    return {"ok": True, "aspiration": asp.add(goal)}

@router.delete("/api/aspirations/{aspiration_id}")
async def remove_aspiration(aspiration_id: str):
    from agent import aspirations as asp
    return {"ok": asp.remove(aspiration_id)}

