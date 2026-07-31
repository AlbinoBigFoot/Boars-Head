# RESEARCH — PLC UDTs → Devices/* map

**Quick id:** `260730-mun`  
**Sources:**
- `gateways/.../tag-type-definition/default/PLC/udts.json`
- `gateways/.../tag-type-definition/default/Devices/udts.json`
- `gateways/.../tag-type-definition/default/_Root/udts.json`
- Instance folders: `tag-definition/default/{Pumps,Valves,Tanks,Sensors,ExhaustFans,Evaporators,Compressors}/`

**Goal:** Drive comprehensive Devices UDT updates (Controls / Config / Interlocks) consistent with the already-expanded `Devices/Compressor`.

---

## 0. Shared foundations

### 0.1 `_Root` bases (what exists)

| Type | Members | Notes |
|------|---------|--------|
| `_Root/Analog` | `Value` (Float4, memory) | **Do not** put `SP` on the type. Add `SP` as an **instance child override** on the Devices member (Compressor `DisP` pattern). Putting `SP` on `_Root/Analog` renames to `SP_duplicate_1` and breaks AnalogValue’s `…/Value` → `…/SP` derivation (`docs/evaporator-hmi-components.md`). |
| `_Root/Digital` | `Value` (Boolean-ish, memory) | Use for latched status bits / alarms shown as tags. |
| `_Root/Multistate` | `Value` (Int4, memory) | Primary for `Status`, mode enums. State labels live in tag `metadata` / faceplate transforms / `SummaryInstances`, not in the UDT schema. |
| `_Root/Expression` | `Value` (expr Float4) + `Metadata` (Document) | Used for `SummaryInstances` overview wiring. |
| `_Root/Document` | `Value` (Document) | Rarely used directly on Devices. |

### 0.2 Companion PlantPAx types (reuse across devices)

| PLC type | Role | Map into Devices as |
|----------|------|---------------------|
| `P_Mode` | Oper / Maint / Prog / Hand / Ovrd ownership | Mode bools (`OPER`/`MAINT`/`PROG`) + acquire/release cmds; or nested `Mode/` folder |
| `P_Intlk` | 16 interlock bits, bypass, first-out, reset | `Interlock/` folder (Compressor already mirrors this) |
| `P_RunTime` | Tot/cur hours, starts, max run | KPI ints/floats (`RuntimeHours`, `MotorStarts`, …) |
| `P_Alarm` | Generic alarm object | Prefer device `_Alarms` (`Config/_Alarms`) + selective `Alm_*` digitals |
| `P_PIDE` | PID loop | Only where a device owns a loop (tank level, evap ZAT) — usually nested or separate Sensor/loop faceplate |
| `P_DOut` | Discrete output AOI | Simple on/off fans/solenoids if not using `P_Motor` / `P_ValveSO` |

### 0.3 Compressor reference (already done — pattern to copy)

**PLC:** `Screw_Compressor` (+ `QHD_Comp*`, `Comp_Sequence` at system level)  
**Devices/Compressor** already has:

- Multistate: `Status`, `CP_Mode`, `SV_Mode`, `Rung`, `Color`
- Analog (+ instance `SP` where needed): `DisP`, `Amps`, `FLA`, `SVP`
- Digital: `Alm`, `Cutout`, `Failed`, `Started`, `Comm`
- Raw bool cmds/modes: `Cmd_Start/Stop/Auto/Manual/Remote`, `OPER`/`MAINT`/`PROG`
- KPI: `RuntimeHours`, `MotorStarts`, `MaxRunTimePerStart`, `AutoEN`, `Min_Runtime_Set`, `Fail_Timer_PRE`
- `Interlock/` ≈ `P_Intlk` (Sts_*, Cfg_Bypassable, OCmd_Reset, Rdy_Reset, Cfg_CondTxt00–15, MSet_Bypass00–15)
- `SummaryInstances`, `_Alarms`

