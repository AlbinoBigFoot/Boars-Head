# Handoff Log

## Handoff: 2026-08-01 — Faceplate shell + Pump reference

### Current Task State
Machine Room faceplate work started with **Pump** as the shared-shell + typed-Controls reference. Merged to `main`. Continuing faceplates later at home — use the plan doc below.

### Key Decisions
- **One Faceplate shell + `_Assets/<Type>/Controls`** (not one mega Controls UI, not full faceplates per device).
- Open via `shared.Alerts.showFaceplate` → popup id `comp-fp-*`.
- Pump Controls: Mode → Faults → Status/cmds → KPI.

### Plan for next agent
**Read first:** [`docs/handoff/faceplate-shell-typed-controls-plan.md`](faceplate-shell-typed-controls-plan.md)

### Next Steps
1. Verify `/machine-room` → HTLR-Pump 1 open/close on plant.
2. Polish Pump Controls if needed.
3. Port ExhaustFan (and other MR devices) to same opener + leaf naming.

### Critical Context
- Do not commit RCP1 udts/tags scan churn.
- Faceplates only under `01_Popups/00_Faceplates/`.
- Repair signatures + scan after Perspective edits.

---

## Prior: RCP1 Simulate mode

**Branch:** `cursor/rcp1-simulate-fix-eb66` (PR #7)

### SIM ON polish (verified 2026-08-01)

- Device labels = instance names (`COMP 1`, `HTLR-Pump 1`, `HTR`, …)
- Pumps: `Val_Sts` 2=RUN / 1=STOP
- Tanks: no OK status chrome (Status row only for abnormal / COMM LOSS)
- Compressors / Main Liq SV: `Comm=False` + discrete Alm bits cleared — no medium alarm chrome
- Sensors: PV seeded (HSS 145 / HSL 42 / LSL 28 / LSS 18 psig)
- HSD-PT3 retargeted from missing `[default]Sensors/HSS-PT` → Plant `…/HSS-Pumps Pressure`
- OPL 1 embeds retargeted from missing `[default]Valves/MAIN-LIQ-SV` → Plant `…/Main Liq SV`
- Stub Compressor Amps/FLA/SVP/DisP Hi/Lo@0 remain disabled

### Scan order

1. `python scripts/repair-resource-signatures.py` (after project edits)
2. `POST /scan/config` then `POST /scan/projects`
3. Toggle SIM OFF→ON to re-seed demo values

### Note

`system.tag.configure` may rewrite RCP1 folders (`udts.json` ↔ nested `tags.json`). Prefer not committing that churn; SIM seed + project scripts are the durable fix.
