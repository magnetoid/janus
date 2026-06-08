---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/teams_pipeline/meetings.py

Symbols in `plugins/teams_pipeline/meetings.py`.

- L14 `TeamsMeetingError` (class) — Base class for Teams meeting pipeline failures.
- L18 `TeamsMeetingNotFoundError` (class) — Raised when the meeting cannot be resolved from Graph.
- L22 `TeamsMeetingArtifactNotFoundError` (class) — Raised when a transcript or recording cannot be found.
- L26 `TeamsMeetingPermissionError` (class) — Raised when Graph access is denied for the requested resource.
- L30 `_meeting_path(meeting_ref: TeamsMeetingRef | str)` (function)
- L35 `_wrap_graph_error(exc: MicrosoftGraphAPIError, *, missing_message: str)` (function)
- L43 `_parse_organizer_user_id(payload: dict[str, Any])` (function)
- L56 `_parse_thread_id(payload: dict[str, Any])` (function)
- L65 `_normalize_meeting_ref(payload: dict[str, Any], *, tenant_id: str | None=None)` (function)
- L85 `_normalize_artifact(artifact_type: str, payload: dict[str, Any], *, default_source_url: str | None=None)` (function)
- L113 `_transcript_sort_key(artifact: MeetingArtifact)` (function)
- L125 `_recording_download_path(meeting_ref: TeamsMeetingRef, artifact: MeetingArtifact)` (function)
- L131 `_transcript_download_path(meeting_ref: TeamsMeetingRef, artifact: MeetingArtifact)` (function)
- L137 `resolve_meeting_reference(client: MicrosoftGraphClient, *, meeting_id: str | None=None, join_web_url: str | None=None, tenant_id: str | None=None)` (function)
- L173 `list_transcript_artifacts(client: MicrosoftGraphClient, meeting_ref: TeamsMeetingRef)` (function)
- L187 `select_preferred_transcript(candidates: list[MeetingArtifact])` (function)
- L194 `download_transcript_text(client: MicrosoftGraphClient, meeting_ref: TeamsMeetingRef, transcript: MeetingArtifact, *, encoding: str='utf-8')` (function)
- L227 `fetch_preferred_transcript_text(client: MicrosoftGraphClient, meeting_ref: TeamsMeetingRef)` (function)
- L241 `list_recording_artifacts(client: MicrosoftGraphClient, meeting_ref: TeamsMeetingRef)` (function)
- L255 `download_recording_artifact(client: MicrosoftGraphClient, meeting_ref: TeamsMeetingRef, recording: MeetingArtifact, destination: str | Path)` (function)
- L280 `fetch_call_record_artifact(client: MicrosoftGraphClient, *, call_record_id: str, allow_permission_errors: bool=True)` (function)
- L319 `enrich_meeting_with_call_record(client: MicrosoftGraphClient, meeting_ref: TeamsMeetingRef, *, call_record_id: str | None=None, allow_permission_errors: bool=True)` (function)
