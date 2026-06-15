from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/interests")
async def list_interests():
    from agent import interests as it
    return {"interests": it.load()}

@router.post("/api/interests")
async def add_interest(body: web_server_mod.InterestCreate):
    from agent import interests as it
    field = (body.field or "").strip()
    if not field:
        raise web_server_mod.HTTPException(status_code=400, detail="field is required")
    return {"ok": True, "interest": it.add(field)}

@router.delete("/api/interests/{interest_id}")
async def remove_interest(interest_id: str):
    from agent import interests as it
    return {"ok": it.remove(interest_id)}

