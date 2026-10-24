---
title: Local Vs Enterprise Mode
sidebar_position: 13
description: The one switch between the local Groveport HMI (default, live) and the enterprise demo (other plants, globe, production KPIs) - what each mode shows, how the switch works and how to add plants or areas.
sources:
  - docs/local-groveport-mode.md
  - gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py
last_verified: 2026-10-23
---

# Local Vs Enterprise Mode

## What it does

The BH project contains two HMIs behind **one Boolean tag**, `[default]_Config/DemoEnterpriseNav`:

| | **Local Groveport** (default, live since 2026-10-23) | **Enterprise demo** |
|---|---|---|
| Tag value | `false` | `true` |
| Nav | Boars Head > Groveport > Utility Overview, the areas (Utility folder flattened: Freezer > CG-A1 directly), Machine Room, Condensers, Operations, Admin | adds the other plants (New Castle, Forrest City, Petersburg, Holland), Enterprise Operations, Production Overview + levels 2 / 3, every area's EPMS / Production nodes |
| Boars Head / Groveport / `/` / header logo | Utility Overview (`/plants/groveport/utility-overview`) | `/enterprise` (globe) / `/plants/groveport` (site overview) |
| Boars Head icon | home | globe |
| Enterprise routes | redirect to the Utility Overview | load normally |
| Report Builder Production source | hidden | offered |

Nothing was deleted: every enterprise view, route, tag and nav node stays in the project.

![Local mode: Groveport Utility Overview](/img/features/local-enterprise/local-utility-overview.png)

![Enterprise mode: the globe landing page](/img/features/local-enterprise/enterprise-globe.png)

## How to switch

In the Designer Tag Browser open `[default]_Config` > `DemoEnterpriseNav` and set its value: `false` = local
Groveport (default), `true` = enterprise. No project edit or restart is needed. Open sessions follow on their next nav
refresh or page change (reload to see it at once). Reading the tag tells you the current mode.

:::warning Do not change it by editing tags.json on disk
That blanks the live value. Change it only in the Tag Browser.
:::

## How it works

- **Nav**: nodes carry `data.hidden` + `data.demo` (enterprise only), `data.flattenLocal` (lift a Utility folder's
  children in local mode), `data.localIcon`, `data.localPage` / `data.demoPage`. The Navigation view's Tree
  transform and `Navigation.Nav` (`demoEnabled`, `navigate`, `pageTitle`) read the switch.
- **Routes**: all enterprise routes stay in page-config. The docked Header has `custom.localRouteGuard`: an
  expression that is the Utility Overview path when the switch is off and `page.props.path` is an enterprise route
  (the list of routes is in the expression), else `''`; its change script only calls `system.perspective.navigate`.
  **Fail-safe**: if the tag cannot be read, the guard does not redirect.
- **Titles**: `Navigation.Nav.pageTitle('/')` = "Groveport Utility Overview" (local) or "Boars Head International"
  (enterprise).
- **Reports**: catalog sources with `"deployment": "enterprise"` are hidden in local mode.

Kept on purpose in local mode: Operations (Alarm Status, Alarm Journal, Trending, Saved Trends, Out Of Service Log,
Forms, PLCs > RCP1) and Admin. Operations > Reports is hidden (`data.hidden`).

## Where the pieces live

| Piece | Where |
|---|---|
| Switch tag | `[default]_Config/DemoEnterpriseNav` (`_Config/tags.json`, default `false`) |
| Views | `00_Pages/00_Docked/Navigation` (+ `TempNav`), `00_Pages/00_Docked/Header` |
| Script | `Navigation.Nav` |

## How To Change It

Everything here is a Designer edit; save, then test in a session in **both** modes (flip the tag, reload).

- **New Groveport area:**
  1. Project Browser > Perspective > Views > `00_Pages/00_Docked/Navigation` > root > `custom.items`.
  2. Add the area under Groveport (area > `Utility` folder > pages) with `data.flattenLocal: true` on the `Utility`
     folder; add hidden `EPMS` / `Production` children with `data.hidden: true` + `data.demo: true` if it should have
     enterprise KPIs.
  3. Mirror the change in the `_Config/Navigation` tag (Tag Browser).
  4. For KPI routes add `/plants/groveport/<area>/epms` and `/production` in Project Browser > Perspective >
     Page Configuration, and add them to the route list in the Header view's `custom.localRouteGuard` expression.
- **New plant (enterprise only):** add a route `/plants/<slug>` in Page Configuration, and a hidden demo child
  (`data.hidden` + `data.demo`) under Boars Head in `custom.items`.
- **Hide or show one node:** set or remove `data.hidden` on it (`data.demo` = enterprise only). Hidden nodes are kept,
  not deleted.
- **Switch the mode:** the Tag Browser step above.

## Moving local Groveport to an Edge gateway (planned)

Plan (2026-10): local Groveport moves to the Edge gateway, Standard stays the enterprise gateway. Check before
moving: create `DemoEnterpriseNav = false` there (Tag Browser > `_Config`); redo co-branding (Standard only); the SQL-dependent features
(Forms, Out Of Service, Reports, saved trends, alarm journal, OpsAudit) need a database connection and DB journal
on Edge or a remote DB; the Reporting module for PDFs; historian retention on Edge.

## Open questions

- Areas Freezer ... Dock have no area page (clicking only expands them). Should they open something?
- Should Operations and Admin be hidden in local mode too?
