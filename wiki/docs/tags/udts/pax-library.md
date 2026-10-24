---
title: PlantPAx Library (PLC/*)
sidebar_label: PlantPAx Library
sidebar_position: 2
description: The reusable read-only PLC library UDTs (P_Motor, P_AIn, P_DIn, P_ValveSO, P_Intlk, P_RunTime and the site types), their parameters, OPC path pattern, tag groups, history and alarms.
sources:
  - gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json
  - gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC_Ref/udts.json
  - gateways/standard/data/config/resources/core/ignition/tag-group/default/PAX_*/config.json
last_verified: 2026-10-24
---

# PlantPAx Library (`PLC/*`)

The PLC `RCP1` (CompactLogix 5370, controller name "BoarsHead") is programmed with Rockwell's **PlantPAx** library:
each motor is a `P_Motor` object, each analog input a `P_AIn`, each solenoid valve a `P_ValveSO`, and so on, plus a
few site-specific types written for this plant (screw compressors, control groups, sequencers). The `PLC/` UDT folder
mirrors those object types **one to one**, so one UDT instance = one controller object.

Generated pages: [PLC/P_Motor](../reference/udts/plc/p-motor.md), [PLC/P_AIn](../reference/udts/plc/p-ain.md),
[PLC/P_DIn](../reference/udts/plc/p-din.md), [PLC/P_ValveSO](../reference/udts/plc/p-valveso.md),
[PLC/P_Intlk](../reference/udts/plc/p-intlk.md), [PLC/P_RunTime](../reference/udts/plc/p-runtime.md),
[PLC/Screw_Compressor](../reference/udts/plc/screw-compressor.md), [PLC/CG_RL_Evap](../reference/udts/plc/cg-rl-evap.md),
[PLC/Comp_Sequence](../reference/udts/plc/comp-sequence.md),
[PLC/FB_2SpUpDownSeqr](../reference/udts/plc/fb-2spupdownseqr.md), [PLC/CR30_Input](../reference/udts/plc/cr30-input.md),
[PLC_Ref/P_AIn](../reference/udts/plc-ref/p-ain.md).

## Where The Library Came From

1. **L5K import.** The UDTs were first created from the controller's L5K export (Studio 5000 data types), which gave
   52 types with the exact PlantPAx member names and data types.
2. **Cleaned in place** for the 11 types the HMI uses: the member set was cut
   to the **HMI whitelist** (members the old FactoryTalk screens, the RA faceplates and our views read, plus a few
   extras), every member made `readOnly`, tag groups, history and engineering units added, state labels copied from
   the old HMI members.
3. **The other ~40 `PLC/*` types** (`TIMER`, `P_PIDE`, `P_DOut`, `QHD_*`, `Recirculator` ...) are still the raw L5K
   import. Nothing uses them; they are kept for reference. Their generated pages say "unused (raw L5K import)".

The analysis behind the whitelist (which members each type keeps and why) is in `docs/rcp1-pax-inventory.md` and
`docs/rcp1-pax-inventory/type_whitelists.json`.

## Parameters (Generic Only)

| Parameter | Meaning | Example |
|---|---|---|
| `DeviceName` | The OPC device connection in Ignition (Gateway > Config > OPC Connections > Devices). | `RCP1` |
| `TagPrefix` | The controller tag of the object, in Logix syntax (array elements and dots allowed). | `HTR_PUMPS[1]`, `COMP[6].Interlock`, `SafetyRelay:I` |
| `Description` | Free text; P_DIn uses it as the alarm display path. | `Pump #1 Alarm` |
| `EngUnit` (P_AIn) | Engineering unit applied to `Val`, the limits and the captured min / max. | `psig`, `°F`, `In"`, `%` |
| `AlarmOnSts` (P_DIn) | `1` turns on the "State Alarm" on `Sts`. Default `0`. | `1` on the tank pump alarm DIs |

There are **no Boars Head paths in the library**: every member's OPC item path is built only from the parameters:

```text
ns=1;s=[{DeviceName}]{TagPrefix}.<member>
ns=1;s=[RCP1]HTR_PUMPS[1].Sts_Running          (DeviceName = RCP1, TagPrefix = HTR_PUMPS[1])
ns=1;s=[RCP1]HTR_PUMPS[1].Mode.Val              (folder Mode / member Val)
ns=1;s=[RCP1]HTR_PUMP1_INTLK.Cfg_CondTxt[3]     (array element, member Cfg_CondTxt/Cfg_CondTxt_3_)
```

That is what makes the library **reusable**: copy the `P_*` entries of `PLC/udts.json` and the `PAX_*` tag groups
into another PlantPAx project, nest them in that project's device UDTs, pass `DeviceName` and `TagPrefix`, done. Since
the names are the PlantPAx names, an FT global object reference such as `{#1}.Sts_Running` maps one to one to
`<device>/Motor/Sts_Running`.

## Member Conventions

- **Exact PlantPAx names and data types** from the controller browse (`Val_Sts` is `Int1`, `Val` is `Float4`).
- **P_Alarm / P_Mode / P_Gate blocks are folders**: `FailToStart/Alm`, `Mode/Val`, `Hi/Ack`.
- **Arrays use the browse form**: `Cfg_CondTxt[3]` becomes the member `Cfg_CondTxt/Cfg_CondTxt_3_`.
- **Prefixes** follow PlantPAx: `Sts_` status, `Val_` values, `Cfg_` configuration, `Alm_` alarm bits, `Ack_`
  acknowledged, `Nrdy_` / `Rdy_` ready flags, `OCmd_` operator commands, `MCmd_` maintenance commands, `PCmd_` program
  commands, `Inp_` inputs, `Inf_` library info.
- **Every member is `readOnly: true`** and has **no value key** (these are OPC tags; a value key would be a write).
  The [PLC Write Lock](../plc-write-lock.md) script flips `readOnly` on these definitions.

## Tag Groups

Every OPC member is on one of three groups (current settings are on [Tag Groups](../reference/tag-groups.md)):

| Group | Mode | Members | Why |
|---|---|---|---|
| `PAX_Status` | Direct, 5,000 ms | Status, values, alarm bits, inputs: `Sts_*`, `Val*` (not limits), `Alm_*`, `Ack_*`, `Inp_*`, `Out*`. | Always polled, so alarms and history work with no screen open. 5 s (was 1 s) because the SecureLink link to the PLC is the bottleneck; on the plant LAN it can go back to 1 s. |
| `PAX_Faceplate` | Leased, leased rate 1,000 ms, background rate 60,000 ms | Configuration and display-only members: `Cfg_*`, commands, `Rdy_/Nrdy_*`, limits, strings (labels, descriptions, condition texts). | Polled fast only while a faceplate shows them; the 60 s background keeps a value ready so a faceplate opens with data (0-5 s instead of 34-48 s). |
| `PAX_Config` | Direct, 30,000 ms | The PLC alarm enables (`Cfg_HasFailAlm`, `Cfg_HasHiAlm` ...), `CG_RL_Evap.Cfg_HasBleedValve`, the P_Intlk condition texts. | Needed without a faceplate (alarm gating, the Interlocks tab rule, 3- vs 4-valve CGs) but they change rarely. |

## History

Every numeric `Val*` member in the **Direct** group is historized (provider `historian`, sample mode **On Change**).
Floats use an absolute deadband of `0.01` with the Analog style; integers `0` with the Discrete style. Leased members
are **not** historized on purpose: history on a Leased tag would only record while a faceplate is open. See
[History And Polling](../history.md) and the [History Index](../reference/history-index.md).

## The Library Types In Use

| UDT | PLC object type | Atomic members | Historized | Ignition alarms (priority) | Used by |
|---|---|---|---|---|---|
| `PLC/P_Motor` | PlantPAx single-speed motor | 109 | `Val_Sts`, `Val_Mode`, `Val_Notify` | `Alm_IOFault` IO Fault (Critical), `Alm_FailToStart` Fail To Start (High), `Alm_FailToStop` Fail To Stop (High), `Alm_IntlkTrip` Interlock Trip (Medium) | Pump `Motor`, Evaporator `Fans` |
| `PLC/P_Intlk` | Interlocks with first out | 50 | - | - | Pump, Valve, Compressor, Evaporator `Intlk` |
| `PLC/P_RunTime` | Run time and starts | 11 | `Val_TotRunHrs`, `Val_CurRunHrs`, `Val_Starts` | - | Pump `RunTime`, Evaporator `FansRunTime` |
| `PLC/P_AIn` | Analog input | 179 | `Val`, `Val_InpPV`, `Val_Fault`, `Val_Mode`, `Val_Notify`, `Val_PVMinCapt`, `Val_PVMaxCapt` | `Sts_Fail` Input Failure (High), `Sts_HiHi` High-High (High), `Sts_Hi` High (Medium), `Sts_Lo` Low (Medium), `Sts_LoLo` Low-Low (High), each **gated on the PLC enable** | Sensor `AIn`, Tank `LvlAIn`, Evaporator `ZAT` |
| `PLC/P_DIn` | Discrete input | 53 | `Val_Fault`, `Val_Notify` | `Sts_TgtDisagree` Target Disagree (Medium, gated on `Cfg_HasTgtDisagreeAlm`), `Sts` State Alarm (High, only where `AlarmOnSts = 1`) | DiscreteInput `DIn`, Tank `HlcoDIn` / `HiHiDIn` / `OplDIn` / `LoLoDIn` / `Pump1Alm` / `Pump2Alm`, ExhaustFan `DIn` |
| `PLC/P_ValveSO` | Solenoid valve | 151 | `Val_Sts`, `Val_Mode`, `Val_Fault`, `Val_Notify` | `Alm_IOFault` IO Fault (High), `Alm_FullStall` Full Stall (High), `Alm_TransitStall` Transit Stall (High), `Alm_IntlkTrip` Interlock Trip (Medium) | Valve `Valve` (4 standalone + 70 CG valves) |
| `PLC/Screw_Compressor` | Site UDT `COMP[n]` (Frick Quantum data read over Ethernet) | 63 | 21 float status members (Amps, FLA, SVP, SucP/T, DisP/T, OilP/T, TotalRuntime, KW ...) and `Rung` | `Failed` (Critical), `Cutout` (High), `Alm` Compressor Alarm (Medium), `Comm` Comm Error (Low) | Compressor `Comp` |
| `PLC/CG_RL_Evap` | Site UDT `CG[n]` (control group: defrost sequencer, setpoints, zone air temp control) | 68 | `Val_CoolingTime`, `Val_RunTime`, `Val_TimeLeft`, `ZAT_High/Low/HiHi/LoLo`, `AIDefrostStart/Stop` | `TooHot` Zone Air Temp Too Hot (Medium), `TooCold` Zone Air Temp Too Cold (Medium) | Evaporator `CG` |
| `PLC/Comp_Sequence` | Site UDT `HSS` / `LSS` (compressor suction sequence) | 44 | 10 pressure / target members | - | SuctionSequence `Seq` |
| `PLC/FB_2SpUpDownSeqr` | AOI `HSD_Seqr` (two-speed up / down sequencer) | 23 | `Inp_PV`, `Val_Target` | - | DischargeSequence `Seqr` |
| `PLC/CR30_Input` | Module input assembly `SafetyRelay:I` of the 440C-CR30 | 32 | - | Safety Relay Major Fault (High), Safety Relay Comm Loss (High), LSS / HSS HLCO Output 0 / 1 Reset Required (Medium) | SafetyRelay `IO` |

`CR30_Input` is a **site library type for a module tag**: the input assembly is not a UDT in the L5K, so the type
was created from the browsed `SafetyRelay:I` members, with the same rules.

## Alarms On The Library

The alarms are defined on these library members (never on instances). Since 2026-10-23 the P_AIn and P_DIn
alarms follow the **PLC's own alarm enables**: an alarm is enabled only while the object's matching `Cfg_Has*Alm` is
1, so the HMI raises exactly the alarms the plant configured in the PLC (FT parity). Details:
[Alarms](../alarms.md).

## `PLC_Ref/P_AIn`: The Reference Twin

Some transmitters are shown by two devices: `SYS_PT2` is both the `HSS-Pumps Pressure` sensor and the HTR tank's
pressure; `LT_CSV` is both the CSV tank level and the `Condenser Sump Level` sensor. To subscribe and alarm each
controller object **once**, one device is the **owner** (nests `PLC/P_AIn`, real OPC, alarms, history) and the other
nests `PLC_Ref/P_AIn`:

- the same member names as `PLC/P_AIn`;
- `valueSource: reference` to `{Source}/<member>`, where the `Source` parameter is the owner's part path, for example
  `[default]Boars_Head/GrovePort/Condensers/Tanks/CSV/LvlAIn`;
- read only, no OPC subscription, no alarms, no history.

Views can treat an `AInRef` part exactly like an `AIn` part (same member names).

| Object | Owner part | Referenced by |
|---|---|---|
| `SYS_PT2` | `Machine Room/Sensors/HSS-Pumps Pressure/AIn` | `Machine Room/Tanks/HTR/PressAIn` |
| `SYS_PT1` | `Machine Room/Sensors/LSS-Pumps Pressure/AIn` | `Machine Room/Tanks/LTR/PressAIn` |
| `LT_CSV` | `Condensers/Tanks/CSV/LvlAIn` | `Machine Room/Sensors/Condenser Sump Level/AInRef` |

## Adding A New PlantPAx Type Or Member

1. Check the controller really has it: the browse catalog `docs/rcp1-pax-inventory.md` (all 197,751 browsed tags) or
   Studio 5000.
2. UDT Definitions > `PLC` > the type: add the member (copy a neighbour), set its OPC item path from the type's
   parameters, **Read Only** on, its tag group (`PAX_Status` / `PAX_Faceplate` / `PAX_Config`), history and engineering
   units like the neighbouring members.
3. If the member needs an alarm, add it in the member's **Alarming** section ([Alarms](../alarms.md#how-to-add-or-change-an-alarm)).
4. Check a faceplate shows the new member.

