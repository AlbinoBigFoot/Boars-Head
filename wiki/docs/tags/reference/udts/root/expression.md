---
title: "_Root/Expression"
sidebar_label: "Expression"
description: "UDT definition _Root/Expression"
generated: true
---

:::note

:::
# UDT `_Root/Expression`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; \_Root &gt; Expression |
| Tag path | `[default]_types_/_Root/Expression` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/_Root/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 2 (2 atomic, 0 nested UDT, 0 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `exprTargetPath` | String | `(OverviewOnly)` | own |
| `exprFunction` | String | `(OverviewOnly)` | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Metadata` | Document | memory = `(document, 47 chars)` | | | | | | |
| `Value` | Float4 | expr | | | | fmt 00000.00 | | |

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [Devices/CoolingTower](../devices/coolingtower.md) (as `SummaryInstances`), [Devices/VFD](../devices/vfd.md) (as `SummaryInstances`), [Devices/Evaporator](../devices/evaporator.md) (as `SummaryInstances`), [Overview/Pump Overview](../overview/pump-overview.md) (as `DeviceCount`), [Overview/Pump Overview](../overview/pump-overview.md) (as `ActiveAlarmCount`), [Overview/Compressor Overview](../overview/compressor-overview.md) (as `DeviceCount`), [Overview/Compressor Overview](../overview/compressor-overview.md) (as `ActiveAlarmCount`), [Overview/Exhaust Fan Overview](../overview/exhaust-fan-overview.md) (as `DeviceCount`), [Overview/Exhaust Fan Overview](../overview/exhaust-fan-overview.md) (as `ActiveAlarmCount`), [Overview/Evaporator Overview](../overview/evaporator-overview.md) (as `DeviceCount`), [Overview/Evaporator Overview](../overview/evaporator-overview.md) (as `ActiveAlarmCount`), [Overview/Cooling Tower Overview](../overview/cooling-tower-overview.md) (as `DeviceCount`), [Overview/Cooling Tower Overview](../overview/cooling-tower-overview.md) (as `ActiveAlarmCount`), [Overview/Tank Overview](../overview/tank-overview.md) (as `DeviceCount`), [Overview/Tank Overview](../overview/tank-overview.md) (as `ActiveAlarmCount`), [Overview/Valve Overview](../overview/valve-overview.md) (as `DeviceCount`), [Overview/Valve Overview](../overview/valve-overview.md) (as `ActiveAlarmCount`), [Overview/Sensor Overview](../overview/sensor-overview.md) (as `DeviceCount`), [Overview/Sensor Overview](../overview/sensor-overview.md) (as `ActiveAlarmCount`), [Units/AHU](../units/ahu.md) (as `SummaryInstances`)

Reached through nesting by 25 top-level instance(s).
