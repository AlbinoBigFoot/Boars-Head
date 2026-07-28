# Handoff: Scout-style alarm badge + blank IconHeader

## Branch

`feature/scout-alarm-icon-header` (from `origin/main`)

## Summary

Clean re-implementation of Scout alarm chrome for **all BH device components**, without the broken layout from `ticket/12654167899-ev01-status` (gray top bar, partial border, misaligned DEF status).

### What was done

1. **`AlarmHeader`** (`03_Elements/01_Status/AlarmHeader`)
   - Shows Scout-style priority badge (Critical / High / Medium / Low SVG icons under `03_Elements/01_Status/Icons/Alarms/`)
   - Visible when `{tagPath}/_Alarms/_Active` is true
   - Badge path from `{tagPath}/_Alarms/_ActiveHighPriority` (1=Critical … 4=Low)
   - Unack flash via `{tagPath}/_Alarms/_Unack` → `alarm-flash` / `alarm-icon-unack`
   - Embedded at Graphic top-left (`x/y = -2`) so it sits on the border

2. **`IconHeader`** (`03_Elements/01_Status/IconHeader`)
   - Blank placeholder row (20×20) in the label header
   - `custom.icons.*` stubs ready for Dylan’s later icon set (Fault / Operator / Disabled / OOS)
   - Replaces the old label-row `DeviceAlarmIndicator`

3. **Colored alarm border** on device `Graphic`
   - CSS classes: `device-graphic alarm-border alarm-priority-{critical|high|medium|low}`
   - `box-sizing: content-box` so the 2px border does **not** shrink SVG / misalign coils (root cause of the failed EV-04 attempt)

4. **Devices wired**
   - Evaporator, EvaporatorDual, EvaporatorTriple, Pump, ExhaustFan, CoolingTower, Compressor

5. **StatusIndicator alignment**
   - Root `width: 100%` + centered flex; label `textAlign: center`
   - Kept existing short status codes on main (CLG / DFT / FLT / …) — did **not** reintroduce Man/phase codes from the failed ticket branch

### Alarm count / severity sourcing

BH does **not** currently expose a numeric alarm count tag per device.

| Tag | Role |
|-----|------|
| `{tagPath}/_Alarms/_Active` | Bool — show badge + border |
| `{tagPath}/_Alarms/_ActiveHighPriority` | Int 1–4 — badge glyph + border color |
| `{tagPath}/_Alarms/_Unack` | Bool — flash when unacknowledged |

Scout pumps show a letter/digit glyph (Critical/High ≈ “1” square; Medium ≈ triangle “2”). That glyph comes from priority icon views, **not** an active-alarm count. Overview totals still use `shared.Overview.buildActiveAlarmCountExpression` (sum of `_Active` bools) separately.

### Before / after layout notes

| Before (failed ticket / main) | After |
|-------------------------------|--------|
| Label-row alarm icon (`DeviceAlarmIndicator`) | Blank `IconHeader` slot in label row |
| No / broken Graphic overlay | `AlarmHeader` overlay at Graphic (−2,−2) |
| Border with `border-box` shrunk SVG (weird pipes/coils, partial edge look) | `content-box` border on Graphic |
| StatusIndicator could sit off-center under temp | StatusIndicator forced full-width + center |
| Status mode overhaul on ticket branch | Left alone (main short codes) |

### Files changed (primary)

- `…/03_Elements/01_Status/AlarmHeader/` (new)
- `…/03_Elements/01_Status/IconHeader/` (new)
- `…/03_Elements/01_Status/Icons/Alarms/{Critical,High,Medium,Low,Blank}/` (new, Scout SVG ports)
- `…/01_Devices/{Evaporator,EvaporatorDual,EvaporatorTriple,Pump,ExhaustFan,CoolingTower,Compressor}/view.json`
- `…/01_Status/StatusIndicator/view.json`
- `…/stylesheet/stylesheet.css` (+ resource signatures via repair script)

### How to verify

1. Checkout `feature/scout-alarm-icon-header`, ensure gateway RUNNING, `python scripts/repair-resource-signatures.py --check`, POST scan/projects.
2. Open client: `http://127.0.0.1:19088/data/perspective/client/BH/evaporators`
3. Force demo alarm on one device (Designer Tag Browser or memory write):
   - `[default]Evaporators/EV-04/_Alarms/_Active = true`
   - `_ActiveHighPriority = 1` (critical red) or `3` (medium / orange triangle)
   - `_Unack = true` to see flash
4. Expect: red/orange border around Graphic, priority badge top-left on border, blank IconHeader left of label, StatusIndicator centered under AnalogValue.
5. Repeat on Pumps / CT / etc.

### Screenshots

Captured under `verify-screenshots/` (local; may show layout with gateway “No Connection” banner if OPC/session was flaky after a gateway password-reset/commissioning incident during implementation):

- `verify-screenshots/scout-alarm-evaporators.png`
- `verify-screenshots/scout-alarm-pumps.png`

### Lab notes / incidents during this work

- Prior agent ran `gwcmd -p` which put the gateway into commissioning; completed and restored `admin` / `.env` password.
- API scan briefly returned 403 until `security-properties` `writePermissions` regained `API Token/Write` (commissioning had dropped it). Confirm scan works: POST `/data/api/v1/scan/projects` with token from `docs/cloud-agent/ignition-scan.json`.
- Do **not** keep demo `_Active=true` values in committed `udts.json` (restored before commit).

### Blank / TODO (Dylan)

- Fill `IconHeader` symbols (cone / info / Fault / Operator / Disabled / OOS) — structural slot only for now.
- Optional: add numeric active-alarm **count** tag if product wants Scout “count” instead of priority glyph.
- Visual QA all four themes once live alarms are forced with a healthy gateway connection.

### Open questions

1. Prefer priority letter/digit glyphs (current Scout port) vs a true count badge?
2. Should Medium triangle be used on pumps too, or square-only for BH refrigeration devices?
3. Keep label-row FaceplateIcon, or move faceplate affordance elsewhere once IconHeader fills in?

### Continue from here

1. Force `_Alarms` on EV-04 + one Pump with a healthy client session; confirm border + badge.
2. Theme pass (light/dark/high-contrast).
3. Design IconHeader icons → wire `custom.icons.*` (or quality tags like Scout OPER/OOS).
4. Open PR referencing this handoff; close/link Monday `12654167899` if this supersedes that draft.
5. Avoid merging the layout-broken `ticket/12654167899-ev01-status` branch as-is.