Use this as the **depth target** for Pump / Valve / ExhaustFan / Evaporator.

### 0.4 HMI status convention

- Prefer a single `Status` (`_Root/Multistate`) driven from PLC `Val_Sts` (or `Sts_State` for CG_RL) **or** a derived demo enum.
- Always pair with text STS codes (`Refridgeration_STS sts-<TOKEN>`), not color alone.
- Keep one-shot operator cmds as **Boolean** memory tags (Compressor style), not `_Root/Digital`, unless the faceplate already binds Digital.

---

## 1. Pump

### PLC type name(s)

| Primary | Secondary / related |
|---------|---------------------|
| **`P_Motor`** (159 leaves) | `P_Mode`, `P_Intlk`, `P_RunTime`; plant vessel context often via `Recirculator.Pump1/Pump2` bools |

### Key PLC members

| Bucket | Members |
|--------|---------|
| **Status (enum)** | `Val_Sts`: 0=?, 1=Stopped, 2=Running, 7=Stopping, 8=Starting, 33=Disabled |
| **Status (bools)** | `Sts_Stopped`, `Sts_Starting`, `Sts_Running`, `Sts_Stopping`, `Sts_Disabled`, `Sts_Available`, `Sts_NotRdy`, `Sts_Err`, `Sts_AlmInh`, `Sts_FailToStart/Stop`, `Sts_IOFault`, `Sts_IntlkTrip` |
| **Modes** | `Sts_Oper`, `Sts_Maint`, `Sts_Prog`, `Sts_Hand`, `Sts_Ovrd`, `Sts_NoMode`, `Val_Mode` |
| **Commands** | `OCmd_Start`, `OCmd_Stop`, `OCmd_Reset`, `OCmd_ResetAckAll`, `OCmd_Bypass`, `OCmd_Check`, `OCmd_AcqLock`, `OCmd_Unlock`; `MCmd_Enable`/`Disable`/`Acq`/`Rel`; `PCmd_Start`/`Stop`/… |
| **Ready** | `Rdy_Start`, `Rdy_Stop`, `Rdy_Reset`, `Rdy_ResetAckAll`, `Rdy_Bypass`, `Rdy_Check`, `Rdy_Enable`, `Rdy_Disable` |
| **Outputs** | `Out_Run`, `Out_Start`, `Out_Stop` |
| **Feedback / KPI** | `Inp_RunFdbk`, `Val_Fdbk` (0=Stopped,1=Running), `Val_Cmd` (0=None,1=Stop,2=Start), `Val_Fault` |
| **Interlocks** | `Inp_IntlkOK`, `Inp_NBIntlkOK`, `Inp_PermOK`, `Inp_NBPermOK` + nested `P_Intlk` object |
| **Alarms** | `Alm_FailToStart`, `Alm_FailToStop`, `Alm_IOFault`, `Alm_IntlkTrip` |
| **Runtime (AOI)** | `P_RunTime`: `Val_TotRunHrs`, `Val_CurRunHrs`, `Val_MaxRunHrs`, `Val_Starts` |
| **Config (HMI-relevant)** | `Cfg_HasRunFdbk`, `Cfg_HasIntlkObj`, `Cfg_HasPermObj`, `Cfg_HasRunTimeObj`, fail timers/severities |

### Devices/Pump — has vs missing

| Has today | Gap vs Compressor / PLC |
|-----------|-------------------------|
| `Status` (`_Root/Multistate`) | No mapped `Val_Sts` semantics documented on type |
| `Temp` (`_Root/Analog`, engUnit **gpm** on instances) | Misnamed — should be flow KPI (`Flow` / `GPM`), keep engUnit `gpm`; add optional `SP` child |
| `SummaryInstances`, `_Alarms` | Keep |
| — | **Missing modes:** `OPER`, `MAINT`, `PROG` (or Mode multistate) |
| — | **Missing cmds:** `Cmd_Start`, `Cmd_Stop`, `Cmd_Auto`/`Manual` (or map OCmd_*), Reset, Bypass/Check |
| — | **Missing digitals:** `Failed`/`Alm`/`Started`/`Comm` (or Alm_FailToStart/Stop, Sts_IOFault) |
| — | **Missing KPI:** `RuntimeHours`, `MotorStarts`, `Fail_Timer_PRE`-style configs |
| — | **Missing `Interlock/`** folder (copy Compressor / `P_Intlk`) |
| — | **Missing Ready bits** if Controls buttons gate on `Rdy_*` |

