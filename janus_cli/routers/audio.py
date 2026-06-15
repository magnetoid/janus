from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.post("/api/audio/transcribe")
async def transcribe_audio_upload(payload: web_server_mod.AudioTranscriptionRequest):
    data_url = (payload.data_url or "").strip()
    if not data_url.startswith("data:") or "," not in data_url:
        raise web_server_mod.HTTPException(status_code=400, detail="Invalid audio payload")

    header, encoded = data_url.split(",", 1)
    if ";base64" not in header:
        raise web_server_mod.HTTPException(
            status_code=400, detail="Audio payload must be base64 encoded"
        )

    mime_type = (
        payload.mime_type or header[5:].split(";", 1)[0] or "audio/webm"
    ).strip()
    normalized_mime_type = mime_type.split(";", 1)[0].lower()
    if not (
        normalized_mime_type.startswith("audio/")
        or normalized_mime_type == "video/webm"
    ):
        raise web_server_mod.HTTPException(
            status_code=400, detail="Payload must be an audio recording"
        )

    try:
        audio_bytes = web_server_mod.base64.b64decode(encoded, validate=True)
    except (web_server_mod.binascii.Error, ValueError):
        raise web_server_mod.HTTPException(status_code=400, detail="Audio payload is not valid base64")

    if not audio_bytes:
        raise web_server_mod.HTTPException(status_code=400, detail="Audio recording is empty")
    if len(audio_bytes) > web_server_mod._MAX_TRANSCRIPTION_UPLOAD_BYTES:
        raise web_server_mod.HTTPException(status_code=413, detail="Audio recording is too large")

    temp_path = ""
    try:
        suffix = web_server_mod._audio_extension_for_mime(mime_type)
        with web_server_mod.tempfile.NamedTemporaryFile(
            prefix="janus-desktop-voice-",
            suffix=suffix,
            delete=False,
        ) as tmp:
            tmp.write(audio_bytes)
            temp_path = tmp.name

        from tools.transcription_tools import transcribe_audio

        loop = web_server_mod.asyncio.get_running_loop()
        result = await loop.run_in_executor(None, transcribe_audio, temp_path)
    except web_server_mod.HTTPException:
        raise
    except Exception as exc:
        web_server_mod._log.exception("Desktop voice transcription failed")
        raise web_server_mod.HTTPException(status_code=500, detail=f"Transcription failed: {exc}")
    finally:
        if temp_path:
            try:
                web_server_mod.os.unlink(temp_path)
            except OSError:
                pass

    if not result.get("success"):
        raise web_server_mod.HTTPException(
            status_code=400,
            detail=result.get("error") or "Transcription failed",
        )

    return {
        "ok": True,
        "transcript": str(result.get("transcript") or "").strip(),
        "provider": result.get("provider"),
    }

@router.get("/api/audio/elevenlabs/voices")
async def get_elevenlabs_voices():
    """Return ElevenLabs voices when an API key is configured.

    The desktop UI uses this for the ``tts.elevenlabs.voice_id`` dropdown.
    Only non-secret voice metadata is returned; the API key stays server-side.
    """
    api_key = (web_server_mod.load_env().get("ELEVENLABS_API_KEY") or web_server_mod.os.environ.get("ELEVENLABS_API_KEY") or "").strip()
    if not api_key:
        return {"available": False, "voices": []}

    request = web_server_mod.urllib.request.Request(
        "https://api.elevenlabs.io/v1/voices",
        headers={
            "Accept": "application/json",
            "xi-api-key": api_key,
        },
    )

    try:
        loop = web_server_mod.asyncio.get_running_loop()

        def _fetch() -> web_server_mod.Dict[str, web_server_mod.Any]:
            with web_server_mod.urllib.request.urlopen(request, timeout=10) as response:
                return web_server_mod.json.loads(response.read().decode("utf-8"))

        payload = await loop.run_in_executor(None, _fetch)
    except Exception as exc:
        web_server_mod._log.warning("ElevenLabs voice list failed: %s", exc)
        raise web_server_mod.HTTPException(status_code=502, detail="Could not load ElevenLabs voices")

    voices = []
    for voice in payload.get("voices") or []:
        if not isinstance(voice, dict):
            continue

        voice_id = str(voice.get("voice_id") or "").strip()
        if not voice_id:
            continue

        voices.append({
            "voice_id": voice_id,
            "name": str(voice.get("name") or voice_id),
            "label": web_server_mod._elevenlabs_voice_label(voice),
        })

    voices.sort(key=lambda item: str(item.get("label") or "").lower())
    return {"available": True, "voices": voices}

@router.post("/api/audio/speak")
async def speak_text(payload: web_server_mod.TTSSpeakRequest):
    """Synthesize speech and return audio as base64 data URL.

    Used by the desktop voice-conversation mode to play back assistant
    responses without exposing the on-disk file path. Reuses the
    existing TTS provider chain (Edge / OpenAI / ElevenLabs / etc.)
    configured in ``~/.janus/config.yaml`` under ``tts.``.
    """
    text = (payload.text or "").strip()
    if not text:
        raise web_server_mod.HTTPException(status_code=400, detail="Text is required")

    try:
        from tools.tts_tool import text_to_speech_tool
        loop = web_server_mod.asyncio.get_running_loop()
        result_json = await loop.run_in_executor(None, text_to_speech_tool, text)
    except Exception as exc:
        web_server_mod._log.exception("Desktop voice TTS failed")
        raise web_server_mod.HTTPException(status_code=500, detail=f"Speech synthesis failed: {exc}")

    try:
        result = web_server_mod.json.loads(result_json) if isinstance(result_json, str) else result_json
    except Exception:
        raise web_server_mod.HTTPException(status_code=500, detail="Invalid TTS response")

    if not result.get("success"):
        raise web_server_mod.HTTPException(
            status_code=400,
            detail=result.get("error") or "Speech synthesis failed",
        )

    file_path = result.get("file_path")
    if not file_path or not web_server_mod.os.path.isfile(file_path):
        raise web_server_mod.HTTPException(status_code=500, detail="Audio file missing")

    ext = web_server_mod.os.path.splitext(file_path)[1].lower()
    mime_type = {
        ".mp3": "audio/mpeg",
        ".ogg": "audio/ogg",
        ".opus": "audio/ogg",
        ".wav": "audio/wav",
        ".flac": "audio/flac",
    }.get(ext, "audio/mpeg")

    try:
        with open(file_path, "rb") as fh:
            audio_bytes = fh.read()
    except OSError as exc:
        raise web_server_mod.HTTPException(status_code=500, detail=f"Could not read audio: {exc}")
    finally:
        try:
            web_server_mod.os.unlink(file_path)
        except OSError:
            pass

    encoded = web_server_mod.base64.b64encode(audio_bytes).decode("ascii")
    return {
        "ok": True,
        "data_url": f"data:{mime_type};base64,{encoded}",
        "mime_type": mime_type,
        "provider": result.get("provider"),
    }

