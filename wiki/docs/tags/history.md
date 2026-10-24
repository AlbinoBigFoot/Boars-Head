---
title: History And Polling
sidebar_label: History And Polling
sidebar_position: 5
description: What is historized and how (provider, sample mode, deadbands), the tag groups and why they are set the way they are, and the RCP1 polling budget over SecureLink.
sources:
  - gateways/standard/data/config/resources/core/com.inductiveautomation.historian/**/config.json
  - gateways/standard/data/config/resources/core/ignition/tag-group/**/config.json
  - docs/pax-mapping/16-user-answers-2026-10-23.md
last_verified: 2026-10-23
---

# History And Polling

## The Historian

Tag history goes to the SQL historian provider **`historian`** (Gateway: **Config > Tags > History**, resource
`com.inductiveautomation.historian/historian-provider/historian`):

| Setting | Value |
|---|---|
| Type | SQL Historian |
| Database | `ignition` (the MSSQL container `bh-mssql`) |
| Partitions | on, 1 month |
| Pruning | off |
| Stale multiplier | 2 |
| Track scan class execution | on |

History is read by the faceplate **Trend** tabs (`shared.FaceplateTrend` default pens), the CG 12 h history, the
trending pages (`/trending`, `/trending/saved`, see
[Features](../features/index.md)) and the report builder.

## What Is Historized

Every historized member is listed, generated, in the [History Index](reference/history-index.md). The rules:

1. **History is configured on UDT definitions**, so every instance gets it (like alarms).
2. **PLC library members**: every numeric `Val*` status member in the **Direct** group (`PAX_Status`), plus a few
   float status members of the site types:

   | Type | Historized members |
   |---|---|
   | `P_Motor` | `Val_Sts`, `Val_Mode`, `Val_Notify` |
   | `P_RunTime` | `Val_TotRunHrs`, `Val_CurRunHrs`, `Val_Starts` |
   | `P_AIn` | `Val`, `Val_InpPV`, `Val_Fault`, `Val_Mode`, `Val_Notify`, `Val_PVMinCapt`, `Val_PVMaxCapt` |
   | `P_DIn` | `Val_Fault`, `Val_Notify` |
   | `P_ValveSO` | `Val_Sts`, `Val_Mode`, `Val_Fault`, `Val_Notify` |
   | `Screw_Compressor` | Amps, FLA, SVP, SucP / SucT, DisP / DisT, OilP / OilT, TotalRuntime, KW, SepT, AuxT, VI, AntiR_Remaining ... (21) and `Rung` |
   | `CG_RL_Evap` | `Val_CoolingTime`, `Val_RunTime`, `Val_TimeLeft`, `ZAT_High` / `Low` / `HiHi` / `LoLo`, `AIDefrostStart` / `Stop` |
   | `Comp_Sequence` | start / stop / target / emergency pressures (10) |
   | `FB_2SpUpDownSeqr` | `Inp_PV`, `Val_Target` |

3. **`_Root` value types** (`Analog`, `Digital`, `String`, `Multistate`) historize their `Value` (On Change), which
   covers the HMI-owned members and the KPI / FCM placeholders built on them.
4. **Leased members are never historized**: history on a Leased tag would record only while a faceplate is open. If a
   setpoint should be trended, move it to a Direct group first. (An audit on 2026-10-23 found all 115 historized
   instance tags on Direct groups: 61 `PAX_Status`, 54 `Default`.)
5. **History starts at mapping time.** The PLC-mapped members have history only since 2026-10-22 / 23; the old flat
   member series are still in the database under their old paths.

### Sample mode and deadbands

| Kind | Sample mode | Deadband |
|---|---|---|
| Float (`Val`, pressures, temperatures) | On Change | 0.01 absolute, **Analog** style (records the slope, not every wiggle) |
| Integer / enum / Boolean (`Val_Sts`, `Val_Fault`, `Val_Mode`) | On Change | 0 absolute, **Discrete** style (records every change) |

