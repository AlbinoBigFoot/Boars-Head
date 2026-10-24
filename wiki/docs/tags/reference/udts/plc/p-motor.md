---
title: "PLC/P_Motor"
sidebar_label: "P_Motor"
description: "UDT definition PLC/P_Motor: PlantPAx P_Motor (read only)"
generated: true
---

:::note

:::
# UDT `PLC/P_Motor`

PlantPAx P\_Motor (read only)

Standard PlantPAx P\_Motor: ns=1;s=\[\{DeviceName\}\]\{TagPrefix\}.&lt;member&gt;, HMI member whitelist, every member readOnly, tag groups PAX\_Status / PAX\_Faceplate

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; P\_Motor |
| Tag path | `[default]_types_/PLC/P_Motor` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 114 (109 atomic, 0 nested UDT, 5 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

109 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `FailToStart/` | Folder | | | | | | | |
| `FailToStart/Ack` | Boolean | OPC `{TagPrefix}.FailToStart.Ack` | PAX\_Status | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `FailToStart/Alm` | Boolean | OPC `{TagPrefix}.FailToStart.Alm` | PAX\_Status | yes | | | | Alarm output 1=In Alarm |
| `FailToStart/Cfg_Exists` | Boolean | OPC `{TagPrefix}.FailToStart.Cfg_Exists` | PAX\_Faceplate | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `FailToStart/Disabled` | Boolean | OPC `{TagPrefix}.FailToStart.Disabled` | PAX\_Status | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `FailToStart/Shelved` | Boolean | OPC `{TagPrefix}.FailToStart.Shelved` | PAX\_Status | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `FailToStart/Suppressed` | Boolean | OPC `{TagPrefix}.FailToStart.Suppressed` | PAX\_Status | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `FailToStop/` | Folder | | | | | | | |
| `FailToStop/Ack` | Boolean | OPC `{TagPrefix}.FailToStop.Ack` | PAX\_Status | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `FailToStop/Alm` | Boolean | OPC `{TagPrefix}.FailToStop.Alm` | PAX\_Status | yes | | | | Alarm output 1=In Alarm |
| `FailToStop/Cfg_Exists` | Boolean | OPC `{TagPrefix}.FailToStop.Cfg_Exists` | PAX\_Faceplate | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `FailToStop/Disabled` | Boolean | OPC `{TagPrefix}.FailToStop.Disabled` | PAX\_Status | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `FailToStop/Shelved` | Boolean | OPC `{TagPrefix}.FailToStop.Shelved` | PAX\_Status | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `FailToStop/Suppressed` | Boolean | OPC `{TagPrefix}.FailToStop.Suppressed` | PAX\_Status | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `IntlkTrip/` | Folder | | | | | | | |
| `IntlkTrip/Ack` | Boolean | OPC `{TagPrefix}.IntlkTrip.Ack` | PAX\_Status | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `IntlkTrip/Alm` | Boolean | OPC `{TagPrefix}.IntlkTrip.Alm` | PAX\_Status | yes | | | | Alarm output 1=In Alarm |
| `IntlkTrip/Cfg_Exists` | Boolean | OPC `{TagPrefix}.IntlkTrip.Cfg_Exists` | PAX\_Faceplate | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `IntlkTrip/Disabled` | Boolean | OPC `{TagPrefix}.IntlkTrip.Disabled` | PAX\_Status | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `IntlkTrip/Shelved` | Boolean | OPC `{TagPrefix}.IntlkTrip.Shelved` | PAX\_Status | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `IntlkTrip/Suppressed` | Boolean | OPC `{TagPrefix}.IntlkTrip.Suppressed` | PAX\_Status | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `IOFault/` | Folder | | | | | | | |
| `IOFault/Ack` | Boolean | OPC `{TagPrefix}.IOFault.Ack` | PAX\_Status | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `IOFault/Alm` | Boolean | OPC `{TagPrefix}.IOFault.Alm` | PAX\_Status | yes | | | | Alarm output 1=In Alarm |
| `IOFault/Cfg_Exists` | Boolean | OPC `{TagPrefix}.IOFault.Cfg_Exists` | PAX\_Faceplate | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `IOFault/Disabled` | Boolean | OPC `{TagPrefix}.IOFault.Disabled` | PAX\_Status | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `IOFault/Shelved` | Boolean | OPC `{TagPrefix}.IOFault.Shelved` | PAX\_Status | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `IOFault/Sts_AlmInh` | Boolean | OPC `{TagPrefix}.IOFault.Sts_AlmInh` | PAX\_Status | yes | | | | 1=Alarm has been suppressed, shelved or disabled, display $QI$Q icon |
| `IOFault/Suppressed` | Boolean | OPC `{TagPrefix}.IOFault.Suppressed` | PAX\_Status | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `IOFault/Val_Notify` | Int1 | OPC `{TagPrefix}.IOFault.Val_Notify` | PAX\_Status | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `Mode/` | Folder | | | | | | | |
| `Mode/OCmd_AcqLock` | Boolean | OPC `{TagPrefix}.Mode.OCmd_AcqLock` | PAX\_Faceplate | yes | | | | Operator Command to Acquire (Prog to Oper) / Lock Ownership |
| `Mode/OCmd_UnlockRel` | Boolean | OPC `{TagPrefix}.Mode.OCmd_UnlockRel` | PAX\_Faceplate | yes | | | | Operator Command to Unlock / Release (Oper to Prog) Ownership |
| `Mode/Rdy_OAcq` | Boolean | OPC `{TagPrefix}.Mode.Rdy_OAcq` | PAX\_Faceplate | yes | | | | 1=Ready for OCmd\_AcqLock, enable Acquire (to Oper) button |
| `Mode/Rdy_OLock` | Boolean | OPC `{TagPrefix}.Mode.Rdy_OLock` | PAX\_Faceplate | yes | | | | 1=Ready for OCmd\_AcqLock, enable Oper Lock button |
| `Mode/Rdy_ORel` | Boolean | OPC `{TagPrefix}.Mode.Rdy_ORel` | PAX\_Faceplate | yes | | | | 1=Ready for OCmd\_UnlockRel, enable Release (to Prog) button |
| `Mode/Rdy_OUnlock` | Boolean | OPC `{TagPrefix}.Mode.Rdy_OUnlock` | PAX\_Faceplate | yes | | | | 1=Ready for OCmd\_UnlockRel, enable Oper Unlock button |
| `Mode/Sts_ProgOperLock` | Boolean | OPC `{TagPrefix}.Mode.Sts_ProgOperLock` | PAX\_Status | yes | | | | 1=Program or Operator has requested Mode Lock |
| `Mode/Sts_ProgOperSel` | Boolean | OPC `{TagPrefix}.Mode.Sts_ProgOperSel` | PAX\_Status | yes | | | | Prog/Oper selection 1=Program, 0=Operator |
| `Mode/Val` | Int1 | OPC `{TagPrefix}.Mode.Val` | PAX\_Status | yes | | | | Mode enum: 0=No, 1=H, 2=M, 3=!, 4=P Lock, 5=O Lock, 6=P (O Def), 7=O (P Def), 8=P (= Def), 9=O (= Def) |
| `Ack_FailToStart` | Boolean | OPC `{TagPrefix}.Ack_FailToStart` | PAX\_Status | yes | | | | 1=Fail to Start Alarm has been acknowledged |
| `Ack_FailToStop` | Boolean | OPC `{TagPrefix}.Ack_FailToStop` | PAX\_Status | yes | | | | 1=Fail to Stop Alarm has been acknowledged |
| `Ack_IntlkTrip` | Boolean | OPC `{TagPrefix}.Ack_IntlkTrip` | PAX\_Status | yes | | | | 1=Interlock Trip Alarm has been acknowledged |
| `Ack_IOFault` | Boolean | OPC `{TagPrefix}.Ack_IOFault` | PAX\_Status | yes | | | | 1=I/O Fault Alarm has been acknowledged |
| `Alm_FailToStart` | Boolean | OPC `{TagPrefix}.Alm_FailToStart` | PAX\_Status | yes | | | 1 | 1=Motor Fail to Start Alarm |
| `Alm_FailToStop` | Boolean | OPC `{TagPrefix}.Alm_FailToStop` | PAX\_Status | yes | | | 1 | 1=Motor Fail to Stop Alarm |
| `Alm_IntlkTrip` | Boolean | OPC `{TagPrefix}.Alm_IntlkTrip` | PAX\_Status | yes | | | 1 | 1=Alarm: Motor stopped by an Interlock NOT OK |
| `Alm_IOFault` | Boolean | OPC `{TagPrefix}.Alm_IOFault` | PAX\_Status | yes | | | 1 | 1=I/O Fault Alarm |
| `Cfg_AllowLocal` | Boolean | OPC `{TagPrefix}.Cfg_AllowLocal` | PAX\_Faceplate | yes | | | | 1=Allow Local Start/Stop without alarm, 0=Start/Stop from HMI/prog only |
| `Cfg_Desc` | String | OPC `{TagPrefix}.Cfg_Desc` | PAX\_Faceplate | yes | | | | |
| `Cfg_FailToStartT` | Int4 | OPC `{TagPrefix}.Cfg_FailToStartT` | PAX\_Faceplate | yes | | s fmt #0.0 | | Time after Start for running feedback before Fault (sec) |
| `Cfg_FailToStopT` | Int4 | OPC `{TagPrefix}.Cfg_FailToStopT` | PAX\_Faceplate | yes | | | | Time after Stop for stopped feedback (=0) before Fault (sec) |
| `Cfg_HasIntlkObj` | Boolean | OPC `{TagPrefix}.Cfg_HasIntlkObj` | PAX\_Faceplate | yes | | | | 1=Enable navigation to interlock object |
| `Cfg_HasOvldObj` | Boolean | OPC `{TagPrefix}.Cfg_HasOvldObj` | PAX\_Faceplate | yes | | | | 1=Enable navigation to overload object |
| `Cfg_HasPermObj` | Boolean | OPC `{TagPrefix}.Cfg_HasPermObj` | PAX\_Faceplate | yes | | | | 1=Enable navigation to permissive object |
| `Cfg_HasResInhObj` | Boolean | OPC `{TagPrefix}.Cfg_HasResInhObj` | PAX\_Faceplate | yes | | | | 1=Enable navigation to restart inhibit object |
| `Cfg_HasRunFdbk` | Boolean | OPC `{TagPrefix}.Cfg_HasRunFdbk` | PAX\_Faceplate | yes | | | | 1=Motor provides run feedback |
| `Cfg_HasRunTimeObj` | Boolean | OPC `{TagPrefix}.Cfg_HasRunTimeObj` | PAX\_Faceplate | yes | | | | 1=Enable navigation to run time object |
| `Cfg_Label` | String | OPC `{TagPrefix}.Cfg_Label` | PAX\_Faceplate | yes | | | | |
| `Cfg_OCmdResets` | Boolean | OPC `{TagPrefix}.Cfg_OCmdResets` | PAX\_Faceplate | yes | | | | 1=New Oper motor cmd. resets fault,$N0=reset req$'d to clear fault |
| `Cfg_OperStopPrio` | Boolean | OPC `{TagPrefix}.Cfg_OperStopPrio` | PAX\_Faceplate | yes | | | | 1=OCmd\_Stop available in any mode, 0=OCmd\_Stop only in Oper, Maint modes. |
| `Cfg_OvrdPermIntlk` | Boolean | OPC `{TagPrefix}.Cfg_OvrdPermIntlk` | PAX\_Faceplate | yes | | | | 1=Override ignores Bypassable Perm/ Intlk; 0=always use Perm/Intlk |
| `Cfg_PCmdClear` | Boolean | OPC `{TagPrefix}.Cfg_PCmdClear` | PAX\_Faceplate | yes | | | | P\_Motor Cfg\_PCmdClear |
| `Cfg_ShedOnFailToStart` | Boolean | OPC `{TagPrefix}.Cfg_ShedOnFailToStart` | PAX\_Faceplate | yes | | | | 1=Stop Motor and Alarm on Fail to Start; 0=Alarm only on Fail to Start |
| `Cfg_ShedOnIOFault` | Boolean | OPC `{TagPrefix}.Cfg_ShedOnIOFault` | PAX\_Faceplate | yes | | | | 1=Stop Motor and Alarm on I/O Fault; 0=Alarm only on I/O Fault |
| `Cfg_SimFdbkT` | Int4 | OPC `{TagPrefix}.Cfg_SimFdbkT` | PAX\_Faceplate | yes | | | | Feedback delay in Simulation (sec) |
| `Cfg_Tag` | String | OPC `{TagPrefix}.Cfg_Tag` | PAX\_Faceplate | yes | | | | |
| `Inf_Lib` | String | OPC `{TagPrefix}.Inf_Lib` | PAX\_Faceplate | yes | | | | |
| `Inf_Type` | String | OPC `{TagPrefix}.Inf_Type` | PAX\_Faceplate | yes | | | | |
| `Inp_IntlkOK` | Boolean | OPC `{TagPrefix}.Inp_IntlkOK` | PAX\_Status | yes | | | | 1=Interlocks OK, motor can start/run |
| `Inp_NBIntlkOK` | Boolean | OPC `{TagPrefix}.Inp_NBIntlkOK` | PAX\_Status | yes | | | | 1=Non-Bypassable Interlocks OK, motor can start/run |
| `Inp_NBPermOK` | Boolean | OPC `{TagPrefix}.Inp_NBPermOK` | PAX\_Status | yes | | | | 1=Non-Bypassable Permissives OK, motor can start |
| `Inp_Ovrd` | Boolean | OPC `{TagPrefix}.Inp_Ovrd` | PAX\_Status | yes | | | | P\_Motor Ovrd |
| `Inp_PermOK` | Boolean | OPC `{TagPrefix}.Inp_PermOK` | PAX\_Status | yes | | | | 1=Permissives OK, motor can start |
| `Inp_Sim` | Boolean | OPC `{TagPrefix}.Inp_Sim` | PAX\_Status | yes | | | | 1=Simulate working motor; 0=Start/Stop/ Monitor actual motor |
| `MCmd_Disable` | Boolean | OPC `{TagPrefix}.MCmd_Disable` | PAX\_Faceplate | yes | | | | Maintenance Command to Disable Motor |
| `MCmd_Enable` | Boolean | OPC `{TagPrefix}.MCmd_Enable` | PAX\_Faceplate | yes | | | | Maintenance Command to Enable (allow to run) Motor |
| `Nrdy_CfgErr` | Boolean | OPC `{TagPrefix}.Nrdy_CfgErr` | PAX\_Faceplate | yes | | | | 1=Device Not Ready: Configuration Error |
| `Nrdy_Disabled` | Boolean | OPC `{TagPrefix}.Nrdy_Disabled` | PAX\_Faceplate | yes | | | | 1=Device Not Ready: Device Disabled by Maintenance |
| `Nrdy_Fail` | Boolean | OPC `{TagPrefix}.Nrdy_Fail` | PAX\_Faceplate | yes | | | | 1=Device Not Ready: Device Failure (Shed Requires Reset) |
| `Nrdy_Intlk` | Boolean | OPC `{TagPrefix}.Nrdy_Intlk` | PAX\_Faceplate | yes | | | | 1=Device Not Ready: Interlock Not OK |
| `Nrdy_IOFault` | Boolean | OPC `{TagPrefix}.Nrdy_IOFault` | PAX\_Faceplate | yes | | | | 1=Device Not Ready: I/O Fault (Shed Requires Reset) |
| `Nrdy_NoMode` | Boolean | OPC `{TagPrefix}.Nrdy_NoMode` | PAX\_Faceplate | yes | | | | 1=Device Not Ready: Device Logic Disabled / NO Mode |
| `Nrdy_Perm` | Boolean | OPC `{TagPrefix}.Nrdy_Perm` | PAX\_Faceplate | yes | | | | 1=Device Not Ready: Permissive Not OK |
| `OCmd_Bypass` | Boolean | OPC `{TagPrefix}.OCmd_Bypass` | PAX\_Faceplate | yes | | | | Operator Command to Bypass all Bypassable Interlocks and Permissives |
| `OCmd_Reset` | Boolean | OPC `{TagPrefix}.OCmd_Reset` | PAX\_Faceplate | yes | | | | Operator Command to Reset all Alarms requiring Reset |
| `OCmd_ResetAckAll` | Boolean | OPC `{TagPrefix}.OCmd_ResetAckAll` | PAX\_Faceplate | yes | | | | Operator Command to Reset all Alarms and latched Shed conditions |
| `OCmd_Start` | Boolean | OPC `{TagPrefix}.OCmd_Start` | PAX\_Faceplate | yes | | | | Operator Command to Start Motor |
| `OCmd_Stop` | Boolean | OPC `{TagPrefix}.OCmd_Stop` | PAX\_Faceplate | yes | | | | Operator Command to Stop Motor |
| `Rdy_ResetAckAll` | Boolean | OPC `{TagPrefix}.Rdy_ResetAckAll` | PAX\_Faceplate | yes | | | | 1=At least one Alarm or latched Shed condition requires Reset or Ack |
| `Rdy_Start` | Boolean | OPC `{TagPrefix}.Rdy_Start` | PAX\_Faceplate | yes | | | | 1=Ready to receive OCmd\_Start (enables HMI button) |
| `Rdy_Stop` | Boolean | OPC `{TagPrefix}.Rdy_Stop` | PAX\_Faceplate | yes | | | | 1=Ready to receive OCmd\_Stop (enables HMI button) |
| `Sts_AlmInh` | Boolean | OPC `{TagPrefix}.Sts_AlmInh` | PAX\_Status | yes | | | | 1=An Alarm is Shelved, Disabled or Suppressed: display icon |
| `Sts_BypActive` | Boolean | OPC `{TagPrefix}.Sts_BypActive` | PAX\_Status | yes | | | | 1=Bypassing Active (Bypassed or Maintenance) |
| `Sts_Disabled` | Boolean | OPC `{TagPrefix}.Sts_Disabled` | PAX\_Status | yes | | | | 1=Motor is Disabled |
| `Sts_Err` | Boolean | OPC `{TagPrefix}.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config: see detail bits for reason |
| `Sts_FailToStart` | Boolean | OPC `{TagPrefix}.Sts_FailToStart` | PAX\_Status | yes | | | | 1=Motor Failed to Start (one-shot) |
| `Sts_FailToStop` | Boolean | OPC `{TagPrefix}.Sts_FailToStop` | PAX\_Status | yes | | | | 1=Motor Failed to Stop |
| `Sts_Hand` | Boolean | OPC `{TagPrefix}.Sts_Hand` | PAX\_Status | yes | | | | P\_Motor Sts\_Hand |
| `Sts_IOFault` | Boolean | OPC `{TagPrefix}.Sts_IOFault` | PAX\_Status | yes | | | | I/O Comm Fault Status (0=OK, 1=Bad) |
| `Sts_Maint` | Boolean | OPC `{TagPrefix}.Sts_Maint` | PAX\_Status | yes | | | | P\_Motor Sts\_Maint |
| `Sts_MaintByp` | Boolean | OPC `{TagPrefix}.Sts_MaintByp` | PAX\_Status | yes | | | | 1=A Maintenance Bypass is Active, display icon |
| `Sts_NoMode` | Boolean | OPC `{TagPrefix}.Sts_NoMode` | PAX\_Status | yes | | | | P\_Motor Sts\_NoMode |
| `Sts_NotRdy` | Boolean | OPC `{TagPrefix}.Sts_NotRdy` | PAX\_Status | yes | | | | 1=Device Not Ready, see detail bits for reason |
| `Sts_Oper` | Boolean | OPC `{TagPrefix}.Sts_Oper` | PAX\_Status | yes | | | | P\_Motor Sts\_Oper |
| `Sts_Ovrd` | Boolean | OPC `{TagPrefix}.Sts_Ovrd` | PAX\_Status | yes | | | | P\_Motor Sts\_Ovrd |
| `Sts_Prog` | Boolean | OPC `{TagPrefix}.Sts_Prog` | PAX\_Status | yes | | | | P\_Motor Sts\_Prog |
| `Sts_Running` | Boolean | OPC `{TagPrefix}.Sts_Running` | PAX\_Status | yes | | | | 1=Motor requested to run and is confirmed running |
| `Sts_Starting` | Boolean | OPC `{TagPrefix}.Sts_Starting` | PAX\_Status | yes | | | | 1=Motor requested to run and awaiting run feedback |
| `Sts_Stopped` | Boolean | OPC `{TagPrefix}.Sts_Stopped` | PAX\_Status | yes | | | | 1=Motor requested to stop and is confirmed stopped |
| `Sts_Stopping` | Boolean | OPC `{TagPrefix}.Sts_Stopping` | PAX\_Status | yes | | | | 1=Motor requested to stop and awaiting stopped feedback |
| `Val_Mode` | Int1 | OPC `{TagPrefix}.Val_Mode` | PAX\_Status | yes | historian, OnChange, db 0.0 Absolute (Discrete) | | | |
| `Val_Notify` | Int1 | OPC `{TagPrefix}.Val_Notify` | PAX\_Status | yes | historian, OnChange, db 0.0 Absolute (Discrete) | | | Current Alarm Level and Acknowledgement (enumeration) |
| `Val_Sts` | Int1 | OPC `{TagPrefix}.Val_Sts` | PAX\_Status | yes | historian, OnChange, db 0.0 Absolute (Discrete) | | | Device Confirmed Sts 0=? 1=Stopped, 2=Running, 7=Stopping, 8=Starting, 33=Disabled |

<details>
<summary>State labels (66 members)</summary>

| Member | States (value = label) |
|---|---|
| `Mode/OCmd_AcqLock` | 0 = Off, 1 = On |
| `Mode/OCmd_UnlockRel` | 0 = Off, 1 = On |
| `Mode/Rdy_OAcq` | 0 = Off, 1 = On |
| `Mode/Rdy_OLock` | 0 = Off, 1 = On |
| `Mode/Rdy_ORel` | 0 = Off, 1 = On |
| `Mode/Rdy_OUnlock` | 0 = Off, 1 = On |
| `Mode/Sts_ProgOperLock` | 0 = Off, 1 = On |
| `Mode/Sts_ProgOperSel` | 0 = Off, 1 = On |
| `Ack_FailToStart` | 0 = Off, 1 = On |
| `Ack_FailToStop` | 0 = Off, 1 = On |
| `Ack_IntlkTrip` | 0 = Off, 1 = On |
| `Ack_IOFault` | 0 = Off, 1 = On |
| `Alm_FailToStart` | 0 = Off, 1 = On |
| `Alm_FailToStop` | 0 = Off, 1 = On |
| `Alm_IntlkTrip` | 0 = Off, 1 = On |
| `Alm_IOFault` | 0 = Off, 1 = On |
| `Cfg_AllowLocal` | 0 = Off, 1 = On |
| `Cfg_HasIntlkObj` | 0 = Off, 1 = On |
| `Cfg_HasOvldObj` | 0 = Off, 1 = On |
| `Cfg_HasPermObj` | 0 = Off, 1 = On |
| `Cfg_HasResInhObj` | 0 = Off, 1 = On |
| `Cfg_HasRunFdbk` | 0 = Off, 1 = On |
| `Cfg_HasRunTimeObj` | 0 = Off, 1 = On |
| `Cfg_OCmdResets` | 0 = Off, 1 = On |
| `Cfg_OperStopPrio` | 0 = Off, 1 = On |
| `Cfg_OvrdPermIntlk` | 0 = Off, 1 = On |
| `Cfg_PCmdClear` | 0 = Off, 1 = On |
| `Cfg_ShedOnFailToStart` | 0 = Off, 1 = On |
| `Cfg_ShedOnIOFault` | 0 = Off, 1 = On |
| `Inp_NBPermOK` | 0 = Off, 1 = On |
| `Inp_Ovrd` | 0 = Off, 1 = On |
| `Inp_PermOK` | 0 = Off, 1 = On |
| `Inp_Sim` | 0 = Off, 1 = On |
| `MCmd_Disable` | 0 = Off, 1 = On |
| `MCmd_Enable` | 0 = Off, 1 = On |
| `Nrdy_CfgErr` | 0 = Off, 1 = On |
| `Nrdy_Disabled` | 0 = Off, 1 = On |
| `Nrdy_Fail` | 0 = Off, 1 = On |
| `Nrdy_Intlk` | 0 = Off, 1 = On |
| `Nrdy_IOFault` | 0 = Off, 1 = On |
| `Nrdy_NoMode` | 0 = Off, 1 = On |
| `Nrdy_Perm` | 0 = Off, 1 = On |
| `OCmd_Bypass` | 0 = Off, 1 = On |
| `OCmd_Reset` | 0 = Off, 1 = On |
| `OCmd_ResetAckAll` | 0 = Off, 1 = On |
| `OCmd_Start` | 0 = Off, 1 = On |
| `OCmd_Stop` | 0 = Off, 1 = On |
| `Rdy_ResetAckAll` | 0 = Off, 1 = On |
| `Rdy_Start` | 0 = Off, 1 = On |
| `Rdy_Stop` | 0 = Off, 1 = On |
| `Sts_AlmInh` | 0 = Off, 1 = On |
| `Sts_Disabled` | 0 = Off, 1 = On |
| `Sts_Err` | 0 = Off, 1 = On |
| `Sts_FailToStart` | 0 = Off, 1 = On |
| `Sts_FailToStop` | 0 = Off, 1 = On |
| `Sts_Hand` | 0 = Off, 1 = On |
| `Sts_IOFault` | 0 = Off, 1 = On |
| `Sts_Maint` | 0 = Off, 1 = On |
| `Sts_MaintByp` | 0 = Off, 1 = On |
| `Sts_NoMode` | 0 = Off, 1 = On |
| `Sts_Oper` | 0 = Off, 1 = On |
| `Sts_Ovrd` | 0 = Off, 1 = On |
| `Sts_Prog` | 0 = Off, 1 = On |
| `Sts_Running` | 0 = Off, 1 = On |
| `Sts_Stopped` | 0 = Off, 1 = On |
| `Val_Sts` | 0 = UNK, 1 = STOPPED, 2 = RUNNING, 7 = STOPPING, 8 = STARTING, 33 = DISABLED |

</details>

## Alarms

| Member | Alarm | Priority | Mode | Enabled | Display path | Notes |
|---|---|---|---|---|---|---|
| `Alm_FailToStart` | Fail To Start | High | WhenTrue | `true` | | PlantPAx P\_Motor Alm\_FailToStart |
| `Alm_FailToStop` | Fail To Stop | High | WhenTrue | `true` | | PlantPAx P\_Motor Alm\_FailToStop |
| `Alm_IntlkTrip` | Interlock Trip | Medium | WhenTrue | `true` | | PlantPAx P\_Motor Alm\_IntlkTrip |
| `Alm_IOFault` | IO Fault | Critical | WhenTrue | `true` | | PlantPAx P\_Motor Alm\_IOFault |

Associated data `Site` / `Area` / `Device` come from the tag path (`split({PathToTag}, '/')` segments 1 / 2 / 4). Alarms are defined only here, on the UDT, never on instances: see [Alarms](../../../alarms.md).

## Used By

Nested in: [Devices/Pump](../devices/pump.md) (as `Motor`), [Devices/Evaporator](../devices/evaporator.md) (as `Fans`), [PLC/Recirculator](recirculator.md) (as `Pump1`), [PLC/Recirculator](recirculator.md) (as `Pump2`)

Reached through nesting by 30 top-level instance(s).
