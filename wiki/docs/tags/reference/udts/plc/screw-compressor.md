---
title: "PLC/Screw_Compressor"
sidebar_label: "Screw_Compressor"
description: "UDT definition PLC/Screw_Compressor: Controller Screw_Compressor (read only)"
generated: true
---

:::note

:::
# UDT `PLC/Screw_Compressor`

Controller Screw\_Compressor (read only)

Standard PlantPAx Screw\_Compressor: ns=1;s=\[\{DeviceName\}\]\{TagPrefix\}.&lt;member&gt;, HMI member whitelist, every member readOnly, tag groups PAX\_Status / PAX\_Faceplate

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; Screw\_Compressor |
| Tag path | `[default]_types_/PLC/Screw_Compressor` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 64 (63 atomic, 0 nested UDT, 1 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | `Compressor` | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

63 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Fail_Timer/` | Folder | | | | | | | |
| `Fail_Timer/ACC` | Int4 | OPC `{TagPrefix}.Fail_Timer.ACC` | PAX\_Status | yes | | | | |
| `Fail_Timer/PRE` | Int4 | OPC `{TagPrefix}.Fail_Timer.PRE` | PAX\_Faceplate | yes | | s fmt #0.0 | | Fail timer preset |
| `A_Code` | Int4 | OPC `{TagPrefix}.A_Code` | PAX\_Status | yes | | | | |
| `Alarm_String` | String | OPC `{TagPrefix}.Alarm_String` | PAX\_Faceplate | yes | | | | |
| `Alm` | Boolean | OPC `{TagPrefix}.Alm` | PAX\_Status | yes | | | 1 | Compressor alarm bit (PLC Alm) |
| `Amps` | Float4 | OPC `{TagPrefix}.Amps` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | A fmt #0.0 | | |
| `AntiR_Remaining` | Float4 | OPC `{TagPrefix}.AntiR_Remaining` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `AntiR_Rest` | Boolean | OPC `{TagPrefix}.AntiR_Rest` | PAX\_Status | yes | | | | |
| `AutoEN` | Boolean | OPC `{TagPrefix}.AutoEN` | PAX\_Status | yes | | | | compressor enabled for automatic control |
| `AutoTarget` | Float4 | OPC `{TagPrefix}.AutoTarget` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `AuxT` | Float4 | OPC `{TagPrefix}.AuxT` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `BHP_Design` | Float4 | OPC `{TagPrefix}.BHP_Design` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `Bkl_Set` | Int4 | OPC `{TagPrefix}.Bkl_Set` | PAX\_Faceplate | yes | | | | |
| `Clear_Failures` | Boolean | OPC `{TagPrefix}.Clear_Failures` | PAX\_Status | yes | | | | |
| `Color` | Int4 | OPC `{TagPrefix}.Color` | PAX\_Status | yes | | | | PLC Color / graphic state (\_Off=0, \_Running=1, \_AntiRec=2, \_Cutout=3, \_CommError=4) |
| `Comm` | Boolean | OPC `{TagPrefix}.Comm` | PAX\_Status | yes | | | 1 | Compressor communications fault bit (PLC Comm) |
| `Comm_Error_Count` | Int4 | OPC `{TagPrefix}.Comm_Error_Count` | PAX\_Status | yes | | | | |
| `CommPath` | String | OPC `{TagPrefix}.CommPath` | PAX\_Faceplate | yes | | | | |
| `CP_Mode` | Int4 | OPC `{TagPrefix}.CP_Mode` | PAX\_Status | yes | | | | Capacity / compressor mode (1 Remote, 2 Auto, 3 Manual) |
| `Cutout` | Boolean | OPC `{TagPrefix}.Cutout` | PAX\_Status | yes | | | 1 | Compressor cutout bit (PLC Cutout) |
| `Cutout_String` | String | OPC `{TagPrefix}.Cutout_String` | PAX\_Faceplate | yes | | | | |
| `DisH` | Float4 | OPC `{TagPrefix}.DisH` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `DisP` | Float4 | OPC `{TagPrefix}.DisP` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | psi fmt #0.0 | | |
| `DisT` | Float4 | OPC `{TagPrefix}.DisT` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | °F fmt #0.0 | | |
| `Failed` | Boolean | OPC `{TagPrefix}.Failed` | PAX\_Status | yes | | | 1 | Compressor failed bit (PLC Failed) |
| `FLA` | Float4 | OPC `{TagPrefix}.FLA` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | % fmt #0 | | |
| `FLTP` | Float4 | OPC `{TagPrefix}.FLTP` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `FU_Code` | Int4 | OPC `{TagPrefix}.FU_Code` | PAX\_Status | yes | | | | |
| `In_Sequence` | Boolean | OPC `{TagPrefix}.In_Sequence` | PAX\_Status | yes | | | | |
| `IP1` | Int4 | OPC `{TagPrefix}.IP1` | PAX\_Status | yes | | | | |
| `IP2` | Int4 | OPC `{TagPrefix}.IP2` | PAX\_Status | yes | | | | |
| `IP3` | Int4 | OPC `{TagPrefix}.IP3` | PAX\_Status | yes | | | | |
| `IP4` | Int4 | OPC `{TagPrefix}.IP4` | PAX\_Status | yes | | | | |
| `KW` | Float4 | OPC `{TagPrefix}.KW` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `LBL_Setpoint` | Int4 | OPC `{TagPrefix}.LBL_Setpoint` | PAX\_Status | yes | | | | |
| `Load_Req` | Boolean | OPC `{TagPrefix}.Load_Req` | PAX\_Status | yes | | | | |
| `Load_Setpoint` | Int4 | OPC `{TagPrefix}.Load_Setpoint` | PAX\_Status | yes | | | | |
| `LU_Mode` | Int4 | OPC `{TagPrefix}.LU_Mode` | PAX\_Status | yes | | | | |
| `LU_Permissive` | Boolean | OPC `{TagPrefix}.LU_Permissive` | PAX\_Status | yes | | | | |
| `LU_Pulse` | Int4 | OPC `{TagPrefix}.LU_Pulse` | PAX\_Status | yes | | | | |
| `Min_Runtime_Set` | Int4 | OPC `{TagPrefix}.Min_Runtime_Set` | PAX\_Faceplate | yes | | s fmt #0 | | Min runtime set |
| `Mode_Change` | Int4 | OPC `{TagPrefix}.Mode_Change` | PAX\_Status | yes | | | | |
| `Number` | Int4 | OPC `{TagPrefix}.Number` | PAX\_Status | yes | | | | |
| `OilP` | Float4 | OPC `{TagPrefix}.OilP` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | psi fmt #0.0 | | |
| `OilT` | Float4 | OPC `{TagPrefix}.OilT` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | °F fmt #0.0 | | |
| `Permissive` | Boolean | OPC `{TagPrefix}.Permissive` | PAX\_Status | yes | | | | |
| `RPM` | Int4 | OPC `{TagPrefix}.RPM` | PAX\_Status | yes | | | | |
| `Rung` | Int4 | OPC `{TagPrefix}.Rung` | PAX\_Status | yes | historian, OnChange, db 0.0 Absolute (Discrete) | | | PLC Rung state (\_Off=0, \_Running=1, \_AntiRec=2, \_Starting=3) |
| `SepT` | Float4 | OPC `{TagPrefix}.SepT` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `Start_Req` | Boolean | OPC `{TagPrefix}.Start_Req` | PAX\_Status | yes | | | | PLC Start\_Req |
| `Started` | Boolean | OPC `{TagPrefix}.Started` | PAX\_Status | yes | | | | Compressor started latch (PLC Started) |
| `Starting` | Boolean | OPC `{TagPrefix}.Starting` | PAX\_Status | yes | | | | |
| `Stop_Req` | Boolean | OPC `{TagPrefix}.Stop_Req` | PAX\_Status | yes | | | | PLC Stop\_Req |
| `SucH` | Float4 | OPC `{TagPrefix}.SucH` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |
| `SucP` | Float4 | OPC `{TagPrefix}.SucP` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | psi fmt #0.0 | | |
| `SucT` | Float4 | OPC `{TagPrefix}.SucT` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | °F fmt #0.0 | | |
| `SV_Mode` | Int4 | OPC `{TagPrefix}.SV_Mode` | PAX\_Status | yes | | | | Slide valve mode (1 Remote, 2 Auto, 3 Manual) |
| `SVP` | Float4 | OPC `{TagPrefix}.SVP` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | % fmt #0 | | |
| `Total_Capacity` | Int4 | OPC `{TagPrefix}.Total_Capacity` | PAX\_Status | yes | | | | |
| `TotalRuntime` | Float4 | OPC `{TagPrefix}.TotalRuntime` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | h fmt #0.0 | | PLC TotalRuntime (hours) |
| `UBL_Setpoint` | Int4 | OPC `{TagPrefix}.UBL_Setpoint` | PAX\_Status | yes | | | | |
| `Unload_Req` | Boolean | OPC `{TagPrefix}.Unload_Req` | PAX\_Status | yes | | | | |
| `VI` | Float4 | OPC `{TagPrefix}.VI` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | |

<details>
<summary>State labels (10 members)</summary>

| Member | States (value = label) |
|---|---|
| `Alm` | 0 = Off, 1 = On |
| `AutoEN` | 0 = Off, 1 = On |
| `Color` | 0 = Off, 1 = Running, 2 = AntiRec, 3 = Cutout, 4 = CommError |
| `Comm` | 0 = Off, 1 = On |
| `CP_Mode` | 1 = Remote, 2 = Auto, 3 = Manual |
| `Cutout` | 0 = Off, 1 = On |
| `Failed` | 0 = Off, 1 = On |
| `Rung` | 0 = Off, 1 = Running, 2 = AntiRec, 3 = Starting |
| `Started` | 0 = Off, 1 = On |
| `SV_Mode` | 1 = Remote, 2 = Auto, 3 = Manual |

</details>

## Alarms

| Member | Alarm | Priority | Mode | Enabled | Display path | Notes |
|---|---|---|---|---|---|---|
| `Alm` | Compressor Alarm | Medium | WhenTrue | `true` | | Screw\_Compressor COMP\[n\].Alm |
| `Comm` | Comm Error | Low | WhenTrue | `true` | | Screw\_Compressor COMP\[n\].Comm |
| `Cutout` | Cutout | High | WhenTrue | `true` | | Screw\_Compressor COMP\[n\].Cutout |
| `Failed` | Failed | Critical | WhenTrue | `true` | | Screw\_Compressor COMP\[n\].Failed |

Associated data `Site` / `Area` / `Device` come from the tag path (`split({PathToTag}, '/')` segments 1 / 2 / 4). Alarms are defined only here, on the UDT, never on instances: see [Alarms](../../../alarms.md).

## Used By

Nested in: [Devices/Compressor](../devices/compressor.md) (as `Comp`)

Reached through nesting by 5 top-level instance(s).
