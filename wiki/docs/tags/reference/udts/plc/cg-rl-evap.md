---
title: "PLC/CG_RL_Evap"
sidebar_label: "CG_RL_Evap"
description: "UDT definition PLC/CG_RL_Evap: Controller CG_RL_Evap (read only)"
generated: true
---

:::note

:::
# UDT `PLC/CG_RL_Evap`

Controller CG\_RL\_Evap (read only)

Standard PlantPAx CG\_RL\_Evap: ns=1;s=\[\{DeviceName\}\]\{TagPrefix\}.&lt;member&gt;, HMI member whitelist, every member readOnly, tag groups PAX\_Status / PAX\_Faceplate

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; CG\_RL\_Evap |
| Tag path | `[default]_types_/PLC/CG_RL_Evap` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 68 (68 atomic, 0 nested UDT, 0 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | `Cooling Stop set point` | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

68 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `AIDefrostStart` | Float4 | OPC `{TagPrefix}.AIDefrostStart` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | Defrost Start - analog input value |
| `AIDefrostStop` | Float4 | OPC `{TagPrefix}.AIDefrostStop` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | Defrost Stop - analog input value |
| `AIStart` | Boolean | OPC `{TagPrefix}.AIStart` | PAX\_Status | yes | | | | Flag set when analog input defrost start is requested |
| `AIStartOns` | Boolean | OPC `{TagPrefix}.AIStartOns` | PAX\_Status | yes | | | | |
| `AIStop` | Boolean | OPC `{TagPrefix}.AIStop` | PAX\_Status | yes | | | | Flag set when analog input defros stop is requested |
| `AIStopOns` | Boolean | OPC `{TagPrefix}.AIStopOns` | PAX\_Status | yes | | | | |
| `Cfg_AIDefrostStart` | Float4 | OPC `{TagPrefix}.Cfg_AIDefrostStart` | PAX\_Faceplate | yes | | | | Analog Input defrost start set point |
| `Cfg_AIStop` | Float4 | OPC `{TagPrefix}.Cfg_AIStop` | PAX\_Faceplate | yes | | | | Analog Input defrost stop set point |
| `Cfg_Bleed` | Float4 | OPC `{TagPrefix}.Cfg_Bleed` | PAX\_Faceplate | yes | | min fmt #0.0 | | Number of Minutes for the Bleed Defrost Step |
| `Cfg_CoolingTime` | Float4 | OPC `{TagPrefix}.Cfg_CoolingTime` | PAX\_Faceplate | yes | | min fmt #0.0 | | Defrost permissive - Minimum cooling time set point |
| `Cfg_CycFans` | Int2 | OPC `{TagPrefix}.Cfg_CycFans` | PAX\_Faceplate | yes | | | | Cycle Fans Mode for When the Unit is in Idle.$N0 == Fans Off$N1 == Cycle Fans$N2 == Fans On |
| `Cfg_Def1stTOD` | Int2 | OPC `{TagPrefix}.Cfg_Def1stTOD` | PAX\_Faceplate | yes | | | | 1st Defrost Time of Day set point |
| `Cfg_Def2ndTOD` | Int2 | OPC `{TagPrefix}.Cfg_Def2ndTOD` | PAX\_Faceplate | yes | | | | 2nd Defrost Time of Day set point |
| `Cfg_Def3rdTOD` | Int2 | OPC `{TagPrefix}.Cfg_Def3rdTOD` | PAX\_Faceplate | yes | | | | 3rd Defrost Time of Day set point |
| `Cfg_Def4thTOD` | Int2 | OPC `{TagPrefix}.Cfg_Def4thTOD` | PAX\_Faceplate | yes | | | | 4th Defrost Time of Day set point |
| `Cfg_DefrostStartMode` | Int2 | OPC `{TagPrefix}.Cfg_DefrostStartMode` | PAX\_Faceplate | yes | | | | HMI Defrost Start Mode $N0 == TOD $N1 == Liquid Time $N2 == Run Time$N3 == DI Intiate$N4 == AI initiate |
| `Cfg_DefrostStopMode` | Int2 | OPC `{TagPrefix}.Cfg_DefrostStopMode` | PAX\_Faceplate | yes | | | | HMI Defrost Stop Mode $N0 == None$N1 == DI Stop$N2 == AI Stop |
| `Cfg_FanDelay` | Float4 | OPC `{TagPrefix}.Cfg_FanDelay` | PAX\_Faceplate | yes | | min fmt #0.0 | | The Amount of Time the Unit is to Remain in the Fan Delay Defrost Srep |
| `Cfg_Has_SoftHotGas` | Boolean | OPC `{TagPrefix}.Cfg_Has_SoftHotGas` | PAX\_Faceplate | yes | | | | |
| `Cfg_HasBleedValve` | Boolean | OPC `{TagPrefix}.Cfg_HasBleedValve` | PAX\_Config | yes | | | | Valve Group has a Bleed Valve 0=No use Suction, 1=Yes |
| `Cfg_MainHotGas` | Float4 | OPC `{TagPrefix}.Cfg_MainHotGas` | PAX\_Faceplate | yes | | min fmt #0.0 | | The Amount of Time the Unit is to Remain in the Mian Hot Gas Defrost Srep |
| `Cfg_PumpOut` | Float4 | OPC `{TagPrefix}.Cfg_PumpOut` | PAX\_Faceplate | yes | | min fmt #0.0 | | The Amount of Time the Unit is to Remain in the Pump Out Defrost Srep |
| `Cfg_RunTime` | Float4 | OPC `{TagPrefix}.Cfg_RunTime` | PAX\_Faceplate | yes | | | | Defrost Initiate permissive - run time set point |
| `Cfg_SoftHotGas` | Float4 | OPC `{TagPrefix}.Cfg_SoftHotGas` | PAX\_Faceplate | yes | | min fmt #0.0 | | The Amount of Time the Unit is to Remain in the Soft Hot Gas Defrost Srep |
| `Cfg_SucType` | Boolean | OPC `{TagPrefix}.Cfg_SucType` | PAX\_Faceplate | yes | | | | Cfg - Type of Suction valve$N0=A4 (direct), 1=CK (reverse) |
| `Cfg_ZoneAirTemp` | Float4 | OPC `{TagPrefix}.Cfg_ZoneAirTemp` | PAX\_Faceplate | yes | | | | Zone Air Temperature Setpoint |
| `Cfg_ZoneAirTempDB` | Float4 | OPC `{TagPrefix}.Cfg_ZoneAirTempDB` | PAX\_Faceplate | yes | | °F fmt #0.0 | | Zone Air Temperature Deadband Setpoint |
| `Cleanup` | Boolean | OPC `{TagPrefix}.Cleanup` | PAX\_Status | yes | | | | Clean Mode Request |
| `CoolingStartOns` | Boolean | OPC `{TagPrefix}.CoolingStartOns` | PAX\_Status | yes | | | | |
| `CoolingTimeStart` | Boolean | OPC `{TagPrefix}.CoolingTimeStart` | PAX\_Status | yes | | | | Flag set when liquid runtime defrost is requested |
| `DIDefrostStart` | Boolean | OPC `{TagPrefix}.DIDefrostStart` | PAX\_Status | yes | | | | Digital Input defrost start set point |
| `DIDefrostStop` | Boolean | OPC `{TagPrefix}.DIDefrostStop` | PAX\_Status | yes | | | | Digital Input defrost stop set point |
| `DIStart` | Boolean | OPC `{TagPrefix}.DIStart` | PAX\_Status | yes | | | | Flag set when digital input defrost is requested |
| `DIStartOns` | Boolean | OPC `{TagPrefix}.DIStartOns` | PAX\_Status | yes | | | | |
| `DIStop` | Boolean | OPC `{TagPrefix}.DIStop` | PAX\_Status | yes | | | | |
| `DIStopOns` | Boolean | OPC `{TagPrefix}.DIStopOns` | PAX\_Status | yes | | | | |
| `HMI_HeatMode_Enable` | Boolean | OPC `{TagPrefix}.HMI_HeatMode_Enable` | PAX\_Faceplate | yes | | | | |
| `HMIEnable` | Boolean | OPC `{TagPrefix}.HMIEnable` | PAX\_Faceplate | yes | | | | The Unit is Enabled to Run by the Operator |
| `HMIStartDefrost` | Boolean | OPC `{TagPrefix}.HMIStartDefrost` | PAX\_Faceplate | yes | | | | Flag from the HMI to Start a Defrost |
| `HMIStopDefrost` | Boolean | OPC `{TagPrefix}.HMIStopDefrost` | PAX\_Faceplate | yes | | | | Flag from the HMI to Stop a Defrost |
| `IntlkOK` | Boolean | OPC `{TagPrefix}.IntlkOK` | PAX\_Status | yes | | | | Flag to Disable the Unit Due to System Interlock |
| `Last_State` | Int2 | OPC `{TagPrefix}.Last_State` | PAX\_Status | yes | | | | State when interlock or disabled occured. |
| `MinHotGasTime` | Int4 | OPC `{TagPrefix}.MinHotGasTime` | PAX\_Status | yes | | | | |
| `Off` | Boolean | OPC `{TagPrefix}.Off` | PAX\_Status | yes | | | | Flag to Indicate the Unit is Turned Off, Either from the HMI or due to a Shutdown. |
| `PermOK` | Boolean | OPC `{TagPrefix}.PermOK` | PAX\_Status | yes | | | | Flag to Disable the Unit Due to System Permissive |
| `RuntimeStart` | Boolean | OPC `{TagPrefix}.RuntimeStart` | PAX\_Status | yes | | | | Flag set when defrost runtime defrost is requested |
| `RuntimeStartOns` | Boolean | OPC `{TagPrefix}.RuntimeStartOns` | PAX\_Status | yes | | | | |
| `SB_Enable` | Boolean | OPC `{TagPrefix}.SB_Enable` | PAX\_Faceplate | yes | | | | |
| `SB_Latch` | Boolean | OPC `{TagPrefix}.SB_Latch` | PAX\_Faceplate | yes | | | | |
| `SB_StartTime` | Int2 | OPC `{TagPrefix}.SB_StartTime` | PAX\_Faceplate | yes | | | | |
| `SB_StopTime` | Int2 | OPC `{TagPrefix}.SB_StopTime` | PAX\_Faceplate | yes | | | | |
| `Seqr_Output` | Int2 | OPC `{TagPrefix}.Seqr_Output` | PAX\_Status | yes | | | | Phase sequencer output word |
| `StartDefrost` | Boolean | OPC `{TagPrefix}.StartDefrost` | PAX\_Status | yes | | | | Flag to begin a defrost cycle |
| `StopDefrost` | Boolean | OPC `{TagPrefix}.StopDefrost` | PAX\_Status | yes | | | | |
| `Sts_State` | Int4 | OPC `{TagPrefix}.Sts_State` | PAX\_Status | yes | historian, OnChange, db 0.0 Absolute (Discrete) | | | Control Group Phases$N0 == Off$N1 == Pump Out$N2 == Soft Hot Gas$N3 == Main Hot Gas$N4 == Bleed$N5 == Fan Delay$N6 == Cooling$N7 == Idle$N8 == Cleanup$N9 == Pe… |
| `TODStart` | Boolean | OPC `{TagPrefix}.TODStart` | PAX\_Status | yes | | | | Flag to start a defrost cycle on time of day |
| `TODStartOns` | Boolean | OPC `{TagPrefix}.TODStartOns` | PAX\_Status | yes | | | | |
| `TooCold` | Boolean | OPC `{TagPrefix}.TooCold` | PAX\_Status | yes | | | | Flag set when ZAT is too cold |
| `TooHot` | Boolean | OPC `{TagPrefix}.TooHot` | PAX\_Status | yes | | | | Flag set when ZAT is too Hot |
| `Val_CoolingTime` | Float4 | OPC `{TagPrefix}.Val_CoolingTime` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | Elapsed cooling (Liquid open) time counter |
| `Val_RunTime` | Float4 | OPC `{TagPrefix}.Val_RunTime` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | Elapsed total evaporator runtime since last defrost |
| `Val_TimeLeft` | Float4 | OPC `{TagPrefix}.Val_TimeLeft` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | min fmt #0.0 | | Time in Minutes Left in the Current Defrost Step |
| `ZAT_High` | Float4 | OPC `{TagPrefix}.ZAT_High` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | Cooling Start set point |
| `ZAT_HiHi` | Float4 | OPC `{TagPrefix}.ZAT_HiHi` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | Too\_hot\_set\_point |
| `ZAT_LoLo` | Float4 | OPC `{TagPrefix}.ZAT_LoLo` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | Too cold set point |
| `ZAT_Low` | Float4 | OPC `{TagPrefix}.ZAT_Low` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | Cooling Stop set point |
| `ZAT_MaxSet` | Float4 | OPC `{TagPrefix}.ZAT_MaxSet` | PAX\_Faceplate | yes | | | | |
| `ZAT_MinSet` | Float4 | OPC `{TagPrefix}.ZAT_MinSet` | PAX\_Faceplate | yes | | | | |

<details>
<summary>State labels (11 members)</summary>

| Member | States (value = label) |
|---|---|
| `Cfg_CycFans` | 0 = Off, 1 = Cycle, 2 = On |
| `Cfg_DefrostStartMode` | 0 = Time of Day, 1 = Cooling Time, 2 = Runtime |
| `Cleanup` | 0 = Off, 1 = On |
| `HMIEnable` | 0 = Off, 1 = On |
| `HMIStartDefrost` | 0 = Off, 1 = On |
| `HMIStopDefrost` | 0 = Off, 1 = On |
| `IntlkOK` | 0 = Off, 1 = On |
| `Off` | 0 = Off, 1 = On |
| `PermOK` | 0 = Off, 1 = On |
| `TooCold` | 0 = Off, 1 = On |
| `TooHot` | 0 = Off, 1 = On |

</details>

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [Devices/Evaporator](../devices/evaporator.md) (as `CG`)

Reached through nesting by 19 top-level instance(s).
