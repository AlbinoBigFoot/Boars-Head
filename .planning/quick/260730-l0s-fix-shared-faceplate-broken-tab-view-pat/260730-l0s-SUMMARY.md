---
quick_id: 260730-l0s
slug: fix-shared-faceplate-broken-tab-view-pat
phase: 260730-l0s-fix-shared-faceplate-broken-tab-view-pat
plan: 01
subsystem: ui
tags: [ignition, perspective, faceplate, apexchart, cas, alarms]
status: complete
date: 2026-07-30
completed: 2026-07-30
duration: 35min
branch: feature/demo-tank-tags
requires:
  - phase: diagnosis
    provides: CAS root cause + Scout Main trend pattern
provides:
  - Controls/Configuration CAS-loadable faceplate tabs
  - alarmstatustable Alarms tab
  - Scout-style in-popup ApexChart Trend with browse pens
  - Readable faceplate tab labels
  - Compressor FLA/SVP/DisP/Amps history on UDT type
affects: [shared-faceplate, compressor-hmi, trending]
tech-stack:
  added: []
  patterns: [Scout browse+HistoryEnabled pens, repair-resource-signatures CAS, CSS-only faceplate-tab-text]
key-files:
  created:
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Trend/view.json
  modified:
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Faceplate/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Alarms/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/AlarmConfiguration/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/stylesheet/stylesheet.css
    - gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json
key-decisions:
  - "Trend stays at _Assets/Trend path; content ported from Scout _Assets/Main (no AdhocTrend)"
  - "Tab contrast via faceplate-tab-text class; header Close keeps font-button on dark chrome"
  - "Do not commit projects/.resources gateway churn; repair script ensures local CAS"
requirements-completed: [D-01, D-02, D-03, D-04, D-05, D-06, D-07]
coverage:
  - id: D1
    description: Controls/Configuration CAS digests present and signatures --check clean
    requirement: D-01
    verification:
      - kind: other
        ref: python scripts/repair-resource-signatures.py --check
        status: pass
    human_judgment: false
  - id: D2
    description: Alarms uses ia.display.alarmstatustable
    requirement: D-02
    verification:
      - kind: unit
        ref: plan Task1 assert AlarmStatusTable type
        status: pass
    human_judgment: false
  - id: D3
    description: Trend is Scout-style ApexChart with browse HistoryEnabled pens (not AdhocTrend)
    requirement: D-03
    verification:
      - kind: unit
        ref: plan Task2 assert kyvislabs + browse + queryTagHistory
        status: pass
    human_judgment: true
    rationale: Visual pen/chart smoke on COMP-01 Faceplate Trend tab needs operator/gateway session
  - id: D4
    description: Faceplate tab labels lack inverse font-button on light chrome
    requirement: D-04
    verification:
      - kind: unit
        ref: plan Task1 assert tab textStyle classes
        status: pass
    human_judgment: false
  - id: D5
    description: Alarm Config short-name list with count title and honest stub
    requirement: D-05
    verification:
      - kind: unit
        ref: plan Task3 assert ticketLog + content strings
        status: pass
    human_judgment: false
  - id: D6
    description: Compressor FLA/SVP/DisP/Amps Value history enabled on type + instances
    requirement: D-06
    verification:
      - kind: unit
        ref: plan Task3 assert historyEnabled/historian
        status: pass
    human_judgment: false
  - id: D7
    description: Signatures --check clean; projects+config scanned
    requirement: D-07
    verification:
      - kind: other
        ref: repair --check exit 0; POST scan/projects + scan/config HTTP 200
        status: pass
    human_judgment: true
    rationale: Runtime Faceplate load (no View Not Found) needs brief client smoke
---

# Quick Task 260730-l0s Summary

**Shared Faceplate tabs fixed: CAS-backed Controls/Config, alarmstatustable Alarms, Scout ApexChart Trend (browse HistoryEnabled pens), readable tab labels, compressor analog history.**

## Performance

- **Duration:** ~35 min
- **Started:** 2026-07-30T15:14:25Z
- **Completed:** 2026-07-30T15:50:00Z
- **Tasks:** 3/3
- **Files modified:** 12+ authored (views, stylesheet, Devices UDT, resource.json)

