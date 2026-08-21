# Milestone context — Groveport KPI navigation & dashboards

**Branch:** `feat/groveport-kpi-nav-dashboard`  
**Started:** 2026-08-20  
**Change log:** `docs/handoff/CHANGE-LOG-feat-groveport-kpi-nav.md`

## Goal

Make Groveport navigation an intuitive KPI dashboard experience (Lightspeed Site/Building patterns), with EPMS / Utility / Production under each site area, home-page KPI cards near the globe, and a live date/time under nav search. Placeholder tags seeded from Utility Tracker sample; real DB/historian later.

## In scope

1. Date/time under search in docked Navigation
2. Lightspeed-style KPI cards on home/Globe landing — **views only** (params / static placeholders OK; no production tag wiring required on cards)
3. Copy + document `Utility Tracker_template.xlsx` under `docs/kpi/`
4. Placeholder tags for EPMS, Utility, Production metrics derived from that workbook
5. Groveport KPI dashboard views (site + area) referencing Lightspeed Site/Building Overview + Dashboard widgets
6. Nav tree: `Boars Head > Groveport > {Area e.g. Freezer} > EPMS | Utility | Production`

## Out of scope (this milestone)

- Live historian / MSSQL KPI queries
- Pixel-perfect Lightspeed clone of every customer Overview
- Full EPMS PLC integration

## Reference paths

- Lightspeed Frontend: `C:\Users\dylan.jones\Documents\Cursor\Ignition QA\assets\Lightspeed-Frontend\projects\Lightspeed-FrontEnd\`
  - Landing cards: `views/00_Pages/LandingPage/MapLayout/`
  - KPI widget: `views/02_Components/02_Widgets/KPI/`
  - Site/Building Overview: `views/00_Pages/*/Site/Overview`, `.../Building/Overview`
  - Dashboards: `views/00_Pages/Dashboard/`
- BH: `gateways/standard/data/projects/BH/` — Navigation dock, LandingPage/Globe, page-config, TempNav
- Sample data: `docs/kpi/Utility Tracker_template.xlsx` (sheets: Dashboard, Variables, CO2, kWh, Therm, H2O, Production lb, Temp, Daily Temp)

## Success criteria

- [ ] Nav shows readable date/time under search
- [ ] Home has Lightspeed-like KPI card layout (placeholder metrics)
- [ ] Groveport areas expose EPMS / Utility / Production nav leaves with working page routes
- [ ] Placeholder tags exist and are documented; views bind to them or params
- [ ] Change log lists every intentional path; commits stage cleanly without CAS noise
