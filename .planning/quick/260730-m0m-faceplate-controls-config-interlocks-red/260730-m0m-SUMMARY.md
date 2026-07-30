---
quick_id: 260730-m0m
slug: faceplate-controls-config-interlocks-red
phase: 260730-m0m-faceplate-controls-config-interlocks-red
plan: 01
subsystem: ui
tags: [ignition, perspective, faceplate, compressor, interlocks, configuration, css]
status: complete
date: 2026-07-30
completed: 2026-07-30
duration: 25min
branch: feature/demo-tank-tags
requires:
  - phase: 260730-l0s
    provides: Shared Faceplate shell with Trend/Alarms working + CSS faceplate-* tokens
provides:
  - Devices/Compressor Mode Cmd KPI Config writables + 16-ch Interlock mirror + sim rows
  - Controls section stack Mode→Status/commands→KPI→Web GUI
  - Scout-like Configuration browse under _Assets/Configuration
  - FT P_Intlk-style Interlocks tab + InterlockRow
  - Faceplate tagFlags empty-tab hide + showInterlocks + webGuiUrl demo
affects: [shared-faceplate, compressor-hmi, pumps-config-later]
tech-stack:
  added: []
  patterns:
    - Scout browse writable non-alarm leaves → ConfigurationRow → AnalogInput|MultiStateInput
    - Faceplate tagFlags AND caller show* for tab visibility
    - Interlock bitfields (Sts_Intlk / Cfg_Bypassable) + Cfg_CondTxtNN labels
key-files:
  created:
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/00_Control/AnalogInput/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/00_Control/MultiStateInput/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Configuration/Configuration/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Configuration/ConfigurationRow/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Interlocks/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/InterlockRow/view.json
  modified:
    - gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json
    - sim/build_plant_sim.py
    - sim/bh-plant-sim.csv
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Compressor/Controls/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Faceplate/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/stylesheet/stylesheet.css
    - gateways/standard/data/projects/BH/ignition/script-python/shared/Alerts/code.py
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Compressor/view.json
key-decisions:
  - "Interlocks tab sits between Configuration and Trend; defaultTab order Controls→Configuration→Interlocks→Trend→Alarm Configuration→Alarms"
  - "Cmd_Auto/Manual/Remote also write CP_Mode/Value 2/3/1 as secondary mode feedback"
  - "Device opener defaults empty webGuiUrl to https://127.0.0.1/ lab placeholder"
  - "Do not commit projects/.resources gateway churn; repair-resource-signatures for CAS"
requirements-completed: [D-01, D-02, D-03, D-04, D-05]
coverage:
  - id: D1
    description: Controls Mode→Status/commands→KPI→Web GUI with demo commands/KPI/webGuiUrl
    requirement: D-01
    verification:
      - kind: unit
        ref: plan Task2 assert OPER/Cmd_Start/RuntimeHours/webGuiUrl/faceplate-section
        status: pass
    human_judgment: true
    rationale: Visual Mode chips, command buttons, KPI layout, and openURL need COMP-01 Faceplate session
  - id: D2
    description: Configuration browse lists writable non-alarm leaves via AnalogInput/MultiStateInput
    requirement: D-02
    verification:
      - kind: unit
        ref: plan Task2 assert system.tag.browse + AlarmEvalEnabled + ConfigurationRow
        status: pass
    human_judgment: true
    rationale: Confirm browsed rows appear for COMP-01 writables in live gateway
  - id: D3
    description: Empty tabs hide via tagFlags; Interlocks shows when Interlock data exists
    requirement: D-03
    verification:
      - kind: unit
        ref: plan Task3 assert tagFlags + showInterlocks + embed paths
        status: pass
    human_judgment: true
    rationale: Tab chrome hide/show depends on live tag quality under COMP-01 vs non-Interlock device
  - id: D4
    description: Interlocks 16-ch FT-style with CondTxt, OK/FLT, bypass gated by Cfg_Bypassable + ReadOnly
    requirement: D-04
    verification:
      - kind: unit
        ref: plan Task1 Interlock members + Task2 Interlocks/InterlockRow asserts
        status: pass
    human_judgment: true
    rationale: Channel labels/status/bypass interaction needs operator smoke
  - id: D5
    description: Professional faceplate CSS; Trend/Alarm Configuration/Alarms still wired
    requirement: D-05
    verification:
      - kind: unit
        ref: plan Task2 CSS faceplate-interlock/section + Task3 embed path case keeps Trend/Alarms
        status: pass
    human_judgment: false
---

# Phase 260730-m0m Plan 01: Faceplate Controls/Config/Interlocks redesign Summary

**Compressor Faceplate now has Mode/Status/commands/KPI/Web GUI Controls, Scout-style Configuration browse, FT-style Interlocks tab, and tagFlags that hide empty tabs — with Devices Interlock mirror + sim demo data.**

## Performance

