---
title: "PLC/QHD_CompWrite"
sidebar_label: "QHD_CompWrite"
description: "UDT definition PLC/QHD_CompWrite"
generated: true
---

:::note

:::
# UDT `PLC/QHD_CompWrite`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; QHD\_CompWrite |
| Tag path | `[default]_types_/PLC/QHD_CompWrite` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 16 (16 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | `1 = start` | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

16 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Capacity_Mode` | Int2 | OPC `{TagPrefix}.Capacity_Mode` | | yes | | | | 1: auto$N2: remote comms$N3: remote io$N4: remote 4-20mA$N5: remote sequence$N6: manual browser |
| `Capacity_SP` | Int2 | OPC `{TagPrefix}.Capacity_SP` | | yes | | | | Set SV + VFD command$N0 - 200% |
| `Clear_Alarm` | Boolean | OPC `{TagPrefix}.Clear_Alarm` | | yes | | | | 1 = clear |
| `Clear_Recycle` | Boolean | OPC `{TagPrefix}.Clear_Recycle` | | yes | | | | 1 = clear recycle delay |
| `Compressor_Mode` | Int2 | OPC `{TagPrefix}.Compressor_Mode` | | yes | | | | 0: manual$N1: auto$N2: remote comms$N3: remote IO$N5: Remote sequence$N6: manual browser |
| `Load` | Int2 | OPC `{TagPrefix}.Load` | | yes | | | | # of seconds to load$N1-15 |
| `RDB_Capacity` | Int2 | OPC `{TagPrefix}.RDB_Capacity` | | yes | | | | 25, 50, 75, 100 (capacity %) |
| `Regulation_Mode` | Int2 | OPC `{TagPrefix}.Regulation_Mode` | | yes | | | | 0: Mode 1$N1: Mode 2$N2: Mode 3$N3: Mode 4 |
| `SV_Position_SP` | Int2 | OPC `{TagPrefix}.SV_Position_SP` | | yes | | | | set SV position $N0 - 100% |
| `Sequence_Mode` | Boolean | OPC `{TagPrefix}.Sequence_Mode` | | yes | | | | 0: Disable$N1: Enable |
| `Start` | Boolean | OPC `{TagPrefix}.Start` | | yes | | | | 1 = start |
| `Stop` | Boolean | OPC `{TagPrefix}.Stop` | | yes | | | | 1 = stop |
| `Unload` | Int2 | OPC `{TagPrefix}.Unload` | | yes | | | | # of seconds to Unload 1-15 |
| `VFD_Speed_SP` | Int2 | OPC `{TagPrefix}.VFD_Speed_SP` | | yes | | | | set VFD Speed$N0 - 100% |
| `ZZZZZZZZZZQHD_CompWr0` | Int1 | OPC `{TagPrefix}.ZZZZZZZZZZQHD_CompWr0` | | yes | | | | |
| `ZZZZZZZZZZQHD_CompWr8` | Int1 | OPC `{TagPrefix}.ZZZZZZZZZZQHD_CompWr8` | | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [PLC/QHD\_CompData](qhd-compdata.md) (as `WriteCommand`)

