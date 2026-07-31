# AUDIT — Devices UDT standalone memory vs `_Root/*` bases

**Quick id:** `260730-mun`  
**Date:** 2026-07-31  
**Scope:** `tag-type-definition/default/Devices/udts.json` members for Pump, ExhaustFan, Valve, Tank, Sensor, Evaporator, CoolingTower, Compressor  
**References:** `_Root/{Analog,Digital,Multistate,Expression,Document}`, Compressor as golden pattern, `RESEARCH-plc-devices-map.md`  
**Mode:** Audit only — no fixes applied

---

## 1. Verdict

Process **status / PV / alarm-bit** members across the eight Devices types are largely already on `_Root/*`. The remaining standalone `AtomicTag` + `valueSource=memory` leaves fall into three buckets:

| Bucket | Action | Count (unique UDT members) |
|--------|--------|----------------------------|
| **A — Convert to `_Root`** | KPI / config analogs (and Sensor alarm limits) that should be Analog folders | **24** across types (Compressor shares the KPI pattern) |
| **B — Keep AtomicTag (golden)** | One-shot `Cmd_*`, mode bits `OPER`/`MAINT`/`PROG`, and similar raw bools | Intentional; matches Compressor + RESEARCH §0.4 |
| **C — Ignore (scoped out)** | `Interlock/` folder atomics, `SummaryInstances` (`_Root/Expression`), `_Alarms` when correctly `Config/_Alarms` | Not conversion targets |

**Highest-risk instance defect (not a UDT shape gap):** most non-Compressor device instances serialize `_Alarms` as `tagType: AtomicTag` with `typeId: Config/_Alarms` (malformed). Compressors correctly use `UdtInstance`. Sensor instances also hardcode limit leaves as flat memory floats, amplifying the UDT defect.

---

## 2. Golden pattern — `Devices/Compressor`

### 2.1 Correct `_Root` usage (15)

| Member | `_Root` base | Notes / suggested states or engUnit |
|--------|--------------|-------------------------------------|
| `Status` | Multistate | Off=0, Run=1, Fault=2, Manual=3, Idle=4 |
| `DisP`, `Amps`, `FLA`, `SVP` | Analog | `psi`, `A`, (FLA/SVP per override); `SP` allowed as **child override** under Analog instance — do **not** put `SP` on `_Root/Analog` type |
| `CP_Mode`, `SV_Mode`, `Rung`, `Color` | Multistate | Mode / visual enums |
| `Alm`, `Cutout`, `Failed`, `Started`, `Comm` | Digital | Off=0, On=1 |
| `SummaryInstances` | Expression | Overview wiring |

### 2.2 Intentional standalone Boolean memory (keep)

| Member | Shape | Rationale |
|--------|-------|-----------|
| `OPER`, `MAINT`, `PROG` | AtomicTag Boolean memory | Mode ownership bits — faceplates bind raw bools |
| `Cmd_Start`, `Cmd_Stop`, `Cmd_Auto`, `Cmd_Manual`, `Cmd_Remote` | AtomicTag Boolean memory | One-shot operator commands (RESEARCH §0.4) |
| `AutoEN` | AtomicTag Boolean memory | Enable latch; same pattern as cmds |

### 2.3 Convert candidates on Compressor itself (KPI / timers)

These are **still** standalone memory on the golden type. Promote for consistency with AnalogValue / historian / faceplate Analog bindings — or explicitly document as “config scalar exception.”

| Member | Current | Required `_Root` | Suggested engUnit / notes |
|--------|---------|------------------|---------------------------|
| `RuntimeHours` | AtomicTag Float4 memory | **Analog** | `h` |
| `MotorStarts` | AtomicTag Int4 memory | **Analog** (count) | engUnit blank or `starts`; **not** Multistate |
| `MaxRunTimePerStart` | AtomicTag Float4 memory | **Analog** | `h` |
| `Min_Runtime_Set` | AtomicTag Float4 memory | **Analog** | `s` |
| `Fail_Timer_PRE` | AtomicTag Float4 memory | **Analog** | `s` |

### 2.4 Also present (ignored per scope)

- `Interlock/` — Folder of ~40 AtomicTags mirroring `P_Intlk` (Sts_*, Cfg_*, OCmd_Reset, …). Same on Pump / ExhaustFan / Valve / Evaporator / CoolingTower.
- `_Alarms` — `UdtInstance` `Config/_Alarms` on the type definition.

---

## 3. Classification rules used

**Flag as convert** when a top-level (or non-Interlock) member is `AtomicTag` with memory/opc/expr and **no** `typeId` `_Root/...`, and it is a process/config **Float4 / Int4 / Boolean status** that faceplates or AnalogValue would bind as a folder.

**Do not convert** (Bucket B):

