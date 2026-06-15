from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.websocket("/api/pty")
async def pty_ws(ws: web_server_mod.WebSocket) -> None:
    peer = ws.client.host if ws.client else "?"

    if not web_server_mod._DASHBOARD_EMBEDDED_CHAT_ENABLED:
        web_server_mod._log.info("pty refused: embedded chat disabled peer=%s", peer)
        await ws.close(code=4404, reason="embedded chat disabled")
        return

    # --- auth + host/origin/peer check (before accept so we can close
    #     cleanly AND tell the client WHY via the close code + reason).
    #     Each gate maps to a distinct close code so the log and the
    #     browser banner agree on the cause:
    #       4401 bad credential   4403 host/origin mismatch
    #       4408 peer not allowed  4404 chat disabled
    auth_reason, cred = web_server_mod._ws_auth_reason(ws)
    mode = web_server_mod._ws_auth_mode()
    if auth_reason is not None:
        web_server_mod._log.warning(
            "pty auth rejected reason=%s mode=%s cred=%s peer=%s",
            auth_reason, mode, cred, peer,
        )
        await ws.close(code=4401, reason=web_server_mod._ws_close_reason(f"auth: {auth_reason}"))
        return

    host_origin_reason = web_server_mod._ws_host_origin_reason(ws)
    if host_origin_reason is not None:
        web_server_mod._log.warning("pty refused: %s peer=%s", host_origin_reason, peer)
        await ws.close(code=4403, reason=web_server_mod._ws_close_reason(host_origin_reason))
        return

    client_reason = web_server_mod._ws_client_reason(ws)
    if client_reason is not None:
        web_server_mod._log.warning("pty refused: %s", client_reason)
        await ws.close(code=4408, reason=web_server_mod._ws_close_reason(client_reason))
        return

    await ws.accept()
    web_server_mod._log.info("pty accepted peer=%s mode=%s cred=%s", peer, mode, cred)

    # On native Windows, the POSIX PTY bridge can't be imported.  Tell the
    # client and close cleanly rather than pretending the feature works.
    if not web_server_mod._PTY_BRIDGE_AVAILABLE:
        await ws.send_text(
            "\r\n\x1b[31mChat unavailable: the embedded terminal requires a "
            "POSIX PTY, which native Windows Python doesn't provide.\x1b[0m\r\n"
            "\x1b[33mInstall Janus inside WSL2 to use the dashboard's /chat "
            "tab — the rest of the dashboard works here.\x1b[0m\r\n"
        )
        await ws.close(code=1011)
        return

    # --- spawn PTY ------------------------------------------------------
    resume = ws.query_params.get("resume") or None
    channel = web_server_mod._channel_or_close_code(ws)
    sidecar_url = web_server_mod._build_sidecar_url(channel) if channel else None

    try:
        argv, cwd, env = web_server_mod._resolve_chat_argv(resume=resume, sidecar_url=sidecar_url)
    except SystemExit as exc:
        # _make_tui_argv calls sys.exit(1) when node/npm is missing.
        await ws.send_text(f"\r\n\x1b[31mChat unavailable: {exc}\x1b[0m\r\n")
        await ws.close(code=1011)
        return


    try:
        bridge = web_server_mod.PtyBridge.spawn(argv, cwd=cwd, env=env)
    except web_server_mod.PtyUnavailableError as exc:
        await ws.send_text(f"\r\n\x1b[31mChat unavailable: {exc}\x1b[0m\r\n")
        await ws.close(code=1011)
        return
    except (FileNotFoundError, OSError) as exc:
        await ws.send_text(f"\r\n\x1b[31mChat failed to start: {exc}\x1b[0m\r\n")
        await ws.close(code=1011)
        return

    loop = web_server_mod.asyncio.get_running_loop()

    # --- reader task: PTY master → WebSocket ----------------------------
    async def pump_pty_to_ws() -> None:
        while True:
            chunk = await loop.run_in_executor(
                None, bridge.read, web_server_mod._PTY_READ_CHUNK_TIMEOUT
            )
            if chunk is None:  # EOF
                return
            if not chunk:  # no data this tick; yield control and retry
                await web_server_mod.asyncio.sleep(0)
                continue
            try:
                await ws.send_bytes(chunk)
            except Exception:
                return

    reader_task = web_server_mod.asyncio.create_task(pump_pty_to_ws())

    # --- writer loop: WebSocket → PTY master ----------------------------
    try:
        while True:
            msg = await ws.receive()
            msg_type = msg.get("type")
            if msg_type == "websocket.disconnect":
                break
            raw = msg.get("bytes")
            if raw is None:
                text = msg.get("text")
                raw = text.encode("utf-8") if isinstance(text, str) else b""
            if not raw:
                continue

            # Resize escape is consumed locally, never written to the PTY.
            match = web_server_mod._RESIZE_RE.match(raw)
            if match and match.end() == len(raw):
                cols = int(match.group(1))
                rows = int(match.group(2))
                bridge.resize(cols=cols, rows=rows)
                continue

            bridge.write(raw)
    except web_server_mod.WebSocketDisconnect:
        pass
    finally:
        reader_task.cancel()
        try:
            await reader_task
        except (web_server_mod.asyncio.CancelledError, Exception):
            pass
        bridge.close()

