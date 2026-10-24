---
title: "PLC/P_ValveSO"
sidebar_label: "P_ValveSO"
description: "UDT definition PLC/P_ValveSO: PlantPAx P_ValveSO (read only)"
generated: true
---

:::note

:::
# UDT `PLC/P_ValveSO`

PlantPAx P\_ValveSO (read only)

Standard PlantPAx P\_ValveSO: ns=1;s=\[\{DeviceName\}\]\{TagPrefix\}.&lt;member&gt;, HMI member whitelist, every member readOnly, tag groups PAX\_Status / PAX\_Faceplate

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; P\_ValveSO |
| Tag path | `[default]_types_/PLC/P_ValveSO` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 156 (151 atomic, 0 nested UDT, 5 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

151 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `FullStall/` | Folder | | | | | | | |
| `FullStall/Ack` | Boolean | OPC `{TagPrefix}.FullStall.Ack` | PAX\_Status | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `FullStall/Alm` | Boolean | OPC `{TagPrefix}.FullStall.Alm` | PAX\_Status | yes | | | | Alarm output 1=In Alarm |
| `FullStall/Cfg_Cond` | String | OPC `{TagPrefix}.FullStall.Cfg_Cond` | PAX\_Faceplate | yes | | | | |
| `FullStall/Cfg_Exists` | Boolean | OPC `{TagPrefix}.FullStall.Cfg_Exists` | PAX\_Faceplate | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `FullStall/Disabled` | Boolean | OPC `{TagPrefix}.FullStall.Disabled` | PAX\_Status | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `FullStall/OCmd_Ack` | Boolean | OPC `{TagPrefix}.FullStall.OCmd_Ack` | PAX\_Faceplate | yes | | | | Operator Command to Acknowledge alarm |
| `FullStall/PCfg_AllowExist` | Boolean | OPC `{TagPrefix}.FullStall.PCfg_AllowExist` | PAX\_Faceplate | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `FullStall/Rdy_Ack` | Boolean | OPC `{TagPrefix}.FullStall.Rdy_Ack` | PAX\_Faceplate | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `FullStall/Shelved` | Boolean | OPC `{TagPrefix}.FullStall.Shelved` | PAX\_Status | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `FullStall/Sts_AlmInh` | Boolean | OPC `{TagPrefix}.FullStall.Sts_AlmInh` | PAX\_Status | yes | | | | 1=Alarm has been suppressed, shelved or disabled, display $QI$Q icon |
| `FullStall/Sts_Err` | Boolean | OPC `{TagPrefix}.FullStall.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `FullStall/Suppressed` | Boolean | OPC `{TagPrefix}.FullStall.Suppressed` | PAX\_Status | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `FullStall/Val_Notify` | Int1 | OPC `{TagPrefix}.FullStall.Val_Notify` | PAX\_Status | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `IntlkTrip/` | Folder | | | | | | | |
| `IntlkTrip/Ack` | Boolean | OPC `{TagPrefix}.IntlkTrip.Ack` | PAX\_Status | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `IntlkTrip/Alm` | Boolean | OPC `{TagPrefix}.IntlkTrip.Alm` | PAX\_Status | yes | | | | Alarm output 1=In Alarm |
| `IntlkTrip/Cfg_Cond` | String | OPC `{TagPrefix}.IntlkTrip.Cfg_Cond` | PAX\_Faceplate | yes | | | | |
| `IntlkTrip/Cfg_Exists` | Boolean | OPC `{TagPrefix}.IntlkTrip.Cfg_Exists` | PAX\_Faceplate | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `IntlkTrip/Disabled` | Boolean | OPC `{TagPrefix}.IntlkTrip.Disabled` | PAX\_Status | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `IntlkTrip/OCmd_Ack` | Boolean | OPC `{TagPrefix}.IntlkTrip.OCmd_Ack` | PAX\_Faceplate | yes | | | | Operator Command to Acknowledge alarm |
| `IntlkTrip/PCfg_AllowExist` | Boolean | OPC `{TagPrefix}.IntlkTrip.PCfg_AllowExist` | PAX\_Faceplate | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `IntlkTrip/Rdy_Ack` | Boolean | OPC `{TagPrefix}.IntlkTrip.Rdy_Ack` | PAX\_Faceplate | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `IntlkTrip/Shelved` | Boolean | OPC `{TagPrefix}.IntlkTrip.Shelved` | PAX\_Status | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `IntlkTrip/Sts_Err` | Boolean | OPC `{TagPrefix}.IntlkTrip.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `IntlkTrip/Suppressed` | Boolean | OPC `{TagPrefix}.IntlkTrip.Suppressed` | PAX\_Status | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `IntlkTrip/Val_Notify` | Int1 | OPC `{TagPrefix}.IntlkTrip.Val_Notify` | PAX\_Status | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `IOFault/` | Folder | | | | | | | |
| `IOFault/Ack` | Boolean | OPC `{TagPrefix}.IOFault.Ack` | PAX\_Status | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `IOFault/Alm` | Boolean | OPC `{TagPrefix}.IOFault.Alm` | PAX\_Status | yes | | | | Alarm output 1=In Alarm |
| `IOFault/Cfg_Cond` | String | OPC `{TagPrefix}.IOFault.Cfg_Cond` | PAX\_Faceplate | yes | | | | |
| `IOFault/Cfg_Exists` | Boolean | OPC `{TagPrefix}.IOFault.Cfg_Exists` | PAX\_Faceplate | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `IOFault/Disabled` | Boolean | OPC `{TagPrefix}.IOFault.Disabled` | PAX\_Status | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `IOFault/OCmd_Ack` | Boolean | OPC `{TagPrefix}.IOFault.OCmd_Ack` | PAX\_Faceplate | yes | | | | Operator Command to Acknowledge alarm |
| `IOFault/PCfg_AllowExist` | Boolean | OPC `{TagPrefix}.IOFault.PCfg_AllowExist` | PAX\_Faceplate | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `IOFault/Rdy_Ack` | Boolean | OPC `{TagPrefix}.IOFault.Rdy_Ack` | PAX\_Faceplate | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `IOFault/Shelved` | Boolean | OPC `{TagPrefix}.IOFault.Shelved` | PAX\_Status | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `IOFault/Sts_AlmInh` | Boolean | OPC `{TagPrefix}.IOFault.Sts_AlmInh` | PAX\_Status | yes | | | | 1=Alarm has been suppressed, shelved or disabled, display $QI$Q icon |
| `IOFault/Sts_Err` | Boolean | OPC `{TagPrefix}.IOFault.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `IOFault/Suppressed` | Boolean | OPC `{TagPrefix}.IOFault.Suppressed` | PAX\_Status | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `IOFault/Val_Notify` | Int1 | OPC `{TagPrefix}.IOFault.Val_Notify` | PAX\_Status | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `Mode/` | Folder | | | | | | | |
| `Mode/Cfg_ProgDefault` | Boolean | OPC `{TagPrefix}.Mode.Cfg_ProgDefault` | PAX\_Faceplate | yes | | | | Default Mode: 1=Program Mode if no requests; 0=Operator Mode if no requests |
| `Mode/Inp_Hand` | Boolean | OPC `{TagPrefix}.Mode.Inp_Hand` | PAX\_Status | yes | | | | 1=Acquire Hand (typ. hardwired local) Mode, 0=Release Hand Mode |
| `Mode/Inp_Ovrd` | Boolean | OPC `{TagPrefix}.Mode.Inp_Ovrd` | PAX\_Status | yes | | | | 1=Acquire Override (higher priority program logic) Mode, 0=Release Override Mode |
| `Mode/MCmd_Acq` | Boolean | OPC `{TagPrefix}.Mode.MCmd_Acq` | PAX\_Faceplate | yes | | | | Maintenance Command to Acquire Ownership (Oper/Prog/Ovrd to Maint) |
| `Mode/MCmd_Rel` | Boolean | OPC `{TagPrefix}.Mode.MCmd_Rel` | PAX\_Faceplate | yes | | | | Maintenance Command to Release Ownership (Maint to Oper/Prog/Ovrd) |
| `Mode/OCmd_AcqLock` | Boolean | OPC `{TagPrefix}.Mode.OCmd_AcqLock` | PAX\_Faceplate | yes | | | | Operator Command to Acquire (Prog to Oper) / Lock Ownership |
| `Mode/OCmd_UnlockRel` | Boolean | OPC `{TagPrefix}.Mode.OCmd_UnlockRel` | PAX\_Faceplate | yes | | | | Operator Command to Unlock / Release (Oper to Prog) Ownership |
| `Mode/Rdy_MAcq` | Boolean | OPC `{TagPrefix}.Mode.Rdy_MAcq` | PAX\_Faceplate | yes | | | | 1=Ready for MCmd\_Acq, enable button |
| `Mode/Rdy_MRel` | Boolean | OPC `{TagPrefix}.Mode.Rdy_MRel` | PAX\_Faceplate | yes | | | | 1=Ready for MCmd\_Rel, enable button |
| `Mode/Rdy_OAcq` | Boolean | OPC `{TagPrefix}.Mode.Rdy_OAcq` | PAX\_Faceplate | yes | | | | 1=Ready for OCmd\_AcqLock, enable Acquire (to Oper) button |
| `Mode/Rdy_OLock` | Boolean | OPC `{TagPrefix}.Mode.Rdy_OLock` | PAX\_Faceplate | yes | | | | 1=Ready for OCmd\_AcqLock, enable Oper Lock button |
| `Mode/Rdy_ORel` | Boolean | OPC `{TagPrefix}.Mode.Rdy_ORel` | PAX\_Faceplate | yes | | | | 1=Ready for OCmd\_UnlockRel, enable Release (to Prog) button |
| `Mode/Rdy_OUnlock` | Boolean | OPC `{TagPrefix}.Mode.Rdy_OUnlock` | PAX\_Faceplate | yes | | | | 1=Ready for OCmd\_UnlockRel, enable Oper Unlock button |
| `Mode/Sts_Oper` | Boolean | OPC `{TagPrefix}.Mode.Sts_Oper` | PAX\_Status | yes | | | | 1=Mode is Operator |
| `Mode/Sts_Prog` | Boolean | OPC `{TagPrefix}.Mode.Sts_Prog` | PAX\_Status | yes | | | | 1=Mode is Program |
| `Mode/Sts_ProgOperLock` | Boolean | OPC `{TagPrefix}.Mode.Sts_ProgOperLock` | PAX\_Status | yes | | | | 1=Program or Operator has requested Mode Lock |
| `Mode/Sts_ProgOperSel` | Boolean | OPC `{TagPrefix}.Mode.Sts_ProgOperSel` | PAX\_Status | yes | | | | Prog/Oper selection 1=Program, 0=Operator |
| `Mode/Val` | Int1 | OPC `{TagPrefix}.Mode.Val` | PAX\_Status | yes | | | | Mode enum: 0=No, 1=H, 2=M, 3=!, 4=P Lock, 5=O Lock, 6=P (O Def), 7=O (P Def), 8=P (= Def), 9=O (= Def) |
| `TransitStall/` | Folder | | | | | | | |
| `TransitStall/Ack` | Boolean | OPC `{TagPrefix}.TransitStall.Ack` | PAX\_Status | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `TransitStall/Alm` | Boolean | OPC `{TagPrefix}.TransitStall.Alm` | PAX\_Status | yes | | | | Alarm output 1=In Alarm |
| `TransitStall/Cfg_Cond` | String | OPC `{TagPrefix}.TransitStall.Cfg_Cond` | PAX\_Faceplate | yes | | | | |
| `TransitStall/Cfg_Exists` | Boolean | OPC `{TagPrefix}.TransitStall.Cfg_Exists` | PAX\_Faceplate | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `TransitStall/Disabled` | Boolean | OPC `{TagPrefix}.TransitStall.Disabled` | PAX\_Status | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `TransitStall/OCmd_Ack` | Boolean | OPC `{TagPrefix}.TransitStall.OCmd_Ack` | PAX\_Faceplate | yes | | | | Operator Command to Acknowledge alarm |
| `TransitStall/PCfg_AllowExist` | Boolean | OPC `{TagPrefix}.TransitStall.PCfg_AllowExist` | PAX\_Faceplate | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `TransitStall/Rdy_Ack` | Boolean | OPC `{TagPrefix}.TransitStall.Rdy_Ack` | PAX\_Faceplate | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `TransitStall/Shelved` | Boolean | OPC `{TagPrefix}.TransitStall.Shelved` | PAX\_Status | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `TransitStall/Sts_AlmInh` | Boolean | OPC `{TagPrefix}.TransitStall.Sts_AlmInh` | PAX\_Status | yes | | | | 1=Alarm has been suppressed, shelved or disabled, display $QI$Q icon |
| `TransitStall/Sts_Err` | Boolean | OPC `{TagPrefix}.TransitStall.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `TransitStall/Suppressed` | Boolean | OPC `{TagPrefix}.TransitStall.Suppressed` | PAX\_Status | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `TransitStall/Val_Notify` | Int1 | OPC `{TagPrefix}.TransitStall.Val_Notify` | PAX\_Status | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `Ack_FullStall` | Boolean | OPC `{TagPrefix}.Ack_FullStall` | PAX\_Status | yes | | | | 1=Full Stall Alarm has been acknowledged |
| `Ack_IntlkTrip` | Boolean | OPC `{TagPrefix}.Ack_IntlkTrip` | PAX\_Status | yes | | | | 1=Interlock Trip Alarm has been acknowledged |
| `Ack_IOFault` | Boolean | OPC `{TagPrefix}.Ack_IOFault` | PAX\_Status | yes | | | | 1=I/O Fault Alarm has been acknowledged |
| `Ack_TransitStall` | Boolean | OPC `{TagPrefix}.Ack_TransitStall` | PAX\_Status | yes | | | | 1=Transit Stall Alarm has been acknowledged |
| `Alm_FullStall` | Boolean | OPC `{TagPrefix}.Alm_FullStall` | PAX\_Status | yes | | | 1 | 1=Valve Full Stall (failed to move at all) Alarm |
| `Alm_IntlkTrip` | Boolean | OPC `{TagPrefix}.Alm_IntlkTrip` | PAX\_Status | yes | | | 1 | 1=Alarm: Valve de-energized by an Interlock NOT OK |
| `Alm_IOFault` | Boolean | OPC `{TagPrefix}.Alm_IOFault` | PAX\_Status | yes | | | 1 | 1=I/O Fault Alarm |
| `Alm_TransitStall` | Boolean | OPC `{TagPrefix}.Alm_TransitStall` | PAX\_Status | yes | | | 1 | 1=Valve Transit Stall (did not reach target pos.) Alarm |
| `Cfg_Desc` | String | OPC `{TagPrefix}.Cfg_Desc` | PAX\_Faceplate | yes | | | | |
| `Cfg_FailOpen` | Boolean | OPC `{TagPrefix}.Cfg_FailOpen` | PAX\_Faceplate | yes | | | | 1=Fail Open (energize to close), 0=Fail Closed (energize to open) |
| `Cfg_FullStallT` | Int4 | OPC `{TagPrefix}.Cfg_FullStallT` | PAX\_Faceplate | yes | | | | After command, time with no motion before Fault (sec) |
| `Cfg_HasClosedLS` | Boolean | OPC `{TagPrefix}.Cfg_HasClosedLS` | PAX\_Faceplate | yes | | | | 1=Valve provides a Closed Limit Switch signal |
| `Cfg_HasIntlkObj` | Boolean | OPC `{TagPrefix}.Cfg_HasIntlkObj` | PAX\_Faceplate | yes | | | | 1=Tells HMI a P\_Intlk is connected to Inp\_Intlk |
| `Cfg_HasOpenLS` | Boolean | OPC `{TagPrefix}.Cfg_HasOpenLS` | PAX\_Faceplate | yes | | | | 1=Valve provides an Open Limit Switch signal |
| `Cfg_HasPermObj` | Boolean | OPC `{TagPrefix}.Cfg_HasPermObj` | PAX\_Faceplate | yes | | | | 1=Tells HMI a P\_Perm is connected to Inp\_Perm |
| `Cfg_HasStatsObj` | Boolean | OPC `{TagPrefix}.Cfg_HasStatsObj` | PAX\_Faceplate | yes | | | | 1=Tells HMI a P\_ValveStats is monitoring this valve |
| `Cfg_Label` | String | OPC `{TagPrefix}.Cfg_Label` | PAX\_Faceplate | yes | | | | |
| `Cfg_LSFail` | Boolean | OPC `{TagPrefix}.Cfg_LSFail` | PAX\_Faceplate | yes | | | | 1=both switches ON=fail, 0=both switches OFF=fail |
| `Cfg_OCmdResets` | Boolean | OPC `{TagPrefix}.Cfg_OCmdResets` | PAX\_Faceplate | yes | | | | 1=New Oper valve cmd. resets fault,$N0=reset req$'d to clear fault |
| `Cfg_OvrdPermIntlk` | Boolean | OPC `{TagPrefix}.Cfg_OvrdPermIntlk` | PAX\_Faceplate | yes | | | | 1=Override ignores Bypassable Perm/ Intlk; 0=always use Perm/Intlk |
| `Cfg_PCmdClear` | Boolean | OPC `{TagPrefix}.Cfg_PCmdClear` | PAX\_Faceplate | yes | | | | |
| `Cfg_ShedOnFullStall` | Boolean | OPC `{TagPrefix}.Cfg_ShedOnFullStall` | PAX\_Faceplate | yes | | | | 1=Stop Valve and Alarm on Full Stall; 0=Alarm only on Full Stall |
| `Cfg_ShedOnIOFault` | Boolean | OPC `{TagPrefix}.Cfg_ShedOnIOFault` | PAX\_Faceplate | yes | | | | 1=Stop Valve and Alarm on I/O Fault; 0=Alarm only on I/O Fault |
| `Cfg_ShedOnTransitStall` | Boolean | OPC `{TagPrefix}.Cfg_ShedOnTransitStall` | PAX\_Faceplate | yes | | | | 1=Stop Valve and Alarm on Transit Stall; 0=Alarm only on Transit Stall |
| `Cfg_SimFdbkT` | Int4 | OPC `{TagPrefix}.Cfg_SimFdbkT` | PAX\_Faceplate | yes | | | | Delay to echo back of Open/Closed status when in Simulation (sec) |
| `Cfg_Tag` | String | OPC `{TagPrefix}.Cfg_Tag` | PAX\_Faceplate | yes | | | | |
| `Cfg_TransitStallT` | Int4 | OPC `{TagPrefix}.Cfg_TransitStallT` | PAX\_Faceplate | yes | | | | After command, time to reach position before fault (sec) |
| `Cfg_UseClosedLS` | Boolean | OPC `{TagPrefix}.Cfg_UseClosedLS` | PAX\_Faceplate | yes | | | | 1=Valve Closed LS should be used for failure checking |
| `Cfg_UseOpenLS` | Boolean | OPC `{TagPrefix}.Cfg_UseOpenLS` | PAX\_Faceplate | yes | | | | 1=Valve Open LS should be used for failure checking |
| `Err_Alarm` | Boolean | OPC `{TagPrefix}.Err_Alarm` | PAX\_Faceplate | yes | | | | 1=Error in Config: Alarm Min On Time, Shelf Time, Severity |
| `Err_Sim` | Boolean | OPC `{TagPrefix}.Err_Sim` | PAX\_Faceplate | yes | | | | 1=Error in Config: Invalid Simulation Time (use 0 to 2147483) |
| `Err_Timer` | Boolean | OPC `{TagPrefix}.Err_Timer` | PAX\_Faceplate | yes | | | | 1=Error in Config: Invalid Check Time (use 0 to 2147483) |
| `Inf_Lib` | String | OPC `{TagPrefix}.Inf_Lib` | PAX\_Faceplate | yes | | | | |
| `Inf_Type` | String | OPC `{TagPrefix}.Inf_Type` | PAX\_Faceplate | yes | | | | |
| `Inp_ClosedLS` | Boolean | OPC `{TagPrefix}.Inp_ClosedLS` | PAX\_Status | yes | | | | Valve Closed Limit Switch 1=confirmed CLOSED |
| `Inp_IntlkOK` | Boolean | OPC `{TagPrefix}.Inp_IntlkOK` | PAX\_Status | yes | | | | 1=Interlocks OK, valve can energize |
| `Inp_NBIntlkOK` | Boolean | OPC `{TagPrefix}.Inp_NBIntlkOK` | PAX\_Status | yes | | | | 1=Non-Bypassable Interlocks OK, valve can energize |
| `Inp_NBPermOK` | Boolean | OPC `{TagPrefix}.Inp_NBPermOK` | PAX\_Status | yes | | | | 1=Non-Bypassable Permissives OK, valve can energize |
| `Inp_OpenLS` | Boolean | OPC `{TagPrefix}.Inp_OpenLS` | PAX\_Status | yes | | | | Valve Open Limit Switch 1=confirmed OPEN |
| `Inp_Ovrd` | Boolean | OPC `{TagPrefix}.Inp_Ovrd` | PAX\_Status | yes | | | | |
| `Inp_PermOK` | Boolean | OPC `{TagPrefix}.Inp_PermOK` | PAX\_Status | yes | | | | 1=Permissives OK, Valve can energize |
| `Inp_Sim` | Boolean | OPC `{TagPrefix}.Inp_Sim` | PAX\_Status | yes | | | | 1=Simulate working valve; 0=Open/Close/ Monitor actual valve |
| `MCmd_Disable` | Boolean | OPC `{TagPrefix}.MCmd_Disable` | PAX\_Faceplate | yes | | | | Maintenance Command to Disable Valve |
| `MCmd_Enable` | Boolean | OPC `{TagPrefix}.MCmd_Enable` | PAX\_Faceplate | yes | | | | Maintenance Command to Enable (allow to energize) Valve |
| `Nrdy_CfgErr` | Boolean | OPC `{TagPrefix}.Nrdy_CfgErr` | PAX\_Faceplate | yes | | | | 1=Device Not Ready: Configuration Error |
| `Nrdy_Disabled` | Boolean | OPC `{TagPrefix}.Nrdy_Disabled` | PAX\_Faceplate | yes | | | | 1=Device Not Ready: Device Disabled by Maintenance |
| `Nrdy_Fail` | Boolean | OPC `{TagPrefix}.Nrdy_Fail` | PAX\_Faceplate | yes | | | | 1=Device Not Ready: Device Failure (Shed Requires Reset) |
| `Nrdy_Intlk` | Boolean | OPC `{TagPrefix}.Nrdy_Intlk` | PAX\_Faceplate | yes | | | | 1=Device Not Ready: Interlock Not OK |
| `Nrdy_IOFault` | Boolean | OPC `{TagPrefix}.Nrdy_IOFault` | PAX\_Faceplate | yes | | | | 1=Device Not Ready: I/O Fault (Shed Requires Reset) |
| `Nrdy_NoMode` | Boolean | OPC `{TagPrefix}.Nrdy_NoMode` | PAX\_Faceplate | yes | | | | 1=Device Not Ready: Device Logic Disabled / NO Mode |
| `Nrdy_Perm` | Boolean | OPC `{TagPrefix}.Nrdy_Perm` | PAX\_Faceplate | yes | | | | 1=Device Not Ready: Permissive Not OK |
| `OCmd_Bypass` | Boolean | OPC `{TagPrefix}.OCmd_Bypass` | PAX\_Faceplate | yes | | | | Operator Command to Bypass all Bypassable Interlocks and Permissives |
| `OCmd_Close` | Boolean | OPC `{TagPrefix}.OCmd_Close` | PAX\_Faceplate | yes | | | | Operator Command to Close Valve |
| `OCmd_Open` | Boolean | OPC `{TagPrefix}.OCmd_Open` | PAX\_Faceplate | yes | | | | Operator Command to Open Valve |
| `OCmd_Reset` | Boolean | OPC `{TagPrefix}.OCmd_Reset` | PAX\_Faceplate | yes | | | | Operator Command to Reset all Alarms requiring Reset |
| `OCmd_ResetAckAll` | Boolean | OPC `{TagPrefix}.OCmd_ResetAckAll` | PAX\_Faceplate | yes | | | | Operator Command to Reset all Alarms and latched Shed conditions |
| `Out` | Boolean | OPC `{TagPrefix}.Out` | PAX\_Status | yes | | | | 1=Energize Valve Solenoid |
| `Rdy_Close` | Boolean | OPC `{TagPrefix}.Rdy_Close` | PAX\_Faceplate | yes | | | | 1=Ready to receive OCmd\_Close (enables HMI button) |
| `Rdy_Disable` | Boolean | OPC `{TagPrefix}.Rdy_Disable` | PAX\_Faceplate | yes | | | | 1=Ready to receive MCmd\_Disable (enables HMI button) |
| `Rdy_Enable` | Boolean | OPC `{TagPrefix}.Rdy_Enable` | PAX\_Faceplate | yes | | | | 1=Ready to receive MCmd\_Enable (enables HMI button) |
| `Rdy_Open` | Boolean | OPC `{TagPrefix}.Rdy_Open` | PAX\_Faceplate | yes | | | | 1=Ready to receive OCmd\_Open (enables HMI button) |
| `SrcQ_IO` | Int1 | OPC `{TagPrefix}.SrcQ_IO` | PAX\_Status | yes | | | | Source and Quality of primary I/O (enumeration) |
| `Sts_AlmInh` | Boolean | OPC `{TagPrefix}.Sts_AlmInh` | PAX\_Status | yes | | | | 1=An Alarm is Shelved, Disabled or Suppressed, display icon |
| `Sts_BypActive` | Boolean | OPC `{TagPrefix}.Sts_BypActive` | PAX\_Status | yes | | | | 1=Bypassing Active (Bypassed or Maintenance) |
| `Sts_Bypass` | Boolean | OPC `{TagPrefix}.Sts_Bypass` | PAX\_Status | yes | | | | 1=Bypassable Interlocks and Permissives are Bypassed |
| `Sts_Closed` | Boolean | OPC `{TagPrefix}.Sts_Closed` | PAX\_Status | yes | | | | 1=Valve requested to Close and is confirmed Closed |
| `Sts_Closing` | Boolean | OPC `{TagPrefix}.Sts_Closing` | PAX\_Status | yes | | | | 1=Valve requested to Close and awaiting Closed feedback |
| `Sts_Disabled` | Boolean | OPC `{TagPrefix}.Sts_Disabled` | PAX\_Status | yes | | | | 1=Valve is Disabled |
| `Sts_Err` | Boolean | OPC `{TagPrefix}.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config: see detail bits for reason |
| `Sts_IOFault` | Boolean | OPC `{TagPrefix}.Sts_IOFault` | PAX\_Status | yes | | | | I/O Comm Fault Status (0=OK, 1=Bad) |
| `Sts_LSFail` | Boolean | OPC `{TagPrefix}.Sts_LSFail` | PAX\_Status | yes | | | | 1=Limit Switch Overlap Failure |
| `Sts_Maint` | Boolean | OPC `{TagPrefix}.Sts_Maint` | PAX\_Status | yes | | | | Maintenance |
| `Sts_MaintByp` | Boolean | OPC `{TagPrefix}.Sts_MaintByp` | PAX\_Status | yes | | | | 1=A Maintenance Bypass is Active, display icon |
| `Sts_NotRdy` | Boolean | OPC `{TagPrefix}.Sts_NotRdy` | PAX\_Status | yes | | | | 1=Device Not Ready, see detail bits for reason |
| `Sts_Opened` | Boolean | OPC `{TagPrefix}.Sts_Opened` | PAX\_Status | yes | | | | 1=Valve requested to open and is confirmed Opened |
| `Sts_Opening` | Boolean | OPC `{TagPrefix}.Sts_Opening` | PAX\_Status | yes | | | | 1=Valve requested to open and awaiting open feedback |
| `Sts_Oper` | Boolean | OPC `{TagPrefix}.Sts_Oper` | PAX\_Status | yes | | | | Operator |
| `Sts_Prog` | Boolean | OPC `{TagPrefix}.Sts_Prog` | PAX\_Status | yes | | | | Program |
| `Val_Fault` | Int1 | OPC `{TagPrefix}.Val_Fault` | PAX\_Status | yes | historian, OnChange, db 0.0 Absolute (Discrete) | | | Device Fault Status 0=None, 16=Transit Stall, 17 = Full Stall, 32=I/O Fault, 34=Config Error |
| `Val_Mode` | Int1 | OPC `{TagPrefix}.Val_Mode` | PAX\_Status | yes | historian, OnChange, db 0.0 Absolute (Discrete) | | | |
| `Val_Notify` | Int1 | OPC `{TagPrefix}.Val_Notify` | PAX\_Status | yes | historian, OnChange, db 0.0 Absolute (Discrete) | | | Current Alarm Level and Acknowledgement (enumeration) |
| `Val_Sts` | Int1 | OPC `{TagPrefix}.Val_Sts` | PAX\_Status | yes | historian, OnChange, db 0.0 Absolute (Discrete) | | | Device Confirmed Sts 0=? 1=Closed 2=Open 5=Closing, 6=Opening, 33=Disabled |

<details>
<summary>State labels (50 members)</summary>

| Member | States (value = label) |
|---|---|
| `Ack_FullStall` | 0 = Off, 1 = On |
| `Ack_IntlkTrip` | 0 = Off, 1 = On |
| `Ack_IOFault` | 0 = Off, 1 = On |
| `Ack_TransitStall` | 0 = Off, 1 = On |
| `Alm_FullStall` | 0 = Off, 1 = On |
| `Alm_IntlkTrip` | 0 = Off, 1 = On |
| `Alm_IOFault` | 0 = Off, 1 = On |
| `Alm_TransitStall` | 0 = Off, 1 = On |
| `Cfg_FailOpen` | 0 = Off, 1 = On |
| `Cfg_HasClosedLS` | 0 = Off, 1 = On |
| `Cfg_HasIntlkObj` | 0 = Off, 1 = On |
| `Cfg_HasOpenLS` | 0 = Off, 1 = On |
| `Cfg_HasPermObj` | 0 = Off, 1 = On |
| `Cfg_HasStatsObj` | 0 = Off, 1 = On |
| `Cfg_LSFail` | 0 = Off, 1 = On |
| `Cfg_OCmdResets` | 0 = Off, 1 = On |
| `Cfg_OvrdPermIntlk` | 0 = Off, 1 = On |
| `Cfg_PCmdClear` | 0 = Off, 1 = On |
| `Cfg_ShedOnFullStall` | 0 = Off, 1 = On |
| `Cfg_ShedOnIOFault` | 0 = Off, 1 = On |
| `Cfg_ShedOnTransitStall` | 0 = Off, 1 = On |
| `Inp_ClosedLS` | 0 = Off, 1 = On |
| `Inp_NBPermOK` | 0 = Off, 1 = On |
| `Inp_OpenLS` | 0 = Off, 1 = On |
| `Inp_Ovrd` | 0 = Off, 1 = On |
| `Inp_PermOK` | 0 = Off, 1 = On |
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
| `OCmd_Close` | 0 = Off, 1 = On |
| `OCmd_Open` | 0 = Off, 1 = On |
| `OCmd_Reset` | 0 = Off, 1 = On |
| `OCmd_ResetAckAll` | 0 = Off, 1 = On |
| `Out` | 0 = Off, 1 = On |
| `Rdy_Close` | 0 = Off, 1 = On |
| `Rdy_Open` | 0 = Off, 1 = On |
| `Sts_Bypass` | 0 = Off, 1 = On |
| `Sts_Disabled` | 0 = Off, 1 = On |
| `Sts_IOFault` | 0 = Off, 1 = On |
| `Sts_Maint` | 0 = Off, 1 = On |
| `Sts_Oper` | 0 = Off, 1 = On |
| `Sts_Prog` | 0 = Off, 1 = On |
| `Val_Sts` | 0 = UNK, 1 = CLOSED, 2 = OPEN, 5 = CLOSING, 6 = OPENING, 33 = DISABLED |

</details>

## Alarms

| Member | Alarm | Priority | Mode | Enabled | Display path | Notes |
|---|---|---|---|---|---|---|
| `Alm_FullStall` | Full Stall | High | WhenTrue | `true` | | PlantPAx P\_ValveSO Alm\_FullStall |
| `Alm_IntlkTrip` | Interlock Trip | Medium | WhenTrue | `true` | | PlantPAx P\_ValveSO Alm\_IntlkTrip |
| `Alm_IOFault` | IO Fault | High | WhenTrue | `true` | | PlantPAx P\_ValveSO Alm\_IOFault |
| `Alm_TransitStall` | Transit Stall | High | WhenTrue | `true` | | PlantPAx P\_ValveSO Alm\_TransitStall |

Associated data `Site` / `Area` / `Device` come from the tag path (`split({PathToTag}, '/')` segments 1 / 2 / 4). Alarms are defined only here, on the UDT, never on instances: see [Alarms](../../../alarms.md).

## Used By

Nested in: [Devices/Valve](../devices/valve.md) (as `Valve`), [PLC/Accumulator](accumulator.md) (as `SV`), [PLC/Recirculator](recirculator.md) (as `OP_LVL1`)

Reached through nesting by 23 top-level instance(s).