Change history settings on the **UDT definition** (Tag Browser > UDT Definitions > the member > Edit Tag > History), so every instance follows. See [How To Change It](#how-to-change-it).

## Tag Groups (Polling)

An OPC tag polls at its **tag group's** rate. Current groups (generated with live counts: [Tag Groups](reference/tag-groups.md)):

| Group | Mode | Rate | Used for |
|---|---|---|---|
| `PAX_Status` | Direct | 5,000 ms | PLC library status / value / alarm members (always polled; feeds alarms and history) |
| `PAX_Faceplate` | Leased | 1,000 ms while leased, 60,000 ms background | PLC configuration, commands, limits, strings (only fast while a faceplate shows them) |
| `PAX_Config` | Direct | 30,000 ms | PLC alarm enables, `Cfg_HasBleedValve`, interlock condition texts |
| `RCP1_Status` | Leased | 1,000 ms while leased, 0 background | the `_RCP1_` mirror's status members (nothing displays them) |
| `RCP1_Faceplate` | Leased | 1,000 ms while leased, 0 background | the `_RCP1_` mirror's configuration members |
| `Default` | Direct | 1,000 ms | everything without a group (memory and expression tags are not polled from a PLC) |
| `Default Historical` | Direct | 10,000 ms | unused by the project |

**Leased** means: while any client subscribes to the tag (a view binding), it polls at the leased rate; otherwise at
the background rate (`0` = not at all). The background rate on `PAX_Faceplate` (60 s) keeps a recent value ready, so a
faceplate opens with data in 0-5 s instead of waiting for the first lease poll.

## The Polling Budget (Why 5 s)

`RCP1` is reached over a **SecureLink** tunnel from the lab, and that link, not the PLC, is the bottleneck. Measured
on 2026-10-23 (read only, `[RCP1][Diagnostics]/Sampling/*`): the driver (`concurrentRequests` 2,
`cipConnectionSize` 500 bytes at the time, about 145 ms per request; it is now 4000) completes about **15 requests/s** (about 400 items/s).

| Step | Monitored items | Requests per cycle | Ideal requests/s | Achieved |
|---|---|---|---|---|
| Before | 32,575 | 639 | 631 | ~13.7 |
| `RCP1_Status` Direct 1 s -> Leased (the mirror only duplicated the device UDTs' polling) | ~14,700 | ~560-595 | ~550-586 | ~15 |
| `PAX_Status` Direct 1 s -> 5 s | 14,856 | 567 | 126 | ~15.4 |

Before the change every value, Direct or Leased, refreshed only about every 40 s and faceplate values took 34-48 s to
appear. After it the link serves 5x less demand: first values in 0-5 s, alarms much sooner, about 80 % fewer reads
asked of RCP1. The Logix driver merges duplicate items, so a member subscribed twice costs almost nothing extra.

**Applied afterwards:** the RCP1 device's `cipConnectionSize` was raised from 500 to 4000 (about 8x fewer requests
for the same data; Connections > Devices > Connections > `RCP1`). Only if needed, `concurrentRequests` 2 -> 4. **On the plant LAN** (no SecureLink) `PAX_Status` can go back to 1,000 ms.

Rollback of the group changes: edit the groups back in the Gateway web UI (Config > Tags > Tag Groups): `PAX_*` to
Direct 1000 / Leased rate 0, and `RCP1_Status` to Direct 1000 (never a tag import on `_RCP1_`).

## How To Change It

- **Historize a tag or UDT member:** Tag Browser > the tag (or, for device members, **UDT Definitions** > the type >
  the member) > right-click > **Edit Tag** > **History**: enable history, set **Sample Mode** (On Change),
  **Deadband** (0.01 absolute, Analog style, for floats; 0 absolute, Discrete style, for integers, enums and
  Booleans), **Tag Group** and the history provider `historian`. Click **OK**. For a UDT member every instance follows.
  A newly historized value can be trended from the right-click menu straight away
  ([Trending](../features/trending.md#how-to-change-it)).
- **Change a tag group's rate or mode:** Gateway web UI > Config > Tags > Tag Groups (or Designer > Tools > Edit Tag
  Groups) > select the group, change **Mode** (Direct / Leased), **Rate** and **Leased Rate**, save. Don't switch
  `_RCP1_` groups to Direct: they are Leased on purpose.
- **Move a tag to another group:** Edit Tag > **Tag Group**.
- **Retention:** Gateway web UI > Config > Tags > History > Historians (pruning), see
  [Historian](../gateway/historian.md).

## Bad, Loading And Stale Values

- A Leased value that has not arrived yet, or any Bad / Uncertain value, shows the gray italic em dash (style class
  `value-bad`); `StatusIndicator` shows COMM LOSS for Bad quality.
- After a driver restart the PLC tags show `Uncertain_LastKnownValue` until the driver catches up (10-30 minutes over
  SecureLink at gateway start).
- PlantPAx's "no limit" value (about 1.5e38) is shown as a dash.
