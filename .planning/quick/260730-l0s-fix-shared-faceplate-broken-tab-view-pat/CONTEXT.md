# Quick context — Fix shared Faceplate tabs

## Locked decisions (user)

1. **Trend tab must NOT use AdhocTrend.** Dedicated view under faceplate `_Assets` (Scout-style), auto-loads pens in-popup.
2. **Which pens / how to know** — still TBD with Dylan. Implement Scout-like mechanism (deviceType → pen list map and/or params) with a sensible Compressor default (FLA, SVP, DisP, Amps) that is easy to change.
3. Prefer **one shared Faceplate shell**; tab content via embeds; tabs from params.
4. Fix broken runtime: Controls/Configuration "View Not Found", Alarms `ia.display.alarm-status-table not found`, tab label contrast (white on light gray), Alarm Config beyond raw stub if feasible.

## Symptoms (screenshots 2026-07-30)

- Controls / Configuration → View Not Found (paths wrong despite views on disk under `Compressor/Controls`, `Compressor/Configuration`)
- Trend → stub list + Open Adhoc Trend (wrong approach)
- Alarm Configuration → stub tag dump
- Alarms → invalid component type `ia.display.alarm-status-table`
- Inactive/active tab text nearly invisible

## Out of scope

- Full Scout AlarmConfiguration editor port (unless lightweight working editor is quick)
- Final pen catalog for every device type (Compressor defaults + extensible map)

## Research in flight

- Path diagnosis → `_faceplate-diag.md`
- Scout Trend / Alarm table → `_scout-faceplate-trend-research.md`