- Names matching `Cmd_*`
- Exact: `OPER`, `MAINT`, `PROG`, `AutoEN`, `HMIEnable`, `Cleanup` (raw HMI/cmd bits)

**Ignore:**

- Folder containers named `Interlock` / `Interlocks` (and their children)
- `_Alarms` when the **type** uses `Config/_Alarms` (still report **instance** malformations)
- `SummaryInstances` already `_Root/Expression`
- Nested `Value` / `SP` / `Metadata` overrides **under** an existing `_Root/*` UdtInstance (expected)

---

## 4. Per-type findings

### 4.1 Pump — `Devices/Pump`

**Already `_Root` (7):** `Status` (Multistate), `Flow` (Analog `gpm` + SP child), `Alm`/`Failed`/`Started`/`Comm` (Digital), `SummaryInstances` (Expression).

**Status states:** UNK=0, STOPPED=1, RUNNING=2, STOPPING=7, STARTING=8, DISABLED=33.

| Member | Current shape | Required `_Root` | Suggested states / engUnit |
|--------|---------------|------------------|----------------------------|
| `RuntimeHours` | AtomicTag Float4 memory | Analog | `h` |
| `MotorStarts` | AtomicTag Int4 memory | Analog | count (no enum) |
| `Fail_Timer_PRE` | AtomicTag Float4 memory | Analog | `s` |

**Keep AtomicTag:** `OPER`/`MAINT`/`PROG`, `Cmd_Start`/`Stop`/`Auto`/`Manual`/`Reset`, `AutoEN`.

**Other:** `_Alarms` → `Config/_Alarms` (OK on type). `Interlock/` present (~40 atomics).

---

### 4.2 ExhaustFan — `Devices/ExhaustFan`

**Already `_Root` (7):** `Status` (Multistate), `Airflow` (Analog `cfm`), `Alm`/`Failed`/`Started`/`Comm` (Digital), `SummaryInstances`.

**Status states:** same P_Motor map as Pump.

| Member | Current shape | Required `_Root` | Suggested states / engUnit |
|--------|---------------|------------------|----------------------------|
| `RuntimeHours` | AtomicTag Float4 memory | Analog | `h` |
| `MotorStarts` | AtomicTag Int4 memory | Analog | count |
| `Fail_Timer_PRE` | AtomicTag Float4 memory | Analog | `s` |

**Keep AtomicTag:** `OPER`/`MAINT`/`PROG`, `Cmd_Start`/`Stop`/`Auto`/`Manual`/`Reset`, `AutoEN`.

**Other:** `_Alarms` OK on type; `Interlock/` present.

---

### 4.3 Valve — `Devices/Valve`

**Already `_Root` (7):** `Status` (Multistate), `OpenLS`/`ClosedLS`/`Failed`/`Comm` (Digital), `TravelTime` (Analog `s`), `SummaryInstances`.

**Status states:** UNK=0, CLOSED=1, OPEN=2, CLOSING=5, OPENING=6, DISABLED=33.

| Member | Current shape | Required `_Root` | Suggested states / engUnit |
|--------|---------------|------------------|----------------------------|
| — | — | **None** | No Bucket-A convert candidates |

**Keep AtomicTag:** `OPER`/`MAINT`/`PROG`, `Cmd_Open`/`Close`/`Reset`.

**Other:** `_Alarms` OK on type; `Interlock/` present. Cleanest type after Tank for `_Root` process leaves.

---

### 4.4 Tank — `Devices/Tank`

**Already `_Root` (10):** `Status` (Multistate), `Level` (Analog `%`), `Pressure` (Analog `psig`), `LSH`/`LSL`/`HH`/`H`/`L`/`LL` (Digital), `SummaryInstances`.

**Status states:** OK=0, LOW=1, HIGH=2, LOLO=3, HIHI=4, FAULT=5.

| Member | Current shape | Required `_Root` | Suggested states / engUnit |
|--------|---------------|------------------|----------------------------|
| — | — | **None** | No standalone process memory leaves outside Interlock/`_Alarms` |

**Other:** `_Alarms` OK on type; small `Interlock/` (~7 atomics). **Best `_Root` compliance** of the eight.

---

### 4.5 Sensor — `Devices/Sensor`

**Already `_Root` (8):** `Value` (Analog), `Status` (Multistate), `HiHi`/`Hi`/`Lo`/`LoLo`/`Fail` (Digital), `SummaryInstances`.

**Status states:** OK=0, HI=1, LO=2, HIHI=3, LOLO=4, FAIL=5, BAD=6.