- **Duration:** ~25 min
- **Started:** 2026-07-30T16:04:53Z
- **Completed:** 2026-07-30T20:20:00Z
- **Tasks:** 3/3
- **Files modified:** ~25 authored (plus sim CSV / signatures)

## Accomplishments

- Expanded `Devices/Compressor` with OPER/MAINT/PROG, Cmd_*, runtime KPIs, AutoEN/Min_Runtime_Set/Fail_Timer_PRE, and 16-channel Interlock folder; sim CSV covers demo paths
- Rebuilt Controls under `_Assets/Compressor/Controls`; ported AnalogInput/MultiStateInput + Configuration browse; added Interlocks/InterlockRow
- Wired Faceplate `tagFlags` + Interlocks tab; retargeted Configuration embed; demo `webGuiUrl`; signatures `--check` clean; scan/projects + scan/config 200

## Task Commits

1. **Task 1: Devices/Compressor UDT + Interlock + sim** - `3c446da` (feat)
2. **Task 2: Controls + Config + Interlocks views + CSS** - `f6be7b1` (feat)
3. **Task 3: Faceplate tagFlags + Interlocks tab + webGuiUrl + signatures** - `e24b8ac` (feat)

**Plan metadata:** (pending docs commit)

## Files Created/Modified

- `Devices/udts.json` — Compressor Mode/Cmd/KPI/Config/Interlock members
- `sim/build_plant_sim.py` + `sim/bh-plant-sim.csv` — faceplate demo Sim rows
- `03_Elements/00_Control/{AnalogInput,MultiStateInput}` — Scout editors with writeBlocking + ReadOnly
- `_Assets/Configuration/{Configuration,ConfigurationRow}` — browse + row routing
- `_Assets/Interlocks` + `_Assets/InterlockRow` — FT-style 16 channels
- `_Assets/Compressor/Controls` — section stack Mode→Status→KPI→Web GUI
- `Faceplate/view.json` — tagFlags, Interlocks tab, embed retargets
- `shared/Alerts/code.py` — `showInterlocks` on `showFaceplate`
- Device Compressor + thin wrapper — webGuiUrl demo + showInterlocks
- `stylesheet.css` — faceplate-section-card, cmd buttons, interlock rows, buttons-6

## Decisions Made

- Interlocks tab order: after Configuration, before Trend
- Auto/Manual/Remote commands pulse Cmd_* and set `CP_Mode/Value` to 2/3/1
- Lab Web GUI default: `https://127.0.0.1/` when opener param empty
- Caller `show*` ANDed with `tagFlags` so openers can force-hide; empty tabs still auto-hide

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 2 - Critical] Removed wrongly nested Faceplates/Compressor/{Controls,Configuration}**
- **Found during:** Task 3 commit staging
- **Issue:** Legacy Controls/Configuration lived under the thin `Faceplates/Compressor/` wrapper folder (violates never-nest-under-view-folder / live embeds are `_Assets/...`)
- **Fix:** Deleted nested pair; live embeds remain `_Assets/Compressor/Controls` and `_Assets/Configuration/Configuration`. Left unused `_Assets/Compressor/Configuration` alone if present
- **Files modified:** deleted `01_Popups/00_Faceplates/Compressor/Controls/*`, `.../Configuration/*`
- **Committed in:** `e24b8ac`

**2. [Rule 1 - Bug] MultiStateInput options/value bindings incomplete in Scout export**
- **Found during:** Task 2
- **Issue:** Scout MultiStateInput had broken `{value}` options/value without path; used HBT/APIModule
- **Fix:** Tag-bound value, metadata/Boolean options script, writeBlocking, no HBT
- **Committed in:** `f6be7b1`

## Threat Mitigations

| ID | Disposition | Implementation |
|----|-------------|----------------|
| T-260730-m0m-01 | mitigate | Writes gated by `session.custom.ReadOnly`; bypass further gated by `Cfg_Bypassable` bit |
| T-260730-m0m-02 | mitigate | openURL only when non-empty webGuiUrl; lab default is local placeholder from opener |
| T-260730-m0m-04 | mitigate | `repair-resource-signatures.py` + `--check` exit 0 |
| T-260730-m0m-05 | mitigate | Scout browse filters; Interlocks fixed 16 rows |

## Known Stubs

None that block the plan goal. Old `_Assets/Compressor/Configuration` (hardcoded FLA/SVP/DisP) left unused by shell retarget — intentional per plan.

## Verification

- Task 1–3 automated asserts: pass
- `python scripts/repair-resource-signatures.py --check`: 0 issues
- POST scan/projects + scan/config: HTTP 200
- Manual smoke (operator): COMP-01 Faceplate Controls/Config/Interlocks/Web GUI + Trend/Alarms

## Self-Check: PASSED

- FOUND: Controls, Configuration, Interlocks, Faceplate view.json artifacts
- FOUND commits: `3c446da`, `f6be7b1`, `e24b8ac`