### Recommended `_Root` + states / engUnits

| Member | Base | States / engUnit |
|--------|------|------------------|
| `Status` | Multistate | Prefer PLC `Val_Sts`: `0=UNK, 1=STOPPED, 2=RUNNING, 7=STOPPING, 8=STARTING, 33=DISABLED`. STS tokens: `STOPPED`, `RUNNING`, `STARTING`, `STOPPING`, `FAULT`, `DISABLED` |
| `Flow` (rename from `Temp`) | Analog | engUnit `gpm`; optional instance `SP` |
| Mode flags | Boolean or Multistate | Align with `Sts_Oper/Maint/Prog` |
| Cmd_* / Alm_* / Failed | Boolean / Digital | — |
| `RuntimeHours` | Analog or Float4 | engUnit `h` |
| `MotorStarts` | Int4 / Multistate N/A | — |
| `Interlock/*` | Boolean/Int4/String | Same schema as Compressor |

**Instances today:** `Pumps/*` → `Devices/Pump` (e.g. PMP-02); Status/Temp often OPC to `[Sim]`.

---

## 2. Valve / `P_ValveSO`

### PLC type name(s)

| Primary | Notes |
|---------|--------|
| **`P_ValveSO`** (159 leaves) | Solenoid / single-output valve AOI used plant-wide |
| Related | `P_Mode`, `P_Intlk`; `FB_AlgSolCtrl` only for analog-solenoid hybrid (rare) |

### Key PLC members

| Bucket | Members |
|--------|---------|
| **Status (enum)** | `Val_Sts`: 0=?, 1=Closed, 2=Open, 5=Closing, 6=Opening, 33=Disabled |
| **Status (bools)** | `Sts_Closed`, `Sts_Closing`, `Sts_Opened`, `Sts_Opening`, `Sts_Disabled`, `Sts_Available`, `Sts_NotRdy`, `Sts_FullStall`, `Sts_TransitStall`, `Sts_LSFail`, `Sts_IOFault`, `Sts_IntlkTrip` |
| **Modes** | Same pattern as motor: `Sts_Oper/Maint/Prog/Hand/Ovrd` |
| **Commands** | `OCmd_Open`, `OCmd_Close`, `OCmd_Reset`, `OCmd_ResetAckAll`, `OCmd_Bypass`, `OCmd_Check`, lock/unlock; `MCmd_Enable`/`Disable`; `PCmd_Open`/`Close` |
| **Ready** | `Rdy_Open`, `Rdy_Close`, `Rdy_Reset`, … |
| **Output** | `Out` (energize solenoid) |
| **Feedback** | `Inp_OpenLS`, `Inp_ClosedLS`, `Val_Fdbk` (0=Moving,1=Closed,2=Opened,3=LS Fail), `Val_Cmd` (0=None,1=Close,2=Open) |
| **Interlocks** | `Inp_IntlkOK`, `Inp_NBIntlkOK`, `Inp_PermOK`, `Inp_NBPermOK` |
| **Alarms** | `Alm_FullStall`, `Alm_TransitStall`, `Alm_IOFault`, `Alm_IntlkTrip` |
| **Config** | `Cfg_HasOpenLS`, `Cfg_HasClosedLS`, `Cfg_UseOpenLS`, `Cfg_UseClosedLS`, `Cfg_FailOpen`, stall timers/severities |

### Devices/Valve — has vs missing

