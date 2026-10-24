---
title: Tag Providers And Tag Groups
sidebar_position: 4
description: The default and System tag providers, and the tag groups (RCP1_*, PAX_*) with their rates, leasing and the reasons behind them.
sources:
  - gateways/standard/data/config/resources/core/ignition/tag-provider/*/config.json
  - gateways/standard/data/config/resources/core/ignition/tag-group/**/config.json
  - docs/rcp1-pax-inventory.md
  - docs/pax-mapping/16-user-answers-2026-10-23.md
last_verified: 2026-10-23
---

# Tag Providers And Tag Groups

## Tag Providers

**Where:** Services > Tags (`ignition/tag-provider/<name>/config.json`).

![Services > Tags lists the realtime tag providers](/img/gateway/tag-providers.png)

| Provider | Type | Tags (2026-10-23) | Settings |
|---|---|---|---|
| **`default`** | Standard Tag Provider | about 88,000 | Value persistence **Database** (memory tag values survive restarts), tag reference store on, no read/write/edit security levels (access is governed by tag-level `readOnly` and the HMI permission matrix), backfill off |
| `System` | Managed Tag Provider | about 250 | Gateway-generated status tags (`[System]Gateway/...`, store and forward pipelines, performance) |

Everything the project defines lives in `[default]`. Top-level folders:

| Folder | What |
|---|---|
| `Boars_Head/GrovePort/<Area>/<Type>/<Device>` | Device instances (UDTs) the HMI shows. Areas: Freezer, SuperChill, Club, Palletizing, East PH, West PH, Dock, Machine Room, Condensers, Production, PLC |
| `_RCP1_` | Browsed controller tags of RCP1, pruned and read only |
| `_Config/**` | Settings: navigation, permissions matrix, security role lists, enums, forms, reports catalog, PLC write lock, demo switch |
| `KPI/**` | Enterprise KPI tags (hidden in local mode) |
| `_types_/**` | UDT definitions (stored in `tag-type-definition/`) |

Files: `config/resources/core/ignition/tag-definition/default/<folder>/tags.json` (instances) and
`tag-type-definition/default/<folder>/udts.json` (types). Full detail in [Tags](../tags/index.md).

## Tag Groups

A **tag group** decides how often OPC tags are read from the device.

- **Direct** mode polls at `rate`, all the time.
- **Leased** mode polls at `leasedRate` only while something subscribes to the tag (an open screen, a binding), and at
  `rate` the rest of the time. **`rate: 0` means "don't poll at all when nobody is looking"**.
- `opcDataMode: Subscribed`: the gateway asks the driver for subscriptions rather than polled reads.

**Where:** not in the web UI. In the Designer: Tag Browser > **Edit Tag Groups** (clock icon). Files
`config/resources/core/ignition/tag-group/default/<group>/config.json`.

| Group | Mode | Rate | Leased Rate | Used For |
|---|---|---|---|---|
| `Default` | Direct | 1000 ms | | Ignition default; memory and expression tags, anything not assigned |
| `Default Historical` | Direct | 10000 ms | | Ignition default |
| **`RCP1_Status`** | **Leased** | 0 (off when idle) | 1000 ms | `_RCP1_` status/value/alarm members (`Sts_*`, `Val*`, `Alm*`, `Inp_*`, `Out*`, timers, I/O images, diagnostics) |
| **`RCP1_Faceplate`** | Leased | 0 | 1000 ms | `_RCP1_` configuration and display members (`Cfg_*`, `PCfg_*`, `*Set_*`, `Inf_*`, commands, limits, settings, every String) |
| **`PAX_Status`** | Direct | **5000 ms** | | Status and value members of the PlantPAx library UDTs inside the device instances: what the overview screens and alarms need continuously |
| **`PAX_Faceplate`** | Leased | 60000 ms background | 1000 ms | Faceplate-only members (configuration, descriptions, limits): fast while a faceplate is open, refreshed once a minute otherwise so values are already there when one opens |
| **`PAX_Config`** | Direct | 30000 ms | | Alarm enables (`Cfg_Has*Alm`) and structure flags such as `Cfg_HasBleedValve` that decide what a screen draws |

### Why These Rates (2026-10-23)

The RCP1 driver is **link-bound**: over SecureLink it completes about 15 requests/s (2 concurrent requests, 500-byte
CIP packets, about 145 ms each). Before tuning, the tag groups asked for about 630 requests/s, so every value,
Direct or Leased, only refreshed about every 40 s, and faceplates took 34 to 48 s to show values.

| Change | Effect |
|---|---|
| `RCP1_Status` Direct 1 s → **Leased, rate 0** | Nothing on screen reads `_RCP1_`; it only duplicated the device UDTs' polling. Monitored items 32,575 → about 14,700 |
| `PAX_Status` Direct 1 s → **5 s** | Ideal demand 631 → 126 requests/s |
| `PAX_Faceplate` gets a 60 s background rate | Faceplate values already populated on open |
| New `PAX_Config` (Direct, 30 s) | Slow-changing structure flags off the fast groups |

Result: faceplate first values **0 to 5 s** (from 34 to 48 s), and RCP1 sees about 80% fewer requested reads.

- **On the plant LAN** (no SecureLink), `PAX_Status` can go back to 1000 ms.
- **Applied:** the RCP1 device's CIP connection size is now 4000 (it was 500; Connections > Devices > Connections >
  `RCP1`). `concurrentRequests` stays 2; raise it to 4 only if needed. Changing either restarts the driver.
- **Rollback:** edit the groups back in the Gateway web UI (Config > Tags > Tag Groups, `PAX_Status` Direct 1000 /
  Leased rate 0, and likewise `RCP1_Status`).

### Changing A Tag Group

1. Gateway web UI > **Config > Tags > Tag Groups** (or Designer > Tools > Edit Tag Groups): select the group, change
   **Mode** (Direct / Leased), **Rate** and **Leased Rate**, save.
2. Tags using the group pick up the new rate right away.
3. The `RCP1_*` and `PAX_*` group folders are whitelisted in `.gitignore`; commit them with the work that needed the
   change.
4. Watch the driver afterwards: `[RCP1][Diagnostics]/Sampling/*` by OPC path.
