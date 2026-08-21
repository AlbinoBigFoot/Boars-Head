# Research briefs — Groveport KPI (2026-08-20)

Captured from parallel explore subagents on `feat/groveport-kpi-nav-dashboard`.

## G1 Nav clock — DONE
Sibling `DateTime` label after Search; `now(1000)` + datetime format; `.psc-nav-clock`.

## G2 Home cards — DONE
Lightspeed MapLayout rail (Site widgets), not KPI trend. BH `MetricCard` + Globe `KpiRail` with static EPMS/Utility/Production placeholders.

## G3 Tags — DONE
`[default]KPI/Groveport/{Site|Areas}/{EPMS|Utility|Production}` memory tags; seed script `_seed_kpi_groveport_tags.py`.

## G4 Dashboards — DONE
Shared `Area/Dashboard` + Domains EPMS/Utility/Production + `Site/Overview`; routes `/plants/groveport/{area}/{domain}`.

## G5 Nav tree — DONE
EPMS | Utility | Production prepended under 8 Groveport areas (Navigation + TempNav + `_Config/Navigation`).