| Has today | Gap |
|-----------|-----|
| `Status` (Multistate) | No Open/Close/Transit semantics |
| `Temp` (Analog, engUnit **°F** on type default) | **Wrong for SO valve** — leftover placeholder; remove or replace with position/unused KPI |
| `_Alarms` | Keep; add SummaryInstances for overview parity |
| — | **Missing:** Open/Close cmds, Reset, Bypass/Check, mode flags |
| — | **Missing:** LS feedback digitals (`OpenLS`, `ClosedLS`), stall/fault digitals |
| — | **Missing:** `Interlock/` folder |
| — | **Missing:** fail-open / has-LS config for Config tab |

### Recommended `_Root` + states / engUnits

| Member | Base | States / engUnit |
|--------|------|------------------|
| `Status` | Multistate | `Val_Sts`: `CLOSED=1`, `OPEN=2`, `CLOSING=5`, `OPENING=6`, `DISABLED=33`; STS: `CLOSED`, `OPEN`, `CLOSING`, `OPENING`, `FAULT`, `DISABLED` |
| Drop `Temp` or replace | — | Do not keep °F on SO valves |
| `OpenLS`, `ClosedLS`, `Failed`, `Comm` | Digital | — |
| `Cmd_Open`, `Cmd_Close`, `Cmd_Reset`, … | Boolean | — |
| `OPER`/`MAINT`/`PROG` | Boolean | — |
| `Interlock/` | same as Compressor | — |
| Optional `TravelTime` / stall PRE | Analog | engUnit `s` |

**Instances:** `Valves/*` (e.g. HPRL-ISO) — currently memory-only stubs.

---

## 3. Tank

### PLC type name(s)

| PLC type | Role |
|----------|------|
| **`Recirculator`** | Vessel + pump lead/lag: `LEVEL`, `LEVEL_SP`, `LEVEL_DP`, `INCHES`, `LT`, `PT`, `HLCO`, `LLCO`, `HLS`, `Pump1/2`, `LEAD_PUMP_SET`, cavitation logic |
| **`Accumulator`** | Simpler: `LT`, `Level_SP`, `HLCO`, `CV`, `SV` |
| **`MakeUp_Water`** | `Level`, `HighLimit`/`LowLimit`, `Alm_HiHi`/`Alm_LoLo`, `Inp_*Level`, `Out` |
| **`P_AIn`** (on `LT`/`PT`) | Scaled level/pressure transmitter |
| **`Liquid_Transfer_Unit`** | Count/alarm — peripheral, not core Tank faceplate |

### Key members (union for HMI)

| Bucket | Members |
|--------|---------|
| **Level PV** | `LEVEL` / `LT` / `Level` → Devices `Level/Value` |
| **SPs** | `LEVEL_SP`, `Level_SP`, Hi/Lo operating bands |
| **Switches** | `HLCO`, `LLCO`, `HLS`, `LSH`/`LSL` |
| **Alarms / bands** | MakeUp `Alm_HiHi`/`Alm_LoLo`; Devices already has HH/H/L/LL Value+SP |
| **Related actuators** | Recirc `Pump1`/`Pump2`, Accumulator `CV`/`SV` (often separate Valve/Pump instances) |

### Devices/Tank — has vs missing

| Has today | Gap |
|-----------|-----|
| `Status` (Multistate) | Undefined enum (ok vs level? vs vessel state?) — document |
| `Level` (Analog, `%`) | Good; add `SP` child for `LEVEL_SP` |
| `LSH`, `LSL` (Digital) | Map from HLS / hi-lo switches |
| `HH`, `H`, `L`, `LL` (custom folders with Value+SP, **not** typed as Digital/Analog) | **Inconsistent** — should be `_Root/Digital` (+ optional SP as Analog or Float4 sibling) like Compressor pattern, or keep Value+SP but type Value as Digital |
| `_Alarms` | Keep |
| — | **Missing:** `SummaryInstances` |
| — | **Missing:** pressure `PT` analog if recirculator |
| — | **Missing:** commands for makeup outlet / resequence (`RESEQUENCE`, `Reseq_Now`) where applicable |
| — | **Missing:** Interlock / COMP_INTERLOCK if used on recirculators |
| — | Level HiHi/LoLo alarm enable config from `P_AIn` if LT is PlantPAx |

