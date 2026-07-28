---
quick_id: 260727-vma
slug: rebuild-adhoc-trend-multi-plot-ux-n-empt
status: complete
date: 2026-07-27
branch: feature/adhoc-trend-nplots
---

# Quick Task 260727-vma Summary

Rebuild Adhoc Trend multi-plot UX on clean `main`: N empty plots via `+` left of Save, type-based routing, UDT-instance pen names, full-height single plot, unclipped toolbar.

## Outcome

Deliverable is on `feature/adhoc-trend-nplots`. A parallel quick task `260727-vny` landed the core feature first; this task audited against locked CONTEXT, fixed the remaining toolbar/clipping defect (Trend still coord with `height: 0.07`), and verified + scanned.

## Commits

| Commit | Notes |
|--------|-------|
| `0589a1b` | shared.AdhocTrend + session plots/penPlots (vny) |
| `7906943` | Plot asset, FlexRepeater, AddPlot +, UDT pens, routing (vny) |
| `b1d871f` | proportional plot CSS + signatures (vny) |
| `2a910a1` | **fix:** Trend coord→flex PlotToolbar 48px + grow-1 Plots; verify scripts (vma) |

## Must-haves

- `+` (`material/add`) first child of Buttons, left of Save Config → `apply_add_plot` plain-list reassignment
- Single plot fills via flex grow; 2+ equal share (CSS `.psc-adhoc-trend-plots` + instancePosition)
- Toolbar: fixed 48px `PlotToolbar` (no % height bindings on Icons/Buttons)
- Pen labels: `pen_label(.../EV-01/Pressure/Value)` → `EV-01`
- Type routing: float→analog; bool/int→discrete Status plot; no magnitude split
- `plots` / `penPlots` in session + Clear/Load defaults
- Signature check clean; Ignition projects scan HTTP 200; gateway RUNNING

## How to test

1. Open http://localhost:19088/data/perspective/client/BH → Adhoc Trend / trending
2. Confirm gear, Realtime, time-range labels fully visible (page + faceplate)
3. One plot fills chart area; click `+` → new empty plot; 2–3 plots share height equally
4. Add `[default]Evaporators/EV-01/Pressure/Value` → legend/table show **EV-01**
5. Add a boolean → Status/discrete plot created; move pens via Plot dropdown

## Known risks

- Nested UDT paths like `EV-01/Fan 1/CMD` label as `Fan 1` (parent-of-leaf after Value strip) — intentional for nested UDT instances
- Parallel vny/vma race left unused scratch scripts (`_apply_vny_nplots_ui.py`, etc.) untracked — ignore
- Do not commit `.resources/*` gateway churn
- Faceplate Apex z-index / toolbar stacking still worth a visual pass

## Verification

- `python scripts/_verify_adhoc_helpers.py` → OK
- `python scripts/_verify_adhoc_views.py` → OK
- `python scripts/repair-resource-signatures.py --check` → 0 issues
- `POST /data/api/v1/scan/projects` → 200, scanActive true
