---
title: "PLC/FB_2SpUpDownSeqr"
sidebar_label: "FB_2SpUpDownSeqr"
description: "UDT definition PLC/FB_2SpUpDownSeqr: Controller FB_2SpUpDownSeqr (read only)"
generated: true
---

:::note

:::
# UDT `PLC/FB_2SpUpDownSeqr`

Controller FB\_2SpUpDownSeqr (read only)

Standard PlantPAx FB\_2SpUpDownSeqr: ns=1;s=\[\{DeviceName\}\]\{TagPrefix\}.&lt;member&gt;, HMI member whitelist, every member readOnly, tag groups PAX\_Status / PAX\_Faceplate

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; FB\_2SpUpDownSeqr |
| Tag path | `[default]_types_/PLC/FB_2SpUpDownSeqr` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 23 (23 atomic, 0 nested UDT, 0 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

23 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Cfg_FastStartDB` | Float4 | OPC `{TagPrefix}.Cfg_FastStartDB` | PAX\_Faceplate | yes | | | | Cfg - Fast Start dead band in PV units |
| `Cfg_FastStartDelay` | Int2 | OPC `{TagPrefix}.Cfg_FastStartDelay` | PAX\_Faceplate | yes | | | | Cfg - Fast Time delay (sec) to start next stage |
| `Cfg_FastStopDB` | Float4 | OPC `{TagPrefix}.Cfg_FastStopDB` | PAX\_Faceplate | yes | | | | Cfg - Fast Stop dead band in PV units |
| `Cfg_FastStopDelay` | Int2 | OPC `{TagPrefix}.Cfg_FastStopDelay` | PAX\_Faceplate | yes | | | | Cfg - Fast Time delay (sec) to stop next stage |
| `Cfg_Mode` | Boolean | OPC `{TagPrefix}.Cfg_Mode` | PAX\_Faceplate | yes | | | | Cfg - Sequencer Mode 0= pump down, 1= Pump up |
| `Cfg_NumOfStage` | Int2 | OPC `{TagPrefix}.Cfg_NumOfStage` | PAX\_Faceplate | yes | | | | Cfg - Number of stages in sequence |
| `Cfg_SlowStartDB` | Float4 | OPC `{TagPrefix}.Cfg_SlowStartDB` | PAX\_Faceplate | yes | | | | Cfg - Slow Start dead band in PV units |
| `Cfg_SlowStartDelay` | Int2 | OPC `{TagPrefix}.Cfg_SlowStartDelay` | PAX\_Faceplate | yes | | | | Cfg - Slow Time delay (sec) to start next stage |
| `Cfg_SlowStopDB` | Float4 | OPC `{TagPrefix}.Cfg_SlowStopDB` | PAX\_Faceplate | yes | | | | Cfg - Slow Stop dead band in PV units |
| `Cfg_SlowStopDelay` | Int2 | OPC `{TagPrefix}.Cfg_SlowStopDelay` | PAX\_Faceplate | yes | | | | Cfg - Slow Time delay (sec) to stop next stage |
| `Cmd_Dec` | Boolean | OPC `{TagPrefix}.Cmd_Dec` | PAX\_Faceplate | yes | | | | Cmd - Decrement sequencer counter |
| `Cmd_FirstNoDelay` | Boolean | OPC `{TagPrefix}.Cmd_FirstNoDelay` | PAX\_Faceplate | yes | | | | Cmd - No time delay when starting first element |
| `Cmd_Inc` | Boolean | OPC `{TagPrefix}.Cmd_Inc` | PAX\_Faceplate | yes | | | | Cmd - Increment sequencer counter |
| `Cmd_Permissive` | Boolean | OPC `{TagPrefix}.Cmd_Permissive` | PAX\_Faceplate | yes | | | | Cmd - Remote Permissive |
| `Cmd_Target` | Float4 | OPC `{TagPrefix}.Cmd_Target` | PAX\_Faceplate | yes | | | | Cfg - Target in PV units |
| `Inp_PV` | Float4 | OPC `{TagPrefix}.Inp_PV` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | Input - Process Variable |
| `Out_NumToRun` | Int2 | OPC `{TagPrefix}.Out_NumToRun` | PAX\_Status | yes | | | | Out - Number of stages requested to run |
| `StartLimit` | Int2 | OPC `{TagPrefix}.StartLimit` | PAX\_Status | yes | | | | |
| `Sts_Starting` | Boolean | OPC `{TagPrefix}.Sts_Starting` | PAX\_Status | yes | | | | Sts - Starting |
| `Sts_StartTimeLeft` | Int2 | OPC `{TagPrefix}.Sts_StartTimeLeft` | PAX\_Status | yes | | | | |
| `Sts_Stopping` | Boolean | OPC `{TagPrefix}.Sts_Stopping` | PAX\_Status | yes | | | | Sts - Stopping |
| `Sts_StopTimeLeft` | Int2 | OPC `{TagPrefix}.Sts_StopTimeLeft` | PAX\_Status | yes | | | | |
| `Val_Target` | Float4 | OPC `{TagPrefix}.Val_Target` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | Val\_Target Setpoint |

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [Devices/DischargeSequence](../devices/dischargesequence.md) (as `Seqr`)

Reached through nesting by 1 top-level instance(s).
