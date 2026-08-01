# Faceplate plan — shared shell + typed Controls

**Status:** Pump is the reference implementation (merged / on `main` as of 2026-08-01).  
**Goal:** One Faceplate shell for all devices; device-specific UI lives in typed Controls modules under `_Assets/<Type>/Controls`.

Use this doc when continuing Machine Room faceplate work in a new session.

---

## Architecture (do this, not the alternatives)

| Approach | Verdict |
|----------|---------|
| **One shell + typed Controls** | **Chosen** — already how BH is structured |
| Literally one Controls UI for every device | Reject — different UDTs / commands / KPIs |
| Full faceplate view per device | Reject — duplicates chrome/tabs/trend/alarms |

```
Device graphic / nav click
  → shared.Alerts.showFaceplate(tagPath, deviceType=…)
      popup id: comp-fp-<tagPath>
  → 01_Popups/00_Faceplates/Faceplate   (shell: header, tabs, Close)
      Controls tab → 01_Popups/00_Faceplates/_Assets/<Type>/Controls
      Shared tabs  → _Assets/Configuration | Interlocks | Trend | AlarmConfiguration | Alarms
```

Thin wrappers under `01_Popups/00_Faceplates/<Device>/` still exist for some nav `viewPath`s; prefer opening the **shell** with `deviceType` going forward (Pump graphic already does).

---

## Key paths

| Piece | Path |
|-------|------|
| Shell | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Faceplate/` |
| Pump Controls (reference) | `…/01_Popups/00_Faceplates/_Assets/Pump/Controls/` |
| Pump wrapper (optional) | `…/01_Popups/00_Faceplates/Pump/` |
| Device graphic | `…/02_Components/01_Devices/Pump/` |
| Machine Room page | `…/00_Pages/Machine Room/Overview/` |
| Open API | `…/ignition/script-python/shared/Alerts/code.py` → `showFaceplate` |
| Nav open helper | `…/ignition/script-python/Navigation/Faceplate/code.py` |
| Faceplate CSS | `…/stylesheet/stylesheet.css` (`.psc-faceplate-*`) |
| Pump UDT | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json` (`Devices/Pump`) |
| Plant instances | `[default]Plant/Machine Room/HTLR-Pump 1` (etc.) → OPC under `[default]RCP1/…` |
| Helper script | `scripts/_pump_faceplate_reference.py` |
| Prior UDT trim notes | `.planning/quick/260731-5un-*/PHASE-pump.md` |

Faceplates live **only** under `01_Popups/00_Faceplates/` (never recreate `01_Faceplates/`). HBT → `shared`.

---

## What landed for Pump (reference)

1. Machine Room four pumps: `faceplate: "Pump"` (was blank → click no-op).
2. Pump graphic click → `shared.Alerts.showFaceplate(..., deviceType='Pump')` → popup id `comp-fp-*`.
3. Shell Close closes `comp-fp-*`, `fp-*`, and legacy `pump-fp-*`.
4. Controls layout: **Mode** (Maint/Prog/Oper) → **Faults** (FTS / IOF / FTS-STS text codes) → **Status** (`Val_Sts` + Start/Stop/Reset) → **KPI** (runtime hrs, starts, fail timer, min runtime).
5. CSS: `.psc-faceplate-fault-*` (status text + class; not color-only).

Shell still auto-shows Configuration / Interlocks / Trend / Alarm tabs from tag browse flags.

---

## Conventions for the next agent

### Opening faceplates
- Prefer `shared.Alerts.showFaceplate(tagPath=…, deviceType='Pump'|…)` from device graphics.
- Popup id must stay `comp-fp-%s` so shell Close works.
- Machine Room embeds need a truthy `params.faceplate` (e.g. `"Pump"`) or the graphic returns early.

### Controls modules
- Put device-unique UI in `_Assets/<Type>/Controls/view.json` only.
- Bind PLC leaf names on the UDT (`Sts_*`, `OCmd_*`, `Val_*`, `Alm_*`) via `/Value` for Digitals.
- Shared tabs stay generic; don’t fork Trend/Alarms per device unless required.
- Ticket Logger on every new/edited view root (see `.cursor/rules/perspective-ticket-logger.mdc`).
- Styling: Advanced Stylesheet classes only (`.cursor/rules/perspective-css-only.mdc`).
- ISA-101: grayscale normal; saturated color for abnormal; always include a text status code.

