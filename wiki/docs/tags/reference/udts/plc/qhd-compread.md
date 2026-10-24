---
title: "PLC/QHD_CompRead"
sidebar_label: "QHD_CompRead"
description: "UDT definition PLC/QHD_CompRead"
generated: true
---

:::note

:::
# UDT `PLC/QHD_CompRead`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; QHD\_CompRead |
| Tag path | `[default]_types_/PLC/QHD_CompRead` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 23 (23 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | `(text, 82 chars)` | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

23 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Comp_Alarm_Status` | Int4 | OPC `{TagPrefix}.Comp_Alarm_Status` | | yes | | | | 1 = alarm |
| `Comp_Capacity_Mode` | Int4 | OPC `{TagPrefix}.Comp_Capacity_Mode` | | yes | | | | 0:manual$N1:auto$N2:remote comms$N3:remote io$N4:remote 4-20$N5:remote sequence$N6:manual browser |
| `Comp_Mode` | Int4 | OPC `{TagPrefix}.Comp_Mode` | | yes | | | | 0:manual$N1:auto$N2:remote comm$N3:remote io$N5:remote sequence$N6: manual browser |
| `Comp_Recycle_Delay` | Int4 | OPC `{TagPrefix}.Comp_Recycle_Delay` | | yes | | | | 1 = in recycle delay |
| `Comp_RegulationMode` | Int4 | OPC `{TagPrefix}.Comp_RegulationMode` | | yes | | | | |
| `Comp_SD_Status` | Int4 | OPC `{TagPrefix}.Comp_SD_Status` | | yes | | | | 1 = shutdown |
| `Comp_SV_Override` | Int4 | OPC `{TagPrefix}.Comp_SV_Override` | | yes | | | | 0 = OK$N1-31 = inhibit$N50-78 = force unload$Nsee manual |
| `Comp_SequencingMode` | Int4 | OPC `{TagPrefix}.Comp_SequencingMode` | | yes | | | | |
| `Comp_Start_Status` | Int4 | OPC `{TagPrefix}.Comp_Start_Status` | | yes | | | | 0 = Ready$N1 = In Shutdown$N2 = In Recycle Delay$N3 = High Discharge Temperature$N4 = High Oil Temperature$N5 = Low Separator Temperature$N6 = Slide Valve Too… |
| `Comp_Status` | Int4 | OPC `{TagPrefix}.Comp_Status` | | yes | | | | 0:off$N1:running$N20:starting$N30:stopping$N31:stopping - high capacity$N32: stopping - pumpdown$N33: stopping - cooldown |
| `Discharge_Pressure` | Float4 | OPC `{TagPrefix}.Discharge_Pressure` | | yes | | | | |
| `Discharge_Temp` | Float4 | OPC `{TagPrefix}.Discharge_Temp` | | yes | | | | |
| `FLA` | Float4 | OPC `{TagPrefix}.FLA` | | yes | | | | |
| `Filter_Pressure` | Float4 | OPC `{TagPrefix}.Filter_Pressure` | | yes | | | | |
| `KW` | Float4 | OPC `{TagPrefix}.KW` | | yes | | | | |
| `Oil_Pressure` | Float4 | OPC `{TagPrefix}.Oil_Pressure` | | yes | | | | |
| `Oil_Temp` | Float4 | OPC `{TagPrefix}.Oil_Temp` | | yes | | | | |
| `SV_Position` | Float4 | OPC `{TagPrefix}.SV_Position` | | yes | | | | |
| `Separator_Temp` | Float4 | OPC `{TagPrefix}.Separator_Temp` | | yes | | | | |
| `Suction_Pressure` | Float4 | OPC `{TagPrefix}.Suction_Pressure` | | yes | | | | |
| `Suction_Temp` | Float4 | OPC `{TagPrefix}.Suction_Temp` | | yes | | | | |
| `VFD_Percent` | Float4 | OPC `{TagPrefix}.VFD_Percent` | | yes | | | | |
| `VI` | Float4 | OPC `{TagPrefix}.VI` | | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [PLC/QHD\_CompData](qhd-compdata.md) (as `ReadData`)

