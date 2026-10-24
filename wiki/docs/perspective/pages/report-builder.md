---
title: Report Builder
sidebar_position: 12
description: The guided four-step Report Builder popup opened from Generate Report buttons - what it shows, its data sources and how it is wired.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/Reports/**/view.json"
  - "docs/report-builder.md"
last_verified: 2026-10-24
---

# Report Builder

A modal popup (not a page) for building a custom report in four steps and exporting it as PDF, Excel or CSV.
The full feature description, source table and historian rules are in [Custom Reports](../../features/custom-reports.md);
this page covers the Perspective side.

## What It Shows

1. **Data Source**: source cards (Alarm History, Zone Temperatures, Compressors, Equipment Runtime, Out Of Service,
   Operations Forms), Quick Report tiles, and saved Templates / Recent reports in a right-hand panel.
2. **Time Range**: Last Shift, Today, Yesterday, Last 7 Days, Last 30 Days or Custom, plus Group Results By and Shifts.
3. **Details**: areas, devices and measures, with a collapsed Advanced Options section.
4. **Preview & Export**: summary cards, chart, tables, then Download and Save As Template.

A **Your Report** rail on the right always shows what will run.

## Where It Lives

| What | Where |
|---|---|
| View | `01_Popups/Reports/ReportBuilder`, parts in `01_Popups/Reports/_Assets/` |
| Opened by | `shared.Reports.open(sourceId, context)`, e.g. the Generate Report button on Alarm Status, Alarm Journal, the Out Of Service Log and Form History |
| Reports page | `/operations/reports` (nav item under Operations, shown to users with `Reports/Page`) |
| Changing it | [Report Builder](../../features/custom-reports.md#how-to-change-it) |
| Style classes | `report-*` on top of the `form-*` classes |

## Key Conventions

- Size and position come from the caller's viewport through `shared.Reports.popupPosition`; never give the popup a
  fixed size.
- It is driven by one computing binding (`builderModel`) plus two query bindings.
- The Production source has `deployment: enterprise` and is hidden while `[default]_Config/DemoEnterpriseNav` is false.
- Permissions are `Reports/Use`, `ShareTemplates`, `ManageTemplates` and one per source.

See the generated [view reference](../reference/index.md) for every param, binding and embed.