| Member | Current shape | Required `_Root` | Suggested states / engUnit |
|--------|---------------|------------------|----------------------------|
| `HiHiLim` | AtomicTag Float4 memory | **Analog** | Match PV engUnit (`psig` / `°F` per instance) |
| `HiLim` | AtomicTag Float4 memory | **Analog** | same |
| `LoLim` | AtomicTag Float4 memory | **Analog** | same |
| `LoLoLim` | AtomicTag Float4 memory | **Analog** | same |

**Keep AtomicTag:** `Cmd_Reset` (one-shot).

**Note:** Limits are operator-facing setpoints; promoting to `_Root/Analog` enables consistent AnalogValue / SP-style UX. Alternate (weaker) option: nest under a `Config/` folder as documented scalars — still better than orphan top-level floats if faceplates expect `/Value`.

**Default type engUnit on `Value`:** `psig` (instances override, e.g. OIL-TT → `°F`).

---

### 4.6 Evaporator — `Devices/Evaporator`

**Already `_Root` (10):** `Pressure` (Analog `psi`), `Status` (Multistate), `Temp` (Analog `°F`), `TooHot`/`TooCold`/`IntlkOK`/`PermOK`/`Off` (Digital), `TimeLeft` (Analog `min`), `SummaryInstances`.

**Status states:** Off=0, Cooling=1, Defrost=2, Fault=3, Manual=4, Idle=5, 1.PD=6, 2.HG=7, 3.BLD=8, 3.FD=9.

| Member | Current shape | Required `_Root` | Suggested states / engUnit |
|--------|---------------|------------------|----------------------------|
| `Cfg_PumpOut` | AtomicTag Float4 memory | Analog | `min` |
| `Cfg_SoftHotGas` | AtomicTag Float4 memory | Analog | `min` |
| `Cfg_MainHotGas` | AtomicTag Float4 memory | Analog | `min` |
| `Cfg_Bleed` | AtomicTag Float4 memory | Analog | `min` |
| `Cfg_FanDelay` | AtomicTag Float4 memory | Analog | `min` |
| `Cfg_CoolingTime` | AtomicTag Float4 memory | Analog | `min` |
| `Cfg_ZoneAirTempDB` | AtomicTag Float4 memory | Analog | `°F` |

**Keep AtomicTag:** `HMIEnable`, `Cmd_StartDefrost`, `Cmd_StopDefrost`, `Cleanup`.

**Non-`_Root` UdtInstances (OK / nested devices):**

| Member | typeId | Notes |
|--------|--------|-------|
| `Fan 1`, `Fan 2`, `Fan 3` | `Devices/VFD` | Nested device; VFD itself uses `_Root/Digital`+`Analog` |
| `_Alarms` | `Config/_Alarms` | Correct on **type** |

**Other:** `Interlock/` present (~40).

---

### 4.7 CoolingTower — `Devices/CoolingTower`

**Already `_Root` (7):** `Status` (Multistate), `Temp` (Analog `°F`), `SPD_FBK` (Analog `Hz`), `Failed`/`Alm`/`Comm` (Digital), `SummaryInstances`.

**Status states:** Off=0, Run=1, Fault=2, Manual=3, Idle=4 (Compressor-like).

| Member | Current shape | Required `_Root` | Suggested states / engUnit |
|--------|---------------|------------------|----------------------------|
| `RuntimeHours` | AtomicTag Float4 memory | Analog | `h` |
| `MotorStarts` | AtomicTag Int4 memory | Analog | count |

**Keep AtomicTag:** `OPER`/`MAINT`/`PROG`, `Cmd_Start`/`Stop`/`Auto`/`Manual`.

**Gap vs Pump/Compressor (informational):** no `Fail_Timer_PRE` / `AutoEN` / `Started` on type yet — not a standalone-memory defect, but incomplete vs motor golden set.

**Other:** `_Alarms` OK on type; `Interlock/` present.

---

### 4.8 Compressor — see §2

Listed again only for completeness: **5** Bucket-A KPI/timers + intentional cmds + full `_Root` process set.

---

## 5. Summary matrix — Bucket A (convert)

| Type | Members to promote → `_Root/Analog` |
|------|-------------------------------------|
| Compressor | `RuntimeHours`, `MotorStarts`, `MaxRunTimePerStart`, `Min_Runtime_Set`, `Fail_Timer_PRE` |
| Pump | `RuntimeHours`, `MotorStarts`, `Fail_Timer_PRE` |
| ExhaustFan | `RuntimeHours`, `MotorStarts`, `Fail_Timer_PRE` |
| CoolingTower | `RuntimeHours`, `MotorStarts` |
| Sensor | `HiHiLim`, `HiLim`, `LoLim`, `LoLoLim` |
| Evaporator | `Cfg_PumpOut`, `Cfg_SoftHotGas`, `Cfg_MainHotGas`, `Cfg_Bleed`, `Cfg_FanDelay`, `Cfg_CoolingTime`, `Cfg_ZoneAirTempDB` |
| Valve | _(none)_ |
| Tank | _(none)_ |

