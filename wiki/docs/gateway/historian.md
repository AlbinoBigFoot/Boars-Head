---
title: Historian
sidebar_position: 5
description: The SQL Historian provider "historian", its partitions and pruning, and how history is used by the HMI.
sources:
  - gateways/standard/data/config/resources/core/com.inductiveautomation.historian/historian-provider/historian/config.json
  - docs/local-groveport-mode.md
last_verified: 2026-10-23
---

# Historian

**Where:** Services > Historians > Historians > `historian`
(`config/resources/core/com.inductiveautomation.historian/historian-provider/historian/config.json`).

In 8.3 tag history is provided by the **Historian** core module plus a storage module; this gateway uses the
**SQL Historian** module, which writes to a database connection.

| Setting | Value | Meaning |
|---|---|---|
| Name | **`historian`** | The history provider name tags refer to (`historyProvider: historian`) and that trend queries use |
| Type | `SqlHistorian` | |
| Database | `ignition` | The MSSQL connection ([Databases](databases.md)) |
| Partitioning | on, **1 month**, not optimised | One data table per month |
| Pruning | **on, 2 years** | History older than 2 years is deleted. Change it under Services > Historians > Historians > `historian` |
| Stale multiplier | 2 | A value is stale after 2 missed scans |
| Track scan class execution | on | Writes `sqlth_sce`, used to tell "no change" from "not scanning" |

## Tables (Database `ignition`)

| Table | Content (row counts 2026-10-23) |
|---|---|
| `sqlth_te` | One row per historized tag path (about 18,800) |
| `sqlth_partitions` | Index of the monthly data tables (4) |
| `sqlt_data_1_2026_07` ... `_2026_10` | The values, one table per month (17 M to 86 M rows each) |
| `sqlth_sce`, `sqlth_scinfo`, `sqlth_drv`, `sqlth_annotations` | Scan class execution, scan info, driver, annotations |

## What Is Historized

History is configured **on the tags**, mostly in the UDT definitions (`historyEnabled`, `historyProvider`,
deadbands). Examples: PlantPAx `Val*` members of tanks, sensors and compressors; CG zone temperatures; the FCM
production KPI tags. Details per UDT: [Tags](../tags/index.md).

## Who Reads History

- **Trending** (`/trending`, ad-hoc trends, Saved Trends) and the right-click **Add To Trend**.
- **Utility Overview** charts (CG averages, status hours).
- **Report Builder** sources that aggregate per time bucket.

See [Features](../features/index.md).

## Notes

- 8.3 renamed things: the gateway page is "Historians", the module "SQL Historian", the provider type
  `SqlHistorian`. Old 8.1 docs talk about "Tag History" providers and "Datasource History".
- On an **Edge** gateway, history is local with limited retention; plan sync to a Standard gateway if long trends
  matter ([The Edge Move](../deployment/edge-move.md)).
- If history stops, check the database connection status, then Store & Forward (Platform > System > Store & Forward)
  for quarantined data.
