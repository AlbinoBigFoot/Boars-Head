---
title: "PLC/MakeUp_Water"
sidebar_label: "MakeUp_Water"
description: "UDT definition PLC/MakeUp_Water"
generated: true
---

:::note

:::
# UDT `PLC/MakeUp_Water`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; MakeUp\_Water |
| Tag path | `[default]_types_/PLC/MakeUp_Water` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 11 (11 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

11 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Alm_HiHi` | Boolean | OPC `{TagPrefix}.Alm_HiHi` | | yes | | | | |
| `Alm_LoLo` | Boolean | OPC `{TagPrefix}.Alm_LoLo` | | yes | | | | |
| `EnableIn` | Boolean | OPC `{TagPrefix}.EnableIn` | | yes | | | | Enable Input - System Defined Parameter |
| `EnableOut` | Boolean | OPC `{TagPrefix}.EnableOut` | | yes | | | | Enable Output - System Defined Parameter |
| `HighLimit` | Float4 | OPC `{TagPrefix}.HighLimit` | | yes | | | | |
| `Inp_HiLevel` | Boolean | OPC `{TagPrefix}.Inp_HiLevel` | | yes | | | | |
| `Inp_LoLevel` | Boolean | OPC `{TagPrefix}.Inp_LoLevel` | | yes | | | | |
| `Inp_LoLoLevel` | Boolean | OPC `{TagPrefix}.Inp_LoLoLevel` | | yes | | | | |
| `Level` | Float4 | OPC `{TagPrefix}.Level` | | yes | | | | |
| `LowLimit` | Float4 | OPC `{TagPrefix}.LowLimit` | | yes | | | | |
| `Out` | Boolean | OPC `{TagPrefix}.Out` | | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