**No Bucket-A Boolean/Int4 leaves were found that should become `_Root/Digital` or `_Root/Multistate`** outside the intentional cmd/mode set — process digitals and status enums are already `_Root` on these types.

---

## 6. Instance overrides conflicting with UDT / `_Root` pattern

Source: `tag-definition/default/{Pumps,ExhaustFans,Valves,Tanks,Sensors,Evaporators,CoolingTowers,Compressors}/udts.json`.

### 6.1 Malformed `_Alarms` (AtomicTag + typeId)

UDT expects `tagType: UdtInstance`, `typeId: Config/_Alarms`.  
Several families **override** with `tagType: AtomicTag`, `typeId: Config/_Alarms`, nested `_Active` / `_ActiveHighPriority` memory children.

| Folder | Instances affected | Shape |
|--------|-------------------|-------|
| Pumps | PMP-01..04 (all 4) | AtomicTag + Config/_Alarms |
| ExhaustFans | EFAN-01..04 (all 4) | AtomicTag + Config/_Alarms |
| CoolingTowers | CT-01..04 (all 4) | AtomicTag + Config/_Alarms |
| Evaporators | EV-* (17) | AtomicTag + Config/_Alarms |
| Tanks | LTR, HPR, HTR (3 of 7) | AtomicTag + Config/_Alarms |
| Compressors | COMP-01..05 | **Correct** UdtInstance |
| Valves | — | No `_Alarms` override spotted |
| Sensors | — | No `_Alarms` on instances |

**Fix direction (later):** rewrite overrides to `tagType: UdtInstance` matching Compressor instances (or delete override and inherit type).

### 6.2 Hardcoded memory leaves that amplify UDT Bucket-A defects

| Folder | Instance(s) | Paths | Conflict |
|--------|-------------|-------|----------|
| Sensors | LSS-PT, HSS-PT, HPR-PT, OIL-TT (all 4) | `HiHiLim`, `HiLim`, `LoLim`, `LoLoLim` | Flat AtomicTag Float4 memory (+ engUnit). After UDT promote to Analog, these must become `UdtInstance` with nested `Value` (and engUnit on Value). |
| Pumps | PMP-01 | `RuntimeHours`, `MotorStarts` | Memory AtomicTag overrides matching UDT standalone shape |
| ExhaustFans | EFAN-01 | `RuntimeHours`, `MotorStarts` | Same |

OPC `Value` overrides under existing `_Root` members (e.g. PMP-02 `Status/Value`, `Flow/Value`) are **normal** and not defects.

### 6.3 Nested / other

- Evaporator `Fan 1..3` → `Devices/VFD`: intentional nested UDT (VFD already `_Root`-based).
- Overview instances (`Overview/Pump Overview`, etc.) use Expression aggregates — out of Devices UDT scope.

---

## 7. `_Root` base cheat-sheet (for the fix pass)

| Leaf kind | Use | Typical metadata |
|-----------|-----|------------------|
| Enum / status int | `_Root/Multistate` | `metadata.states` on `Value` override |
| Bool status / alarm bit | `_Root/Digital` | Off=0, On=1 |
| Process / KPI / limit / timer float|int | `_Root/Analog` | `engUnit`, format, optional `SP` **child** |
| Overview rollup | `_Root/Expression` | `SummaryInstances` |
| One-shot HMI command | **AtomicTag Boolean memory** | Keep Compressor style |
| Interlock AOI mirror | Folder of AtomicTags | Keep; do not explode into `_Root` per bit unless faceplate needs it |

---

## 8. Recommended fix order (do not execute in this audit)

1. Promote Bucket-A members on **Devices** UDTs (start with Sensor limits + shared motor KPIs; align Compressor KPIs so Pump/ExhaustFan/CoolingTower stay in lockstep).
2. Repair instance `_Alarms` `AtomicTag` → `UdtInstance` for Pumps, ExhaustFans, CoolingTowers, Evaporators, Tanks.
3. Rewrite Sensor (and PMP-01 / EFAN-01 KPI) instance overrides to nested `_Root/Analog` `Value` shapes; preserve engUnits (`psig` / `°F` / `h`).
4. Re-run signature repair + project scan; smoke faceplate Controls bindings that assume `/Value`.

---

## 9. Sources / tooling

- `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json`
- `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/_Root/udts.json`
- `gateways/standard/data/config/resources/core/ignition/tag-definition/default/*/udts.json`
- Working scan outputs: `_audit_root_bases.py`, `_audit_root_bases_v2.py`, `*_audit_root_bases*.json` (same quick folder)