### After edits
```text
python scripts/repair-resource-signatures.py --path <resource.json>
POST /data/api/v1/scan/config
POST /data/api/v1/scan/projects
```
Token/port: `docs/cloud-agent/ignition-scan.json` or `.env`.  
Do not commit RCP1 `udts.json` ↔ nested `tags.json` scan churn or StoreAndForward junk.

### Do not
- Invent a parallel faceplate tree.
- Reintroduce old ExhaustFan leaf names (`OPER` / `Cmd_*`) onto Pump.
- Hide amCharts watermark without a commercial license (unrelated but noted elsewhere).
- Use Designer Style Classes / path-style `Fonts/…` classes.

---

## Suggested next work (priority)

### P0 — Prove Pump end-to-end on plant
1. Hard refresh `/machine-room` → HTLR-Pump 1 → Controls → Close.
2. Confirm Interlocks / Configuration tabs with live RCP1 quality.
3. Exercise Start/Stop/Reset and mode chips (respect `session.custom.ReadOnly`).

### P1 — Finish Pump Controls polish
4. Align fault chip tooltips / labels with operator language.
5. Verify `Fail_Timer_PRE` / `Min_Runtime_Set` eng units; writable fields belong on Configuration tab if operators edit them.
6. Optional: secondary running indication (`Sts_Running`) if Val_Sts alone is unclear.
7. Capture updated screenshot → `docs/handoff/fp-controls-Pump.png`.

### P2 — Clone pattern to other Machine Room motors
8. **ExhaustFan** — rename Controls bindings to P_Motor-style leaves (Pump is the template); wire Machine Room `faceplate`; use `showFaceplate`.
9. **Compressor** — already deeper Controls; migrate opener/Close to `comp-fp` / `showFaceplate` if not already.
10. **CoolingTower / Sensor / Valve / Tank** — same open path + Controls completeness pass.
11. Machine Room Overview: set remaining empty `faceplate` params for devices that have Controls assets.

### P3 — Cleanup
12. Migrate Unit Overview / nav entries from wrappers to shell + `deviceType` where easy.
13. Fix or remove broken page-config `/pumps` routes pointing at missing Overview/Graphic views.
14. Keep DesignOverview sim `Pumps/PMP-*` separate from plant `[default]Plant/Machine Room/…` paths.

---

## DeviceType → Controls map (shell)

| `deviceType` | Controls path |
|--------------|---------------|
| Pump | `_Assets/Pump/Controls` |
| Compressor | `_Assets/Compressor/Controls` |
| ExhaustFan | `_Assets/ExhaustFan/Controls` |
| Evaporator | `_Assets/Evaporator/Controls` |
| CoolingTower | `_Assets/CoolingTower/Controls` |
| Sensor | `_Assets/Sensor/Controls` |
| Tank | `_Assets/Tank/Controls` |
| Valve | `_Assets/Valve/Controls` (SolenoidValve wrappers map here) |

---

## Paste into next session

```text
Continue BH faceplate work using docs/handoff/faceplate-shell-typed-controls-plan.md.
Architecture: shared Faceplate shell + typed _Assets/<Type>/Controls. Pump is the reference.
Plant path: /machine-room → HTLR-Pump 1. Open via shared.Alerts.showFaceplate (comp-fp id).
Next: verify Pump on plant, then port ExhaustFan to the same opener + leaf naming pattern.
Rules: Ticket Logger on views; CSS-only styling; repair-resource-signatures + scan after edits;
no RCP1 scan churn commits; faceplates only under 01_Popups/00_Faceplates/.
```

---

## Related session notes (2026-08-01)

- Globe home + enterprise nav + Groveport plant overview are on `main`.
- Collapsible left nav + right Legend docks are on `main` (Legend uses NotificationIcons Critical/High/Medium/Low).
- amCharts logo on globe: free-license watermark; needs commercial license to remove.
