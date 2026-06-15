from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/pairing")
async def list_pairing():
    store = web_server_mod._pairing_store()
    return {
        "pending": store.list_pending(),
        "approved": store.list_approved(),
    }

@router.post("/api/pairing/approve")
async def approve_pairing(body: web_server_mod.PairingApprove):
    store = web_server_mod._pairing_store()
    platform = (body.platform or "").lower().strip()
    code = (body.code or "").upper().strip()
    if not platform or not code:
        raise web_server_mod.HTTPException(status_code=400, detail="platform and code are required")

    result = store.approve_code(platform, code)
    if result:
        return {"ok": True, "user": result}
    if store._is_locked_out(platform):
        raise web_server_mod.HTTPException(
            status_code=429,
            detail=f"Platform '{platform}' is locked out after too many failed approvals.",
        )
    raise web_server_mod.HTTPException(
        status_code=404,
        detail=f"Code '{code}' not found or expired for platform '{platform}'.",
    )

@router.post("/api/pairing/revoke")
async def revoke_pairing(body: web_server_mod.PairingRevoke):
    store = web_server_mod._pairing_store()
    platform = (body.platform or "").lower().strip()
    if not platform or not body.user_id:
        raise web_server_mod.HTTPException(status_code=400, detail="platform and user_id are required")
    if store.revoke(platform, body.user_id):
        return {"ok": True}
    raise web_server_mod.HTTPException(
        status_code=404,
        detail=f"User {body.user_id} not found in approved list for {platform}.",
    )

@router.post("/api/pairing/clear-pending")
async def clear_pending_pairing():
    store = web_server_mod._pairing_store()
    count = store.clear_pending()
    return {"ok": True, "cleared": count}

