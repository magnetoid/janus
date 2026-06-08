---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# skills/productivity/maps/scripts/maps_client.py

Symbols in `skills/productivity/maps/scripts/maps_client.py`.

- L127 `_tags_for(category)` (function) — Return the CATEGORY_TAGS entry as a list of (key, value) pairs.
- L149 `print_json(data)` (function) — Print data as pretty-printed JSON to stdout.
- L154 `error_exit(message, code=1)` (function) — Print an error result as JSON and exit.
- L164 `http_get(url, params=None, retries=MAX_RETRIES, silent=False)` (function) — Perform an HTTP GET request, returning parsed JSON.
- L202 `http_get_text(url, params=None, retries=MAX_RETRIES, silent=False)` (function) — Like http_get but returns raw text instead of parsed JSON.
- L235 `http_post(url, data_str, retries=MAX_RETRIES)` (function) — Perform an HTTP POST with a plain-text body (for Overpass QL).
- L272 `overpass_query(query)` (function) — POST an Overpass QL query, trying each URL in OVERPASS_URLS in turn.
- L300 `haversine_m(lat1, lon1, lat2, lon2)` (function) — Return distance in metres between two lat/lon points (Haversine).
- L316 `nominatim_search(query, limit=5)` (function) — Geocode a free-text query. Returns list of result dicts.
- L328 `nominatim_reverse(lat, lon)` (function) — Reverse geocode lat/lon. Returns a single result dict.
- L340 `geocode_single(query)` (function) — Geocode a query and return (lat, lon, display_name).
- L356 `build_overpass_nearby(tag_key, tag_val, lat, lon, radius, limit, religion=None, tag_pairs=None)` (function) — Build an Overpass QL query for nearby POIs around a point.
- L389 `build_overpass_bbox(tag_key, tag_val, south, west, north, east, limit, religion=None, tag_pairs=None)` (function) — Build an Overpass QL query for POIs within a bounding box.
- L419 `parse_overpass_elements(elements, ref_lat=None, ref_lon=None)` (function) — Parse Overpass elements into a clean list of POI dicts.
- L501 `cmd_search(args)` (function) — Geocode a place name and return top results.
- L548 `cmd_reverse(args)` (function) — Reverse geocode coordinates to a human-readable address.
- L596 `cmd_nearby(args)` (function) — Find nearby POIs using the Overpass API.
- L686 `cmd_distance(args)` (function) — Calculate road distance and travel time between two places.
- L754 `_format_duration(seconds)` (function) — Format seconds into a human-readable string.
- L766 `_format_distance(metres)` (function) — Format metres into a human-readable string.
- L773 `cmd_directions(args)` (function) — Get turn-by-turn directions between two places via OSRM.
- L889 `cmd_timezone(args)` (function) — Get timezone information for a lat/lon coordinate.
- L969 `cmd_bbox(args)` (function) — Find POIs within a bounding box using the Overpass API.
- L1032 `cmd_area(args)` (function) — Get bounding box and area info for a named place.
- L1086 `build_parser()` (function)
- L1274 `main()` (function)