### Recommended `_Root` + states / engUnits

| Member | Base | States / engUnit |
|--------|------|------------------|
| `Status` | Multistate | Suggest: `0=OK, 1=LOW, 2=HIGH, 3=LOLO, 4=HIHI, 5=FAULT` **or** leave neutral `READY/ALARM` and rely on HH/H/L/LL bits + STS |
| `Level` | Analog | engUnit `%` (or `in` if using `INCHES`); instance `SP` ← `LEVEL_SP` |
| `LSH`/`LSL` | Digital | — |
| `HH`/`H`/`L`/`LL` | Digital Value + Float4 `SP` | engUnit `%` on SP |
| Optional `Pressure` | Analog | engUnit `psi` / `psig` |

**Instances:** `Tanks/*` (LTR, etc.) — memory stubs with Level/%.

---

## 4. Sensor / `P_AIn` / `P_DIn`

### PLC type name(s)

| Kind | PLC type |
|------|----------|
| Analog transmitter | **`P_AIn`** (192 leaves) |
| Discrete input | **`P_DIn`** (58 leaves) |
| Optional | Channel object via `Cfg_HasChanObj`; limits via `OSet_*Lim` / `PSet_*Lim` |

### Key PLC members — `P_AIn`

| Bucket | Members |
|--------|---------|
| **PV** | **`Val`** (EU after subst), `Val_InpPV`, `Inp_PV`, `Set_SimPV`, `MSet_SubstPV` |
| **Quality** | `Inp_PVBad`, `Inp_PVUncertain`, `Sts_PVBad`, `Sts_PVUncertain`, `SrcQ` |
| **Status bits** | `Sts_HiHi`, `Sts_Hi`, `Sts_Lo`, `Sts_LoLo`, `Sts_Fail`, `Sts_Err`, `Sts_Maint`, `Sts_SubstPV`, `Sts_InpPV` |
| **Alarms** | `Alm_HiHi`, `Alm_Hi`, `Alm_Lo`, `Alm_LoLo`, `Alm_Fail` |
| **Limits (live)** | `Val_HiHiLim`, `Val_HiLim`, `Val_LoLim`, `Val_LoLoLim` |
| **Limits (set)** | `OSet_HiHiLim`…`OSet_LoLoLim`, `PSet_*`, `Cfg_PVEUMax`/`Min`, `Cfg_FailHiLim`/`LoLim`, `Cfg_FiltTC` |
| **Commands** | `OCmd_Reset`, `OCmd_ResetAckAll`, `OCmd_ClearCapt`, subst PV MCmds |
| **Fault enum** | `Val_Fault`: 20=Lo, 21=Hi, 24=LoLo, 25=HiHi, 32=Fail, 34=CfgErr |

### Key PLC members — `P_DIn`

| Bucket | Members |
|--------|---------|
| **PV** | `Inp_PV`, `Sts_PV`, `Sts` / `Val_Sts` (0=PV Good, 6=PV Bad, 7=Subst) |
| **Target** | `Inp_Target`, `Sts_TgtDisagree`, `Alm_TgtDisagree` |
| **Commands** | `OCmd_Reset`, `MCmd_InpPV` / `MCmd_SubstPV`, `MSet_SubstPV` |

### Devices/Sensor — has vs missing

