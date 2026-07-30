---
quick_id: 260730-mun
slug: device-udt-faceplate-controls-sweep-pump
phase: 260730-mun-device-udt-faceplate-controls-sweep-pump
plan: 01
subsystem: ui
tags: [ignition, perspective, faceplate, devices, udt, controls, pushover, sim]
status: complete
date: 2026-07-30
completed: 2026-07-30
duration: ~
branch: feature/demo-tank-tags
requires:
  - phase: 260730-m0m
    provides: Shared Faceplate Controls/Config/Interlocks pattern for Compressor
provides:
  - Devices UDTs expanded for Pump, ExhaustFan, Valve, Tank, Sensor, Evaporator, CoolingTower
  - Plant sim FOLDERS + Controls-grade leaves for Valves/Tanks/Sensors
  - Per-device `_Assets/{Type}/Controls` Mode→Status→KPI embeds
  - Unified Faceplate case(deviceType) + device openers with deviceType
  - Pushover Controls screenshots for all 8 device types (D-07)
affects: [shared-faceplate, device-hmi, plant-sim]
tech-stack:
  added: []
  patterns:
    - Faceplate Controls path case(deviceType) → `_Assets/{Device}/Controls`
    - Header Web GUI only when deviceType=Compressor && webGuiUrl non-empty
    - Device graphic → Navigation.Faceplate.openFaceplate(..., deviceType=…)
key-files:
  created:
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Pump/Controls/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/CoolingTower/Controls/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Valve/Controls/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Tank/Controls/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Sensor/Controls/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Evaporator/Controls/view.json
    - docs/handoff/fp-controls-Compressor.png
    - docs/handoff/fp-controls-Pump.png
    - docs/handoff/fp-controls-ExhaustFan.png
    - docs/handoff/fp-controls-CoolingTower.png
    - docs/handoff/fp-controls-Valve.png
    - docs/handoff/fp-controls-Tank.png
    - docs/handoff/fp-controls-Sensor.png
    - docs/handoff/fp-controls-Evaporator.png
  modified:
    - gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json
    - sim/build_plant_sim.py
    - sim/bh-plant-sim.csv
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Faceplate/view.json
    - gateways/standard/data/projects/BH/ignition/script-python/shared/Alerts/code.py
    - scripts/pushover_nav_screenshots.py
key-decisions:
  - "Evaporator Status remains HMI simplified enum (Option B); PLC Sts_State 0–10 mapped below"
  - "Web GUI header-only for Compressor; never in Controls body or other types"
  - "C1 fixed Faceplate view.json trailing comma that blocked gateway deserialize (View Not Found)"
requirements-completed: [D-01, D-02, D-03, D-04, D-05, D-06, D-07, D-08]
---

# 260730-mun — Device UDT + Faceplate Controls sweep

## Status: complete

Wave C (C1) Playwright proof + Pushover delivered. Waves A/B shipped UDTs, sim, Controls assets, and Faceplate/opener wiring.

## What shipped (all waves)

- **Devices UDTs:** Pump/ExhaustFan motor pattern (Flow/Airflow KPIs); Valve without Temp; Tank level/alarms; Sensor `_Root/Analog` PV + limits; Evaporator defrost/enable leaves; CoolingTower motor Controls/Interlock.
- **Sim:** FOLDERS include Valves/Tanks/Sensors; CSV regen with Controls-grade leaves.
- **Controls assets:** `_Assets/{Pump,ExhaustFan,CoolingTower,Valve,Tank,Sensor,Evaporator}/Controls` Mode→Status→KPI stacks.
- **Faceplate shell:** `hasControlsAsset` + `case(deviceType)` for all eight types; device openers pass `deviceType` (SolenoidValve* → Valve).
- **D-01 verify:** COMP-01 header shows **Web GUI**; Pump/ExhaustFan/CoolingTower/Valve/Tank/Sensor/Evaporator do **not**.

## C1 capture notes

1. Reset trial via `POST /data/api/v1/trial` (expired at start).
2. Initial COMP-01 open → **View Not Found** — root cause: illegal trailing comma in `Faceplate/view.json` propConfig (gateway `Unable to deserialize view`). Removed comma, repaired signature, scan/projects; retry succeeded.
3. Captured Controls tab for: COMP-01, PMP-01, EFAN-01, CT-01, valve wall instance, LTR-01, sensor wall instance, EV-01.
4. Valve/Sensor wall labels don't always show instance names in a11y tree (status tokens / SNS stubs); opened via status click; Controls content verified.

## Evaporator PLC → HMI Status map (Option B)

| PLC `Sts_State` | PLC meaning | HMI `Status` (simplified) |
|-----------------|-------------|---------------------------|
| 0 | Off | 0 STOP |
| 1 | Pump Out | 2 DFT (defrost family) |
| 2 | Soft Hot Gas | 2 DFT |
| 3 | Main Hot Gas | 2 DFT |
| 4 | Bleed | 2 DFT |
| 5 | Fan Delay | 2 DFT |
| 6 | Cooling | 1 CLG |
| 7 | Idle | 5 IDLE |
| 8 | Cleanup | 5 IDLE (or DFT if cleanup treated as sequence) |
| 9 | Permissive | 0 STOP |
| 10 | Interlock | 3 FLT |

HMI enum used by StatusIndicator: **0=STOP, 1=CLG, 2=DFT, 3=FLT, 5=IDLE**.

## Pushover (D-07)

| PNG | Title | HTTP |
|-----|-------|------|
| `docs/handoff/fp-controls-Compressor.png` | BH Controls: Compressor | 200 status=1 |
| `docs/handoff/fp-controls-Pump.png` | BH Controls: Pump | 200 status=1 |
| `docs/handoff/fp-controls-ExhaustFan.png` | BH Controls: ExhaustFan | 200 status=1 |
| `docs/handoff/fp-controls-CoolingTower.png` | BH Controls: CoolingTower | 200 status=1 |
| `docs/handoff/fp-controls-Valve.png` | BH Controls: Valve | 200 status=1 |
| `docs/handoff/fp-controls-Tank.png` | BH Controls: Tank | 200 status=1 |
| `docs/handoff/fp-controls-Sensor.png` | BH Controls: Sensor | 200 status=1 |
| `docs/handoff/fp-controls-Evaporator.png` | BH Controls: Evaporator | 200 status=1 |

**Sent: 8 of 8.** Script: `scripts/pushover_nav_screenshots.py` (default Controls set; `--nav` for legacy nav shots).

## Follow-ups (non-blocking)

- Sensors Overview wall still shows SNS / COMM LOSS chrome while tagPaths point at LSS-PT etc. — faceplate opens; graphic label/quality polish deferred.
- Valves Overview cards may not expose instance name as exact a11y text — opener works via status click.
- Commit Faceplate trailing-comma fix with project resources if not already in Wave B commit.
