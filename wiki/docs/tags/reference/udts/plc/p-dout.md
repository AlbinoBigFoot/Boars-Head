---
title: "PLC/P_DOut"
sidebar_label: "P_DOut"
description: "UDT definition PLC/P_DOut"
generated: true
---

:::note

:::
# UDT `PLC/P_DOut`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; P\_DOut |
| Tag path | `[default]_types_/PLC/P_DOut` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 173 (173 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

173 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Ack_IOFault` | Boolean | OPC `{TagPrefix}.Ack_IOFault` | | yes | | | | 1=I/O Fault Alarm has been acknowledged |
| `Ack_IntlkTrip` | Boolean | OPC `{TagPrefix}.Ack_IntlkTrip` | | yes | | | | 1=Interlock Trip Alarm has been acknowledged |
| `Ack_OffFail` | Boolean | OPC `{TagPrefix}.Ack_OffFail` | | yes | | | | 1=Fail to Turn OFF Alarm has been acknowledged |
| `Ack_OnFail` | Boolean | OPC `{TagPrefix}.Ack_OnFail` | | yes | | | | 1=Fail to Turn ON Alarm has been acknowledged |
| `Alm_IOFault` | Boolean | OPC `{TagPrefix}.Alm_IOFault` | | yes | | | | 1=I/O Fault Alarm |
| `Alm_IntlkTrip` | Boolean | OPC `{TagPrefix}.Alm_IntlkTrip` | | yes | | | | 1=Alarm: Device turned OFF by an Interlock NOT OK |
| `Alm_OffFail` | Boolean | OPC `{TagPrefix}.Alm_OffFail` | | yes | | | | 1=Device Fail to Turn OFF Alarm |
| `Alm_OnFail` | Boolean | OPC `{TagPrefix}.Alm_OnFail` | | yes | | | | 1=Device Fail to Turn ON Alarm |
| `Cfg_CompletePulse` | Boolean | OPC `{TagPrefix}.Cfg_CompletePulse` | | yes | | | | 1=Finish Pulse when commanded ON or OFF; 0=switch immediately |
| `Cfg_FdbkFail` | Boolean | OPC `{TagPrefix}.Cfg_FdbkFail` | | yes | | | | 1=Both feedbacks ON is invalid; 0=Both feedbacks OFF is invalid |
| `Cfg_HasIOFaultAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasIOFaultAlm` | | yes | | | | 1=I/O Fault Alarm exists and will be checked |
| `Cfg_HasIntlkObj` | Boolean | OPC `{TagPrefix}.Cfg_HasIntlkObj` | | yes | | | | 1=Tells HMI a P\_Intlk is connected to Inp\_Intlk |
| `Cfg_HasIntlkTripAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasIntlkTripAlm` | | yes | | | | 1=Interlock Trip Alarm exists and will be checked |
| `Cfg_HasOffFailAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasOffFailAlm` | | yes | | | | 1=Fail to Turn OFF Alarm exists and will be checked |
| `Cfg_HasOffFdbk` | Boolean | OPC `{TagPrefix}.Cfg_HasOffFdbk` | | yes | | | | 1=Device provides an OFF feedback signal |
| `Cfg_HasOnFailAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasOnFailAlm` | | yes | | | | 1=Fail to Turn ON Alarm exists and will be checked |
| `Cfg_HasOnFdbk` | Boolean | OPC `{TagPrefix}.Cfg_HasOnFdbk` | | yes | | | | 1=Device provides an ON feedback signal |
| `Cfg_HasPermObj` | Boolean | OPC `{TagPrefix}.Cfg_HasPermObj` | | yes | | | | 1=Tells HMI a P\_Perm is connected to Inp\_Perm |
| `Cfg_IOFaultAckReqd` | Boolean | OPC `{TagPrefix}.Cfg_IOFaultAckReqd` | | yes | | | | 1=Acknowledge required for I/O Fault Alarm |
| `Cfg_IOFaultResetReqd` | Boolean | OPC `{TagPrefix}.Cfg_IOFaultResetReqd` | | yes | | | | 1=Reset required to clear I/O Fault Alarm |
| `Cfg_IOFaultSeverity` | Int2 | OPC `{TagPrefix}.Cfg_IOFaultSeverity` | | yes | | | | I/O Fault Alarm Severity: 1..250=Low, 251..500=Medium, 501..750=High, 751..1000=Urgent |
| `Cfg_IntlkTripAckReqd` | Boolean | OPC `{TagPrefix}.Cfg_IntlkTripAckReqd` | | yes | | | | 1=Acknowledge required for Interlock Trip Alarm |
| `Cfg_IntlkTripResetReqd` | Boolean | OPC `{TagPrefix}.Cfg_IntlkTripResetReqd` | | yes | | | | 1=Reset required to clear Interlock Trip Alarm |
| `Cfg_IntlkTripSeverity` | Int2 | OPC `{TagPrefix}.Cfg_IntlkTripSeverity` | | yes | | | | Interlock Trip Alarm Severity: 1..250=Low, 251..500=Medium, 501..750=High, 751..1000=Urgent |
| `Cfg_OCmdResets` | Boolean | OPC `{TagPrefix}.Cfg_OCmdResets` | | yes | | | | 1=New Oper state cmd. resets fault,$N0=reset req$'d to clear fault |
| `Cfg_OffDelayT` | Float4 | OPC `{TagPrefix}.Cfg_OffDelayT` | | yes | | | | Delay before initially turning output OFF (sec) |
| `Cfg_OffFailAckReqd` | Boolean | OPC `{TagPrefix}.Cfg_OffFailAckReqd` | | yes | | | | 1=Acknowledge required for Fail to Turn OFF Alarm |
| `Cfg_OffFailResetReqd` | Boolean | OPC `{TagPrefix}.Cfg_OffFailResetReqd` | | yes | | | | 1=Reset required to clear Fail to Turn OFF Alarm |
| `Cfg_OffFailSeverity` | Int2 | OPC `{TagPrefix}.Cfg_OffFailSeverity` | | yes | | | | Fail To Turn ON Alarm Severity: 1..250=Low, 251..500=Medium, 501..750=High, 751..1000=Urgent |
| `Cfg_OffFailT` | Int4 | OPC `{TagPrefix}.Cfg_OffFailT` | | yes | | | | Time after Output OFF to get OFF Feedback before Fault (sec) |
| `Cfg_OffPulseT` | Float4 | OPC `{TagPrefix}.Cfg_OffPulseT` | | yes | | | | Output OFF time for Pulse OFF or Pulse Continuous |
| `Cfg_OnDelayT` | Float4 | OPC `{TagPrefix}.Cfg_OnDelayT` | | yes | | | | Delay before initially turning output ON (sec) |
| `Cfg_OnFailAckReqd` | Boolean | OPC `{TagPrefix}.Cfg_OnFailAckReqd` | | yes | | | | 1=Acknowledge required for Fail to Turn ON Alarm |
| `Cfg_OnFailResetReqd` | Boolean | OPC `{TagPrefix}.Cfg_OnFailResetReqd` | | yes | | | | 1=Reset required to clear Fail to Turn ON Alarm |
| `Cfg_OnFailSeverity` | Int2 | OPC `{TagPrefix}.Cfg_OnFailSeverity` | | yes | | | | Fail To Turn OFF Alarm Severity: 1..250=Low, 251..500=Medium, 501..750=High, 751..1000=Urgent |
| `Cfg_OnFailT` | Int4 | OPC `{TagPrefix}.Cfg_OnFailT` | | yes | | | | Time after Output ON to get ON Feedback before Fault (sec) |
| `Cfg_OnPulseT` | Float4 | OPC `{TagPrefix}.Cfg_OnPulseT` | | yes | | | | Output ON time for Pulse ON or Pulse Continuous |
| `Cfg_OperOffPrio` | Boolean | OPC `{TagPrefix}.Cfg_OperOffPrio` | | yes | | | | 1=OCmd\_Off has priority, accepted any time, 0=OCmd\_Off only in Oper, Maint Mode. |
| `Cfg_OvrdPermIntlk` | Boolean | OPC `{TagPrefix}.Cfg_OvrdPermIntlk` | | yes | | | | 1=Override ignores Bypassable Perm/ Intlk; 0=always use Perm/Intlk |
| `Cfg_PCmdClear` | Boolean | OPC `{TagPrefix}.Cfg_PCmdClear` | | yes | | | | |
| `Cfg_ProgDefault` | Boolean | OPC `{TagPrefix}.Cfg_ProgDefault` | | yes | | | | |
| `Cfg_ShedOnFail` | Boolean | OPC `{TagPrefix}.Cfg_ShedOnFail` | | yes | | | | 1=Go to State 0 and Alarm on Fail to reach position; 0=Alarm only on Fail |
| `Cfg_ShedOnIOFault` | Boolean | OPC `{TagPrefix}.Cfg_ShedOnIOFault` | | yes | | | | 1=Go to State 0 and Alarm on I/O Fault; 0=Alarm only on I/O Fault |
| `Cfg_SimFdbkT` | Int4 | OPC `{TagPrefix}.Cfg_SimFdbkT` | | yes | | | | Delay to echo back of ON/OFF status when in Simulation (sec) |
| `Cfg_UseOffFdbk` | Boolean | OPC `{TagPrefix}.Cfg_UseOffFdbk` | | yes | | | | 1=Device OFF feedback should be used for failure checking |
| `Cfg_UseOnFdbk` | Boolean | OPC `{TagPrefix}.Cfg_UseOnFdbk` | | yes | | | | 1=Device ON feedback should be used for failure checking |
| `EnableIn` | Boolean | OPC `{TagPrefix}.EnableIn` | | yes | | | | Enable Input - System Defined Parameter |
| `EnableOut` | Boolean | OPC `{TagPrefix}.EnableOut` | | yes | | | | Enable Output - System Defined Parameter |
| `Err_Alarm` | Boolean | OPC `{TagPrefix}.Err_Alarm` | | yes | | | | 1=Error in Config: Alarm Min On Time, Shelf Time, Severity |
| `Err_Sim` | Boolean | OPC `{TagPrefix}.Err_Sim` | | yes | | | | 1=Error in Config: Simulation timer preset (use 0 to 2147483) |
| `Err_Timer` | Boolean | OPC `{TagPrefix}.Err_Timer` | | yes | | | | 1=Error in Config: Feeback Check timer preset (use 0 to 2147483) |
| `Inp_Hand` | Boolean | OPC `{TagPrefix}.Inp_Hand` | | yes | | | | |
| `Inp_IOFault` | Boolean | OPC `{TagPrefix}.Inp_IOFault` | | yes | | | | Input Communication Status 0=OK, 1=fail |
| `Inp_IntlkOK` | Boolean | OPC `{TagPrefix}.Inp_IntlkOK` | | yes | | | | 1=Interlocks OK, device can turn ON and stay ON |
| `Inp_NBIntlkOK` | Boolean | OPC `{TagPrefix}.Inp_NBIntlkOK` | | yes | | | | 1=Non-Bypassable Interlocks OK, device can turn ON and stay ON |
| `Inp_NBPermOK` | Boolean | OPC `{TagPrefix}.Inp_NBPermOK` | | yes | | | | 1=Non-Bypassable ON Permissives OK, device can turn ON |
| `Inp_OffFdbk` | Boolean | OPC `{TagPrefix}.Inp_OffFdbk` | | yes | | | | Input Signal: OFF feedback from device |
| `Inp_OnFdbk` | Boolean | OPC `{TagPrefix}.Inp_OnFdbk` | | yes | | | | Input Signal: ON feedback from device |
| `Inp_Ovrd` | Boolean | OPC `{TagPrefix}.Inp_Ovrd` | | yes | | | | |
| `Inp_OvrdCmd` | Int4 | OPC `{TagPrefix}.Inp_OvrdCmd` | | yes | | | | Ovrd Device Command 0=None, 1=Off, 2=On, 3=Pulse Off, 4=Pulse On, 5=Pulse Cont |
| `Inp_PermOK` | Boolean | OPC `{TagPrefix}.Inp_PermOK` | | yes | | | | 1=ON Permissives OK, device can turn ON |
| `Inp_Reset` | Boolean | OPC `{TagPrefix}.Inp_Reset` | | yes | | | | 1=Reset all fault conditions and latched Alarms |
| `Inp_Sim` | Boolean | OPC `{TagPrefix}.Inp_Sim` | | yes | | | | 1=Simulate working device; 0=Turn ON/OFF actual device |
| `MCmd_Acq` | Boolean | OPC `{TagPrefix}.MCmd_Acq` | | yes | | | | |
| `MCmd_Disable` | Boolean | OPC `{TagPrefix}.MCmd_Disable` | | yes | | | | Maintenance Command to Disable Device |
| `MCmd_Enable` | Boolean | OPC `{TagPrefix}.MCmd_Enable` | | yes | | | | Maintenance Command to Enable (allow to turn ON) Device |
| `MCmd_Rel` | Boolean | OPC `{TagPrefix}.MCmd_Rel` | | yes | | | | |
| `Nrdy_CfgErr` | Boolean | OPC `{TagPrefix}.Nrdy_CfgErr` | | yes | | | | 1=Device Not Ready: Configuration Error |
| `Nrdy_Disabled` | Boolean | OPC `{TagPrefix}.Nrdy_Disabled` | | yes | | | | 1=Device Not Ready: Device Disabled by Maintenance |
| `Nrdy_Fail` | Boolean | OPC `{TagPrefix}.Nrdy_Fail` | | yes | | | | 1=Device Not Ready: Device Failure (Shed Requires Reset) |
| `Nrdy_IOFault` | Boolean | OPC `{TagPrefix}.Nrdy_IOFault` | | yes | | | | 1=Device Not Ready: I/O Fault (Shed Requires Reset) |
| `Nrdy_Intlk` | Boolean | OPC `{TagPrefix}.Nrdy_Intlk` | | yes | | | | 1=Device Not Ready: Interlock Not OK |
| `Nrdy_NoMode` | Boolean | OPC `{TagPrefix}.Nrdy_NoMode` | | yes | | | | 1=Device Not Ready: Device Logic Disabled / NO Mode |
| `Nrdy_OperPrio` | Boolean | OPC `{TagPrefix}.Nrdy_OperPrio` | | yes | | | | 1=Device Not Ready: Operator State 0 Priority Command Requires Reset |
| `Nrdy_Perm` | Boolean | OPC `{TagPrefix}.Nrdy_Perm` | | yes | | | | 1=Device Not Ready: Permissive Not OK |
| `OCmd_AcqLock` | Boolean | OPC `{TagPrefix}.OCmd_AcqLock` | | yes | | | | |
| `OCmd_Bypass` | Boolean | OPC `{TagPrefix}.OCmd_Bypass` | | yes | | | | Operator Command to Bypass all Bypassable Interlocks and Permissives |
| `OCmd_Check` | Boolean | OPC `{TagPrefix}.OCmd_Check` | | yes | | | | Operator Command to Check (not bypass) all Interlocks and Permissives |
| `OCmd_ContPulse` | Boolean | OPC `{TagPrefix}.OCmd_ContPulse` | | yes | | | | Operator Command to pulse device continuously (blink) |
| `OCmd_Off` | Boolean | OPC `{TagPrefix}.OCmd_Off` | | yes | | | | Operator Command to turn device OFF |
| `OCmd_OffPulse` | Boolean | OPC `{TagPrefix}.OCmd_OffPulse` | | yes | | | | Operator Command to pulse device (which is ON) OFF once |
| `OCmd_On` | Boolean | OPC `{TagPrefix}.OCmd_On` | | yes | | | | Operator Command to turn device ON |
| `OCmd_OnPulse` | Boolean | OPC `{TagPrefix}.OCmd_OnPulse` | | yes | | | | Operator Command to pulse device (which is OFF) ON once |
| `OCmd_Reset` | Boolean | OPC `{TagPrefix}.OCmd_Reset` | | yes | | | | Operator Command to Reset all Alarms requiring Reset |
| `OCmd_ResetAckAll` | Boolean | OPC `{TagPrefix}.OCmd_ResetAckAll` | | yes | | | | Operator Command to Reset all Alarms and latched Shed conditions |
| `OCmd_Unlock` | Boolean | OPC `{TagPrefix}.OCmd_Unlock` | | yes | | | | |
| `Out` | Boolean | OPC `{TagPrefix}.Out` | | yes | | | | Primary Output 1=ON, 0=OFF |
| `PCmd_Acq` | Boolean | OPC `{TagPrefix}.PCmd_Acq` | | yes | | | | |
| `PCmd_ContPulse` | Boolean | OPC `{TagPrefix}.PCmd_ContPulse` | | yes | | | | Program Command to pulse device continuously (blink) |
| `PCmd_IOFaultAck` | Boolean | OPC `{TagPrefix}.PCmd_IOFaultAck` | | yes | | | | Program Command to Acknowledge I/O Fault Alarm |
| `PCmd_IOFaultSuppress` | Boolean | OPC `{TagPrefix}.PCmd_IOFaultSuppress` | | yes | | | | Program Command to Suppress I/O Fault Alarm |
| `PCmd_IOFaultUnshelve` | Boolean | OPC `{TagPrefix}.PCmd_IOFaultUnshelve` | | yes | | | | Program Command to Unshelve I/O Fault Alarm |
| `PCmd_IOFaultUnsuppress` | Boolean | OPC `{TagPrefix}.PCmd_IOFaultUnsuppress` | | yes | | | | Program Command to Unsuppress I/O Fault Alarm |
| `PCmd_IntlkTripAck` | Boolean | OPC `{TagPrefix}.PCmd_IntlkTripAck` | | yes | | | | Program Command to Acknowledge Interlock Trip Alarm |
| `PCmd_IntlkTripSuppress` | Boolean | OPC `{TagPrefix}.PCmd_IntlkTripSuppress` | | yes | | | | Program Command to Suppress Interlock Trip Alarm |
| `PCmd_IntlkTripUnshelve` | Boolean | OPC `{TagPrefix}.PCmd_IntlkTripUnshelve` | | yes | | | | Program Command to Unshelve Interlock Trip Alarm |
| `PCmd_IntlkTripUnsuppress` | Boolean | OPC `{TagPrefix}.PCmd_IntlkTripUnsuppress` | | yes | | | | Program Command to Unsuppress Interlock Trip Alarm |
| `PCmd_Lock` | Boolean | OPC `{TagPrefix}.PCmd_Lock` | | yes | | | | |
| `PCmd_Off` | Boolean | OPC `{TagPrefix}.PCmd_Off` | | yes | | | | Program Command to turn device OFF |
| `PCmd_OffFailAck` | Boolean | OPC `{TagPrefix}.PCmd_OffFailAck` | | yes | | | | Program Command to Acknowledge Fail to Turn OFF Alarm |
| `PCmd_OffFailSuppress` | Boolean | OPC `{TagPrefix}.PCmd_OffFailSuppress` | | yes | | | | Program Command to Suppress Fail to Turn OFF Alarm |
| `PCmd_OffFailUnshelve` | Boolean | OPC `{TagPrefix}.PCmd_OffFailUnshelve` | | yes | | | | Program Command to Unshelve Failt to Turn OFF Alarm |
| `PCmd_OffFailUnsuppress` | Boolean | OPC `{TagPrefix}.PCmd_OffFailUnsuppress` | | yes | | | | Program Command to Unsuppress Fail to Turn OFF Alarm |
| `PCmd_OffPulse` | Boolean | OPC `{TagPrefix}.PCmd_OffPulse` | | yes | | | | Program Command to pulse device (which is ON) OFF once |
| `PCmd_On` | Boolean | OPC `{TagPrefix}.PCmd_On` | | yes | | | | Program Command to turn device ON |
| `PCmd_OnFailAck` | Boolean | OPC `{TagPrefix}.PCmd_OnFailAck` | | yes | | | | Program Command to Acknowledge Fail to Turn ON Alarm |
| `PCmd_OnFailSuppress` | Boolean | OPC `{TagPrefix}.PCmd_OnFailSuppress` | | yes | | | | Program Command to Suppress Fail to Turn ON Alarm |
| `PCmd_OnFailUnshelve` | Boolean | OPC `{TagPrefix}.PCmd_OnFailUnshelve` | | yes | | | | Program Command to Unshelve Fail to Turn ON Alarm |
| `PCmd_OnFailUnsuppress` | Boolean | OPC `{TagPrefix}.PCmd_OnFailUnsuppress` | | yes | | | | Program Command to UnsuppressFail to Turn ON Alarm |
| `PCmd_OnPulse` | Boolean | OPC `{TagPrefix}.PCmd_OnPulse` | | yes | | | | Program Command to pulse device (which is OFF) ON once |
| `PCmd_Rel` | Boolean | OPC `{TagPrefix}.PCmd_Rel` | | yes | | | | |
| `PCmd_Reset` | Boolean | OPC `{TagPrefix}.PCmd_Reset` | | yes | | | | Program Command to Reset all Alarms requiring Reset |
| `PCmd_Unlock` | Boolean | OPC `{TagPrefix}.PCmd_Unlock` | | yes | | | | |
| `PSet_Owner` | Int4 | OPC `{TagPrefix}.PSet_Owner` | | yes | | | | Program Owner Request ID (non-zero) or Release (zero) |
| `P_DOut` | Boolean | OPC `{TagPrefix}.P_DOut` | | yes | | | | Unique Parameter Name for auto - discovery |
| `Rdy_Bypass` | Boolean | OPC `{TagPrefix}.Rdy_Bypass` | | yes | | | | 1=Ready to receive OCmd\_Bypass (enables HMI button) |
| `Rdy_Check` | Boolean | OPC `{TagPrefix}.Rdy_Check` | | yes | | | | 1=Ready to receive OCmd\_Check (enables HMI button) |
| `Rdy_ContPulse` | Boolean | OPC `{TagPrefix}.Rdy_ContPulse` | | yes | | | | 1=Ready to receive OCmd\_ContPulse (enables HMI button) |
| `Rdy_Disable` | Boolean | OPC `{TagPrefix}.Rdy_Disable` | | yes | | | | 1=Ready to receive MCmd\_Disable (enables HMI button) |
| `Rdy_Enable` | Boolean | OPC `{TagPrefix}.Rdy_Enable` | | yes | | | | 1=Ready to receive MCmd\_Enable (enables HMI button) |
| `Rdy_Off` | Boolean | OPC `{TagPrefix}.Rdy_Off` | | yes | | | | 1=Ready to receive OCmd\_Off (enables HMI button) |
| `Rdy_OffPulse` | Boolean | OPC `{TagPrefix}.Rdy_OffPulse` | | yes | | | | 1=Ready to receive OCmd\_OffPulse (enables HMI button) |
| `Rdy_On` | Boolean | OPC `{TagPrefix}.Rdy_On` | | yes | | | | 1=Ready to receive OCmd\_On (enables HMI button) |
| `Rdy_OnPulse` | Boolean | OPC `{TagPrefix}.Rdy_OnPulse` | | yes | | | | 1=Ready to receive OCmd\_OnPulse (enables HMI button) |
| `Rdy_Reset` | Boolean | OPC `{TagPrefix}.Rdy_Reset` | | yes | | | | 1=At least one Alarm or Latched Shed requires Reset |
| `Rdy_ResetAckAll` | Boolean | OPC `{TagPrefix}.Rdy_ResetAckAll` | | yes | | | | 1=At least one Alarm or latched Shed condition requires Reset or Ack |
| `SrcQ` | Int1 | OPC `{TagPrefix}.SrcQ` | | yes | | | | Source and Quality of primary Val/Sts (enumeration) |
| `SrcQ_IO` | Int1 | OPC `{TagPrefix}.SrcQ_IO` | | yes | | | | Source and Quality of primary I/O (enumeration) |
| `Sts_AlmInh` | Boolean | OPC `{TagPrefix}.Sts_AlmInh` | | yes | | | | 1=One or more Alarms Shelved, Disabled or Suppressed |
| `Sts_Available` | Boolean | OPC `{TagPrefix}.Sts_Available` | | yes | | | | 1=Device available for control by automation (Prog) |
| `Sts_BypActive` | Boolean | OPC `{TagPrefix}.Sts_BypActive` | | yes | | | | 1=Interlock / Permissive Bypassing Active (Bypassed or Maintenance) |
| `Sts_Bypass` | Boolean | OPC `{TagPrefix}.Sts_Bypass` | | yes | | | | 1=Bypassable Interlocks and Permissives are Bypassed |
| `Sts_Disabled` | Boolean | OPC `{TagPrefix}.Sts_Disabled` | | yes | | | | 1=Device is Disabled (output held OFF) |
| `Sts_Err` | Boolean | OPC `{TagPrefix}.Sts_Err` | | yes | | | | 1=Error in Config: see detail bits for reason |
| `Sts_FdbkFail` | Boolean | OPC `{TagPrefix}.Sts_FdbkFail` | | yes | | | | 1=Feedbacks are in an INVALID state (not ON, OFF or TRANSIT) |
| `Sts_FdbkOff` | Boolean | OPC `{TagPrefix}.Sts_FdbkOff` | | yes | | | | 1=Device Feedback shows device in OFF state |
| `Sts_FdbkOn` | Boolean | OPC `{TagPrefix}.Sts_FdbkOn` | | yes | | | | 1=Device Feedback shows device in ON state |
| `Sts_Hand` | Boolean | OPC `{TagPrefix}.Sts_Hand` | | yes | | | | |
| `Sts_IOFault` | Boolean | OPC `{TagPrefix}.Sts_IOFault` | | yes | | | | I/O Comm Fault Status (0=OK, 1=Bad) |
| `Sts_IOFaultDisabled` | Boolean | OPC `{TagPrefix}.Sts_IOFaultDisabled` | | yes | | | | 1=I/O Fault Alarm has been Disabled by Maintenance |
| `Sts_IOFaultShelved` | Boolean | OPC `{TagPrefix}.Sts_IOFaultShelved` | | yes | | | | 1=I/O Fault Alarm has been Shelved by Operator |
| `Sts_IOFaultSuppressed` | Boolean | OPC `{TagPrefix}.Sts_IOFaultSuppressed` | | yes | | | | 1=I/O Fault Alarm has been Suppressed by Program |
| `Sts_IntlkTrip` | Boolean | OPC `{TagPrefix}.Sts_IntlkTrip` | | yes | | | | 1=Device turned OFF by an Interlock NOT OK (one-shot) |
| `Sts_IntlkTripDisabled` | Boolean | OPC `{TagPrefix}.Sts_IntlkTripDisabled` | | yes | | | | 1=Interlock Trip Alarm has been Disabled by Maintenance |
| `Sts_IntlkTripShelved` | Boolean | OPC `{TagPrefix}.Sts_IntlkTripShelved` | | yes | | | | 1=Interlock Trip Alarm has been Shelved by Operator |
| `Sts_IntlkTripSuppressed` | Boolean | OPC `{TagPrefix}.Sts_IntlkTripSuppressed` | | yes | | | | 1=Interlock Trip Alarm has been Suppressed by Program |
| `Sts_MAcqRcvd` | Boolean | OPC `{TagPrefix}.Sts_MAcqRcvd` | | yes | | | | |
| `Sts_Maint` | Boolean | OPC `{TagPrefix}.Sts_Maint` | | yes | | | | |
| `Sts_MaintByp` | Boolean | OPC `{TagPrefix}.Sts_MaintByp` | | yes | | | | 1=Device has a Maintenance Bypass function active |
| `Sts_NoMode` | Boolean | OPC `{TagPrefix}.Sts_NoMode` | | yes | | | | |
| `Sts_NotRdy` | Boolean | OPC `{TagPrefix}.Sts_NotRdy` | | yes | | | | 1=Device Not Ready, see detail bits for reason |
| `Sts_OffFail` | Boolean | OPC `{TagPrefix}.Sts_OffFail` | | yes | | | | 1=Device Failed to Turn OFF |
| `Sts_OffFailDisabled` | Boolean | OPC `{TagPrefix}.Sts_OffFailDisabled` | | yes | | | | 1=Fail to Turn OFF Alarm has been Disabled by Maintenance |
| `Sts_OffFailShelved` | Boolean | OPC `{TagPrefix}.Sts_OffFailShelved` | | yes | | | | 1=Fail to Turn OFF Alarm has been Shelved by Operator |
| `Sts_OffFailSuppressed` | Boolean | OPC `{TagPrefix}.Sts_OffFailSuppressed` | | yes | | | | 1=Fail to Turn OFF Alarm has been Suppressed by Program |
| `Sts_OnFail` | Boolean | OPC `{TagPrefix}.Sts_OnFail` | | yes | | | | 1=Device Failed to Turn ON |
| `Sts_OnFailDisabled` | Boolean | OPC `{TagPrefix}.Sts_OnFailDisabled` | | yes | | | | 1=Fail to Turn ON Alarm has been Disabled by Maintenance |
| `Sts_OnFailShelved` | Boolean | OPC `{TagPrefix}.Sts_OnFailShelved` | | yes | | | | 1=Fail to Turn ON Alarm has been Shelved by Operator |
| `Sts_OnFailSuppressed` | Boolean | OPC `{TagPrefix}.Sts_OnFailSuppressed` | | yes | | | | 1=Fail to Turn ON Alarm has been Suppressed by Program |
| `Sts_Oper` | Boolean | OPC `{TagPrefix}.Sts_Oper` | | yes | | | | |
| `Sts_Out` | Boolean | OPC `{TagPrefix}.Sts_Out` | | yes | | | | 1=Output is ON (energized), 0=Output is OFF (de-energized) |
| `Sts_Ovrd` | Boolean | OPC `{TagPrefix}.Sts_Ovrd` | | yes | | | | |
| `Sts_Prog` | Boolean | OPC `{TagPrefix}.Sts_Prog` | | yes | | | | |
| `Sts_ProgOperLock` | Boolean | OPC `{TagPrefix}.Sts_ProgOperLock` | | yes | | | | |
| `Sts_Pulsing` | Boolean | OPC `{TagPrefix}.Sts_Pulsing` | | yes | | | | 1=Output is in a pusling sequence |
| `Val_Cmd` | Int1 | OPC `{TagPrefix}.Val_Cmd` | | yes | | | | Device Command: 0=None, 1=Off, 2=On, 3=Pulse Off, 4=Pulse On, 5=Pulse Cont |
| `Val_Fault` | Int1 | OPC `{TagPrefix}.Val_Fault` | | yes | | | | Device Fault Status 0=none, 16=Feedback Fault, 32=I/O Fault, 34=Config Error |
| `Val_Fdbk` | Int1 | OPC `{TagPrefix}.Val_Fdbk` | | yes | | | | Device Feedback: 0=Transition, 1=Off, 2=On, 3=Invalid |
| `Val_Mode` | Int1 | OPC `{TagPrefix}.Val_Mode` | | yes | | | | |
| `Val_Notify` | Int1 | OPC `{TagPrefix}.Val_Notify` | | yes | | | | Current Alarm Level and Acknowledgement (enumeration) |
| `Val_Owner` | Int4 | OPC `{TagPrefix}.Val_Owner` | | yes | | | | Current Object Owner ID (0=not owned) |
| `Val_State` | Int1 | OPC `{TagPrefix}.Val_State` | | yes | | | | Internal Logic State (for animating STD on faceplate), see manual |
| `Val_Sts` | Int1 | OPC `{TagPrefix}.Val_Sts` | | yes | | | | Device Status 0=off 1=on 2=pulse off 3=pulse on 4=pulse cont. 5=turning off 6=turning on 33=disabled |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
