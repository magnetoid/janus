from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/media")
async def get_media(path: str):
    """Return a gateway-local image file as a base64 data URL.

    Lets remote clients (the desktop app over the network, or the web dashboard
    in a browser) display images the agent wrote to *this* machine's filesystem
    — they can't read the gateway's local disk directly.

    Auth-gated by the session token like every other /api route. Restricted to
    an image-extension allowlist, a size cap, AND the gateway's own media roots
    (resolved, symlink-safe) so it can't be used to read arbitrary files.
    """
    try:
        target = web_server_mod.Path(path).expanduser().resolve()
    except (OSError, RuntimeError):
        raise web_server_mod.HTTPException(status_code=400, detail="Invalid path")

    if target.suffix.lower() not in web_server_mod._MEDIA_CONTENT_TYPES:
        raise web_server_mod.HTTPException(status_code=415, detail="Unsupported media type")

    roots = web_server_mod._media_serve_roots()
    if not any(target == root or root in target.parents for root in roots):
        raise web_server_mod.HTTPException(status_code=403, detail="Path outside media roots")

    if not target.is_file():
        raise web_server_mod.HTTPException(status_code=404, detail="File not found")
    if target.stat().st_size > web_server_mod._MEDIA_MAX_BYTES:
        raise web_server_mod.HTTPException(status_code=413, detail="File too large")

    encoded = web_server_mod.base64.b64encode(target.read_bytes()).decode("ascii")
    return {"data_url": f"data:{web_server_mod._MEDIA_CONTENT_TYPES[target.suffix.lower()]};base64,{encoded}"}

