from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.websocket("/api/pub")
async def pub_ws(ws: web_server_mod.WebSocket) -> None:
    if not web_server_mod._DASHBOARD_EMBEDDED_CHAT_ENABLED:
        await ws.close(code=4403)
        return

    if not web_server_mod._ws_auth_ok(ws):
        await ws.close(code=4401)
        return

    if not web_server_mod._ws_request_is_allowed(ws):
        await ws.close(code=4403)
        return

    channel = web_server_mod._channel_or_close_code(ws)
    if not channel:
        await ws.close(code=4400)
        return

    await ws.accept()

    try:
        while True:
            await web_server_mod._broadcast_event(ws.app, channel, await ws.receive_text())
    except web_server_mod.WebSocketDisconnect:
        pass