## Accomplishments

- Repaired Controls/Configuration CAS digests so EmbeddedView paths resolve (paths were already correct)
- Fixed Alarms component type to `ia.display.alarmstatustable`
- Replaced `_Assets/Trend` AdhocTrend stub with Scout `_Assets/Main` pattern (Kyvis ApexChart + recursive browse)
- Added `faceplate-tab-text` CSS; removed inverse `font-button` from five tab labels
- Enabled historian on Devices/Compressor FLA/SVP/DisP/Amps Value tags; instances already had history
- Alarm Config: count title + short aliases + deferred-editors note

## Task Commits

1. **Task 1: CAS + Alarms + tab contrast + Trend params** — `d808179` + `cff5e15` (view.json follow-up)
2. **Task 2: Scout ApexChart Trend** — `5e10e51`
3. **Task 3: History + Alarm Config + signatures/scan** — `2b4bd34`
4. **Plan metadata** — `19ea00d` (docs: SUMMARY + STATE Quick Tasks)

## Files Created/Modified

- `.../Faceplate/view.json` — hiddenFromTrend → hiddenTags; tab textStyle
- `.../_Assets/Alarms/view.json` — alarmstatustable
- `.../_Assets/Trend/view.json` — Scout Main port + ticket logger
- `.../_Assets/AlarmConfiguration/view.json` — short-name UX
- `.../Compressor/Controls|Configuration/{view,resource}.json` — CAS repair + tracked views
- `stylesheet.css` — `.psc-faceplate-tab-text`
- `Devices/udts.json` — Compressor analog Value history flags

## Decisions Made

- Keep BH path `_Assets/Trend`; port Scout Main content (locked: no AdhocTrend)
- Pen discovery is runtime browse + HistoryEnabled/Enabled/numeric — not a deviceType map
- Skip committing `projects/.resources/*` churn; repair ensures digests locally

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 2 - Missing Critical] Controls/Configuration view.json were untracked**
- **Found during:** Task 1 commit
- **Issue:** Only `resource.json` was staged; view bodies needed for CAS content
- **Fix:** Follow-up commit `cff5e15` added both `view.json` files
- **Files modified:** Compressor/Controls/view.json, Compressor/Configuration/view.json
- **Committed in:** `cff5e15`

**2. [Rule 1 - Scope] Left Compressors instance udts.json gateway rewrite uncommitted**
- **Found during:** Task 3
- **Issue:** Working-tree diff after scan reordered/rewrote instance JSON extensively
- **Fix:** Did not stage; instances already satisfied history asserts before rewrite
- **Impact:** Avoids accidental COMP instance churn in git

---

**Total deviations:** 2 auto-handled (1 missing file commit, 1 intentional non-commit)
**Impact on plan:** Plan goals met; no architectural change

## Issues Encountered

- First CAS assert failed mid-task until repair re-wrote digests after scan churn — re-ran repair; `--check` clean

## Known Stubs

- Alarm Configuration setpoint editors still deferred (honest stub copy retained) — intentional per D-05 / CONTEXT out of scope

## User Setup Required

None — no external service configuration required.

## Verification notes

- `python scripts/repair-resource-signatures.py --check` → `0 issue(s) of 138`
- Controls digest `8e9986f21ddad663…` and Configuration `7d969c1579afe498…` present under `projects/.resources/`
- Task 1–3 automated asserts: `task1-ok`, `task2-ok`, `task3-ok`
- `POST /data/api/v1/scan/projects` → 200; `POST .../scan/config` → 200
- Manual smoke still recommended: Faceplate on `[default]Compressors/COMP-01` — Controls/Config load, Alarms table, Trend pens, readable tabs

## Self-Check: PASSED

- SUMMARY path exists
- Commits `d808179`, `cff5e15`, `5e10e51`, `2b4bd34` present on branch
- Key artifacts on disk: Trend/Alarms/Faceplate/stylesheet/Devices udts

## Next Phase Readiness

- Shared Faceplate tabs ready for operator smoke on COMP-01
- Full Scout AlarmConfiguration editor still deferred
- Machine Room Figma approval remains separate Phase 3 blocker

---
*Quick: 260730-l0s*
*Completed: 2026-07-30*
