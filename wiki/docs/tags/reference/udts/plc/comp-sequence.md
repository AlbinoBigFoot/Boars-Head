---
title: "PLC/Comp_Sequence"
sidebar_label: "Comp_Sequence"
description: "UDT definition PLC/Comp_Sequence: Controller Comp_Sequence (read only)"
generated: true
---

:::note

:::
# UDT `PLC/Comp_Sequence`

Controller Comp\_Sequence (read only)

Standard PlantPAx Comp\_Sequence: ns=1;s=\[\{DeviceName\}\]\{TagPrefix\}.&lt;member&gt;, HMI member whitelist, every member readOnly, tag groups PAX\_Status / PAX\_Faceplate

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; Comp\_Sequence |
| Tag path | `[default]_types_/PLC/Comp_Sequence` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 45 (44 atomic, 0 nested UDT, 1 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

44 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Sequence_Set/` | Folder | | | | | | | |
| `Sequence_Set/Sequence_Set_0_` | Int4 | OPC `{TagPrefix}.Sequence_Set[0]` | PAX\_Faceplate | yes | | | | |
| `Sequence_Set/Sequence_Set_1_` | Int4 | OPC `{TagPrefix}.Sequence_Set[1]` | PAX\_Faceplate | yes | | | | |
| `Sequence_Set/Sequence_Set_2_` | Int4 | OPC `{TagPrefix}.Sequence_Set[2]` | PAX\_Faceplate | yes | | | | |
| `Sequence_Set/Sequence_Set_3_` | Int4 | OPC `{TagPrefix}.Sequence_Set[3]` | PAX\_Faceplate | yes | | | | |
| `Sequence_Set/Sequence_Set_4_` | Int4 | OPC `{TagPrefix}.Sequence_Set[4]` | PAX\_Faceplate | yes | | | | |
| `Emergency_Stop_Pressure` | Float4 | OPC `{TagPrefix}.Emergency_Stop_Pressure` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `Emergency_Unload_Pressure` | Float4 | OPC `{TagPrefix}.Emergency_Unload_Pressure` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `Floating_Target` | Float4 | OPC `{TagPrefix}.Floating_Target` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `Fully_Unload_Lead` | Boolean | OPC `{TagPrefix}.Fully_Unload_Lead` | PAX\_Status | yes | | | | |
| `Hold` | Boolean | OPC `{TagPrefix}.Hold` | PAX\_Status | yes | | | | |
| `In_Sequence` | Boolean | OPC `{TagPrefix}.In_Sequence` | PAX\_Status | yes | | | | |
| `Lag_Compressor` | Int4 | OPC `{TagPrefix}.Lag_Compressor` | PAX\_Status | yes | | | | |
| `Lead_Compressor` | Int4 | OPC `{TagPrefix}.Lead_Compressor` | PAX\_Status | yes | | | | |
| `LeadLag_Capacity` | Int4 | OPC `{TagPrefix}.LeadLag_Capacity` | PAX\_Status | yes | | | | |
| `Load` | Boolean | OPC `{TagPrefix}.Load` | PAX\_Status | yes | | | | |
| `LU_Delay_Set` | Float4 | OPC `{TagPrefix}.LU_Delay_Set` | PAX\_Faceplate | yes | | | | |
| `LU_Pulse` | Int2 | OPC `{TagPrefix}.LU_Pulse` | PAX\_Status | yes | | | | |
| `Num_In_Sequence` | Int2 | OPC `{TagPrefix}.Num_In_Sequence` | PAX\_Status | yes | | | | |
| `Num_Rung` | Int2 | OPC `{TagPrefix}.Num_Rung` | PAX\_Status | yes | | | | |
| `Num_Rung_LBL` | Int2 | OPC `{TagPrefix}.Num_Rung_LBL` | PAX\_Status | yes | | | | |
| `Num_Rung_Loaded` | Int2 | OPC `{TagPrefix}.Num_Rung_Loaded` | PAX\_Status | yes | | | | |
| `Num_Rung_UBL` | Int2 | OPC `{TagPrefix}.Num_Rung_UBL` | PAX\_Status | yes | | | | |
| `ReSequence` | Boolean | OPC `{TagPrefix}.ReSequence` | PAX\_Status | yes | | | | |
| `SB_Enable` | Boolean | OPC `{TagPrefix}.SB_Enable` | PAX\_Faceplate | yes | | | | |
| `SB_Start_Time_Set` | Int2 | OPC `{TagPrefix}.SB_Start_Time_Set` | PAX\_Faceplate | yes | | | | |
| `SB_Stop_Time_Set` | Int2 | OPC `{TagPrefix}.SB_Stop_Time_Set` | PAX\_Faceplate | yes | | | | |
| `Start_Delay_Set` | Float4 | OPC `{TagPrefix}.Start_Delay_Set` | PAX\_Faceplate | yes | | | | |
| `Start_Pressure` | Float4 | OPC `{TagPrefix}.Start_Pressure` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `Start_Pressure_DB` | Float4 | OPC `{TagPrefix}.Start_Pressure_DB` | PAX\_Faceplate | yes | | | | |
| `Start_Time_Left` | Int4 | OPC `{TagPrefix}.Start_Time_Left` | PAX\_Status | yes | | | | |
| `Stop_Delay_Set` | Float4 | OPC `{TagPrefix}.Stop_Delay_Set` | PAX\_Faceplate | yes | | | | |
| `Stop_Pressure` | Float4 | OPC `{TagPrefix}.Stop_Pressure` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `Stop_Pressure_DB` | Float4 | OPC `{TagPrefix}.Stop_Pressure_DB` | PAX\_Faceplate | yes | | | | |
| `Stop_Time_Left` | Int4 | OPC `{TagPrefix}.Stop_Time_Left` | PAX\_Status | yes | | | | |
| `Target_DB_Set` | Float4 | OPC `{TagPrefix}.Target_DB_Set` | PAX\_Faceplate | yes | | | | |
| `Target_Max` | Float4 | OPC `{TagPrefix}.Target_Max` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `Target_Max_Set` | Float4 | OPC `{TagPrefix}.Target_Max_Set` | PAX\_Faceplate | yes | | | | |
| `Target_Min` | Float4 | OPC `{TagPrefix}.Target_Min` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `Target_Min_Set` | Float4 | OPC `{TagPrefix}.Target_Min_Set` | PAX\_Faceplate | yes | | | | |
| `Target_Pressure` | Float4 | OPC `{TagPrefix}.Target_Pressure` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `Target_Pressure_Hi` | Float4 | OPC `{TagPrefix}.Target_Pressure_Hi` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `Target_Pressure_Lo` | Float4 | OPC `{TagPrefix}.Target_Pressure_Lo` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `Target_Pressure_Set` | Float4 | OPC `{TagPrefix}.Target_Pressure_Set` | PAX\_Faceplate | yes | | | | |
| `Unload` | Boolean | OPC `{TagPrefix}.Unload` | PAX\_Status | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [Devices/SuctionSequence](../devices/suctionsequence.md) (as `Seq`)

Reached through nesting by 2 top-level instance(s).
