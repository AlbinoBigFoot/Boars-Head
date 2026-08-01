# Handoff — RCP1 Simulate mode

**Branch:** `cursor/rcp1-simulate-fix-eb66` (PR #7)

## SIM ON polish (verified 2026-08-01)

- Device labels = instance names (`COMP 1`, `HTLR-Pump 1`, `HTR`, …)
- Pumps: `Val_Sts` 2=RUN / 1=STOP
- Tanks: no OK status chrome (Status row only for abnormal / COMM LOSS)
- Compressors / Main Liq SV: `Comm=False` + discrete Alm bits cleared — no medium alarm chrome
- Sensors: PV seeded (HSS 145 / HSL 42 / LSL 28 / LSS 18 psig)
- HSD-PT3 retargeted from missing `[default]Sensors/HSS-PT` → Plant `…/HSS-Pumps Pressure`
- OPL 1 embeds retargeted from missing `[default]Valves/MAIN-LIQ-SV` → Plant `…/Main Liq SV`
- Stub Compressor Amps/FLA/SVP/DisP Hi/Lo@0 remain disabled

## Root causes fixed this pass

1. **Medium alarm chrome** — `Comm` Equality@1 (High) maps UI case→CSS medium; disk/runtime had `Comm=True`
2. **Blank sensors** — Status seed matched `"Pump"` inside `*-Pumps Pressure` (wrong); Value defaults were 0; HSD-PT3 hard-coded missing path
3. **OPL COMM LOSS** — hard-coded `[default]Valves/MAIN-LIQ-SV` missing

## Scan order

1. `python scripts/repair-resource-signatures.py` (after project edits)
2. `POST /scan/config` then `POST /scan/projects`
3. Toggle SIM OFF→ON to re-seed demo values

## Note

`system.tag.configure` may rewrite RCP1 folders (`udts.json` ↔ nested `tags.json`). Prefer not committing that churn; SIM seed + project scripts are the durable fix.