| Has today | Gap |
|-----------|-----|
| `Value` (**raw Float4**, not `_Root/Analog`) | **Should be** `_Root/Analog` named `Value` or `PV` for engUnit/history/SP parity |
| `Status` (Multistate) | Map from `Val_Fault` or Hi/Lo/Fail aggregate |
| `_Alarms` | Keep |
| — | **Missing:** HiHi/Hi/Lo/LoLo digitals + limit SPs (Tank-like or nested `Limits/`) |
| — | **Missing:** `Fail` / quality Digital |
| — | **Missing:** subst PV / reset cmds for Config/Controls |
| — | **Missing:** `SummaryInstances` |
| — | No discrete Sensor variant — either paramize Sensor or add `Devices/DigitalSensor` later |

### Recommended `_Root` + states / engUnits

| Member | Base | States / engUnit |
|--------|------|------------------|
| `Value` (PV) | **Analog** (migrate off bare Float4) | engUnit per instance (`psig`, `°F`, `%`, …); optional `SP` only if sensor has operator SP |
| `Status` | Multistate | `0=OK, 1=HI, 2=LO, 3=HIHI, 4=LOLO, 5=FAIL, 6=BAD` (align with `Val_Fault` where possible) |
| `HiHi`/`Hi`/`Lo`/`LoLo`/`Fail` | Digital | — |
| Limit SPs | Float4 or Analog.SP | Same engUnit as PV |
| Discrete path | Digital for PV; Multistate Status | engUnit N/A |

**Instances:** `Sensors/*` (e.g. LSS-PT, engUnit `psig`).

---

## 5. ExhaustFan

### PLC type name(s)

| Primary | Alternate |
|---------|-----------|
| **`P_Motor`** (same as Pump) | `P_DOut` if fan is simple discrete; VFD fans may resemble `Devices/VFD` |

Plant has no dedicated ExhaustFan PLC UDT — treat as **motor** (or DO) with airflow KPI.

### Key members

Same Control/Status/Mode/Interlock/Runtime set as **Pump / `P_Motor`**.  
KPI differs: airflow (`cfm`) instead of `gpm`.

### Devices/ExhaustFan — has vs missing

| Has today | Gap |
|-----------|-----|
| Same shallow shape as Pump: `Status`, `Temp` (engUnit **cfm**), `SummaryInstances`, `_Alarms` | Identical gaps to Pump (cmds, modes, interlocks, runtime, fault digitals) |
| `Temp` name | Rename to `Flow` / `Airflow` (keep engUnit `cfm`) |

### Recommended `_Root` + states / engUnits

Same as Pump:

| Member | Base | engUnit / states |
|--------|------|------------------|
| `Status` | Multistate | `Val_Sts` motor enum → `STOPPED/RUNNING/…` |
| `Airflow` (ex-`Temp`) | Analog | `cfm` + optional `SP` |
| Cmds / modes / Interlock / Runtime | Boolean / folder | Mirror Pump & Compressor |

**Instances:** `ExhaustFans/*` (EFAN-*), OPC to Sim.

---

## 6. Evaporator / `CG_RL_Evap`

### PLC type name(s)

| Primary | Related |
|---------|---------|
| **`CG_RL_Evap`** (96 leaves) | Control-group evaporator sequencer |
| **`Control_Group_DIO`** | Parallel/legacy DIO group: defrost TOD, ZAT, fans, timers |
| Fans | Often `Devices/VFD` children or discrete outs — not full `P_Motor` in Devices today |

### Key `CG_RL_Evap` members

