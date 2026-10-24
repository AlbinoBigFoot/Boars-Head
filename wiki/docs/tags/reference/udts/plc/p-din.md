---
title: "PLC/P_DIn"
sidebar_label: "P_DIn"
description: "UDT definition PLC/P_DIn: PlantPAx P_DIn (read only)"
generated: true
---

:::note

:::
# UDT `PLC/P_DIn`

PlantPAx P\_DIn (read only)

Standard PlantPAx P\_DIn: ns=1;s=\[\{DeviceName\}\]\{TagPrefix\}.&lt;member&gt;, HMI member whitelist, every member readOnly, tag groups PAX\_Status / PAX\_Faceplate

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; P\_DIn |
| Tag path | `[default]_types_/PLC/P_DIn` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 55 (53 atomic, 0 nested UDT, 2 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `AlarmOnSts` | Integer | `0` | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

53 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `TgtDisagree/` | Folder | | | | | | | |
| `TgtDisagree/Ack` | Boolean | OPC `{TagPrefix}.TgtDisagree.Ack` | PAX\_Status | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `TgtDisagree/Alm` | Boolean | OPC `{TagPrefix}.TgtDisagree.Alm` | PAX\_Status | yes | | | | Alarm output 1=In Alarm |
| `TgtDisagree/Cfg_Cond` | String | OPC `{TagPrefix}.TgtDisagree.Cfg_Cond` | PAX\_Faceplate | yes | | | | |
| `TgtDisagree/Cfg_Exists` | Boolean | OPC `{TagPrefix}.TgtDisagree.Cfg_Exists` | PAX\_Faceplate | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `TgtDisagree/Disabled` | Boolean | OPC `{TagPrefix}.TgtDisagree.Disabled` | PAX\_Status | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `TgtDisagree/OCmd_Ack` | Boolean | OPC `{TagPrefix}.TgtDisagree.OCmd_Ack` | PAX\_Faceplate | yes | | | | Operator Command to Acknowledge alarm |
| `TgtDisagree/PCfg_AllowExist` | Boolean | OPC `{TagPrefix}.TgtDisagree.PCfg_AllowExist` | PAX\_Faceplate | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `TgtDisagree/Rdy_Ack` | Boolean | OPC `{TagPrefix}.TgtDisagree.Rdy_Ack` | PAX\_Faceplate | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `TgtDisagree/Shelved` | Boolean | OPC `{TagPrefix}.TgtDisagree.Shelved` | PAX\_Status | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `TgtDisagree/Sts_Err` | Boolean | OPC `{TagPrefix}.TgtDisagree.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `TgtDisagree/Suppressed` | Boolean | OPC `{TagPrefix}.TgtDisagree.Suppressed` | PAX\_Status | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `TgtDisagree/Val_Notify` | Int1 | OPC `{TagPrefix}.TgtDisagree.Val_Notify` | PAX\_Status | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `TgtDisagreeGate/` | Folder | | | | | | | |
| `TgtDisagreeGate/Cfg_InpCond` | String | OPC `{TagPrefix}.TgtDisagreeGate.Cfg_InpCond` | PAX\_Faceplate | yes | | | | |
| `TgtDisagreeGate/Sts_Err` | Boolean | OPC `{TagPrefix}.TgtDisagreeGate.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config (see detail Err\_ bits for reason), display icon |
| `TgtDisagreeGate/Sts_Gate` | Boolean | OPC `{TagPrefix}.TgtDisagreeGate.Sts_Gate` | PAX\_Status | yes | | | | 1=Gate Delay done, Output is enabled |
| `Alm_TgtDisagree` | Boolean | OPC `{TagPrefix}.Alm_TgtDisagree` | PAX\_Status | yes | | | | 1=Alarm: Input is not in Target state |
| `Cfg_0StText` | String | OPC `{TagPrefix}.Cfg_0StText` | PAX\_Faceplate | yes | | | | |
| `Cfg_1StText` | String | OPC `{TagPrefix}.Cfg_1StText` | PAX\_Faceplate | yes | | | | |
| `Cfg_Debounce` | Float4 | OPC `{TagPrefix}.Cfg_Debounce` | PAX\_Faceplate | yes | | | | Minimum time Input Sts must maintain state (sec) |
| `Cfg_Desc` | String | OPC `{TagPrefix}.Cfg_Desc` | PAX\_Faceplate | yes | | | | |
| `Cfg_HasTgtDisagreeAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasTgtDisagreeAlm` | PAX\_Config | yes | | | | |
| `Cfg_Label` | String | OPC `{TagPrefix}.Cfg_Label` | PAX\_Faceplate | yes | | | | |
| `Cfg_NormTextVis` | Boolean | OPC `{TagPrefix}.Cfg_NormTextVis` | PAX\_Faceplate | yes | | | | 1=Display state text in $Qnormal$Q state (= target), 0=hide (some HMI objects) |
| `Cfg_NoSubstPV` | Boolean | OPC `{TagPrefix}.Cfg_NoSubstPV` | PAX\_Faceplate | yes | | | | 1=Disallow selection of Substitute PV |
| `Cfg_PCmdClear` | Boolean | OPC `{TagPrefix}.Cfg_PCmdClear` | PAX\_Faceplate | yes | | | | 1=Clear Program Commands on receipt$N0=Leave Set |
| `Cfg_Tag` | String | OPC `{TagPrefix}.Cfg_Tag` | PAX\_Faceplate | yes | | | | |
| `Err_Alarm` | Boolean | OPC `{TagPrefix}.Err_Alarm` | PAX\_Faceplate | yes | | | | 1=Error in Config: Alarm Min On Time, Shelf Time, Severity |
| `Err_Timer` | Boolean | OPC `{TagPrefix}.Err_Timer` | PAX\_Faceplate | yes | | | | 1=Error in Config: Invalid Timer Preset (use 0 to 2147483) |
| `Inf_Lib` | String | OPC `{TagPrefix}.Inf_Lib` | PAX\_Faceplate | yes | | | | |
| `Inf_Type` | String | OPC `{TagPrefix}.Inf_Type` | PAX\_Faceplate | yes | | | | |
| `Inp_Sim` | Boolean | OPC `{TagPrefix}.Inp_Sim` | PAX\_Status | yes | | | | 1=Use simulated PV (Set\_SimPV); 0=Use Input (Inp\_PV) |
| `Inp_Target` | Boolean | OPC `{TagPrefix}.Inp_Target` | PAX\_Status | yes | | | | Target State of Input (Disagree Status if not in Target State) |
| `MCmd_InpPV` | Boolean | OPC `{TagPrefix}.MCmd_InpPV` | PAX\_Faceplate | yes | | | | Maintenance Command to use Input PV (normal) |
| `MCmd_SubstPV` | Boolean | OPC `{TagPrefix}.MCmd_SubstPV` | PAX\_Faceplate | yes | | | | Maintenance Command to use Substitute PV (override input) |
| `MSet_SubstPV` | Boolean | OPC `{TagPrefix}.MSet_SubstPV` | PAX\_Faceplate | yes | | | | Maintenance-Entered Substitute PV |
| `OCmd_Reset` | Boolean | OPC `{TagPrefix}.OCmd_Reset` | PAX\_Faceplate | yes | | | | Operator Command to Reset all latched Alarms |
| `OCmd_ResetAckAll` | Boolean | OPC `{TagPrefix}.OCmd_ResetAckAll` | PAX\_Faceplate | yes | | | | Operator Command to Reset and Acknowledge all Alarms |
| `Rdy_InpPV` | Boolean | OPC `{TagPrefix}.Rdy_InpPV` | PAX\_Faceplate | yes | | | | 1=Ready for MCmd\_InpPV |
| `Rdy_SubstPV` | Boolean | OPC `{TagPrefix}.Rdy_SubstPV` | PAX\_Faceplate | yes | | | | 1=Ready for MCmd\_SubstPV |
| `Set_SimPV` | Boolean | OPC `{TagPrefix}.Set_SimPV` | PAX\_Faceplate | yes | | | | PV used in Simulation (Inp\_Sim=1) |
| `SrcQ_IO` | Int1 | OPC `{TagPrefix}.SrcQ_IO` | PAX\_Status | yes | | | | Source and Quality of primary I/O (enumeration) |
| `Sts` | Boolean | OPC `{TagPrefix}.Sts` | PAX\_Status | yes | | | 1 | Discrete Input Status (incl. Debounce, Manual Override, if used) |
| `Sts_AlmInh` | Boolean | OPC `{TagPrefix}.Sts_AlmInh` | PAX\_Status | yes | | | | 1=One or more Alarms Shelved, Disabled or Suppressed |
| `Sts_Err` | Boolean | OPC `{TagPrefix}.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config: see detail bits for reason |
| `Sts_InpPV` | Boolean | OPC `{TagPrefix}.Sts_InpPV` | PAX\_Status | yes | | | | 1=Using Input PV (normal) |
| `Sts_MaintByp` | Boolean | OPC `{TagPrefix}.Sts_MaintByp` | PAX\_Status | yes | | | | 1=Device has a Maintenance Bypass function active |
| `Sts_PV` | Boolean | OPC `{TagPrefix}.Sts_PV` | PAX\_Status | yes | | | | Discrete Input Status (actual, not subject to Override) |
| `Sts_PVBad` | Boolean | OPC `{TagPrefix}.Sts_PVBad` | PAX\_Status | yes | | | | Input Comm Status/ Quality (0=OK, 1=Bad) |
| `Sts_SubstPV` | Boolean | OPC `{TagPrefix}.Sts_SubstPV` | PAX\_Status | yes | | | | 1=Using Substitute PV (Input being overridden) |
| `Sts_TgtDisagree` | Boolean | OPC `{TagPrefix}.Sts_TgtDisagree` | PAX\_Status | yes | | | 1 | 1=Input is not in Target state |
| `Sts_TgtDisagreeCmp` | Boolean | OPC `{TagPrefix}.Sts_TgtDisagreeCmp` | PAX\_Status | yes | | | | Input vs. Target comparicon result 1=Disagree |
| `Val_Fault` | Int1 | OPC `{TagPrefix}.Val_Fault` | PAX\_Status | yes | historian, OnChange, db 0.0 Absolute (Discrete) | | | Device Fault Status 0=none, 16=Tgt Disagree, 34=CfgErr |
| `Val_Notify` | Int1 | OPC `{TagPrefix}.Val_Notify` | PAX\_Status | yes | historian, OnChange, db 0.0 Absolute (Discrete) | | | Current Alarm Level and Acknowledgement (enumeration) |

## Alarms

| Member | Alarm | Priority | Mode | Enabled | Display path | Notes |
|---|---|---|---|---|---|---|
| `Sts` | State Alarm | High | WhenTrue | `{AlarmOnSts}` | \{Description\} | PlantPAx P\_DIn Sts (AlarmOnSts) |
| `Sts_TgtDisagree` | Target Disagree | Medium | WhenTrue | `coalesce({[.]Cfg_HasTgtDisagreeAlm}, false)` | | PlantPAx P\_DIn Sts\_TgtDisagree |

Associated data `Site` / `Area` / `Device` come from the tag path (`split({PathToTag}, '/')` segments 1 / 2 / 4). Alarms are defined only here, on the UDT, never on instances: see [Alarms](../../../alarms.md).

## Used By

Nested in: [Devices/ExhaustFan](../devices/exhaustfan.md) (as `DIn`), [Devices/Tank](../devices/tank.md) (as `HlcoDIn`), [Devices/Tank](../devices/tank.md) (as `HiHiDIn`), [Devices/Tank](../devices/tank.md) (as `OplDIn`), [Devices/Tank](../devices/tank.md) (as `LoLoDIn`), [Devices/Tank](../devices/tank.md) (as `Pump1Alm`), [Devices/Tank](../devices/tank.md) (as `Pump2Alm`), [Devices/DiscreteInput](../devices/discreteinput.md) (as `DIn`), [PLC/Accumulator](accumulator.md) (as `HLCO`), [PLC/Recirculator](recirculator.md) (as `HLCO`), [PLC/Recirculator](recirculator.md) (as `HLS`), [PLC/Recirculator](recirculator.md) (as `LLCO`), [PLC/Liquid\_Transfer\_Unit](liquid-transfer-unit.md) (as `LTU_Input`)

Reached through nesting by 59 top-level instance(s).
