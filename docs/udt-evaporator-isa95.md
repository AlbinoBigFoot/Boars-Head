# Evaporator Equipment Class — ISA-95 Draft

Reference sources:
- `Refrigeration MCC IPs.xlsx` — AU# evaporators on PowerFlex 525 (e.g. `AU#501-E1` @ `10.80.31.107`)
- Tracker ID 28 (UDT / hierarchy), ID 11 (relabel), ID 18/38 (timers / defrost)
- Process: pumped liquid NH3 overfeed (ID 46)

This is a **One Shot draft** for Ignition UDT + HMI faceplate alignment — not FBCO-approved P&ID truth.

---

## ISA-95 equipment hierarchy (proposed)

| Level | ISA-95 term | This plant (example) |
|------:|-------------|------------|
| 4 | Enterprise | BoarsHead / FBCO |
| 3 | Site | RCP |
| 2 | Area | REF (Refrigeration) |
| 1 | Process Cell | HT_LOOP (High-temp recirculator loop) |
| 0 | Unit | **EVAP_501** (Air unit / evaporator) |
| − | Equipment Module | FAN, DEFROST, TEMP_CTRL |
| − | Control Module | VFD, SOL_*, TT_*, SS_* |

### Path / tag folder (Ignition)

```
RCP/REF/HT_LOOP/EVAP_501/
  Meta/
  FAN/
  DEFROST/
  TEMP_CTRL/
  Alarms/
```

Legacy MCC name retained as attribute: `LegacyId = "AU#501-E1"`, `MccIp = "10.80.31.107"`.

---

## Equipment class: `Evaporator` (Unit)

Reusable UDT / UDT instance for each AU# evaporator.

### Meta (identity)

| Member | Type | Example | Notes |
|--------|------|---------|-------|
| `EquipmentId` | String | `EVAP_501` | ISA-95 Unit id |
| `Area` | String | `REF` | |
| `ProcessCell` | String | `HT_LOOP` | |
| `LegacyId` | String | `AU#501-E1` | From MCC sheet |
| `MccIp` | String | `10.80.31.107` | PowerFlex bucket |
| `InService` | Bool | true | Hide graphic if false (ID 11) |
| `Description` | String | `Cold storage air unit 501` | |

### FAN (Equipment Module)

| Member | Type | Notes |
|--------|------|-------|
| `Cmd` | Int / Enum | 0=Stop, 1=Run, 2=DefrostInterlock |
| `Mode` | Enum | Auto / Manual / Maint |
| `Running` | Bool | Feedback |
| `Fault` | Bool | VFD / starter fault |
| `SpeedFbk` | Float | % or RPM |
| `SpeedSp` | Float | Manual speed SP |
| `StartInhibit` | Bool | Timer / interlock active |
| `StartDelayRem` | Float | Seconds remaining (ID 18) |
| `StartDelaySp` | Float | TON seconds |
| `StopDelaySp` | Float | TOFF seconds |
| `StartBypass` | Bool | Want ID 14 — gated by role |

### TEMP_CTRL (Equipment Module)

| Member | Type | Notes |
|--------|------|-------|
| `RoomTemp` | Float | °F |
| `TempSp` | Float | °F |
| `Deadband` | Float | °F |
| `CoolingReq` | Bool | Demand to run fan / liquid |

### DEFROST (Equipment Module)

| Member | Type | Notes |
|--------|------|-------|
| `Active` | Bool | |
| `Mode` | Enum | Sched / Manual / Off |
| `Step` | String / Int | Sequence step |
| `NextDue` | DateTime / String | |
| `ManualReq` | Bool | Operator override request |

### Alarms (unit-level)

| Member | Type | Priority sketch |
|--------|------|-----------------|
| `Alm_VfdFault` | Alarm | High |
| `Alm_FanFailToStart` | Alarm | High |
| `Alm_TempHi` | Alarm | Medium |
| `Alm_TempLo` | Alarm | Medium |
| `Alm_DefrostOvertime` | Alarm | Medium |

---

## Instance map (from MCC inventory)

| EquipmentId | LegacyId | MccIp |
|-------------|----------|-------|
| EVAP_201 | AU#201-B1 | 10.80.31.104 |
| EVAP_301 | AU#301-C1 | 10.80.31.105 |
| EVAP_401 | AU#401-D1 | 10.80.31.106 |
| EVAP_501 | AU#501-E1 | 10.80.31.107 |
| EVAP_502 | AU#502-E2 | 10.80.31.108 |
| EVAP_503 | AU#503-E3 | 10.80.31.109 |
| EVAP_504 | AU#504-E4 | 10.80.31.110 |
| EVAP_601 | AU#601-F1 | 10.80.31.111 |
| EVAP_602 | AU#602-F2 | 10.80.31.112 |
| EVAP_603 | AU#603-F3 | 10.80.31.113 |
| EVAP_604 | AU#604-F4 | 10.80.31.114 |
| EVAP_701 | AU#701-G1 | 10.80.31.115 |
| EVAP_702 | AU#702-G2 | 10.80.31.116 |
| EVAP_703 | AU#703-G3 | 10.80.31.117 |
| EVAP_704 | AU#704-G4 | 10.80.31.118 |
| EVAP_705 | AU#705-G5 | 10.80.31.119 |

---

## HMI graphics

| Asset | Role |
|-------|------|
| **Overview symbol** (`Evaporator / Overview Symbol`) | Plant overview graphic (ISA-95 Unit). Operator **clicks** this to open the faceplate. Variants: Running / Stopped / Fault / Defrost. |
| **Faceplate** | Detail popup/panel for the selected unit (commands, modules, alarms). |

Figma: [BH Refrigeration — Evaporator Faceplate (ISA-95)](https://www.figma.com/design/Q8EmmXokQsiX91aPMtLm2w) (Drafts).
