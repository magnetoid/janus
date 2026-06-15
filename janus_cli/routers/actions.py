from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/actions/{name}/status")
async def get_action_status(name: str, lines: int = 200):
    """Tail an action log and report whether the process is still running."""
    log_file_name = web_server_mod._ACTION_LOG_FILES.get(name)
    if log_file_name is None:
        raise web_server_mod.HTTPException(status_code=404, detail=f"Unknown action: {name}")

    log_path = web_server_mod._ACTION_LOG_DIR / log_file_name
    tail = web_server_mod._tail_lines(log_path, min(max(lines, 1), 2000))

    proc = web_server_mod._ACTION_PROCS.get(name)
    if proc is None:
        result = web_server_mod._ACTION_RESULTS.get(name)
        running = False
        exit_code = result.get("exit_code") if result else None
        pid = result.get("pid") if result else None
    else:
        exit_code = proc.poll()
        running = exit_code is None
        pid = proc.pid

    return {
        "name": name,
        "running": running,
        "exit_code": exit_code,
        "pid": pid,
        "lines": tail,
    }

