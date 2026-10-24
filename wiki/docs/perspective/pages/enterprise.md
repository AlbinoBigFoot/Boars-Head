---
title: Enterprise Demo Pages
sidebar_position: 14
description: The enterprise demo pages (globe, site dashboards, Production levels, area EPMS / Production KPIs, plant placeholders) that are hidden in local Groveport mode.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/page-config/config.json"
  - "docs/local-groveport-mode.md"
last_verified: 2026-10-24
---

# Enterprise Demo Pages

These pages are still in the project but are **unreachable in local Groveport mode** (the default): their nav nodes
carry `data.hidden` + `data.demo`, and the Header route guard redirects their URLs to the Utility Overview. They
come back by setting `[default]_Config/DemoEnterpriseNav` to `true` in the Tag Browser (see
[Navigation](../navigation.md#local-vs-enterprise-mode)). No screenshots: the lab runs in local mode.

| Route | View | What it is |
|---|---|---|
| `/enterprise` | [`00_Pages/Boars Head/LandingPage/Globe`](../reference/views/00-pages/boars-head/landingpage/globe.md) | Boar's Head International: a globe of the plants (WebDev resource `globe`, `shared.Globe`) |
| `/plants/new-castle`, `/plants/forrest-city`, `/plants/petersburg`, `/plants/holland` | [`LandingPage/PlantPlaceholder`](../reference/views/00-pages/boars-head/landingpage/plantplaceholder.md) | Placeholder per other plant |
| `/plants/groveport` | [`00_Pages/Groveport/Site/Overview`](../reference/views/00-pages/groveport/site/overview.md) | Groveport site overview (site cards, KPIs) |
| `/plants/groveport/classic`, `/plants/groveport/executive` | `Site/OverviewClassic`, `Site/OverviewExecutive` | Alternative site dashboards |
| `/plants/groveport/production-overview` | [`Production/Level1/Overview`](../reference/views/00-pages/groveport/production/level1/overview.md) | Production Overview (FCM line KPIs, `docs/production-overview.md`) |
| `/plants/groveport/production/level-2/prep`, `/forming`, `/packaging` | `Production/Level2/*` | Level 2 zones |
| `/plants/groveport/production/<machine>` (vat-dumper, hopper, handtman, loaders, roll-stock, shrink-tunnel, lazy-susan) | `Production/Level3/*` | Level 3 machines |
| `/plants/groveport/<area>/epms`, `/<area>/production` (16 routes) | [`00_Pages/Groveport/Area/DomainKpis`](../reference/views/00-pages/groveport/area/domainkpis.md) | Area KPI pages; the view reads the area and domain from the URL |

Their KPI values are memory placeholders (`KPI/Groveport/**`, FCM tags, `shared.ProductionMetrics`), not live
data; see `docs/sim-removal.md`. The widget components they use are `02_Components/02_Widgets/KPI`, `MetricCard`
and `SiteCard`. Edit them in the Designer like any other view; keep the Header route guard list
(`custom.localRouteGuard`) in step when you add an enterprise route.
