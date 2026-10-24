---
title: Deployment Modes
sidebar_position: 1
description: Local Groveport mode (default) vs the enterprise demo, the one switch between them, what each hides, and how to add areas or plants in the Designer.
sources:
  - docs/local-groveport-mode.md
  - gateways/standard/data/config/resources/core/ignition/tag-definition/default/_Config/tags.json
last_verified: 2026-10-24
---

# Deployment Modes

The BH HMI has **two modes behind one switch**. Nothing is deleted in either mode; every view, route, tag and nav node
stays in the project.

| | Local Groveport (default, live now) | Enterprise Demo |
|---|---|---|
| Tag `[default]_Config/DemoEnterpriseNav` | `false` | `true` |
| Nav | Boars Head > Groveport > Utility Overview, the areas' CG pages directly, Machine Room, Condensers, Operations, Admin | + other plants, Enterprise Operations, Production Overview (Level 2/3), each area's EPMS / Utility / Production folders |
| `/` and the logo | redirect to `/plants/groveport/utility-overview` | the enterprise globe `/enterprise` |
| Boars Head node icon | home | globe |
| Page title of `/` | "Groveport Utility Overview" | "Boars Head International" |

## How To Switch Modes

1. In the Designer open the **Tag Browser** and select the `[default]` provider.
2. Open the `_Config` folder and select `DemoEnterpriseNav` (a memory Boolean).
3. Change its value: `false` = Local Groveport, `true` = Enterprise Demo. Either double-click the value in the Tag
   Browser or open the tag editor (right-click > Edit Tag) and set **Value**.
4. Open sessions pick it up on their next nav refresh or page change; reload the browser to see it at once.

The tag editor's **Value** field writes the live value. Do not change the mode by editing `tags.json` on disk: that
blanks the live value. To check the mode, read the tag: `false` means local, `true` means enterprise.

## How The Switch Works

- **Nav:** nodes with `data.hidden` + `data.demo` show only in enterprise mode; `data.flattenLocal` lifts an area's
  `Utility` folder children into the area in local mode; `data.localIcon` / `data.localPage` / `data.demoPage` choose
  icon and target per mode. The Navigation view's Tree transform and `Navigation.Nav` apply these rules.
- **Routes:** the enterprise routes stay in page-config. In local mode a **route guard** on the Header
  (`custom.localRouteGuard`, an expression; its change script only calls `system.perspective.navigate`) redirects
  `/`, `/enterprise`, `/plants/...`, the Production routes and the 16 area KPI routes to the Utility Overview.
- **Fail-safe:** if the tag can't be read, the nav shows local and the guard doesn't redirect.

## Kept In Local Mode On Purpose

- **Operations:** Alarm Status, Alarm Journal, Trending, Saved Trends, Out Of Service Log, Forms, PLCs > RCP1
  (read-only rack / I/O view). **Reports** is hidden (`data.hidden`) but still in the project.
- **Admin:** Audit Log, User Management, Roles & Permissions (gated by the permission matrix).

## How To Change It

All of these are Designer edits; save, then test in a Perspective session in both modes.

- **A new Groveport area:**
  1. Project Browser > Perspective > Views > `00_Docked/Navigation`; select the root and edit `custom.items`.
  2. Add the area under Groveport (area > `Utility` folder > pages). Give it hidden `EPMS` / `Production` children with
     `data.hidden: true` + `data.demo: true` if it gets enterprise KPIs.
  3. Mirror the same change in the tag `[default]_Config/Navigation` (Tag Browser > `_Config` > `Navigation`).
  4. If the area has KPI routes: Project Browser > Perspective > Page Configuration > add the
     `/plants/groveport/<area>/epms` and `/production` routes, and add them to the route list in the Header view's
     `custom.localRouteGuard` expression so local mode redirects them.
- **A new plant (enterprise only):** add a route `/plants/<slug>` in Page Configuration and a hidden demo child
  (`data.hidden` + `data.demo`) under Boars Head in `custom.items`.
- **Hide or show one node:** on the node set `data.hidden: true` (plus `data.demo: true` for enterprise-only) or remove
  it. Hidden nodes are kept, not deleted.
- **A second local plant** would need a per-site home (for example a `_Config/Deployment/Site` tag); not set up yet.

Source document: `docs/local-groveport-mode.md`. Nav and page details: [Perspective](../perspective/index.md).
