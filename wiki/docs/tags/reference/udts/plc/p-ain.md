---
title: "PLC/P_AIn"
sidebar_label: "P_AIn"
description: "UDT definition PLC/P_AIn: PlantPAx P_AIn (read only)"
generated: true
---

:::note

:::
# UDT `PLC/P_AIn`

PlantPAx P\_AIn (read only)

Standard PlantPAx P\_AIn: ns=1;s=\[\{DeviceName\}\]\{TagPrefix\}.&lt;member&gt;, HMI member whitelist, every member readOnly, tag groups PAX\_Status / PAX\_Faceplate

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; P\_AIn |
| Tag path | `[default]_types_/PLC/P_AIn` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 190 (179 atomic, 0 nested UDT, 11 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |
| `EngUnit` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

179 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Fail/` | Folder | | | | | | | |
| `Fail/Ack` | Boolean | OPC `{TagPrefix}.Fail.Ack` | PAX\_Status | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `Fail/Alm` | Boolean | OPC `{TagPrefix}.Fail.Alm` | PAX\_Status | yes | | | | Alarm output 1=In Alarm |
| `Fail/Cfg_Cond` | String | OPC `{TagPrefix}.Fail.Cfg_Cond` | PAX\_Faceplate | yes | | | | |
| `Fail/Cfg_Exists` | Boolean | OPC `{TagPrefix}.Fail.Cfg_Exists` | PAX\_Faceplate | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `Fail/Disabled` | Boolean | OPC `{TagPrefix}.Fail.Disabled` | PAX\_Status | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `Fail/OCmd_Ack` | Boolean | OPC `{TagPrefix}.Fail.OCmd_Ack` | PAX\_Faceplate | yes | | | | Operator Command to Acknowledge alarm |
| `Fail/PCfg_AllowExist` | Boolean | OPC `{TagPrefix}.Fail.PCfg_AllowExist` | PAX\_Faceplate | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `Fail/Rdy_Ack` | Boolean | OPC `{TagPrefix}.Fail.Rdy_Ack` | PAX\_Faceplate | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `Fail/Shelved` | Boolean | OPC `{TagPrefix}.Fail.Shelved` | PAX\_Status | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `Fail/Sts_AlmInh` | Boolean | OPC `{TagPrefix}.Fail.Sts_AlmInh` | PAX\_Status | yes | | | | 1=Alarm has been suppressed, shelved or disabled, display $QI$Q icon |
| `Fail/Sts_Err` | Boolean | OPC `{TagPrefix}.Fail.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `Fail/Suppressed` | Boolean | OPC `{TagPrefix}.Fail.Suppressed` | PAX\_Status | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `Fail/Val_Notify` | Int1 | OPC `{TagPrefix}.Fail.Val_Notify` | PAX\_Status | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `FailGate/` | Folder | | | | | | | |
| `FailGate/Cfg_InpCond` | String | OPC `{TagPrefix}.FailGate.Cfg_InpCond` | PAX\_Faceplate | yes | | | | |
| `FailGate/Sts_Err` | Boolean | OPC `{TagPrefix}.FailGate.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config (see detail Err\_ bits for reason), display icon |
| `FailGate/Sts_Gate` | Boolean | OPC `{TagPrefix}.FailGate.Sts_Gate` | PAX\_Status | yes | | | | 1=Gate Delay done, Output is enabled |
| `Hi/` | Folder | | | | | | | |
| `Hi/Ack` | Boolean | OPC `{TagPrefix}.Hi.Ack` | PAX\_Status | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `Hi/Alm` | Boolean | OPC `{TagPrefix}.Hi.Alm` | PAX\_Status | yes | | | | Alarm output 1=In Alarm |
| `Hi/Cfg_Cond` | String | OPC `{TagPrefix}.Hi.Cfg_Cond` | PAX\_Faceplate | yes | | | | |
| `Hi/Cfg_Exists` | Boolean | OPC `{TagPrefix}.Hi.Cfg_Exists` | PAX\_Faceplate | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `Hi/Disabled` | Boolean | OPC `{TagPrefix}.Hi.Disabled` | PAX\_Status | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `Hi/OCmd_Ack` | Boolean | OPC `{TagPrefix}.Hi.OCmd_Ack` | PAX\_Faceplate | yes | | | | Operator Command to Acknowledge alarm |
| `Hi/PCfg_AllowExist` | Boolean | OPC `{TagPrefix}.Hi.PCfg_AllowExist` | PAX\_Faceplate | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `Hi/Rdy_Ack` | Boolean | OPC `{TagPrefix}.Hi.Rdy_Ack` | PAX\_Faceplate | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `Hi/Shelved` | Boolean | OPC `{TagPrefix}.Hi.Shelved` | PAX\_Status | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `Hi/Sts_AlmInh` | Boolean | OPC `{TagPrefix}.Hi.Sts_AlmInh` | PAX\_Status | yes | | | | 1=Alarm has been suppressed, shelved or disabled, display $QI$Q icon |
| `Hi/Sts_Err` | Boolean | OPC `{TagPrefix}.Hi.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `Hi/Suppressed` | Boolean | OPC `{TagPrefix}.Hi.Suppressed` | PAX\_Status | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `Hi/Val_Notify` | Int1 | OPC `{TagPrefix}.Hi.Val_Notify` | PAX\_Status | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `HiGate/` | Folder | | | | | | | |
| `HiGate/Cfg_InpCond` | String | OPC `{TagPrefix}.HiGate.Cfg_InpCond` | PAX\_Faceplate | yes | | | | |
| `HiGate/Sts_Err` | Boolean | OPC `{TagPrefix}.HiGate.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config (see detail Err\_ bits for reason), display icon |
| `HiGate/Sts_Gate` | Boolean | OPC `{TagPrefix}.HiGate.Sts_Gate` | PAX\_Status | yes | | | | 1=Gate Delay done, Output is enabled |
| `HiHi/` | Folder | | | | | | | |
| `HiHi/Ack` | Boolean | OPC `{TagPrefix}.HiHi.Ack` | PAX\_Status | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `HiHi/Alm` | Boolean | OPC `{TagPrefix}.HiHi.Alm` | PAX\_Status | yes | | | | Alarm output 1=In Alarm |
| `HiHi/Cfg_Cond` | String | OPC `{TagPrefix}.HiHi.Cfg_Cond` | PAX\_Faceplate | yes | | | | |
| `HiHi/Cfg_Exists` | Boolean | OPC `{TagPrefix}.HiHi.Cfg_Exists` | PAX\_Faceplate | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `HiHi/Disabled` | Boolean | OPC `{TagPrefix}.HiHi.Disabled` | PAX\_Status | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `HiHi/OCmd_Ack` | Boolean | OPC `{TagPrefix}.HiHi.OCmd_Ack` | PAX\_Faceplate | yes | | | | Operator Command to Acknowledge alarm |
| `HiHi/PCfg_AllowExist` | Boolean | OPC `{TagPrefix}.HiHi.PCfg_AllowExist` | PAX\_Faceplate | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `HiHi/Rdy_Ack` | Boolean | OPC `{TagPrefix}.HiHi.Rdy_Ack` | PAX\_Faceplate | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `HiHi/Shelved` | Boolean | OPC `{TagPrefix}.HiHi.Shelved` | PAX\_Status | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `HiHi/Sts_AlmInh` | Boolean | OPC `{TagPrefix}.HiHi.Sts_AlmInh` | PAX\_Status | yes | | | | 1=Alarm has been suppressed, shelved or disabled, display $QI$Q icon |
| `HiHi/Sts_Err` | Boolean | OPC `{TagPrefix}.HiHi.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `HiHi/Suppressed` | Boolean | OPC `{TagPrefix}.HiHi.Suppressed` | PAX\_Status | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `HiHi/Val_Notify` | Int1 | OPC `{TagPrefix}.HiHi.Val_Notify` | PAX\_Status | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `HiHiGate/` | Folder | | | | | | | |
| `HiHiGate/Cfg_InpCond` | String | OPC `{TagPrefix}.HiHiGate.Cfg_InpCond` | PAX\_Faceplate | yes | | | | |
| `HiHiGate/Sts_Err` | Boolean | OPC `{TagPrefix}.HiHiGate.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config (see detail Err\_ bits for reason), display icon |
| `HiHiGate/Sts_Gate` | Boolean | OPC `{TagPrefix}.HiHiGate.Sts_Gate` | PAX\_Status | yes | | | | 1=Gate Delay done, Output is enabled |
| `Lo/` | Folder | | | | | | | |
| `Lo/Ack` | Boolean | OPC `{TagPrefix}.Lo.Ack` | PAX\_Status | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `Lo/Alm` | Boolean | OPC `{TagPrefix}.Lo.Alm` | PAX\_Status | yes | | | | Alarm output 1=In Alarm |
| `Lo/Cfg_Cond` | String | OPC `{TagPrefix}.Lo.Cfg_Cond` | PAX\_Faceplate | yes | | | | |
| `Lo/Cfg_Exists` | Boolean | OPC `{TagPrefix}.Lo.Cfg_Exists` | PAX\_Faceplate | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `Lo/Disabled` | Boolean | OPC `{TagPrefix}.Lo.Disabled` | PAX\_Status | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `Lo/OCmd_Ack` | Boolean | OPC `{TagPrefix}.Lo.OCmd_Ack` | PAX\_Faceplate | yes | | | | Operator Command to Acknowledge alarm |
| `Lo/PCfg_AllowExist` | Boolean | OPC `{TagPrefix}.Lo.PCfg_AllowExist` | PAX\_Faceplate | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `Lo/Rdy_Ack` | Boolean | OPC `{TagPrefix}.Lo.Rdy_Ack` | PAX\_Faceplate | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `Lo/Shelved` | Boolean | OPC `{TagPrefix}.Lo.Shelved` | PAX\_Status | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `Lo/Sts_AlmInh` | Boolean | OPC `{TagPrefix}.Lo.Sts_AlmInh` | PAX\_Status | yes | | | | 1=Alarm has been suppressed, shelved or disabled, display $QI$Q icon |
| `Lo/Sts_Err` | Boolean | OPC `{TagPrefix}.Lo.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `Lo/Suppressed` | Boolean | OPC `{TagPrefix}.Lo.Suppressed` | PAX\_Status | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `Lo/Val_Notify` | Int1 | OPC `{TagPrefix}.Lo.Val_Notify` | PAX\_Status | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `LoGate/` | Folder | | | | | | | |
| `LoGate/Cfg_InpCond` | String | OPC `{TagPrefix}.LoGate.Cfg_InpCond` | PAX\_Faceplate | yes | | | | |
| `LoGate/Sts_Err` | Boolean | OPC `{TagPrefix}.LoGate.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config (see detail Err\_ bits for reason), display icon |
| `LoGate/Sts_Gate` | Boolean | OPC `{TagPrefix}.LoGate.Sts_Gate` | PAX\_Status | yes | | | | 1=Gate Delay done, Output is enabled |
| `LoLo/` | Folder | | | | | | | |
| `LoLo/Ack` | Boolean | OPC `{TagPrefix}.LoLo.Ack` | PAX\_Status | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `LoLo/Alm` | Boolean | OPC `{TagPrefix}.LoLo.Alm` | PAX\_Status | yes | | | | Alarm output 1=In Alarm |
| `LoLo/Cfg_Cond` | String | OPC `{TagPrefix}.LoLo.Cfg_Cond` | PAX\_Faceplate | yes | | | | |
| `LoLo/Cfg_Exists` | Boolean | OPC `{TagPrefix}.LoLo.Cfg_Exists` | PAX\_Faceplate | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `LoLo/Disabled` | Boolean | OPC `{TagPrefix}.LoLo.Disabled` | PAX\_Status | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `LoLo/OCmd_Ack` | Boolean | OPC `{TagPrefix}.LoLo.OCmd_Ack` | PAX\_Faceplate | yes | | | | Operator Command to Acknowledge alarm |
| `LoLo/PCfg_AllowExist` | Boolean | OPC `{TagPrefix}.LoLo.PCfg_AllowExist` | PAX\_Faceplate | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `LoLo/Rdy_Ack` | Boolean | OPC `{TagPrefix}.LoLo.Rdy_Ack` | PAX\_Faceplate | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `LoLo/Shelved` | Boolean | OPC `{TagPrefix}.LoLo.Shelved` | PAX\_Status | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `LoLo/Sts_AlmInh` | Boolean | OPC `{TagPrefix}.LoLo.Sts_AlmInh` | PAX\_Status | yes | | | | 1=Alarm has been suppressed, shelved or disabled, display $QI$Q icon |
| `LoLo/Sts_Err` | Boolean | OPC `{TagPrefix}.LoLo.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `LoLo/Suppressed` | Boolean | OPC `{TagPrefix}.LoLo.Suppressed` | PAX\_Status | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `LoLo/Val_Notify` | Int1 | OPC `{TagPrefix}.LoLo.Val_Notify` | PAX\_Status | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `LoLoGate/` | Folder | | | | | | | |
| `LoLoGate/Cfg_InpCond` | String | OPC `{TagPrefix}.LoLoGate.Cfg_InpCond` | PAX\_Faceplate | yes | | | | |
| `LoLoGate/Sts_Err` | Boolean | OPC `{TagPrefix}.LoLoGate.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config (see detail Err\_ bits for reason), display icon |
| `LoLoGate/Sts_Gate` | Boolean | OPC `{TagPrefix}.LoLoGate.Sts_Gate` | PAX\_Status | yes | | | | 1=Gate Delay done, Output is enabled |
| `Mode/` | Folder | | | | | | | |
| `Mode/Cfg_ProgDefault` | Boolean | OPC `{TagPrefix}.Mode.Cfg_ProgDefault` | PAX\_Faceplate | yes | | | | Default Mode: 1=Program Mode if no requests; 0=Operator Mode if no requests |
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
| `Mode/Sts_Maint` | Boolean | OPC `{TagPrefix}.Mode.Sts_Maint` | PAX\_Status | yes | | | | 1=Mode is Maintenance (supersedes Ovrd, Prog, Oper) |
| `Mode/Sts_Oper` | Boolean | OPC `{TagPrefix}.Mode.Sts_Oper` | PAX\_Status | yes | | | | 1=Mode is Operator |
| `Mode/Sts_Prog` | Boolean | OPC `{TagPrefix}.Mode.Sts_Prog` | PAX\_Status | yes | | | | 1=Mode is Program |
| `Mode/Sts_ProgOperLock` | Boolean | OPC `{TagPrefix}.Mode.Sts_ProgOperLock` | PAX\_Status | yes | | | | 1=Program or Operator has requested Mode Lock |
| `Mode/Sts_ProgOperSel` | Boolean | OPC `{TagPrefix}.Mode.Sts_ProgOperSel` | PAX\_Status | yes | | | | Prog/Oper selection 1=Program, 0=Operator |
| `Mode/Val` | Int1 | OPC `{TagPrefix}.Mode.Val` | PAX\_Status | yes | | | | Mode enum: 0=No, 1=H, 2=M, 3=!, 4=P Lock, 5=O Lock, 6=P (O Def), 7=O (P Def), 8=P (= Def), 9=O (= Def) |
| `Cfg_Desc` | String | OPC `{TagPrefix}.Cfg_Desc` | PAX\_Faceplate | yes | | | | |
| `Cfg_EU` | String | OPC `{TagPrefix}.Cfg_EU` | PAX\_Faceplate | yes | | | | |
| `Cfg_FailDB` | Float4 | OPC `{TagPrefix}.Cfg_FailDB` | PAX\_Faceplate | yes | | | | Out-of-Range (fail) High/Low Deadband (EU) |
| `Cfg_FailHiLim` | Float4 | OPC `{TagPrefix}.Cfg_FailHiLim` | PAX\_Faceplate | yes | | | | Out-of-Range (fail) High Limit (EU) |
| `Cfg_FailLoLim` | Float4 | OPC `{TagPrefix}.Cfg_FailLoLim` | PAX\_Faceplate | yes | | | | Out-of-Range (fail) Low Limit (EU) |
| `Cfg_FiltTC` | Float4 | OPC `{TagPrefix}.Cfg_FiltTC` | PAX\_Faceplate | yes | | | | PV Filter Time Constant (s),$N0.0 = unfiltered |
| `Cfg_HasChanObj` | Boolean | OPC `{TagPrefix}.Cfg_HasChanObj` | PAX\_Faceplate | yes | | | | 1=Tells HMI a Channel object (AIChan, etc.) is used for Inp\_PV |
| `Cfg_HasFailAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasFailAlm` | PAX\_Config | yes | | | | |
| `Cfg_HasHiAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasHiAlm` | PAX\_Config | yes | | | | |
| `Cfg_HasHiHiAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasHiHiAlm` | PAX\_Config | yes | | | | |
| `Cfg_HasLoAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasLoAlm` | PAX\_Config | yes | | | | |
| `Cfg_HasLoLoAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasLoLoAlm` | PAX\_Config | yes | | | | |
| `Cfg_HiDB` | Float4 | OPC `{TagPrefix}.Cfg_HiDB` | PAX\_Faceplate | yes | | | | High Status Deadband (EU) |
| `Cfg_HiHiDB` | Float4 | OPC `{TagPrefix}.Cfg_HiHiDB` | PAX\_Faceplate | yes | | | | High-High Status Deadband (EU) |
| `Cfg_InpRawMax` | Float4 | OPC `{TagPrefix}.Cfg_InpRawMax` | PAX\_Faceplate | yes | | | | Input (unscaled) Maximum for Scaling |
| `Cfg_InpRawMin` | Float4 | OPC `{TagPrefix}.Cfg_InpRawMin` | PAX\_Faceplate | yes | | | | Input (unscaled) Minimum for Scaling |
| `Cfg_Label` | String | OPC `{TagPrefix}.Cfg_Label` | PAX\_Faceplate | yes | | | | |
| `Cfg_LoDB` | Float4 | OPC `{TagPrefix}.Cfg_LoDB` | PAX\_Faceplate | yes | | | | Low Status Deadband (EU) |
| `Cfg_LoLoDB` | Float4 | OPC `{TagPrefix}.Cfg_LoLoDB` | PAX\_Faceplate | yes | | | | Low-Low Status Deadband (EU) |
| `Cfg_NoSubstPV` | Boolean | OPC `{TagPrefix}.Cfg_NoSubstPV` | PAX\_Faceplate | yes | | | | 1=Disallow selection of Substitute PV |
| `Cfg_PCmdClear` | Boolean | OPC `{TagPrefix}.Cfg_PCmdClear` | PAX\_Faceplate | yes | | | | |
| `Cfg_PVEUMax` | Float4 | OPC `{TagPrefix}.Cfg_PVEUMax` | PAX\_Faceplate | yes | | | | PV (Output) Maximum for Scaling to EU |
| `Cfg_PVEUMin` | Float4 | OPC `{TagPrefix}.Cfg_PVEUMin` | PAX\_Faceplate | yes | | | | PV (Output) Minimum for Scaling to EU |
| `Cfg_SetTrack` | Boolean | OPC `{TagPrefix}.Cfg_SetTrack` | PAX\_Faceplate | yes | | | | 1=PSets track OSets in Oper, OSets track PSets in Prog, 0=no tracking |
| `Cfg_Tag` | String | OPC `{TagPrefix}.Cfg_Tag` | PAX\_Faceplate | yes | | | | |
| `Err_Alarm` | Boolean | OPC `{TagPrefix}.Err_Alarm` | PAX\_Faceplate | yes | | | | 1=Error in Config: Alarm Min On Time, Shelf Time, Severity |
| `Err_DB` | Boolean | OPC `{TagPrefix}.Err_DB` | PAX\_Faceplate | yes | | | | 1=Error in Config: a Status Deadband is &lt; 0.0 |
| `Err_EU` | Boolean | OPC `{TagPrefix}.Err_EU` | PAX\_Faceplate | yes | | | | 1=Error in Config: Scaled EU Min = Max |
| `Err_Filt` | Boolean | OPC `{TagPrefix}.Err_Filt` | PAX\_Faceplate | yes | | | | 1=Error in Config: PV filter params (RateTime, TC) |
| `Err_Raw` | Boolean | OPC `{TagPrefix}.Err_Raw` | PAX\_Faceplate | yes | | | | 1=Error in Config: Raw Input Scaling Min = Max |
| `Err_Timer` | Boolean | OPC `{TagPrefix}.Err_Timer` | PAX\_Faceplate | yes | | | | 1=Error in Config: On Delay, Off Delay, Gate Delay Time Invalid (use 0 to 2147483 s) |
| `Inf_Lib` | String | OPC `{TagPrefix}.Inf_Lib` | PAX\_Faceplate | yes | | | | |
| `Inf_Type` | String | OPC `{TagPrefix}.Inf_Type` | PAX\_Faceplate | yes | | | | |
| `Inp_PV` | Float4 | OPC `{TagPrefix}.Inp_PV` | PAX\_Status | yes | | | | Input Signal (process variable) from Sensor |
| `Inp_PVBad` | Boolean | OPC `{TagPrefix}.Inp_PVBad` | PAX\_Status | yes | | | | 1=PV or I/O Comms Status Bad, 0=OK |
| `Inp_PVUncertain` | Boolean | OPC `{TagPrefix}.Inp_PVUncertain` | PAX\_Status | yes | | | | 1=PV Value Not Reliable, 0=OK |
| `Inp_Sim` | Boolean | OPC `{TagPrefix}.Inp_Sim` | PAX\_Status | yes | | | | 1=Use simulated PV (Set\_SimPV); 0=Use Input (Inp\_PV) |
| `MCmd_InpPV` | Boolean | OPC `{TagPrefix}.MCmd_InpPV` | PAX\_Faceplate | yes | | | | Maintenance Command to use Input PV (normal) |
| `MCmd_SubstPV` | Boolean | OPC `{TagPrefix}.MCmd_SubstPV` | PAX\_Faceplate | yes | | | | Maintenance Command to use Substitute PV (override input) |
| `MSet_SubstPV` | Float4 | OPC `{TagPrefix}.MSet_SubstPV` | PAX\_Faceplate | yes | | | | Maintenance-Entered Substitute PV (EU) |
| `OCmd_ClearCapt` | Boolean | OPC `{TagPrefix}.OCmd_ClearCapt` | PAX\_Faceplate | yes | | | | Operator Command to Clear the captured min / max PV excursion values |
| `OCmd_Reset` | Boolean | OPC `{TagPrefix}.OCmd_Reset` | PAX\_Faceplate | yes | | | | Operator Command to Reset all Alarms requiring Reset |
| `OCmd_ResetAckAll` | Boolean | OPC `{TagPrefix}.OCmd_ResetAckAll` | PAX\_Faceplate | yes | | | | Operator Command to Reset and Acknowledge all Alarms |
| `OSet_HiHiLim` | Float4 | OPC `{TagPrefix}.OSet_HiHiLim` | PAX\_Faceplate | yes | | | | Operator-Entered High-High Status Threshold (EU) |
| `OSet_HiLim` | Float4 | OPC `{TagPrefix}.OSet_HiLim` | PAX\_Faceplate | yes | | | | Operator-Entered High Status Threshold (EU) |
| `OSet_LoLim` | Float4 | OPC `{TagPrefix}.OSet_LoLim` | PAX\_Faceplate | yes | | | | Operator-Entered Low Status Threshold (EU) |
| `OSet_LoLoLim` | Float4 | OPC `{TagPrefix}.OSet_LoLoLim` | PAX\_Faceplate | yes | | | | Operator-Entered Low-Low Status Threshold (EU) |
| `Rdy_InpPV` | Boolean | OPC `{TagPrefix}.Rdy_InpPV` | PAX\_Faceplate | yes | | | | 1=Ready for MCmd\_InpPV |
| `Rdy_OSet` | Boolean | OPC `{TagPrefix}.Rdy_OSet` | PAX\_Faceplate | yes | | | | 1=Ready to receive OSets (enables data entry fields) |
| `Rdy_SubstPV` | Boolean | OPC `{TagPrefix}.Rdy_SubstPV` | PAX\_Faceplate | yes | | | | 1=Ready for MCmd\_SubstPV |
| `Set_SimPV` | Float4 | OPC `{TagPrefix}.Set_SimPV` | PAX\_Faceplate | yes | | | | PV used in Simulation (Inp\_Sim=1) (EU) |
| `SrcQ` | Int1 | OPC `{TagPrefix}.SrcQ` | PAX\_Status | yes | | | | Source and Quality of primary Val/Sts (enumeration) |
| `SrcQ_IO` | Int1 | OPC `{TagPrefix}.SrcQ_IO` | PAX\_Status | yes | | | | Source and Quality of primary I/O (enumeration) |
| `Sts_AlmInh` | Boolean | OPC `{TagPrefix}.Sts_AlmInh` | PAX\_Status | yes | | | | 1=An Alarm is Shelved, Disabled or Suppressed: display icon |
| `Sts_Err` | Boolean | OPC `{TagPrefix}.Sts_Err` | PAX\_Status | yes | | | | 1=Error in Config (see detail Err\_ bits for reason), display icon |
| `Sts_Fail` | Boolean | OPC `{TagPrefix}.Sts_Fail` | PAX\_Status | yes | | | 1 | 1=Analog Input is Out of Range or PV Bad |
| `Sts_Hi` | Boolean | OPC `{TagPrefix}.Sts_Hi` | PAX\_Status | yes | | | 1 | 1=Analog Input is above High limit |
| `Sts_HiHi` | Boolean | OPC `{TagPrefix}.Sts_HiHi` | PAX\_Status | yes | | | 1 | 1=Analog Input is above High-High limit |
| `Sts_InpPV` | Boolean | OPC `{TagPrefix}.Sts_InpPV` | PAX\_Status | yes | | | | 1=Using Input PV (normal) |
| `Sts_Lo` | Boolean | OPC `{TagPrefix}.Sts_Lo` | PAX\_Status | yes | | | 1 | 1=Analog Input is below Low limit |
| `Sts_LoLo` | Boolean | OPC `{TagPrefix}.Sts_LoLo` | PAX\_Status | yes | | | 1 | 1=Analog Input is below Low-Low limit |
| `Sts_Maint` | Boolean | OPC `{TagPrefix}.Sts_Maint` | PAX\_Status | yes | | | | |
| `Sts_MaintByp` | Boolean | OPC `{TagPrefix}.Sts_MaintByp` | PAX\_Status | yes | | | | 1=A Maintenance Bypass is Active, display icon |
| `Sts_NoMode` | Boolean | OPC `{TagPrefix}.Sts_NoMode` | PAX\_Status | yes | | | | |
| `Sts_Oper` | Boolean | OPC `{TagPrefix}.Sts_Oper` | PAX\_Status | yes | | | | |
| `Sts_Prog` | Boolean | OPC `{TagPrefix}.Sts_Prog` | PAX\_Status | yes | | | | |
| `Sts_PVBad` | Boolean | OPC `{TagPrefix}.Sts_PVBad` | PAX\_Status | yes | | | | 1=PV Bad quality or Out of Range |
| `Sts_PVUncertain` | Boolean | OPC `{TagPrefix}.Sts_PVUncertain` | PAX\_Status | yes | | | | 1=PV Value is Uncertain (quality) |
| `Sts_SubstPV` | Boolean | OPC `{TagPrefix}.Sts_SubstPV` | PAX\_Status | yes | | | | 1=Using Substitute PV (Input being overridden) |
| `Val` | Float4 | OPC `{TagPrefix}.Val` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | \{EngUnit\} | | Analog Value (after Substitute PV, if used) |
| `Val_Fault` | Int1 | OPC `{TagPrefix}.Val_Fault` | PAX\_Status | yes | historian, OnChange, db 0.0 Absolute (Discrete) | | | Device Fault Status 0=none, 20=Lo, 21=Hi, 24=LoLo, 25=HiHi, 32=Fail, 34=CfgErr |
| `Val_HiHiLim` | Float4 | OPC `{TagPrefix}.Val_HiHiLim` | PAX\_Faceplate | yes | | \{EngUnit\} | | Current High-High Status Threshold |
| `Val_HiLim` | Float4 | OPC `{TagPrefix}.Val_HiLim` | PAX\_Faceplate | yes | | \{EngUnit\} | | Current High Status Threshold |
| `Val_InpPV` | Float4 | OPC `{TagPrefix}.Val_InpPV` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | Analog Input Value (actual, before Substitute PV selection) |
| `Val_LoLim` | Float4 | OPC `{TagPrefix}.Val_LoLim` | PAX\_Faceplate | yes | | \{EngUnit\} | | Current Low Status Threshold |
| `Val_LoLoLim` | Float4 | OPC `{TagPrefix}.Val_LoLoLim` | PAX\_Faceplate | yes | | \{EngUnit\} | | Current Low-Low Status Threshold |
| `Val_Mode` | Int1 | OPC `{TagPrefix}.Val_Mode` | PAX\_Status | yes | historian, OnChange, db 0.0 Absolute (Discrete) | | | |
| `Val_Notify` | Int1 | OPC `{TagPrefix}.Val_Notify` | PAX\_Status | yes | historian, OnChange, db 0.0 Absolute (Discrete) | | | Current Alarm Level and Acknowledgement (enumeration) |
| `Val_PVEUMax` | Float4 | OPC `{TagPrefix}.Val_PVEUMax` | PAX\_Faceplate | yes | | \{EngUnit\} | | Maximum of scaled range = MAX (Cfg\_PVEUMin, Cfg\_PVEUMax) |
| `Val_PVEUMin` | Float4 | OPC `{TagPrefix}.Val_PVEUMin` | PAX\_Faceplate | yes | | \{EngUnit\} | | Minimum of scaled range = MIN (Cfg\_PVEUMin, Cfg\_PVEUMax) |
| `Val_PVMaxCapt` | Float4 | OPC `{TagPrefix}.Val_PVMaxCapt` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | \{EngUnit\} | | Captured PV Maximum (excursion) since last cleared |
| `Val_PVMinCapt` | Float4 | OPC `{TagPrefix}.Val_PVMinCapt` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | \{EngUnit\} | | Captured PV Minimum (excursion) since last cleared |

<details>
<summary>State labels (1 members)</summary>

| Member | States (value = label) |
|---|---|
| `Val_Fault` | 0 = OK, 20 = LO, 21 = HI, 24 = LOLO, 25 = HIHI, 32 = FAIL, 34 = CFGERR |

</details>

## Alarms

| Member | Alarm | Priority | Mode | Enabled | Display path | Notes |
|---|---|---|---|---|---|---|
| `Sts_Fail` | Input Failure | High | WhenTrue | `coalesce({[.]Cfg_HasFailAlm}, false)` | | PlantPAx P\_AIn Sts\_Fail |
| `Sts_Hi` | High | Medium | WhenTrue | `coalesce({[.]Cfg_HasHiAlm}, false)` | | PlantPAx P\_AIn Sts\_Hi |
| `Sts_HiHi` | High-High | High | WhenTrue | `coalesce({[.]Cfg_HasHiHiAlm}, false)` | | PlantPAx P\_AIn Sts\_HiHi |
| `Sts_Lo` | Low | Medium | WhenTrue | `coalesce({[.]Cfg_HasLoAlm}, false)` | | PlantPAx P\_AIn Sts\_Lo |
| `Sts_LoLo` | Low-Low | High | WhenTrue | `coalesce({[.]Cfg_HasLoLoAlm}, false)` | | PlantPAx P\_AIn Sts\_LoLo |

Associated data `Site` / `Area` / `Device` come from the tag path (`split({PathToTag}, '/')` segments 1 / 2 / 4). Alarms are defined only here, on the UDT, never on instances: see [Alarms](../../../alarms.md).

## Used By

Nested in: [Devices/Tank](../devices/tank.md) (as `LvlAIn`), [Devices/Sensor](../devices/sensor.md) (as `AIn`), [Devices/Evaporator](../devices/evaporator.md) (as `ZAT`), [PLC/Accumulator](accumulator.md) (as `LT`), [PLC/Recirculator](recirculator.md) (as `LT`), [PLC/Recirculator](recirculator.md) (as `PT`)

Reached through nesting by 32 top-level instance(s).
