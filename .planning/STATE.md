# Project State

## Status

**Phase 3 pilot — Machine Room HMI** (Figma complete; awaiting Dylan approval). Lab (Phase 1) remains up; Phase 2 PLC/UDT work still pending in parallel.

## Current focus

- **Machine Room Figma** done in Dev Jam — page `248:1953`, frame `248:1954` ([link](https://www.figma.com/design/Q8EmmXokQsiX91aPMtLm2w/Dev-Jam?node-id=248-1954)); black piping (provisional); Ignition blocked until Dylan approves
- Context: `.planning/phases/3-hmi-machine-room/CONTEXT.md`
- Quick: shared Faceplate tabs fixed (CAS Controls/Config, Alarms type, Scout Trend, tab contrast)

## Next action

Dylan reviews Machine Room P&ID in Figma → approve → then Ignition import/build.

## Blockers

- Dylan Figma approval before any Ignition Machine Room view
- Open questions in CONTEXT (tag binding timing; Sensor Ignition path; route/nav; valves on screen; piping color revisit)
- Production DB vendor not confirmed (assuming MSSQL for lab)
- Standard ↔ Edge mirror still to validate

## Session notes

- Repo: https://github.com/AlbinoBigFoot/Boars-Head
- Local folder historically named `Bors`; project is Boars-Head
- One Shot = contractor; FBCO = client responsibilities per Excel tracker
- BH components inventory captured in Machine Room CONTEXT (Sensor/Piping gaps noted)
- Figma deliverable: Dev Jam `Q8EmmXokQsiX91aPMtLm2w` / Machine Room — P&ID `248:1954`

### Quick Tasks Completed

| # | Description | Date | Commit | Directory |
|---|-------------|------|--------|-----------|
| 260730-l0s | Fix shared Faceplate broken tabs (CAS, Alarms, Scout Trend, contrast) | 2026-07-30 | 2b4bd34 | [260730-l0s-fix-shared-faceplate-broken-tab-view-pat](./quick/260730-l0s-fix-shared-faceplate-broken-tab-view-pat/) |

Last activity: 2026-07-30 - Completed quick task 260730-l0s: Fix shared Faceplate broken tabs

---
*Updated: 2026-07-30*
