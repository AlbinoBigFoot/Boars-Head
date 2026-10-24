---
title: "PLC_Ref/P_AIn"
sidebar_label: "P_AIn"
description: "UDT definition PLC_Ref/P_AIn: PlantPAx P_AIn reference (read only)"
generated: true
---

:::note

:::
# UDT `PLC_Ref/P_AIn`

PlantPAx P\_AIn reference (read only)

Read-only references to the P\_AIn part that owns the controller object (\{Source\}); the owner subscribes, alarms and historizes it

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC\_Ref &gt; P\_AIn |
| Tag path | `[default]_types_/PLC_Ref/P_AIn` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC_Ref/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 190 (179 atomic, 0 nested UDT, 11 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `Source` | String | - | own |
| `EngUnit` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Fail/` | Folder | | | | | | | |
| `Fail/Ack` | Boolean | reference `{Source}/Fail/Ack` | | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `Fail/Alm` | Boolean | reference `{Source}/Fail/Alm` | | yes | | | | Alarm output 1=In Alarm |
| `Fail/Cfg_Cond` | String | reference `{Source}/Fail/Cfg_Cond` | | yes | | | | |
| `Fail/Cfg_Exists` | Boolean | reference `{Source}/Fail/Cfg_Exists` | | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `Fail/Disabled` | Boolean | reference `{Source}/Fail/Disabled` | | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `Fail/OCmd_Ack` | Boolean | reference `{Source}/Fail/OCmd_Ack` | | yes | | | | Operator Command to Acknowledge alarm |
| `Fail/PCfg_AllowExist` | Boolean | reference `{Source}/Fail/PCfg_AllowExist` | | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `Fail/Rdy_Ack` | Boolean | reference `{Source}/Fail/Rdy_Ack` | | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `Fail/Shelved` | Boolean | reference `{Source}/Fail/Shelved` | | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `Fail/Sts_AlmInh` | Boolean | reference `{Source}/Fail/Sts_AlmInh` | | yes | | | | 1=Alarm has been suppressed, shelved or disabled, display $QI$Q icon |
| `Fail/Sts_Err` | Boolean | reference `{Source}/Fail/Sts_Err` | | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `Fail/Suppressed` | Boolean | reference `{Source}/Fail/Suppressed` | | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `Fail/Val_Notify` | Int1 | reference `{Source}/Fail/Val_Notify` | | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `FailGate/` | Folder | | | | | | | |
| `FailGate/Cfg_InpCond` | String | reference `{Source}/FailGate/Cfg_InpCond` | | yes | | | | |
| `FailGate/Sts_Err` | Boolean | reference `{Source}/FailGate/Sts_Err` | | yes | | | | 1=Error in Config (see detail Err\_ bits for reason), display icon |
| `FailGate/Sts_Gate` | Boolean | reference `{Source}/FailGate/Sts_Gate` | | yes | | | | 1=Gate Delay done, Output is enabled |
| `Hi/` | Folder | | | | | | | |
| `Hi/Ack` | Boolean | reference `{Source}/Hi/Ack` | | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `Hi/Alm` | Boolean | reference `{Source}/Hi/Alm` | | yes | | | | Alarm output 1=In Alarm |
| `Hi/Cfg_Cond` | String | reference `{Source}/Hi/Cfg_Cond` | | yes | | | | |
| `Hi/Cfg_Exists` | Boolean | reference `{Source}/Hi/Cfg_Exists` | | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `Hi/Disabled` | Boolean | reference `{Source}/Hi/Disabled` | | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `Hi/OCmd_Ack` | Boolean | reference `{Source}/Hi/OCmd_Ack` | | yes | | | | Operator Command to Acknowledge alarm |
| `Hi/PCfg_AllowExist` | Boolean | reference `{Source}/Hi/PCfg_AllowExist` | | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `Hi/Rdy_Ack` | Boolean | reference `{Source}/Hi/Rdy_Ack` | | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `Hi/Shelved` | Boolean | reference `{Source}/Hi/Shelved` | | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `Hi/Sts_AlmInh` | Boolean | reference `{Source}/Hi/Sts_AlmInh` | | yes | | | | 1=Alarm has been suppressed, shelved or disabled, display $QI$Q icon |
| `Hi/Sts_Err` | Boolean | reference `{Source}/Hi/Sts_Err` | | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `Hi/Suppressed` | Boolean | reference `{Source}/Hi/Suppressed` | | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `Hi/Val_Notify` | Int1 | reference `{Source}/Hi/Val_Notify` | | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `HiGate/` | Folder | | | | | | | |
| `HiGate/Cfg_InpCond` | String | reference `{Source}/HiGate/Cfg_InpCond` | | yes | | | | |
| `HiGate/Sts_Err` | Boolean | reference `{Source}/HiGate/Sts_Err` | | yes | | | | 1=Error in Config (see detail Err\_ bits for reason), display icon |
| `HiGate/Sts_Gate` | Boolean | reference `{Source}/HiGate/Sts_Gate` | | yes | | | | 1=Gate Delay done, Output is enabled |
| `HiHi/` | Folder | | | | | | | |
| `HiHi/Ack` | Boolean | reference `{Source}/HiHi/Ack` | | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `HiHi/Alm` | Boolean | reference `{Source}/HiHi/Alm` | | yes | | | | Alarm output 1=In Alarm |
| `HiHi/Cfg_Cond` | String | reference `{Source}/HiHi/Cfg_Cond` | | yes | | | | |
| `HiHi/Cfg_Exists` | Boolean | reference `{Source}/HiHi/Cfg_Exists` | | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `HiHi/Disabled` | Boolean | reference `{Source}/HiHi/Disabled` | | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `HiHi/OCmd_Ack` | Boolean | reference `{Source}/HiHi/OCmd_Ack` | | yes | | | | Operator Command to Acknowledge alarm |
| `HiHi/PCfg_AllowExist` | Boolean | reference `{Source}/HiHi/PCfg_AllowExist` | | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `HiHi/Rdy_Ack` | Boolean | reference `{Source}/HiHi/Rdy_Ack` | | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `HiHi/Shelved` | Boolean | reference `{Source}/HiHi/Shelved` | | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `HiHi/Sts_AlmInh` | Boolean | reference `{Source}/HiHi/Sts_AlmInh` | | yes | | | | 1=Alarm has been suppressed, shelved or disabled, display $QI$Q icon |
| `HiHi/Sts_Err` | Boolean | reference `{Source}/HiHi/Sts_Err` | | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `HiHi/Suppressed` | Boolean | reference `{Source}/HiHi/Suppressed` | | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `HiHi/Val_Notify` | Int1 | reference `{Source}/HiHi/Val_Notify` | | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `HiHiGate/` | Folder | | | | | | | |
| `HiHiGate/Cfg_InpCond` | String | reference `{Source}/HiHiGate/Cfg_InpCond` | | yes | | | | |
| `HiHiGate/Sts_Err` | Boolean | reference `{Source}/HiHiGate/Sts_Err` | | yes | | | | 1=Error in Config (see detail Err\_ bits for reason), display icon |
| `HiHiGate/Sts_Gate` | Boolean | reference `{Source}/HiHiGate/Sts_Gate` | | yes | | | | 1=Gate Delay done, Output is enabled |
| `Lo/` | Folder | | | | | | | |
| `Lo/Ack` | Boolean | reference `{Source}/Lo/Ack` | | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `Lo/Alm` | Boolean | reference `{Source}/Lo/Alm` | | yes | | | | Alarm output 1=In Alarm |
| `Lo/Cfg_Cond` | String | reference `{Source}/Lo/Cfg_Cond` | | yes | | | | |
| `Lo/Cfg_Exists` | Boolean | reference `{Source}/Lo/Cfg_Exists` | | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `Lo/Disabled` | Boolean | reference `{Source}/Lo/Disabled` | | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `Lo/OCmd_Ack` | Boolean | reference `{Source}/Lo/OCmd_Ack` | | yes | | | | Operator Command to Acknowledge alarm |
| `Lo/PCfg_AllowExist` | Boolean | reference `{Source}/Lo/PCfg_AllowExist` | | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `Lo/Rdy_Ack` | Boolean | reference `{Source}/Lo/Rdy_Ack` | | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `Lo/Shelved` | Boolean | reference `{Source}/Lo/Shelved` | | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `Lo/Sts_AlmInh` | Boolean | reference `{Source}/Lo/Sts_AlmInh` | | yes | | | | 1=Alarm has been suppressed, shelved or disabled, display $QI$Q icon |
| `Lo/Sts_Err` | Boolean | reference `{Source}/Lo/Sts_Err` | | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `Lo/Suppressed` | Boolean | reference `{Source}/Lo/Suppressed` | | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `Lo/Val_Notify` | Int1 | reference `{Source}/Lo/Val_Notify` | | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `LoGate/` | Folder | | | | | | | |
| `LoGate/Cfg_InpCond` | String | reference `{Source}/LoGate/Cfg_InpCond` | | yes | | | | |
| `LoGate/Sts_Err` | Boolean | reference `{Source}/LoGate/Sts_Err` | | yes | | | | 1=Error in Config (see detail Err\_ bits for reason), display icon |
| `LoGate/Sts_Gate` | Boolean | reference `{Source}/LoGate/Sts_Gate` | | yes | | | | 1=Gate Delay done, Output is enabled |
| `LoLo/` | Folder | | | | | | | |
| `LoLo/Ack` | Boolean | reference `{Source}/LoLo/Ack` | | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `LoLo/Alm` | Boolean | reference `{Source}/LoLo/Alm` | | yes | | | | Alarm output 1=In Alarm |
| `LoLo/Cfg_Cond` | String | reference `{Source}/LoLo/Cfg_Cond` | | yes | | | | |
| `LoLo/Cfg_Exists` | Boolean | reference `{Source}/LoLo/Cfg_Exists` | | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `LoLo/Disabled` | Boolean | reference `{Source}/LoLo/Disabled` | | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `LoLo/OCmd_Ack` | Boolean | reference `{Source}/LoLo/OCmd_Ack` | | yes | | | | Operator Command to Acknowledge alarm |
| `LoLo/PCfg_AllowExist` | Boolean | reference `{Source}/LoLo/PCfg_AllowExist` | | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `LoLo/Rdy_Ack` | Boolean | reference `{Source}/LoLo/Rdy_Ack` | | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `LoLo/Shelved` | Boolean | reference `{Source}/LoLo/Shelved` | | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `LoLo/Sts_AlmInh` | Boolean | reference `{Source}/LoLo/Sts_AlmInh` | | yes | | | | 1=Alarm has been suppressed, shelved or disabled, display $QI$Q icon |
| `LoLo/Sts_Err` | Boolean | reference `{Source}/LoLo/Sts_Err` | | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `LoLo/Suppressed` | Boolean | reference `{Source}/LoLo/Suppressed` | | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `LoLo/Val_Notify` | Int1 | reference `{Source}/LoLo/Val_Notify` | | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `LoLoGate/` | Folder | | | | | | | |
| `LoLoGate/Cfg_InpCond` | String | reference `{Source}/LoLoGate/Cfg_InpCond` | | yes | | | | |
| `LoLoGate/Sts_Err` | Boolean | reference `{Source}/LoLoGate/Sts_Err` | | yes | | | | 1=Error in Config (see detail Err\_ bits for reason), display icon |
| `LoLoGate/Sts_Gate` | Boolean | reference `{Source}/LoLoGate/Sts_Gate` | | yes | | | | 1=Gate Delay done, Output is enabled |
| `Mode/` | Folder | | | | | | | |
| `Mode/Cfg_ProgDefault` | Boolean | reference `{Source}/Mode/Cfg_ProgDefault` | | yes | | | | Default Mode: 1=Program Mode if no requests; 0=Operator Mode if no requests |
| `Mode/MCmd_Acq` | Boolean | reference `{Source}/Mode/MCmd_Acq` | | yes | | | | Maintenance Command to Acquire Ownership (Oper/Prog/Ovrd to Maint) |
| `Mode/MCmd_Rel` | Boolean | reference `{Source}/Mode/MCmd_Rel` | | yes | | | | Maintenance Command to Release Ownership (Maint to Oper/Prog/Ovrd) |
| `Mode/OCmd_AcqLock` | Boolean | reference `{Source}/Mode/OCmd_AcqLock` | | yes | | | | Operator Command to Acquire (Prog to Oper) / Lock Ownership |
| `Mode/OCmd_UnlockRel` | Boolean | reference `{Source}/Mode/OCmd_UnlockRel` | | yes | | | | Operator Command to Unlock / Release (Oper to Prog) Ownership |
| `Mode/Rdy_MAcq` | Boolean | reference `{Source}/Mode/Rdy_MAcq` | | yes | | | | 1=Ready for MCmd\_Acq, enable button |
| `Mode/Rdy_MRel` | Boolean | reference `{Source}/Mode/Rdy_MRel` | | yes | | | | 1=Ready for MCmd\_Rel, enable button |
| `Mode/Rdy_OAcq` | Boolean | reference `{Source}/Mode/Rdy_OAcq` | | yes | | | | 1=Ready for OCmd\_AcqLock, enable Acquire (to Oper) button |
| `Mode/Rdy_OLock` | Boolean | reference `{Source}/Mode/Rdy_OLock` | | yes | | | | 1=Ready for OCmd\_AcqLock, enable Oper Lock button |
| `Mode/Rdy_ORel` | Boolean | reference `{Source}/Mode/Rdy_ORel` | | yes | | | | 1=Ready for OCmd\_UnlockRel, enable Release (to Prog) button |
| `Mode/Rdy_OUnlock` | Boolean | reference `{Source}/Mode/Rdy_OUnlock` | | yes | | | | 1=Ready for OCmd\_UnlockRel, enable Oper Unlock button |
| `Mode/Sts_Maint` | Boolean | reference `{Source}/Mode/Sts_Maint` | | yes | | | | 1=Mode is Maintenance (supersedes Ovrd, Prog, Oper) |
| `Mode/Sts_Oper` | Boolean | reference `{Source}/Mode/Sts_Oper` | | yes | | | | 1=Mode is Operator |
| `Mode/Sts_Prog` | Boolean | reference `{Source}/Mode/Sts_Prog` | | yes | | | | 1=Mode is Program |
| `Mode/Sts_ProgOperLock` | Boolean | reference `{Source}/Mode/Sts_ProgOperLock` | | yes | | | | 1=Program or Operator has requested Mode Lock |
| `Mode/Sts_ProgOperSel` | Boolean | reference `{Source}/Mode/Sts_ProgOperSel` | | yes | | | | Prog/Oper selection 1=Program, 0=Operator |
| `Mode/Val` | Int1 | reference `{Source}/Mode/Val` | | yes | | | | Mode enum: 0=No, 1=H, 2=M, 3=!, 4=P Lock, 5=O Lock, 6=P (O Def), 7=O (P Def), 8=P (= Def), 9=O (= Def) |
| `Cfg_Desc` | String | reference `{Source}/Cfg_Desc` | | yes | | | | |
| `Cfg_EU` | String | reference `{Source}/Cfg_EU` | | yes | | | | |
| `Cfg_FailDB` | Float4 | reference `{Source}/Cfg_FailDB` | | yes | | | | Out-of-Range (fail) High/Low Deadband (EU) |
| `Cfg_FailHiLim` | Float4 | reference `{Source}/Cfg_FailHiLim` | | yes | | | | Out-of-Range (fail) High Limit (EU) |
| `Cfg_FailLoLim` | Float4 | reference `{Source}/Cfg_FailLoLim` | | yes | | | | Out-of-Range (fail) Low Limit (EU) |
| `Cfg_FiltTC` | Float4 | reference `{Source}/Cfg_FiltTC` | | yes | | | | PV Filter Time Constant (s),$N0.0 = unfiltered |
| `Cfg_HasChanObj` | Boolean | reference `{Source}/Cfg_HasChanObj` | | yes | | | | 1=Tells HMI a Channel object (AIChan, etc.) is used for Inp\_PV |
| `Cfg_HasFailAlm` | Boolean | reference `{Source}/Cfg_HasFailAlm` | | yes | | | | |
| `Cfg_HasHiAlm` | Boolean | reference `{Source}/Cfg_HasHiAlm` | | yes | | | | |
| `Cfg_HasHiHiAlm` | Boolean | reference `{Source}/Cfg_HasHiHiAlm` | | yes | | | | |
| `Cfg_HasLoAlm` | Boolean | reference `{Source}/Cfg_HasLoAlm` | | yes | | | | |
| `Cfg_HasLoLoAlm` | Boolean | reference `{Source}/Cfg_HasLoLoAlm` | | yes | | | | |
| `Cfg_HiDB` | Float4 | reference `{Source}/Cfg_HiDB` | | yes | | | | High Status Deadband (EU) |
| `Cfg_HiHiDB` | Float4 | reference `{Source}/Cfg_HiHiDB` | | yes | | | | High-High Status Deadband (EU) |
| `Cfg_InpRawMax` | Float4 | reference `{Source}/Cfg_InpRawMax` | | yes | | | | Input (unscaled) Maximum for Scaling |
| `Cfg_InpRawMin` | Float4 | reference `{Source}/Cfg_InpRawMin` | | yes | | | | Input (unscaled) Minimum for Scaling |
| `Cfg_Label` | String | reference `{Source}/Cfg_Label` | | yes | | | | |
| `Cfg_LoDB` | Float4 | reference `{Source}/Cfg_LoDB` | | yes | | | | Low Status Deadband (EU) |
| `Cfg_LoLoDB` | Float4 | reference `{Source}/Cfg_LoLoDB` | | yes | | | | Low-Low Status Deadband (EU) |
| `Cfg_NoSubstPV` | Boolean | reference `{Source}/Cfg_NoSubstPV` | | yes | | | | 1=Disallow selection of Substitute PV |
| `Cfg_PCmdClear` | Boolean | reference `{Source}/Cfg_PCmdClear` | | yes | | | | |
| `Cfg_PVEUMax` | Float4 | reference `{Source}/Cfg_PVEUMax` | | yes | | | | PV (Output) Maximum for Scaling to EU |
| `Cfg_PVEUMin` | Float4 | reference `{Source}/Cfg_PVEUMin` | | yes | | | | PV (Output) Minimum for Scaling to EU |
| `Cfg_SetTrack` | Boolean | reference `{Source}/Cfg_SetTrack` | | yes | | | | 1=PSets track OSets in Oper, OSets track PSets in Prog, 0=no tracking |
| `Cfg_Tag` | String | reference `{Source}/Cfg_Tag` | | yes | | | | |
| `Err_Alarm` | Boolean | reference `{Source}/Err_Alarm` | | yes | | | | 1=Error in Config: Alarm Min On Time, Shelf Time, Severity |
| `Err_DB` | Boolean | reference `{Source}/Err_DB` | | yes | | | | 1=Error in Config: a Status Deadband is &lt; 0.0 |
| `Err_EU` | Boolean | reference `{Source}/Err_EU` | | yes | | | | 1=Error in Config: Scaled EU Min = Max |
| `Err_Filt` | Boolean | reference `{Source}/Err_Filt` | | yes | | | | 1=Error in Config: PV filter params (RateTime, TC) |
| `Err_Raw` | Boolean | reference `{Source}/Err_Raw` | | yes | | | | 1=Error in Config: Raw Input Scaling Min = Max |
| `Err_Timer` | Boolean | reference `{Source}/Err_Timer` | | yes | | | | 1=Error in Config: On Delay, Off Delay, Gate Delay Time Invalid (use 0 to 2147483 s) |
| `Inf_Lib` | String | reference `{Source}/Inf_Lib` | | yes | | | | |
| `Inf_Type` | String | reference `{Source}/Inf_Type` | | yes | | | | |
| `Inp_PV` | Float4 | reference `{Source}/Inp_PV` | | yes | | | | Input Signal (process variable) from Sensor |
| `Inp_PVBad` | Boolean | reference `{Source}/Inp_PVBad` | | yes | | | | 1=PV or I/O Comms Status Bad, 0=OK |
| `Inp_PVUncertain` | Boolean | reference `{Source}/Inp_PVUncertain` | | yes | | | | 1=PV Value Not Reliable, 0=OK |
| `Inp_Sim` | Boolean | reference `{Source}/Inp_Sim` | | yes | | | | 1=Use simulated PV (Set\_SimPV); 0=Use Input (Inp\_PV) |
| `MCmd_InpPV` | Boolean | reference `{Source}/MCmd_InpPV` | | yes | | | | Maintenance Command to use Input PV (normal) |
| `MCmd_SubstPV` | Boolean | reference `{Source}/MCmd_SubstPV` | | yes | | | | Maintenance Command to use Substitute PV (override input) |
| `MSet_SubstPV` | Float4 | reference `{Source}/MSet_SubstPV` | | yes | | | | Maintenance-Entered Substitute PV (EU) |
| `OCmd_ClearCapt` | Boolean | reference `{Source}/OCmd_ClearCapt` | | yes | | | | Operator Command to Clear the captured min / max PV excursion values |
| `OCmd_Reset` | Boolean | reference `{Source}/OCmd_Reset` | | yes | | | | Operator Command to Reset all Alarms requiring Reset |
| `OCmd_ResetAckAll` | Boolean | reference `{Source}/OCmd_ResetAckAll` | | yes | | | | Operator Command to Reset and Acknowledge all Alarms |
| `OSet_HiHiLim` | Float4 | reference `{Source}/OSet_HiHiLim` | | yes | | | | Operator-Entered High-High Status Threshold (EU) |
| `OSet_HiLim` | Float4 | reference `{Source}/OSet_HiLim` | | yes | | | | Operator-Entered High Status Threshold (EU) |
| `OSet_LoLim` | Float4 | reference `{Source}/OSet_LoLim` | | yes | | | | Operator-Entered Low Status Threshold (EU) |
| `OSet_LoLoLim` | Float4 | reference `{Source}/OSet_LoLoLim` | | yes | | | | Operator-Entered Low-Low Status Threshold (EU) |
| `Rdy_InpPV` | Boolean | reference `{Source}/Rdy_InpPV` | | yes | | | | 1=Ready for MCmd\_InpPV |
| `Rdy_OSet` | Boolean | reference `{Source}/Rdy_OSet` | | yes | | | | 1=Ready to receive OSets (enables data entry fields) |
| `Rdy_SubstPV` | Boolean | reference `{Source}/Rdy_SubstPV` | | yes | | | | 1=Ready for MCmd\_SubstPV |
| `Set_SimPV` | Float4 | reference `{Source}/Set_SimPV` | | yes | | | | PV used in Simulation (Inp\_Sim=1) (EU) |
| `SrcQ` | Int1 | reference `{Source}/SrcQ` | | yes | | | | Source and Quality of primary Val/Sts (enumeration) |
| `SrcQ_IO` | Int1 | reference `{Source}/SrcQ_IO` | | yes | | | | Source and Quality of primary I/O (enumeration) |
| `Sts_AlmInh` | Boolean | reference `{Source}/Sts_AlmInh` | | yes | | | | 1=An Alarm is Shelved, Disabled or Suppressed: display icon |
| `Sts_Err` | Boolean | reference `{Source}/Sts_Err` | | yes | | | | 1=Error in Config (see detail Err\_ bits for reason), display icon |
| `Sts_Fail` | Boolean | reference `{Source}/Sts_Fail` | | yes | | | | 1=Analog Input is Out of Range or PV Bad |
| `Sts_Hi` | Boolean | reference `{Source}/Sts_Hi` | | yes | | | | 1=Analog Input is above High limit |
| `Sts_HiHi` | Boolean | reference `{Source}/Sts_HiHi` | | yes | | | | 1=Analog Input is above High-High limit |
| `Sts_InpPV` | Boolean | reference `{Source}/Sts_InpPV` | | yes | | | | 1=Using Input PV (normal) |
| `Sts_Lo` | Boolean | reference `{Source}/Sts_Lo` | | yes | | | | 1=Analog Input is below Low limit |
| `Sts_LoLo` | Boolean | reference `{Source}/Sts_LoLo` | | yes | | | | 1=Analog Input is below Low-Low limit |
| `Sts_Maint` | Boolean | reference `{Source}/Sts_Maint` | | yes | | | | |
| `Sts_MaintByp` | Boolean | reference `{Source}/Sts_MaintByp` | | yes | | | | 1=A Maintenance Bypass is Active, display icon |
| `Sts_NoMode` | Boolean | reference `{Source}/Sts_NoMode` | | yes | | | | |
| `Sts_Oper` | Boolean | reference `{Source}/Sts_Oper` | | yes | | | | |
| `Sts_Prog` | Boolean | reference `{Source}/Sts_Prog` | | yes | | | | |
| `Sts_PVBad` | Boolean | reference `{Source}/Sts_PVBad` | | yes | | | | 1=PV Bad quality or Out of Range |
| `Sts_PVUncertain` | Boolean | reference `{Source}/Sts_PVUncertain` | | yes | | | | 1=PV Value is Uncertain (quality) |
| `Sts_SubstPV` | Boolean | reference `{Source}/Sts_SubstPV` | | yes | | | | 1=Using Substitute PV (Input being overridden) |
| `Val` | Float4 | reference `{Source}/Val` | | yes | | \{EngUnit\} | | Analog Value (after Substitute PV, if used) |
| `Val_Fault` | Int1 | reference `{Source}/Val_Fault` | | yes | | | | Device Fault Status 0=none, 20=Lo, 21=Hi, 24=LoLo, 25=HiHi, 32=Fail, 34=CfgErr |
| `Val_HiHiLim` | Float4 | reference `{Source}/Val_HiHiLim` | | yes | | \{EngUnit\} | | Current High-High Status Threshold |
| `Val_HiLim` | Float4 | reference `{Source}/Val_HiLim` | | yes | | \{EngUnit\} | | Current High Status Threshold |
| `Val_InpPV` | Float4 | reference `{Source}/Val_InpPV` | | yes | | | | Analog Input Value (actual, before Substitute PV selection) |
| `Val_LoLim` | Float4 | reference `{Source}/Val_LoLim` | | yes | | \{EngUnit\} | | Current Low Status Threshold |
| `Val_LoLoLim` | Float4 | reference `{Source}/Val_LoLoLim` | | yes | | \{EngUnit\} | | Current Low-Low Status Threshold |
| `Val_Mode` | Int1 | reference `{Source}/Val_Mode` | | yes | | | | |
| `Val_Notify` | Int1 | reference `{Source}/Val_Notify` | | yes | | | | Current Alarm Level and Acknowledgement (enumeration) |
| `Val_PVEUMax` | Float4 | reference `{Source}/Val_PVEUMax` | | yes | | \{EngUnit\} | | Maximum of scaled range = MAX (Cfg\_PVEUMin, Cfg\_PVEUMax) |
| `Val_PVEUMin` | Float4 | reference `{Source}/Val_PVEUMin` | | yes | | \{EngUnit\} | | Minimum of scaled range = MIN (Cfg\_PVEUMin, Cfg\_PVEUMax) |
| `Val_PVMaxCapt` | Float4 | reference `{Source}/Val_PVMaxCapt` | | yes | | \{EngUnit\} | | Captured PV Maximum (excursion) since last cleared |
| `Val_PVMinCapt` | Float4 | reference `{Source}/Val_PVMinCapt` | | yes | | \{EngUnit\} | | Captured PV Minimum (excursion) since last cleared |

<details>
<summary>State labels (1 members)</summary>

| Member | States (value = label) |
|---|---|
| `Val_Fault` | 0 = OK, 20 = LO, 21 = HI, 24 = LOLO, 25 = HIHI, 32 = FAIL, 34 = CFGERR |

</details>

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [Devices/Tank](../devices/tank.md) (as `PressAIn`), [Devices/Sensor](../devices/sensor.md) (as `AInRef`)

Reached through nesting by 13 top-level instance(s).
