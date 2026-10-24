---
title: "PLC/P_Mode"
sidebar_label: "P_Mode"
description: "UDT definition PLC/P_Mode"
generated: true
---

:::note

:::
# UDT `PLC/P_Mode`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; P\_Mode |
| Tag path | `[default]_types_/PLC/P_Mode` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 32 (32 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

32 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Cfg_OvrdOverLock` | Boolean | OPC `{TagPrefix}.Cfg_OvrdOverLock` | | yes | | | | 1=Override supersedes Prog/Oper Lock, 0=don$'t override Lock |
| `Cfg_PCmdClear` | Boolean | OPC `{TagPrefix}.Cfg_PCmdClear` | | yes | | | | 1=Clear Program Command on receipt; 0=Use Level-based (maintained) PCmds |
| `Cfg_ProgDefault` | Boolean | OPC `{TagPrefix}.Cfg_ProgDefault` | | yes | | | | Default Mode: 1=Program Mode if no requests; 0=Operator Mode if no requests |
| `EnableIn` | Boolean | OPC `{TagPrefix}.EnableIn` | | yes | | | | Enable Input - System Defined Parameter |
| `EnableOut` | Boolean | OPC `{TagPrefix}.EnableOut` | | yes | | | | Enable Output - System Defined Parameter |
| `Inp_Hand` | Boolean | OPC `{TagPrefix}.Inp_Hand` | | yes | | | | 1=Acquire Hand (typ. hardwired local) Mode, 0=Release Hand Mode |
| `Inp_Ovrd` | Boolean | OPC `{TagPrefix}.Inp_Ovrd` | | yes | | | | 1=Acquire Override (higher priority program logic) Mode, 0=Release Override Mode |
| `MCmd_Acq` | Boolean | OPC `{TagPrefix}.MCmd_Acq` | | yes | | | | Maintenance Command to Acquire Ownership (Oper/Prog/Ovrd to Maint) |
| `MCmd_Rel` | Boolean | OPC `{TagPrefix}.MCmd_Rel` | | yes | | | | Maintenance Command to Release Ownership (Maint to Oper/Prog/Ovrd) |
| `OCmd_AcqLock` | Boolean | OPC `{TagPrefix}.OCmd_AcqLock` | | yes | | | | Operator Command to Acquire (Prog to Oper) / Lock Ownership |
| `OCmd_UnlockRel` | Boolean | OPC `{TagPrefix}.OCmd_UnlockRel` | | yes | | | | Operator Command to Unlock / Release (Oper to Prog) Ownership |
| `PCmd_Acq` | Boolean | OPC `{TagPrefix}.PCmd_Acq` | | yes | | | | Program Command to Acquire Ownership (Oper to Prog) |
| `PCmd_Lock` | Boolean | OPC `{TagPrefix}.PCmd_Lock` | | yes | | | | Program Command to Lock Mode in Prog |
| `PCmd_Rel` | Boolean | OPC `{TagPrefix}.PCmd_Rel` | | yes | | | | Program Command to Release Ownership (Prog to Oper) |
| `PCmd_Unlock` | Boolean | OPC `{TagPrefix}.PCmd_Unlock` | | yes | | | | Program Command to Unlock Mode |
| `P_Mode` | Boolean | OPC `{TagPrefix}.P_Mode` | | yes | | | | Unique Parameter Name for auto - discovery |
| `Rdy_MAcq` | Boolean | OPC `{TagPrefix}.Rdy_MAcq` | | yes | | | | 1=Ready for MCmd\_Acq, enable button |
| `Rdy_MRel` | Boolean | OPC `{TagPrefix}.Rdy_MRel` | | yes | | | | 1=Ready for MCmd\_Rel, enable button |
| `Rdy_OAcq` | Boolean | OPC `{TagPrefix}.Rdy_OAcq` | | yes | | | | 1=Ready for OCmd\_AcqLock, enable Acquire (to Oper) button |
| `Rdy_OLock` | Boolean | OPC `{TagPrefix}.Rdy_OLock` | | yes | | | | 1=Ready for OCmd\_AcqLock, enable Oper Lock button |
| `Rdy_ORel` | Boolean | OPC `{TagPrefix}.Rdy_ORel` | | yes | | | | 1=Ready for OCmd\_UnlockRel, enable Release (to Prog) button |
| `Rdy_OUnlock` | Boolean | OPC `{TagPrefix}.Rdy_OUnlock` | | yes | | | | 1=Ready for OCmd\_UnlockRel, enable Oper Unlock button |
| `Sts_Hand` | Boolean | OPC `{TagPrefix}.Sts_Hand` | | yes | | | | 1=Mode is Hand (supersedes Maint, Ovrd, Prog, Oper) |
| `Sts_MAcqRcvd` | Boolean | OPC `{TagPrefix}.Sts_MAcqRcvd` | | yes | | | | 1=Maintenance Acquire command received this scan |
| `Sts_Maint` | Boolean | OPC `{TagPrefix}.Sts_Maint` | | yes | | | | 1=Mode is Maintenance (supersedes Ovrd, Prog, Oper) |
| `Sts_NoMode` | Boolean | OPC `{TagPrefix}.Sts_NoMode` | | yes | | | | 1=Mode is No Mode (no owner, disabled or not scanned) |
| `Sts_Oper` | Boolean | OPC `{TagPrefix}.Sts_Oper` | | yes | | | | 1=Mode is Operator |
| `Sts_Ovrd` | Boolean | OPC `{TagPrefix}.Sts_Ovrd` | | yes | | | | 1=Mode is Override (supersedes Prog, Oper) |
| `Sts_Prog` | Boolean | OPC `{TagPrefix}.Sts_Prog` | | yes | | | | 1=Mode is Program |
| `Sts_ProgOperLock` | Boolean | OPC `{TagPrefix}.Sts_ProgOperLock` | | yes | | | | 1=Program or Operator has requested Mode Lock |
| `Sts_ProgOperSel` | Boolean | OPC `{TagPrefix}.Sts_ProgOperSel` | | yes | | | | Prog/Oper selection 1=Program, 0=Operator |
| `Val` | Int1 | OPC `{TagPrefix}.Val` | | yes | | | | Mode enum: 0=No, 1=H, 2=M, 3=!, 4=P Lock, 5=O Lock, 6=P (O Def), 7=O (P Def), 8=P (= Def), 9=O (= Def) |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
