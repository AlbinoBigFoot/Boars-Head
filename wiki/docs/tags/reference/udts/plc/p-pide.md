---
title: "PLC/P_PIDE"
sidebar_label: "P_PIDE"
description: "UDT definition PLC/P_PIDE"
generated: true
---

:::note

:::
# UDT `PLC/P_PIDE`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; P\_PIDE |
| Tag path | `[default]_types_/PLC/P_PIDE` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 311 (311 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

311 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Ack_Fail` | Boolean | OPC `{TagPrefix}.Ack_Fail` | | yes | | | | 1=Loop Failure Alarm has been acknowledged |
| `Ack_HiDev` | Boolean | OPC `{TagPrefix}.Ack_HiDev` | | yes | | | | 1=High Deviation Alarm has been acknowledged |
| `Ack_HiHiDev` | Boolean | OPC `{TagPrefix}.Ack_HiHiDev` | | yes | | | | 1=High-High Deviation Alarm has been acknowledged |
| `Ack_IntlkTrip` | Boolean | OPC `{TagPrefix}.Ack_IntlkTrip` | | yes | | | | 1=Interlock Trip Alarm has been acknowledged |
| `Ack_LoDev` | Boolean | OPC `{TagPrefix}.Ack_LoDev` | | yes | | | | 1=Loiw Deviation Alarm has been acknowledged |
| `Ack_LoLoDev` | Boolean | OPC `{TagPrefix}.Ack_LoLoDev` | | yes | | | | 1=Low-Loiw Deviation Alarm has been acknowledged |
| `Alm_Fail` | Boolean | OPC `{TagPrefix}.Alm_Fail` | | yes | | | | 1=Loop Failure Alarm: PV Bad, SP Bad or CV Comm Failure or Bad |
| `Alm_HiDev` | Boolean | OPC `{TagPrefix}.Alm_HiDev` | | yes | | | | 1=Loop High Deviation Alarm |
| `Alm_HiHiDev` | Boolean | OPC `{TagPrefix}.Alm_HiHiDev` | | yes | | | | 1=Loop High-High Deviation Alarm |
| `Alm_IntlkTrip` | Boolean | OPC `{TagPrefix}.Alm_IntlkTrip` | | yes | | | | 1=Interlock Trip Alarm |
| `Alm_LoDev` | Boolean | OPC `{TagPrefix}.Alm_LoDev` | | yes | | | | 1=Loop Low Deviation Alarm |
| `Alm_LoLoDev` | Boolean | OPC `{TagPrefix}.Alm_LoLoDev` | | yes | | | | 1=Loop Low-Low Deviation Alarm |
| `Cfg_CVEUMax` | Boolean | OPC `{TagPrefix}.Cfg_CVEUMax` | | yes | | | | CV Engineering Units Maximum Value (CVEU) |
| `Cfg_CVEUMin` | Boolean | OPC `{TagPrefix}.Cfg_CVEUMin` | | yes | | | | CV Engineering Units Minimum Value (CVEU) |
| `Cfg_CVRoCLim` | Boolean | OPC `{TagPrefix}.Cfg_CVRoCLim` | | yes | | | | CV Rate of Change Limit (CV%/sec) |
| `Cfg_CtrlAction` | Boolean | OPC `{TagPrefix}.Cfg_CtrlAction` | | yes | | | | 1=Direct acting (E=PV-SP), 0=Reverse acting (E=SP-PV) |
| `Cfg_DGain` | Boolean | OPC `{TagPrefix}.Cfg_DGain` | | yes | | | | Derivative Gain (min) |
| `Cfg_Depend` | Boolean | OPC `{TagPrefix}.Cfg_Depend` | | yes | | | | 1=Dependent gains equation, 0=Independent gains |
| `Cfg_DerivSPAct` | Boolean | OPC `{TagPrefix}.Cfg_DerivSPAct` | | yes | | | | Deriv. Action on SP Change 1=Deriv of PV only (no action), 0=Deriv of Error (full action) |
| `Cfg_DerivSmooth` | Boolean | OPC `{TagPrefix}.Cfg_DerivSmooth` | | yes | | | | 1=Use Derivative Smoothing |
| `Cfg_DevDB` | Boolean | OPC `{TagPrefix}.Cfg_DevDB` | | yes | | | | Devation Alarm Deadband (PVEU) |
| `Cfg_FailAckReqd` | Boolean | OPC `{TagPrefix}.Cfg_FailAckReqd` | | yes | | | | 1=Acknowledge required for Loop Failure Alarm |
| `Cfg_FailResetReqd` | Boolean | OPC `{TagPrefix}.Cfg_FailResetReqd` | | yes | | | | 1=Reset required to clear Loop Failure Alarm |
| `Cfg_FailSeverity` | Int2 | OPC `{TagPrefix}.Cfg_FailSeverity` | | yes | | | | Loop Failure Alarm Severity: 1..250=Low, 251..500=Medium, 501..750=High, 751..1000=Urgent |
| `Cfg_HasCVNav` | Boolean | OPC `{TagPrefix}.Cfg_HasCVNav` | | yes | | | | 1=Tells HMI to enable navigation to a connected CV object |
| `Cfg_HasCasc` | Boolean | OPC `{TagPrefix}.Cfg_HasCasc` | | yes | | | | 1=Enable the loop to be placed into cascade/ratio mode |
| `Cfg_HasCascSPNav` | Boolean | OPC `{TagPrefix}.Cfg_HasCascSPNav` | | yes | | | | 1=Tells HMI to enable navigation to a connected cascade SP object |
| `Cfg_HasFailAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasFailAlm` | | yes | | | | 1=Loop Failure Alarm exists and will be checked |
| `Cfg_HasHiDevAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasHiDevAlm` | | yes | | | | 1=High Deviation Alarm exists and will be checked |
| `Cfg_HasHiHiDevAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasHiHiDevAlm` | | yes | | | | 1=High-High Deviation Alarm exists and will be checked |
| `Cfg_HasIntlkObj` | Boolean | OPC `{TagPrefix}.Cfg_HasIntlkObj` | | yes | | | | 1=Tells HMI a P\_Intlk is connected to Inp\_Intlk |
| `Cfg_HasIntlkTripAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasIntlkTripAlm` | | yes | | | | 1=Interlock Trip Alarm exists and will be checked |
| `Cfg_HasLoDevAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasLoDevAlm` | | yes | | | | 1=Low Deviation Alarm exists and will be checked |
| `Cfg_HasLoLoDevAlm` | Boolean | OPC `{TagPrefix}.Cfg_HasLoLoDevAlm` | | yes | | | | 1=Low-Low Deviation Alarm exists and will be checked |
| `Cfg_HasPVNav` | Boolean | OPC `{TagPrefix}.Cfg_HasPVNav` | | yes | | | | 1=Tells HMI to enable navigation to a connected PV object |
| `Cfg_HasRatio` | Boolean | OPC `{TagPrefix}.Cfg_HasRatio` | | yes | | | | 1=Casc Loop Mode is Ratio, 0=Casc Loop Mode is Cascade |
| `Cfg_HiDevAckReqd` | Boolean | OPC `{TagPrefix}.Cfg_HiDevAckReqd` | | yes | | | | 1=Acknowledge required for High Deviation Alarm |
| `Cfg_HiDevGateDly` | Int4 | OPC `{TagPrefix}.Cfg_HiDevGateDly` | | yes | | | | High Deviation Status Gate Delay (sec) |
| `Cfg_HiDevOffDly` | Int4 | OPC `{TagPrefix}.Cfg_HiDevOffDly` | | yes | | | | Minimum time below High Deviation Limit to clear Status (sec) |
| `Cfg_HiDevOnDly` | Int4 | OPC `{TagPrefix}.Cfg_HiDevOnDly` | | yes | | | | Minimum time above High Deviation Limit to raise Status (sec) |
| `Cfg_HiDevResetReqd` | Boolean | OPC `{TagPrefix}.Cfg_HiDevResetReqd` | | yes | | | | 1=Reset required to clear High Deviation Alarm |
| `Cfg_HiDevSeverity` | Int2 | OPC `{TagPrefix}.Cfg_HiDevSeverity` | | yes | | | | High Deviation Severity: 1..250=Low, 251..500=Medium, 501..750=High, 751..1000=Urgent |
| `Cfg_HiHiDevAckReqd` | Boolean | OPC `{TagPrefix}.Cfg_HiHiDevAckReqd` | | yes | | | | 1=Acknowledge required for High-High Deviation Alarm |
| `Cfg_HiHiDevGateDly` | Int4 | OPC `{TagPrefix}.Cfg_HiHiDevGateDly` | | yes | | | | High-High Deviation Status Gate Delay (sec) |
| `Cfg_HiHiDevOffDly` | Int4 | OPC `{TagPrefix}.Cfg_HiHiDevOffDly` | | yes | | | | Minimum time below High-High Deviation Limit to clear Status (sec) |
| `Cfg_HiHiDevOnDly` | Int4 | OPC `{TagPrefix}.Cfg_HiHiDevOnDly` | | yes | | | | Minimum time above High-High Deviation Limit to raise Status (sec) |
| `Cfg_HiHiDevResetReqd` | Boolean | OPC `{TagPrefix}.Cfg_HiHiDevResetReqd` | | yes | | | | 1=Reset required to clear High-High Deviation Alarm |
| `Cfg_HiHiDevSeverity` | Int2 | OPC `{TagPrefix}.Cfg_HiHiDevSeverity` | | yes | | | | High-High Deviation Severity: 1..250=Low, 251..500=Medium, 501..750=High, 751..1000=Urgent |
| `Cfg_IGain` | Boolean | OPC `{TagPrefix}.Cfg_IGain` | | yes | | | | Integral Gain (1/min independent or min/repeat dependent) |
| `Cfg_InitToMan` | Boolean | OPC `{TagPrefix}.Cfg_InitToMan` | | yes | | | | 1=Go to Manual Loop Mode when an init request is seen |
| `Cfg_IntlkCV` | Boolean | OPC `{TagPrefix}.Cfg_IntlkCV` | | yes | | | | CV to use when Interlocks not OK (CV%) |
| `Cfg_IntlkTripAckReqd` | Boolean | OPC `{TagPrefix}.Cfg_IntlkTripAckReqd` | | yes | | | | 1=Acknowledge required for Interlock Trip Alarm |
| `Cfg_IntlkTripResetReqd` | Boolean | OPC `{TagPrefix}.Cfg_IntlkTripResetReqd` | | yes | | | | 1=Reset required to clear Interlock Trip Alarm |
| `Cfg_IntlkTripSeverity` | Int2 | OPC `{TagPrefix}.Cfg_IntlkTripSeverity` | | yes | | | | Interlock Trip Alarm Severity: 1..250=Low, 251..500=Medium, 501..750=High, 751..1000=Urgent |
| `Cfg_LimitManCV` | Boolean | OPC `{TagPrefix}.Cfg_LimitManCV` | | yes | | | | 1=CV limits enforced in Manual, 0=No CV Limiting in Manual |
| `Cfg_LoDevAckReqd` | Boolean | OPC `{TagPrefix}.Cfg_LoDevAckReqd` | | yes | | | | 1=Acknowledge required for Low Deviation Alarm |
| `Cfg_LoDevGateDly` | Int4 | OPC `{TagPrefix}.Cfg_LoDevGateDly` | | yes | | | | Low Deviation Status Gate Delay (sec) |
| `Cfg_LoDevOffDly` | Int4 | OPC `{TagPrefix}.Cfg_LoDevOffDly` | | yes | | | | Minimum time above Low Deviation Limit to clear Status (sec) |
| `Cfg_LoDevOnDly` | Int4 | OPC `{TagPrefix}.Cfg_LoDevOnDly` | | yes | | | | Minimum time below Low Deviation Limit to raise Status (sec) |
| `Cfg_LoDevResetReqd` | Boolean | OPC `{TagPrefix}.Cfg_LoDevResetReqd` | | yes | | | | 1=Reset required to clear Low Deviation Alarm |
| `Cfg_LoDevSeverity` | Int2 | OPC `{TagPrefix}.Cfg_LoDevSeverity` | | yes | | | | Low Deviation Severity: 1..250=Low, 251..500=Medium, 501..750=High, 751..1000=Urgent |
| `Cfg_LoLoDevAckReqd` | Boolean | OPC `{TagPrefix}.Cfg_LoLoDevAckReqd` | | yes | | | | 1=Acknowledge required for Low-Low Deviation Alarm |
| `Cfg_LoLoDevGateDly` | Int4 | OPC `{TagPrefix}.Cfg_LoLoDevGateDly` | | yes | | | | Low-Low Deviation Status Gate Delay (sec) |
| `Cfg_LoLoDevOffDly` | Int4 | OPC `{TagPrefix}.Cfg_LoLoDevOffDly` | | yes | | | | Minimum time below Low-Low Deviation Limit to clear Status (sec) |
| `Cfg_LoLoDevOnDly` | Int4 | OPC `{TagPrefix}.Cfg_LoLoDevOnDly` | | yes | | | | Minimum time below Low-Low Deviation Limit to raise Status (sec) |
| `Cfg_LoLoDevResetReqd` | Boolean | OPC `{TagPrefix}.Cfg_LoLoDevResetReqd` | | yes | | | | 1=Reset required to clear Low-Low Deviation Alarm |
| `Cfg_LoLoDevSeverity` | Int2 | OPC `{TagPrefix}.Cfg_LoLoDevSeverity` | | yes | | | | Low-Low Deviation Severity: 1..250=Low, 251..500=Medium, 501..750=High, 751..1000=Urgent |
| `Cfg_MaxCV` | Boolean | OPC `{TagPrefix}.Cfg_MaxCV` | | yes | | | | Maximum allowed Controlled Variable (CV) value (CV%) |
| `Cfg_MaxInactiveCV` | Float4 | OPC `{TagPrefix}.Cfg_MaxInactiveCV` | | yes | | | | When Val\_CV is greater than this value (CV%) set Sts\_Active (for HMI) |
| `Cfg_MaxRatio` | Boolean | OPC `{TagPrefix}.Cfg_MaxRatio` | | yes | | | | Maximum allowed Ratio (unitless) |
| `Cfg_MaxSP` | Boolean | OPC `{TagPrefix}.Cfg_MaxSP` | | yes | | | | Maximum allowed Setpoint (SP) value (PVEU) |
| `Cfg_MinCV` | Boolean | OPC `{TagPrefix}.Cfg_MinCV` | | yes | | | | Minimum allowed Controlled Variable (CV) value (CV%) |
| `Cfg_MinRatio` | Boolean | OPC `{TagPrefix}.Cfg_MinRatio` | | yes | | | | Minimum allowed Ratio (unitless) |
| `Cfg_MinSP` | Boolean | OPC `{TagPrefix}.Cfg_MinSP` | | yes | | | | Minimum allowed Setpoint (SP) value (PVEU) |
| `Cfg_OvrdIntlk` | Boolean | OPC `{TagPrefix}.Cfg_OvrdIntlk` | | yes | | | | 1=Override ignores Bypassable Intlk; 0=always use Intlk |
| `Cfg_PCmdClear` | Boolean | OPC `{TagPrefix}.Cfg_PCmdClear` | | yes | | | | |
| `Cfg_PGain` | Boolean | OPC `{TagPrefix}.Cfg_PGain` | | yes | | | | Proportional (independent) or Loop (dependent) Gain (unitless) |
| `Cfg_PVEUMax` | Boolean | OPC `{TagPrefix}.Cfg_PVEUMax` | | yes | | | | PV Engineering Units Maximum Value (PVEU) |
| `Cfg_PVEUMin` | Boolean | OPC `{TagPrefix}.Cfg_PVEUMin` | | yes | | | | PV Engineering Units Mimimum Value (PVEU) |
| `Cfg_PVTrack` | Boolean | OPC `{TagPrefix}.Cfg_PVTrack` | | yes | | | | 1=SP tracks PV in Manual, 0=no PV tracking |
| `Cfg_ProgDefault` | Boolean | OPC `{TagPrefix}.Cfg_ProgDefault` | | yes | | | | |
| `Cfg_PropSPAct` | Boolean | OPC `{TagPrefix}.Cfg_PropSPAct` | | yes | | | | Prop. Action on SP Change 1=Prop of PV only (no action), 0=Prop of Error (full action) |
| `Cfg_PwrupCV` | Float4 | OPC `{TagPrefix}.Cfg_PwrupCV` | | yes | | | | Loop CV (CV %) on powerup, used if Cfg\_PwrupLM &lt;&gt; 0 (none) |
| `Cfg_PwrupLM` | Int1 | OPC `{TagPrefix}.Cfg_PwrupLM` | | yes | | | | Powerup Loop Mode$N0=No change (last), 1=Man (w/ CV),$N2=Auto (w/ SP),$N3=Casc/Ratio |
| `Cfg_PwrupSP` | Float4 | OPC `{TagPrefix}.Cfg_PwrupSP` | | yes | | | | Loop SP on powerup, used if Cfg\_PwrupLM = 1 (Manual) or 2 (Auto) |
| `Cfg_SetTrack` | Boolean | OPC `{TagPrefix}.Cfg_SetTrack` | | yes | | | | 1=PSets track OSets in Oper, OSets track PSets in Prog, 0=no Settings tracking |
| `Cfg_SetTrackOvrdHand` | Boolean | OPC `{TagPrefix}.Cfg_SetTrackOvrdHand` | | yes | | | | 1=Prog/Oper Settings track Override/Hand Inputs (CV, SP, Ratio) |
| `Cfg_ZCDB` | Boolean | OPC `{TagPrefix}.Cfg_ZCDB` | | yes | | | | Normal Zero Crossing Deadband (PVEU) |
| `Cfg_ZCOff` | Boolean | OPC `{TagPrefix}.Cfg_ZCOff` | | yes | | | | 1=need not cross zero error to be in deadband, 0=must cross zero error |
| `EnableIn` | Boolean | OPC `{TagPrefix}.EnableIn` | | yes | | | | Enable Input - System Defined Parameter |
| `EnableOut` | Boolean | OPC `{TagPrefix}.EnableOut` | | yes | | | | Enable Output - System Defined Parameter |
| `Err_Alarm` | Boolean | OPC `{TagPrefix}.Err_Alarm` | | yes | | | | 1=Error in Config: Alarm Min On Time, Shelf Time, Severity |
| `Err_CVEU` | Boolean | OPC `{TagPrefix}.Err_CVEU` | | yes | | | | 1=Error in Config: CV EU Max/Min Invalid |
| `Err_CVLim` | Boolean | OPC `{TagPrefix}.Err_CVLim` | | yes | | | | 1=Error in Config: CV Clamping Limits Invalid |
| `Err_DB` | Boolean | OPC `{TagPrefix}.Err_DB` | | yes | | | | 1=Error in Config: Deviation Alarm Deadband Invalid |
| `Err_PVEU` | Boolean | OPC `{TagPrefix}.Err_PVEU` | | yes | | | | 1=Error in Config: PV EU Max/Min Invalid |
| `Err_RatioLim` | Boolean | OPC `{TagPrefix}.Err_RatioLim` | | yes | | | | 1=Error in Config: Ratio Clamping Limits Invalid |
| `Err_SPLim` | Boolean | OPC `{TagPrefix}.Err_SPLim` | | yes | | | | 1=Error in Config: Setpoint Clamping Limits Invalid |
| `Err_Timer` | Boolean | OPC `{TagPrefix}.Err_Timer` | | yes | | | | 1=Error in Config: Status On-Delay or Off-Delay Time Invalid |
| `Inp_CVIOFault` | Boolean | OPC `{TagPrefix}.Inp_CVIOFault` | | yes | | | | 1=CV I/O Comms Status Bad, 0=OK |
| `Inp_CVInitVal` | Boolean | OPC `{TagPrefix}.Inp_CVInitVal` | | yes | | | | Value to Initialize the CV to when requested (CVEU) |
| `Inp_CVPrev` | Boolean | OPC `{TagPrefix}.Inp_CVPrev` | | yes | | | | CV Feedback from downstream block (CV%) |
| `Inp_CascSP` | Boolean | OPC `{TagPrefix}.Inp_CascSP` | | yes | | | | Setpoint in Cascade, Independent PV in Ratio (PVEU) |
| `Inp_FF` | Boolean | OPC `{TagPrefix}.Inp_FF` | | yes | | | | FeedForward term (CV%) |
| `Inp_FFPrev` | Boolean | OPC `{TagPrefix}.Inp_FFPrev` | | yes | | | | FF feedback from downstream block (CV%) |
| `Inp_Hand` | Boolean | OPC `{TagPrefix}.Inp_Hand` | | yes | | | | |
| `Inp_HandFdbk` | Boolean | OPC `{TagPrefix}.Inp_HandFdbk` | | yes | | | | CV Feedback used in Hand Mode (CV%) |
| `Inp_HandFdbkBad` | Boolean | OPC `{TagPrefix}.Inp_HandFdbkBad` | | yes | | | | 1=Inp\_HandFdbk input quality or I/O Comms Status Bad, 0=OK |
| `Inp_HiDevGate` | Boolean | OPC `{TagPrefix}.Inp_HiDevGate` | | yes | | | | High Deviation Status Gate, 1=enabled |
| `Inp_HiHiDevGate` | Boolean | OPC `{TagPrefix}.Inp_HiHiDevGate` | | yes | | | | High-High Deviation Status Gate, 1=enabled |
| `Inp_IntlkOK` | Boolean | OPC `{TagPrefix}.Inp_IntlkOK` | | yes | | | | 1=Interlocks OK, Analog Output can be set |
| `Inp_LoDevGate` | Boolean | OPC `{TagPrefix}.Inp_LoDevGate` | | yes | | | | Low Deviation Status Gate, 1=enabled |
| `Inp_LoLoDevGate` | Boolean | OPC `{TagPrefix}.Inp_LoLoDevGate` | | yes | | | | Low-Low Deviation Status Gate, 1=enabled |
| `Inp_NBIntlkOK` | Boolean | OPC `{TagPrefix}.Inp_NBIntlkOK` | | yes | | | | 1=Non-Bypassable Interlocks OK, Analog Output can be set |
| `Inp_Ovrd` | Boolean | OPC `{TagPrefix}.Inp_Ovrd` | | yes | | | | |
| `Inp_OvrdCV` | Float4 | OPC `{TagPrefix}.Inp_OvrdCV` | | yes | | | | CV to use in Override Mode (CV%) |
| `Inp_OvrdCmd` | Int1 | OPC `{TagPrefix}.Inp_OvrdCmd` | | yes | | | | Override Loop Mode Command 0=None, 1=Man, 2=Auto, 3=Casc |
| `Inp_OvrdRatio` | Float4 | OPC `{TagPrefix}.Inp_OvrdRatio` | | yes | | | | Ratio to use in Override Mode (unitless) |
| `Inp_OvrdSP` | Float4 | OPC `{TagPrefix}.Inp_OvrdSP` | | yes | | | | Setpoint to use in Override Mode (PVEU) |
| `Inp_PV` | Boolean | OPC `{TagPrefix}.Inp_PV` | | yes | | | | Process Variable (PVEU) |
| `Inp_PVBad` | Boolean | OPC `{TagPrefix}.Inp_PVBad` | | yes | | | | 1=PV quality or PV I/O Comms Status Bad, 0=OK |
| `Inp_PVSrcQ` | Int1 | OPC `{TagPrefix}.Inp_PVSrcQ` | | yes | | | | Source and Quality of Inp\_PV (enum) |
| `Inp_PVUncertain` | Boolean | OPC `{TagPrefix}.Inp_PVUncertain` | | yes | | | | 1=PV Value Not Reliable, 0=OK |
| `Inp_Reset` | Boolean | OPC `{TagPrefix}.Inp_Reset` | | yes | | | | 1=Reset latched Alarms |
| `Inp_UseCVInitVal` | Boolean | OPC `{TagPrefix}.Inp_UseCVInitVal` | | yes | | | | 1=Initialize CV to Inp\_CVInitValue |
| `Inp_UseCVPrev` | Boolean | OPC `{TagPrefix}.Inp_UseCVPrev` | | yes | | | | 1=Use Inp\_CVPrev as previous CV value, 0=Use last scan value |
| `Inp_UseFFPrev` | Boolean | OPC `{TagPrefix}.Inp_UseFFPrev` | | yes | | | | 1=Use Inp\_FFPrev as previous FF value, 0=Use last scan value |
| `Inp_WindupHi` | Boolean | OPC `{TagPrefix}.Inp_WindupHi` | | yes | | | | Windup High Signal 1=regulator will not increase the output. |
| `Inp_WindupLo` | Boolean | OPC `{TagPrefix}.Inp_WindupLo` | | yes | | | | Windup Low Signal 1=regulator will not decrease the output. |
| `MCmd_Acq` | Boolean | OPC `{TagPrefix}.MCmd_Acq` | | yes | | | | |
| `MCmd_Disable` | Boolean | OPC `{TagPrefix}.MCmd_Disable` | | yes | | | | Maintenance Command to Disable PID Loop |
| `MCmd_Enable` | Boolean | OPC `{TagPrefix}.MCmd_Enable` | | yes | | | | Maintenance Command to Enable PID Loop |
| `MCmd_Rel` | Boolean | OPC `{TagPrefix}.MCmd_Rel` | | yes | | | | |
| `Nrdy_CfgErr` | Boolean | OPC `{TagPrefix}.Nrdy_CfgErr` | | yes | | | | 1=Device Not Ready: Configuration Error |
| `Nrdy_Disabled` | Boolean | OPC `{TagPrefix}.Nrdy_Disabled` | | yes | | | | 1=Device Not Ready: Device Disabled by Maintenance |
| `Nrdy_IOFault` | Boolean | OPC `{TagPrefix}.Nrdy_IOFault` | | yes | | | | 1=Device Not Ready: I/O Fault (Shed Requires Reset) |
| `Nrdy_Init` | Boolean | OPC `{TagPrefix}.Nrdy_Init` | | yes | | | | 1=Device Not Ready: Initialized to Manual Mode |
| `Nrdy_Intlk` | Boolean | OPC `{TagPrefix}.Nrdy_Intlk` | | yes | | | | 1=Device Not Ready: Interlock Not OK |
| `Nrdy_NoMode` | Boolean | OPC `{TagPrefix}.Nrdy_NoMode` | | yes | | | | 1=Device Not Ready: Device Logic Disabled / NO Mode |
| `OCmd_AcqLock` | Boolean | OPC `{TagPrefix}.OCmd_AcqLock` | | yes | | | | |
| `OCmd_Auto` | Boolean | OPC `{TagPrefix}.OCmd_Auto` | | yes | | | | Operator Command to select Automatic control |
| `OCmd_Bypass` | Boolean | OPC `{TagPrefix}.OCmd_Bypass` | | yes | | | | Operator Command to Bypass all Bypassable Interlocks |
| `OCmd_Casc` | Boolean | OPC `{TagPrefix}.OCmd_Casc` | | yes | | | | Operator Command to select Cascade / Ratio control |
| `OCmd_Check` | Boolean | OPC `{TagPrefix}.OCmd_Check` | | yes | | | | Operator Command to Check (not bypass) all Interlocks |
| `OCmd_Man` | Boolean | OPC `{TagPrefix}.OCmd_Man` | | yes | | | | Operator Command to select Manual control |
| `OCmd_Reset` | Boolean | OPC `{TagPrefix}.OCmd_Reset` | | yes | | | | Operator Command to Reset all Alarms requiring Reset |
| `OCmd_ResetAckAll` | Boolean | OPC `{TagPrefix}.OCmd_ResetAckAll` | | yes | | | | Operator Command to Reset all Alarms and latched Shed conditions |
| `OCmd_Unlock` | Boolean | OPC `{TagPrefix}.OCmd_Unlock` | | yes | | | | |
| `OSet_CV` | Float4 | OPC `{TagPrefix}.OSet_CV` | | yes | | | | Operator Setting for Controlled Variable (loop Manual) (CV%) |
| `OSet_HiDevLim` | Float4 | OPC `{TagPrefix}.OSet_HiDevLim` | | yes | | | | Operator Setting for High Deviation Status Threshold (PVEU) |
| `OSet_HiHiDevLim` | Float4 | OPC `{TagPrefix}.OSet_HiHiDevLim` | | yes | | | | Operator Setting for High-High Deviation Status Threshold (PVEU) |
| `OSet_LoDevLim` | Float4 | OPC `{TagPrefix}.OSet_LoDevLim` | | yes | | | | Operator Setting for Low Deviation Status Threshold (PVEU) |
| `OSet_LoLoDevLim` | Float4 | OPC `{TagPrefix}.OSet_LoLoDevLim` | | yes | | | | Operator Setting for Low-Low Deviation Status Threshold (PVEU) |
| `OSet_Ratio` | Float4 | OPC `{TagPrefix}.OSet_Ratio` | | yes | | | | Operator Setting for Ratio (loop CasRat and Ratio enabled) (unitless) |
| `OSet_SP` | Float4 | OPC `{TagPrefix}.OSet_SP` | | yes | | | | Operator Setting for Setpoint (loop Auto) (PVEU) |
| `Out_CV` | Boolean | OPC `{TagPrefix}.Out_CV` | | yes | | | | CV to final control element (CVEU) |
| `PCmd_Acq` | Boolean | OPC `{TagPrefix}.PCmd_Acq` | | yes | | | | |
| `PCmd_Auto` | Boolean | OPC `{TagPrefix}.PCmd_Auto` | | yes | | | | Program Command to select Automatic control |
| `PCmd_Casc` | Boolean | OPC `{TagPrefix}.PCmd_Casc` | | yes | | | | Program Command to select Cascade / Ratio control |
| `PCmd_FailAck` | Boolean | OPC `{TagPrefix}.PCmd_FailAck` | | yes | | | | Program Command to Acknowledge Loop Failure Alarm |
| `PCmd_FailSuppress` | Boolean | OPC `{TagPrefix}.PCmd_FailSuppress` | | yes | | | | Program Command to Suppress Loop Failure Alarm |
| `PCmd_FailUnshelve` | Boolean | OPC `{TagPrefix}.PCmd_FailUnshelve` | | yes | | | | Program Command to Unshelve Loop Failure Alarm |
| `PCmd_FailUnsuppress` | Boolean | OPC `{TagPrefix}.PCmd_FailUnsuppress` | | yes | | | | Program Command to Unsuppress Loop Failure Alarm |
| `PCmd_HiDevAck` | Boolean | OPC `{TagPrefix}.PCmd_HiDevAck` | | yes | | | | Program Command to Acknowledge High Deviation Alarm |
| `PCmd_HiDevSuppress` | Boolean | OPC `{TagPrefix}.PCmd_HiDevSuppress` | | yes | | | | Program Command to Suppress High Deviation Alarm |
| `PCmd_HiDevUnshelve` | Boolean | OPC `{TagPrefix}.PCmd_HiDevUnshelve` | | yes | | | | Program Command to Unshelve High Deviation Alarm |
| `PCmd_HiDevUnsuppress` | Boolean | OPC `{TagPrefix}.PCmd_HiDevUnsuppress` | | yes | | | | Program Command to Unsuppress High Deviation Alarm |
| `PCmd_HiHiDevAck` | Boolean | OPC `{TagPrefix}.PCmd_HiHiDevAck` | | yes | | | | Program Command to Acknowledge High-High Deviation Alarm |
| `PCmd_HiHiDevSuppress` | Boolean | OPC `{TagPrefix}.PCmd_HiHiDevSuppress` | | yes | | | | Program Command to Suppress High-High Deviation Alarm |
| `PCmd_HiHiDevUnshelve` | Boolean | OPC `{TagPrefix}.PCmd_HiHiDevUnshelve` | | yes | | | | Program Command to Unshelve High-High Deviation Alarm |
| `PCmd_HiHiDevUnsuppress` | Boolean | OPC `{TagPrefix}.PCmd_HiHiDevUnsuppress` | | yes | | | | Program Command to UnsuppressHigh-High Deviation Alarm |
| `PCmd_IntlkTripAck` | Boolean | OPC `{TagPrefix}.PCmd_IntlkTripAck` | | yes | | | | Program Command to Acknowledge Interlock Trip Alarm |
| `PCmd_IntlkTripSuppress` | Boolean | OPC `{TagPrefix}.PCmd_IntlkTripSuppress` | | yes | | | | Program Command to Suppress Interlock Trip Alarm |
| `PCmd_IntlkTripUnshelve` | Boolean | OPC `{TagPrefix}.PCmd_IntlkTripUnshelve` | | yes | | | | Program Command to Unshelve Interlock Trip Alarm |
| `PCmd_IntlkTripUnsuppress` | Boolean | OPC `{TagPrefix}.PCmd_IntlkTripUnsuppress` | | yes | | | | Program Command to Unsuppress Interlock Trip Alarm |
| `PCmd_LoDevAck` | Boolean | OPC `{TagPrefix}.PCmd_LoDevAck` | | yes | | | | Program Command to Acknowledge Low Deviation Alarm |
| `PCmd_LoDevSuppress` | Boolean | OPC `{TagPrefix}.PCmd_LoDevSuppress` | | yes | | | | Program Command to Suppress Low Deviation Alarm |
| `PCmd_LoDevUnshelve` | Boolean | OPC `{TagPrefix}.PCmd_LoDevUnshelve` | | yes | | | | Program Command to Unshelve Low Deviation Alarm |
| `PCmd_LoDevUnsuppress` | Boolean | OPC `{TagPrefix}.PCmd_LoDevUnsuppress` | | yes | | | | Program Command to Unsuppress Low Deviation Alarm |
| `PCmd_LoLoDevAck` | Boolean | OPC `{TagPrefix}.PCmd_LoLoDevAck` | | yes | | | | Program Command to Acknowledge Low-Low Deviation Alarm |
| `PCmd_LoLoDevSuppress` | Boolean | OPC `{TagPrefix}.PCmd_LoLoDevSuppress` | | yes | | | | Program Command to Suppress Low-Low Deviation Alarm |
| `PCmd_LoLoDevUnshelve` | Boolean | OPC `{TagPrefix}.PCmd_LoLoDevUnshelve` | | yes | | | | Program Command to Unshelve Low-Low Deviation Alarm |
| `PCmd_LoLoDevUnsuppress` | Boolean | OPC `{TagPrefix}.PCmd_LoLoDevUnsuppress` | | yes | | | | Program Command to Unsuppress Low-Low Deviation Alarm |
| `PCmd_Lock` | Boolean | OPC `{TagPrefix}.PCmd_Lock` | | yes | | | | |
| `PCmd_Man` | Boolean | OPC `{TagPrefix}.PCmd_Man` | | yes | | | | Program Command to select Manual control |
| `PCmd_Rel` | Boolean | OPC `{TagPrefix}.PCmd_Rel` | | yes | | | | |
| `PCmd_Reset` | Boolean | OPC `{TagPrefix}.PCmd_Reset` | | yes | | | | Program Command to Reset all Alarms requiring Reset |
| `PCmd_Unlock` | Boolean | OPC `{TagPrefix}.PCmd_Unlock` | | yes | | | | |
| `PSet_CV` | Float4 | OPC `{TagPrefix}.PSet_CV` | | yes | | | | Program Setting for Controlled Variable (loop Manual) (CV%) |
| `PSet_HiDevLim` | Float4 | OPC `{TagPrefix}.PSet_HiDevLim` | | yes | | | | Program Setting for High Deviation Status Threshold (PVEU) |
| `PSet_HiHiDevLim` | Float4 | OPC `{TagPrefix}.PSet_HiHiDevLim` | | yes | | | | Program Setting for High-High Deviation Status Threshold (PVEU) |
| `PSet_LoDevLim` | Float4 | OPC `{TagPrefix}.PSet_LoDevLim` | | yes | | | | Program Setting for Low Deviation Status Threshold (PVEU) |
| `PSet_LoLoDevLim` | Float4 | OPC `{TagPrefix}.PSet_LoLoDevLim` | | yes | | | | Program Setting for Low-Low Deviation Status Threshold (PVEU) |
| `PSet_Owner` | Int4 | OPC `{TagPrefix}.PSet_Owner` | | yes | | | | Program Owner Request ID (non-zero) or Release (zero) |
| `PSet_Ratio` | Float4 | OPC `{TagPrefix}.PSet_Ratio` | | yes | | | | Program Setting for Ratio (loop CasRat and Ratio enabled) (unitless) |
| `PSet_SP` | Float4 | OPC `{TagPrefix}.PSet_SP` | | yes | | | | Program Setting for Setpoint (loop Auto) (PVEU) |
| `P_PIDE` | Boolean | OPC `{TagPrefix}.P_PIDE` | | yes | | | | Unique Parameter Name for auto - discovery |
| `Rdy_Auto` | Boolean | OPC `{TagPrefix}.Rdy_Auto` | | yes | | | | 1=Ready to receive OCmd\_Auto (enables HMI button) |
| `Rdy_Bypass` | Boolean | OPC `{TagPrefix}.Rdy_Bypass` | | yes | | | | 1=Ready to receive OCmd\_Bypass (enables HMI button) |
| `Rdy_CV` | Boolean | OPC `{TagPrefix}.Rdy_CV` | | yes | | | | 1=Ready to receive OSet\_CV (enables data entry field) |
| `Rdy_Casc` | Boolean | OPC `{TagPrefix}.Rdy_Casc` | | yes | | | | 1=Ready to receive OCmd\_Casc (enables HMI button) |
| `Rdy_Check` | Boolean | OPC `{TagPrefix}.Rdy_Check` | | yes | | | | 1=Ready to receive OCmd\_Check (enables HMI button) |
| `Rdy_Disable` | Boolean | OPC `{TagPrefix}.Rdy_Disable` | | yes | | | | 1=Ready to receive MCmd\_Disable (enables HMI button) |
| `Rdy_Enable` | Boolean | OPC `{TagPrefix}.Rdy_Enable` | | yes | | | | 1=Ready to receive MCmd\_Enable (enables HMI button) |
| `Rdy_Man` | Boolean | OPC `{TagPrefix}.Rdy_Man` | | yes | | | | 1=Ready to receive OCmd\_Man (enables HMI button) |
| `Rdy_OSet` | Boolean | OPC `{TagPrefix}.Rdy_OSet` | | yes | | | | 1=Ready to receive other OSets (enables data entry fields) |
| `Rdy_Ratio` | Boolean | OPC `{TagPrefix}.Rdy_Ratio` | | yes | | | | 1=Ready to receive OSet\_Ratio (enables data entry field) |
| `Rdy_Reset` | Boolean | OPC `{TagPrefix}.Rdy_Reset` | | yes | | | | 1=Ready to receive OCmd\_Reset (enables HMI button) |
| `Rdy_ResetAckAll` | Boolean | OPC `{TagPrefix}.Rdy_ResetAckAll` | | yes | | | | 1=At least one Alarm or latched Shed condition requires Reset or Ack |
| `Rdy_SP` | Boolean | OPC `{TagPrefix}.Rdy_SP` | | yes | | | | 1=Ready to receive OSet\_SP (enables data entry field) |
| `SrcQ` | Int1 | OPC `{TagPrefix}.SrcQ` | | yes | | | | Source and Quality of primary Val/Sts (enumeration) |
| `SrcQ_IO` | Int1 | OPC `{TagPrefix}.SrcQ_IO` | | yes | | | | Source and Quality of primary I/O (enumeration) |
| `Sts_Active` | Boolean | OPC `{TagPrefix}.Sts_Active` | | yes | | | | 1=CV is greater than Cfg\_MaxInactiveCV, show graphic symbol as $Qactive$Q |
| `Sts_AlmInh` | Boolean | OPC `{TagPrefix}.Sts_AlmInh` | | yes | | | | 1=One or more Alarms Shelved, Disabled or Suppressed |
| `Sts_Auto` | Boolean | OPC `{TagPrefix}.Sts_Auto` | | yes | | | | 1=Loop Mode is Auto |
| `Sts_Available` | Boolean | OPC `{TagPrefix}.Sts_Available` | | yes | | | | 1=Loop available for manipulation in Prog Mode |
| `Sts_BypActive` | Boolean | OPC `{TagPrefix}.Sts_BypActive` | | yes | | | | 1=Bypassing Active (Bypassed or Maintenance) |
| `Sts_Bypass` | Boolean | OPC `{TagPrefix}.Sts_Bypass` | | yes | | | | 1=Bypassable Interlocks are Bypassed |
| `Sts_CVBad` | Boolean | OPC `{TagPrefix}.Sts_CVBad` | | yes | | | | 1=CV Value is Bad (quality) or invalid or CV comms fault |
| `Sts_CVClamped` | Boolean | OPC `{TagPrefix}.Sts_CVClamped` | | yes | | | | 1=Selected CV is being clamped (for faceplate animation) |
| `Sts_CVInitValBad` | Boolean | OPC `{TagPrefix}.Sts_CVInitValBad` | | yes | | | | 1=Inp\_CVInitVal is &lt;0.0, &gt;100.0, or not a number (NaN) |
| `Sts_CVPrevBad` | Boolean | OPC `{TagPrefix}.Sts_CVPrevBad` | | yes | | | | 1=Inp\_CVPrev is &lt;0.0, &gt;100.0, or not a number (NaN) |
| `Sts_CVRamping` | Boolean | OPC `{TagPrefix}.Sts_CVRamping` | | yes | | | | 1=CV is ramping toward Val\_CVSet, 0=ramp complete |
| `Sts_Casc` | Boolean | OPC `{TagPrefix}.Sts_Casc` | | yes | | | | 1=Loop Mode is Cascade/Ratio |
| `Sts_Disabled` | Boolean | OPC `{TagPrefix}.Sts_Disabled` | | yes | | | | 1=Loop is Disabled (held at configured Interlock CV) |
| `Sts_Err` | Boolean | OPC `{TagPrefix}.Sts_Err` | | yes | | | | 1=Error in Config: see detail Err bits for reason |
| `Sts_FFBad` | Boolean | OPC `{TagPrefix}.Sts_FFBad` | | yes | | | | 1=Fedforward Term Value is invalid |
| `Sts_FFPrevBad` | Boolean | OPC `{TagPrefix}.Sts_FFPrevBad` | | yes | | | | 1=Inp\_FFPrev is &lt;-100.0, &gt;100.0, or not a number (NaN) |
| `Sts_Fail` | Boolean | OPC `{TagPrefix}.Sts_Fail` | | yes | | | | 1=Loop Failure: PV Bad, SP Bad or CV Comm Failure or Bad |
| `Sts_FailDisabled` | Boolean | OPC `{TagPrefix}.Sts_FailDisabled` | | yes | | | | 1=Loop Failure Alarm has been Disabled by Maintenance |
| `Sts_FailShelved` | Boolean | OPC `{TagPrefix}.Sts_FailShelved` | | yes | | | | 1=Loop Failure Alarm has been Shelved by Operator |
| `Sts_FailSuppressed` | Boolean | OPC `{TagPrefix}.Sts_FailSuppressed` | | yes | | | | 1=Loop Failure Alarm has been Suppressed by Program |
| `Sts_Hand` | Boolean | OPC `{TagPrefix}.Sts_Hand` | | yes | | | | |
| `Sts_HandFdbkBad` | Boolean | OPC `{TagPrefix}.Sts_HandFdbkBad` | | yes | | | | 1=Hand FB (Tieback) Value is Bad (quality) or invalid or comms fault |
| `Sts_HiDev` | Boolean | OPC `{TagPrefix}.Sts_HiDev` | | yes | | | | 1=PV Deviation is above High limit |
| `Sts_HiDevCmp` | Boolean | OPC `{TagPrefix}.Sts_HiDevCmp` | | yes | | | | High Deviation comparison result 1=Dev High |
| `Sts_HiDevDisabled` | Boolean | OPC `{TagPrefix}.Sts_HiDevDisabled` | | yes | | | | 1=High Deviation Alarm has been Disabled by Maintenance |
| `Sts_HiDevGate` | Boolean | OPC `{TagPrefix}.Sts_HiDevGate` | | yes | | | | High Deviation Gate Delay Status, 1=done |
| `Sts_HiDevShelved` | Boolean | OPC `{TagPrefix}.Sts_HiDevShelved` | | yes | | | | 1=High Deviation Alarm has been Shelved by Operator |
| `Sts_HiDevSuppressed` | Boolean | OPC `{TagPrefix}.Sts_HiDevSuppressed` | | yes | | | | 1=High Deviation Alarm has been Suppressed by Program |
| `Sts_HiHiDev` | Boolean | OPC `{TagPrefix}.Sts_HiHiDev` | | yes | | | | 1=PV Deviation is above High-High limit |
| `Sts_HiHiDevCmp` | Boolean | OPC `{TagPrefix}.Sts_HiHiDevCmp` | | yes | | | | High-High Deviation comparison result 1=Dev High-High |
| `Sts_HiHiDevDisabled` | Boolean | OPC `{TagPrefix}.Sts_HiHiDevDisabled` | | yes | | | | 1=High-High Deviation Alarm has been Disabled by Maintenance |
| `Sts_HiHiDevGate` | Boolean | OPC `{TagPrefix}.Sts_HiHiDevGate` | | yes | | | | High-High Deviation Gate Delay Status, 1=done |
| `Sts_HiHiDevShelved` | Boolean | OPC `{TagPrefix}.Sts_HiHiDevShelved` | | yes | | | | 1=High-High Deviation Alarm has been Shelved by Operator |
| `Sts_HiHiDevSuppressed` | Boolean | OPC `{TagPrefix}.Sts_HiHiDevSuppressed` | | yes | | | | 1=High-High Deviation Alarm has been Suppressed by Program |
| `Sts_InitReq` | Boolean | OPC `{TagPrefix}.Sts_InitReq` | | yes | | | | 1=CV Initialize Request to this loop$'s Primary |
| `Sts_Initializing` | Boolean | OPC `{TagPrefix}.Sts_Initializing` | | yes | | | | 1=CV is initializing because of Request from this loop$'s Secondary |
| `Sts_InstrFaults1` | Int4 | OPC `{TagPrefix}.Sts_InstrFaults1` | | yes | | | | PIDE Block Status1 Instruction Fault bits (See PIDE Instruction Help) |
| `Sts_InstrFaults2` | Int4 | OPC `{TagPrefix}.Sts_InstrFaults2` | | yes | | | | PIDE Block Status2 Instruction Fault bits (See PIDE Instruction Help) |
| `Sts_IntlkCV` | Boolean | OPC `{TagPrefix}.Sts_IntlkCV` | | yes | | | | 1=CV ivalue s being set by shed to Interlock CV |
| `Sts_IntlkTrip` | Boolean | OPC `{TagPrefix}.Sts_IntlkTrip` | | yes | | | | 1=Interlock NOT OK caused loop output to hold or change |
| `Sts_IntlkTripDisabled` | Boolean | OPC `{TagPrefix}.Sts_IntlkTripDisabled` | | yes | | | | 1=Interlock Trip Alarm has been Disabled by Maintenance |
| `Sts_IntlkTripShelved` | Boolean | OPC `{TagPrefix}.Sts_IntlkTripShelved` | | yes | | | | 1=Interlock Trip Alarm has been Shelved by Operator |
| `Sts_IntlkTripSuppressed` | Boolean | OPC `{TagPrefix}.Sts_IntlkTripSuppressed` | | yes | | | | 1=Interlock Trip Alarm has been Suppressed by Program |
| `Sts_LoDev` | Boolean | OPC `{TagPrefix}.Sts_LoDev` | | yes | | | | 1=PV Deviation is below Low limit |
| `Sts_LoDevCmp` | Boolean | OPC `{TagPrefix}.Sts_LoDevCmp` | | yes | | | | Low Deviation comparison result 1=Dev Low |
| `Sts_LoDevDisabled` | Boolean | OPC `{TagPrefix}.Sts_LoDevDisabled` | | yes | | | | 1=Low Deviation Alarm has been Disabled by Maintenance |
| `Sts_LoDevGate` | Boolean | OPC `{TagPrefix}.Sts_LoDevGate` | | yes | | | | Low Deviation Gate Delay Status, 1=done |
| `Sts_LoDevShelved` | Boolean | OPC `{TagPrefix}.Sts_LoDevShelved` | | yes | | | | 1=Low Deviation Alarm has been Shelved by Operator |
| `Sts_LoDevSuppressed` | Boolean | OPC `{TagPrefix}.Sts_LoDevSuppressed` | | yes | | | | 1=Low Deviation Alarm has been Suppressed by Program |
| `Sts_LoLoDev` | Boolean | OPC `{TagPrefix}.Sts_LoLoDev` | | yes | | | | 1=PV Deviation is below Low-Low limit |
| `Sts_LoLoDevCmp` | Boolean | OPC `{TagPrefix}.Sts_LoLoDevCmp` | | yes | | | | Low-Low Deviation comparison result 1=Dev Low-Low |
| `Sts_LoLoDevDisabled` | Boolean | OPC `{TagPrefix}.Sts_LoLoDevDisabled` | | yes | | | | 1=Low-Low Deviation Alarm has been Disabled by Maintenance |
| `Sts_LoLoDevGate` | Boolean | OPC `{TagPrefix}.Sts_LoLoDevGate` | | yes | | | | Low-Low Deviation Gate Delay Status, 1=done |
| `Sts_LoLoDevShelved` | Boolean | OPC `{TagPrefix}.Sts_LoLoDevShelved` | | yes | | | | 1=Low-Low Deviation Alarm has been Shelved by Operator |
| `Sts_LoLoDevSuppressed` | Boolean | OPC `{TagPrefix}.Sts_LoLoDevSuppressed` | | yes | | | | 1=Low-Low Deviation Alarm has been Suppressed by Program |
| `Sts_MAcqRcvd` | Boolean | OPC `{TagPrefix}.Sts_MAcqRcvd` | | yes | | | | |
| `Sts_Maint` | Boolean | OPC `{TagPrefix}.Sts_Maint` | | yes | | | | |
| `Sts_MaintByp` | Boolean | OPC `{TagPrefix}.Sts_MaintByp` | | yes | | | | 1=Device has a Maintenance Bypass function active |
| `Sts_Man` | Boolean | OPC `{TagPrefix}.Sts_Man` | | yes | | | | 1=Loop Mode is Manual |
| `Sts_NoMode` | Boolean | OPC `{TagPrefix}.Sts_NoMode` | | yes | | | | |
| `Sts_NotRdy` | Boolean | OPC `{TagPrefix}.Sts_NotRdy` | | yes | | | | 1=Device Not Ready, see detail bits for reason |
| `Sts_Oper` | Boolean | OPC `{TagPrefix}.Sts_Oper` | | yes | | | | |
| `Sts_Ovrd` | Boolean | OPC `{TagPrefix}.Sts_Ovrd` | | yes | | | | |
| `Sts_PVBad` | Boolean | OPC `{TagPrefix}.Sts_PVBad` | | yes | | | | 1=PV Value, comms, quality or EU Limitis Bad |
| `Sts_PVUncertain` | Boolean | OPC `{TagPrefix}.Sts_PVUncertain` | | yes | | | | 1=PV Value is Uncertain (quality) |
| `Sts_Prog` | Boolean | OPC `{TagPrefix}.Sts_Prog` | | yes | | | | |
| `Sts_ProgOperLock` | Boolean | OPC `{TagPrefix}.Sts_ProgOperLock` | | yes | | | | |
| `Sts_RatioClamped` | Boolean | OPC `{TagPrefix}.Sts_RatioClamped` | | yes | | | | 1=Selected Ratio (PSet/OSet\_Ratio or Inp\_OvrdRatio) has been clamped |
| `Sts_SPBad` | Boolean | OPC `{TagPrefix}.Sts_SPBad` | | yes | | | | 1=SP Value is Bad (quality) or invalid or Casc SP comms fault |
| `Sts_SPClamped` | Boolean | OPC `{TagPrefix}.Sts_SPClamped` | | yes | | | | 1=Selected SP is being clamped (for faceplate animation) |
| `Sts_WindupHi` | Boolean | OPC `{TagPrefix}.Sts_WindupHi` | | yes | | | | 1=This loop winding up High, to Inp\_WindupHi of this loop$'s Primary |
| `Sts_WindupLo` | Boolean | OPC `{TagPrefix}.Sts_WindupLo` | | yes | | | | 1=This loop winding up Low, to Inp\_WindupLo of this loop$'s Primary |
| `Sts_ZCDBOn` | Boolean | OPC `{TagPrefix}.Sts_ZCDBOn` | | yes | | | | Deadband indictaor. 1=CV is within ZC deadband and will not change |
| `Val_ActExecT` | Boolean | OPC `{TagPrefix}.Val_ActExecT` | | yes | | | | Actual PID Algorithm Execution Time (Interval) (sec) |
| `Val_CVEUMax` | Float4 | OPC `{TagPrefix}.Val_CVEUMax` | | yes | | | | Maximum of CV scaled range (CVEU) |
| `Val_CVEUMin` | Float4 | OPC `{TagPrefix}.Val_CVEUMin` | | yes | | | | Minimum of CV scaled range (CVEU) |
| `Val_CVOut` | Boolean | OPC `{TagPrefix}.Val_CVOut` | | yes | | | | Value of CV Output (after ramping and clamping (CV%) |
| `Val_CVSet` | Float4 | OPC `{TagPrefix}.Val_CVSet` | | yes | | | | Value of CV Output (after ramping and clamping (CV%) |
| `Val_E` | Boolean | OPC `{TagPrefix}.Val_E` | | yes | | | | Loop Error (PV-SP) (PVEU) |
| `Val_EPercent` | Boolean | OPC `{TagPrefix}.Val_EPercent` | | yes | | | | Loop Error (PV-SP) (percent of span) |
| `Val_Fault` | Int1 | OPC `{TagPrefix}.Val_Fault` | | yes | | | | Loop Fault Status: TBD |
| `Val_HiDevLim` | Boolean | OPC `{TagPrefix}.Val_HiDevLim` | | yes | | | | Current High Deviation Status Threshold (PVEU) |
| `Val_HiHiDevLim` | Boolean | OPC `{TagPrefix}.Val_HiHiDevLim` | | yes | | | | Current High-High Deviation Status Threshold (PVEU) |
| `Val_Init` | Float4 | OPC `{TagPrefix}.Val_Init` | | yes | | | | Initialization Value for this loop$'s Cascade Primary |
| `Val_LoDevLim` | Float4 | OPC `{TagPrefix}.Val_LoDevLim` | | yes | | | | Current Low Deviation Status Threshold (PVEU) |
| `Val_LoLoDevLim` | Float4 | OPC `{TagPrefix}.Val_LoLoDevLim` | | yes | | | | Current Low-Low Deviation Status Threshold (PVEU) |
| `Val_Mode` | Int1 | OPC `{TagPrefix}.Val_Mode` | | yes | | | | |
| `Val_Notify` | Int1 | OPC `{TagPrefix}.Val_Notify` | | yes | | | | Current Alarm Level and Acknowledgement (enumeration) |
| `Val_Owner` | Int4 | OPC `{TagPrefix}.Val_Owner` | | yes | | | | Current Object Owner ID (0=not owned) |
| `Val_PV` | Float4 | OPC `{TagPrefix}.Val_PV` | | yes | | | | Loop PV (PVEU) |
| `Val_PVEUMax` | Float4 | OPC `{TagPrefix}.Val_PVEUMax` | | yes | | | | Maximum of PV scaled range (PVEU) |
| `Val_PVEUMin` | Float4 | OPC `{TagPrefix}.Val_PVEUMin` | | yes | | | | Minimum of PV scaled range (PVEU) |
| `Val_PVPercent` | Boolean | OPC `{TagPrefix}.Val_PVPercent` | | yes | | | | Loop PV (percent of span) |
| `Val_Ratio` | Boolean | OPC `{TagPrefix}.Val_Ratio` | | yes | | | | The current ratio (unitless) |
| `Val_SP` | Boolean | OPC `{TagPrefix}.Val_SP` | | yes | | | | Value of SP being used (after clamping) (PVEU) |
| `Val_SPPercent` | Boolean | OPC `{TagPrefix}.Val_SPPercent` | | yes | | | | Loop SP (percent of span) |
| `Val_SPSet` | Float4 | OPC `{TagPrefix}.Val_SPSet` | | yes | | | | Value of selected SP (before clamping) (PVEU) |
| `Val_State` | Int1 | OPC `{TagPrefix}.Val_State` | | yes | | | | Loop Algorithm State: TBD |
| `Val_Sts` | Int1 | OPC `{TagPrefix}.Val_Sts` | | yes | | | | Loop Status enum: TBD |

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [PLC/Accumulator](accumulator.md) (as `CV`), [PLC/Recirculator](recirculator.md) (as `LVL_CV`)