| Bucket | Members |
|--------|---------|
| **Status / phase** | **`Sts_State`**: 0=Off, 1=Pump Out, 2=Soft Hot Gas, 3=Main Hot Gas, 4=Bleed, 5=Fan Delay, 6=Cooling, 7=Idle, 8=Cleanup, 9=Permissive, 10=Interlock |
| **Enable / off** | `HMIEnable`, `Off`, `IntlkOK`, `PermOK`, `Last_State` |
| **Defrost cmds** | `HMIStartDefrost`, `HMIStopDefrost`, `StartDefrost`, `StopDefrost`, `Cleanup` |
| **ZAT / KPIs** | `Cfg_ZoneAirTemp`, `Cfg_ZoneAirTempDB`, `ZAT_High`/`Low`/`HiHi`/`LoLo`, `ZAT_MaxSet`/`MinSet`, `TooHot`, `TooCold` |
| **Defrost config** | `Cfg_DefrostStartMode`, `Cfg_DefrostStopMode`, `Cfg_Def1stTOD`…`Cfg_Def4thTOD`, `Cfg_PumpOut`, `Cfg_SoftHotGas`, `Cfg_MainHotGas`, `Cfg_Bleed`, `Cfg_FanDelay`, `Cfg_CoolingTime`, `Cfg_RunTime`, `Cfg_CycFans`, valve flags |
| **Timers / vals** | `Val_TimeLeft`, `Val_CoolingTime`, `Val_RunTime`, `Tmr_*` |
| **AI/DI defrost** | `AIDefrostStart/Stop`, `DIDefrostStart/Stop`, `Cfg_AIDefrostStart`, `Cfg_AIStop` |

`Control_Group_DIO` adds: `Status`, `ZAT_Target`, `Superheat`/`Superheat_Set`, `BEGIN_DEFROST`, `DEFROST_NOW`, `STOP_DEF`, `HAS_VFD`, fan cycle, heat enable, etc.

### Devices/Evaporator — has vs missing

| Has today | Gap |
|-----------|-----|
| `Fan 1..3` (`Devices/VFD`: CMD, Fault, SPD_FBK) | OK for overview; expand VFD or add motor cmds if Controls need more |
| `Pressure` (Analog, `psi`) | Keep; optional SP |
| `Temp` (Analog, `°F`) | Map to ZAT; ensure `SP` ← `Cfg_ZoneAirTemp` / `ZAT_High` |
| `Status` (Multistate) | Demo StatusIndicator uses **simplified** 0=STOP,1=CLG,2=DFT,3=FLT,5=IDLE — **not** full `Sts_State` 0–10. Decide: keep HMI enum + map from PLC, or adopt PLC phases |
| `SummaryInstances`, `_Alarms` | Keep |
| — | **Missing Controls:** Enable, Start/Stop Defrost, Cleanup |
| — | **Missing Config:** defrost mode, TOD slots, step times, cycle-fans, DB |
| — | **Missing:** `TooHot`/`TooCold`, `IntlkOK`/`PermOK`, `Val_TimeLeft`, `Off` |
| — | **Missing:** Interlock folder / permissive display |
| — | **Missing:** Superheat KPI if using Control_Group_DIO |

### Recommended `_Root` + states / engUnits

| Member | Base | States / engUnit |
|--------|------|------------------|
| `Status` | Multistate | **Option A (PLC-faithful):** `Sts_State` 0–10 → STS `OFF`, `PUMPOUT`, `SHG`, `MHG`, `BLEED`, `FANDELAY`, `COOLING`, `IDLE`, `CLEANUP`, `PERM`, `INTLK`. **Option B (current HMI):** keep simplified demo map; document PLC→HMI mapping table in faceplate |
| `Temp` (ZAT) | Analog | `°F` + `SP` |
| `Pressure` | Analog | `psi` |
| `TimeLeft` | Analog | `min` |
| `HMIEnable`, defrost cmds, TooHot/TooCold | Digital/Boolean | — |
| Fan SPD_FBK | Analog (via VFD) | typically `%` or `Hz` — set per instance |

**Instances:** `Evaporators/EV-*` (18) — Fans + Pressure/Temp/Status on Sim OPC.

---

## 7. Compressor (reference only — already expanded)

| PLC | Devices coverage |
|-----|------------------|
| `Screw_Compressor` | Strong overlap: DisP, Amps, FLA, SVP, modes, Alm/Cutout/Failed/Started/Comm, AutoEN, runtime, Interlock |
| `QHD_CompData/Read/Write` | Comms plumbing — not all mirrored in Devices (OK) |
| `Comp_Sequence` | System sequencer — not per-compressor Devices type |

