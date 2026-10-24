---
title: "PLC/FB_AlgSolCtrl"
sidebar_label: "FB_AlgSolCtrl"
description: "UDT definition PLC/FB_AlgSolCtrl"
generated: true
---

:::note

:::
# UDT `PLC/FB_AlgSolCtrl`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; FB\_AlgSolCtrl |
| Tag path | `[default]_types_/PLC/FB_AlgSolCtrl` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 9 (9 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

9 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `EnableIn` | Boolean | OPC `{TagPrefix}.EnableIn` | | yes | | | | Enable Input - System Defined Parameter |
| `EnableOut` | Boolean | OPC `{TagPrefix}.EnableOut` | | yes | | | | Enable Output - System Defined Parameter |
| `Err` | Boolean | OPC `{TagPrefix}.Err` | | yes | | | | |
| `Out` | Boolean | OPC `{TagPrefix}.Out` | | yes | | | | Output - Function is True |
| `OutN` | Boolean | OPC `{TagPrefix}.OutN` | | yes | | | | Output - Function is Not True |
| `PV` | Float4 | OPC `{TagPrefix}.PV` | | yes | | | | Input - Process Variable |
| `Polarity` | Boolean | OPC `{TagPrefix}.Polarity` | | yes | | | | Cfg - Logic Polarity 1 = Increasing |
| `SP1` | Float4 | OPC `{TagPrefix}.SP1` | | yes | | | | Input - Setpoint 1 |
| `SP2` | Float4 | OPC `{TagPrefix}.SP2` | | yes | | | | Input - Setpoint 2 |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
