# REQUIREMENTS — Groveport KPI Nav (v1.1 slice)

## REQ-KPI-01 — Nav date/time
Docked Navigation shows current date and time under the search control, updating live (session/client clock OK).

## REQ-KPI-02 — Home KPI cards
Landing/Globe area presents Lightspeed-style metric cards (layout/visual parity with MapLayout KPI cards). Views only; values may be params or placeholders.

## REQ-KPI-03 — Sample data retained
`docs/kpi/Utility Tracker_template.xlsx` committed as the KPI reference workbook (CO2, kWh, Therm, H2O, Production lb, Temp).

## REQ-KPI-04 — Placeholder tags
Memory (or similar) placeholder tags for EPMS, Utility, and Production metrics seeded from sample workbook columns/KPI names. Document mapping for future DB/historian swap.

## REQ-KPI-05 — Groveport KPI dashboards
Perspective views for Groveport site/area KPI dashboards patterned on Lightspeed Site/Building Overview + Dashboard pages. Domains: EPMS, Utility, Production.

## REQ-KPI-06 — Hierarchical nav
Nav tree: Boars Head → Groveport → Area (e.g. Freezer, Machine Room, …) → EPMS | Utility | Production, with page routes to the new dashboards.

## Non-goals
Historian queries, production OPC, full Lightspeed multi-customer clone.