**Still optional later:** OilP/OilT/SepT/DisT/DisH, KW, RPM, Load_Setpoint, Anti-recycle, Seq bits — only if Controls/Config tabs need them.

---

## 8. Cross-cutting recommendations

### 8.1 Priority order for Devices UDT edits

1. **Pump** + **ExhaustFan** (clone motor Controls/Interlock from Compressor; rename KPI)
2. **Valve** (`P_ValveSO` Open/Close + stalls + Interlock; remove bogus Temp)
3. **Sensor** (promote PV to `_Root/Analog`; add limit digitals/SPs from `P_AIn`)
4. **Tank** (normalize HH/H/L/LL typing; Level SP; optional Recirculator extras)
5. **Evaporator** (defrost/ZAT/enable from `CG_RL_Evap`; resolve Status enum strategy)
6. Touch **CoolingTower** / **VFD** only if faceplate sweep includes them (CONTEXT deliverable mentions CT optionally)

### 8.2 Standard folders to add (all actuated devices)

Copy from `Devices/Compressor`:

```
Status          _Root/Multistate
…KPIs…          _Root/Analog (+ instance SP)
…flags…         _Root/Digital or Boolean
Cmd_*           Boolean
OPER/MAINT/PROG Boolean
Interlock/      P_Intlk-shaped folder (+ Cfg_CondTxt* HMI strings)
SummaryInstances _Root/Expression
_Alarms         Config/_Alarms
```

### 8.3 What stays PLC-only (do not dump entire AOI)

- Full `Cfg_*Severity`, shelve/suppress/ack matrices, `Err_*`, `Nrdy_*` detail bits — expose only what Config/Interlocks tabs need
- Raw `PCmd_*` program commands — HMI uses `OCmd_*` / BH `Cmd_*`
- `EnableIn`/`EnableOut`, `ZZZZ*` padding tags

### 8.4 Sim / instance follow-up

After type updates, refresh:

- `tag-definition/default/{Pumps,Valves,…}` overrides (engUnits, SP defaults)
- `sim/bh-plant-sim.csv` paths for new leaves
- Faceplate Controls bindings per device family

### 8.5 Mapping cheat-sheet

| Devices type | Primary PLC UDT(s) | Status source | Primary KPI |
|--------------|-------------------|---------------|-------------|
| Pump | `P_Motor` | `Val_Sts` | Flow `gpm` |
| ExhaustFan | `P_Motor` | `Val_Sts` | Airflow `cfm` |
| Valve | `P_ValveSO` | `Val_Sts` | (none / LS only) |
| Tank | `Recirculator` / `Accumulator` / `MakeUp_Water` + `P_AIn` | derived or vessel enum | Level `%` |
| Sensor | `P_AIn` / `P_DIn` | `Val_Fault` / quality | `Val` (+ engUnit) |
| Evaporator | `CG_RL_Evap` (+ `Control_Group_DIO`) | `Sts_State` (or HMI map) | Temp °F, Pressure psi |
| Compressor | `Screw_Compressor` | plant Status enum | DisP, Amps, FLA, SVP |

---

## 9. Open decisions (for implementers)

1. **Evaporator Status:** adopt full `Sts_State` 0–10 vs keep simplified StatusIndicator enum (requires explicit PLC→HMI map).
2. **Pump/EFAN KPI name:** rename `Temp` → `Flow`/`Airflow` (breaking for existing bindings — update Overview/AnalogValue paths).
3. **Valve `Temp`:** delete vs repurpose — recommend **delete**.
4. **Sensor shape:** single UDT with analog+optional discrete members vs two types.
5. **Interlock text:** keep HMI-only `Cfg_CondTxt00–15` (not in `P_Intlk` PLC UDT) — populate from plant docs/CSV.
6. **Mode UX:** raw bools (`OPER`/`MAINT`/`PROG`) like Compressor vs nested `P_Mode` `Val` enum.

---

*Generated for quick `260730-mun` device UDT + faceplate controls sweep.*
