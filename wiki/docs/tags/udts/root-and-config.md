---
title: _Root, Config And Overview UDTs
sidebar_label: _Root, Config, Overview
sidebar_position: 5
description: The single-value _Root building blocks, the Config helper UDTs (_Alarms, Interlock, Integration), the Overview table UDTs and the write-lock test type.
sources:
  - gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/_Root/udts.json
  - gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Config/udts.json
  - gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Overview/udts.json
  - gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/_PlcWriteLockTest/udts.json
last_verified: 2026-10-23
---

# `_Root`, `Config` And `Overview` UDTs

These are the small helper types. They hold no PLC data of their own.

## `_Root`

Single-value building blocks: each has one atomic member `Value` (plus metadata) and history settings. They come from
the original HMI design, where every device field was its own `<Field>/Value` tag; since the
[flat-member cleanup](../pax-mapping/flat-member-cleanup.md) the device UDTs use them only for the members we own and
for the Machine Room SAFETYS `Digitals`.

| UDT | `Value` | Value source (default) | History | Generated page |
|---|---|---|---|---|
| `_Root/Analog` | Float4 | **reference** (empty source) | yes, On Change, deadband 0.01 | [page](../reference/udts/root/analog.md) |
| `_Root/Digital` | Boolean, states Off / On | **reference** (empty source) | yes, On Change | [page](../reference/udts/root/digital.md) |
| `_Root/Multistate` | Int4, states 0 Start / 1 Stop / 2 Auto | reference | yes, On Change | [page](../reference/udts/root/multistate.md) |
| `_Root/String` | String | memory | yes, On Change | [page](../reference/udts/root/string.md) |
| `_Root/Document` | Document | memory | no | [page](../reference/udts/root/document.md) |
| `_Root/Expression` | Float4 expression + `Metadata` document; parameters `exprTargetPath`, `exprFunction` | expr | off | [page](../reference/udts/root/expression.md) |

:::warning The reference default
`_Root/Analog` and `_Root/Digital` default to `valueSource: reference` with no source path, so an instance that only
sets `"value": x` reads **null**. Override with `"valueSource": "memory"` (an HMI setting) or set `sourceTagPath`
(a mirror of another tag). Example of the second: `Machine Room/Digitals/FIRE/Value` references
`[default]_RCP1_/Program:RCP_Alarm_Circuit/FD_Alarm`.
:::

Used by: the SAFETYS lamps (`Boars_Head/GrovePort/Machine Room/Digitals`, eight `_Root/Digital` instances, see
[Machine Room SAFETYS](../pax-mapping/machine-room-safetys.md)), the owned members of Valve (`Cmd_Position`,
`valveType`), Compressor (`Cfg_WebGuiUrl`), the sequence settings, LTU `ResetDaily` / `ResetTime`, Tank `Interlock/*`,
and the old `CoolingTower` / `VFD` / `Units/AHU` layouts.

## Config

### `Config/_Alarms`

Every device UDT nests one `_Alarms` instance. It turns Ignition's built-in **Alarm Metrics** of the parent instance
(`[.]../Alarm Metrics.activeUnackCount`, `hasActive`, `highestActivePriority` ...) into plain members the views can
bind to, and maps the highest priority to a color and an icon:

| Member | What |
|---|---|
| `_Active`, `_ActiveCount`, `_ActiveCountCritical` / `High` / `Medium` / `Low` | reference tags on the parent's Alarm Metrics |
| `_ActiveHighPriority`, `_AckHighPriority`, `_HighestPriority` | highest active / acknowledged priority (0-4) |
| `_Color` | `case(_HighestPriority, 4, {[~]_Config/Colors/Alarms/Critical}, 3, ...High, 2, ...Medium, 1, ...Low)` |
| `_Icon` | same with `_Config/Icons/Alarms/*` |
| `_Flash` | blinks with `{[~]_Config/Flash}` while a higher priority is active than acknowledged |

So the alarm badge and frame on a device tile come from the device's own alarms (all of them PLC library alarms on the
nested parts, see [Alarms](../alarms.md)) with no per-device setup. [Generated page](../reference/udts/config/alarms.md).

### `Config/Interlock`

The HMI interlock layout of the original design (`Cfg_CondTxt00..15`, `MSet_Bypass00..15`, `Sts_IntlkOK`,
`Sts_FirstOut` ... as `_Root` leaves). Mapped devices read their PLC `Intlk` part (`PLC/P_Intlk`) instead; this type
is only nested by the unmapped `Devices/CoolingTower`. [Generated page](../reference/udts/config/interlock.md).

### `Config/Integration`

One API endpoint / connection, used under `[default]_Config/Integrations/<Name>` (Provider, Description, Enabled,
Endpoint URL, API Version, API Token, Connected, Last Check, Last Error, Settings). `shared.Integrations` reads and
edits it; Ticket Logger > Integrations lists it. The instance folder is **not in git** because it holds the token, and
the token is write-only from the HMI. [Generated page](../reference/udts/config/integration.md).

## Overview

One UDT per device table: `Pump Overview`, `Compressor Overview`, `Exhaust Fan Overview`, `Evaporator Overview`,
`Cooling Tower Overview`, `Tank Overview`, `Valve Overview`, `Sensor Overview`. An instance named `Overview` sits in a
device type folder (for example `Machine Room/Pumps/Overview`) and holds the cached rows (`Instances`), device count
and active alarm count of that folder's Details table. The gateway tag-change scripts `rebuildOverviewInstances` /
`overviewRebuild` rebuild them through `shared.Overview` when the folder's `Overview/Rebuild` tag (or
`_Config/Rebuild`) goes true. See [Scripting](../../scripting/index.md) for `shared.Overview`. Generated pages:
[Overview folder](../reference/udts/overview/pump-overview.md) and siblings.

## `_PlcWriteLockTest/TestCard`

A test-only type with three PlantPAx-named memory members (`OCmd_Start`, `Val_SP`, `Alarm/Cfg_Limit`) and one
instance, `[default]_Config/PlcWriteLock/_Test/Instance`. The PLC write lock self test flips their `readOnly` on the
definition through the TEST boolean `_Config/PlcWriteLock/_Test/Locked`, never through the real lock. See
[PLC Write Lock](../plc-write-lock.md#testing).
