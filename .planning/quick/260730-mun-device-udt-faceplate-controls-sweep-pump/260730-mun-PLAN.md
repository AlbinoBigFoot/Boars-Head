---
phase: 260730-mun-device-udt-faceplate-controls-sweep-pump
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json
  - gateways/standard/data/config/resources/core/ignition/tag-definition/default/Pumps/udts.json
  - gateways/standard/data/config/resources/core/ignition/tag-definition/default/ExhaustFans/udts.json
  - gateways/standard/data/config/resources/core/ignition/tag-definition/default/Valves/udts.json
  - gateways/standard/data/config/resources/core/ignition/tag-definition/default/Tanks/udts.json
  - gateways/standard/data/config/resources/core/ignition/tag-definition/default/Sensors/udts.json
  - gateways/standard/data/config/resources/core/ignition/tag-definition/default/Evaporators/udts.json
  - gateways/standard/data/config/resources/core/ignition/tag-definition/default/CoolingTowers/udts.json
  - sim/build_plant_sim.py
  - sim/bh-plant-sim.csv
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Valves/Overview/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Sensors/Overview/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Evaporators/Overview/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Faceplate/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Pump/Controls/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Valve/Controls/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Tank/Controls/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Sensor/Controls/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Evaporator/Controls/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/CoolingTower/Controls/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Pump/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/ExhaustFan/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/CoolingTower/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Evaporator/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Tank/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Sensor/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/SolenoidValve/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/SolenoidValve3Way/view.json
  - gateways/standard/data/projects/BH/ignition/script-python/shared/Alerts/code.py
  - scripts/pushover_nav_screenshots.py
  - docs/handoff/fp-controls-Compressor.png
  - docs/handoff/fp-controls-Pump.png
  - docs/handoff/fp-controls-Valve.png
  - docs/handoff/fp-controls-Tank.png
  - docs/handoff/fp-controls-Sensor.png
  - docs/handoff/fp-controls-ExhaustFan.png
  - docs/handoff/fp-controls-Evaporator.png
  - docs/handoff/fp-controls-CoolingTower.png
autonomous: true
requirements:
  - D-01
  - D-02
  - D-03
  - D-04
  - D-05
  - D-06
  - D-07
  - D-08
user_setup:
  - service: pushover
    why: "AFK proof — Controls-tab screenshots per device type"
    env_vars:
      - name: PUSHOVER_TOKEN
        source: "repo .env (gitignored)"
      - name: PUSHOVER_USER
        source: "repo .env (gitignored)"

must_haves:
  truths:
    - Web GUI button remains header-only and visible only when deviceType is Compressor with non-empty webGuiUrl (D-01 verify)
    - Devices UDTs for Pump, ExhaustFan, Valve, Tank, Sensor, Evaporator, CoolingTower expose Controls-grade leaves (Status Multistate + Mode/Cmd/KPI/Interlock as family warrants) on _Root bases with engUnits and bool/multistate metadata (D-02, D-08)
    - Plant sim covers new leaves for all families including Valves/Tanks/Sensors; Overview walls for Valves/Sensors use live instance tagPaths (D-03, D-04, D-06)
    - Unified Faceplate opens from every device graphic with correct deviceType; Controls tab embeds _Assets/{Device}/Controls Mode→Status/commands→KPI; empty Config/Interlocks tabs hide (D-05)
    - Pushover delivers Controls screenshots for Compressor, Pump, Valve, Tank, Sensor, ExhaustFan, Evaporator, CoolingTower (D-07)
  artifacts:
    - gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json
    - sim/build_plant_sim.py
    - sim/bh-plant-sim.csv
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Pump/Controls/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Valve/Controls/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Tank/Controls/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Sensor/Controls/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Evaporator/Controls/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/CoolingTower/Controls/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Faceplate/view.json
    - docs/handoff/fp-controls-Pump.png
  key_links:
    - Devices/{Type} members → sim/bh-plant-sim.csv paths → OPC [default]_Sim_/…
    - Faceplate hasControlsAsset + case(deviceType) → _Assets/{Device}/Controls
    - Device graphic click → shared.Alerts.showFaceplate(…, deviceType=…)
    - Overview tagPath → live UdtInstance (not SV-*/SNS-*)
    - repair-resource-signatures.py → scan/projects + scan/config
---

<objective>
Comprehensive Devices UDT + plant-sim + unified Faceplate Controls sweep for Pump, ExhaustFan, Valve, Tank, Sensor, Evaporator, CoolingTower (Compressor already deep — verify Web GUI only). Fix broken Valves/Sensors Overview walls; wire openFaceplate from all device clicks; deliver Pushover Controls screenshots per type.

Purpose: Operators get Mode→Status/commands→KPI Controls on every device family with Config/Interlocks when data exists, backed by demo sim — not live PLC OPC for every leaf.
Output: Expanded Devices UDTs + sim; per-device Controls assets; Faceplate/opener wiring; Overview fixes; Pushover PNGs.
</objective>

<execution_context>
@$HOME/.cursor/gsd-core/workflows/execute-plan.md
@$HOME/.cursor/gsd-core/templates/summary.md
</execution_context>

<context>
@.planning/quick/260730-mun-device-udt-faceplate-controls-sweep-pump/CONTEXT.md
@.planning/quick/260730-mun-device-udt-faceplate-controls-sweep-pump/RESEARCH-plc-devices-map.md
@.planning/quick/260730-mun-device-udt-faceplate-controls-sweep-pump/RESEARCH-sim-overviews.md
@.planning/quick/260730-mun-device-udt-faceplate-controls-sweep-pump/RESEARCH-faceplate-controls-ext.md
@.cursor/rules/perspective-reference.mdc
@.cursor/rules/perspective-css-only.mdc
@.cursor/rules/perspective-ticket-logger.mdc
@.cursor/rules/perspective-json-newlines.mdc
@.cursor/rules/ignition-resource-signatures.mdc
@.cursor/rules/ignition-8-3-scan-api.mdc

# Patterns to copy
@gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json
@gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Compressor/Controls/view.json
@gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Faceplate/view.json
@gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Compressor/view.json
@sim/build_plant_sim.py
@scripts/pushover_nav_screenshots.py
</context>

## Parallel execution map (up to 8 agents)

| Wave | Agents | Ownership rule |
|------|--------|----------------|
| **A** | A1–A6 (parallel) | Each agent owns **one family type block** in `Devices/udts.json` (StrReplace only that type’s JSON object) + that family’s `tag-definition/default/{Folder}/udts.json` + Overview tagPaths for that family. **Do not** regenerate full CSV yet — write/append family profile helpers in `build_plant_sim.py` behind clear `# --- {FAMILY} ---` markers. |
| **A-merge** | 1 agent (after A1–A6) | Own `sim/build_plant_sim.py` FOLDERS union + regenerate `sim/bh-plant-sim.csv`; fix any Overview walls still broken; optional EV-17 on Evaporators wall. |
| **B** | B1–B4 (parallel after A-merge) | B1–B3 create Controls views (no shared file overlap). **B4 alone** owns Faceplate shell + all device openers + thin wrappers/nav. |
| **C** | 1 agent (after B) | Playwright capture + `pushover_nav_screenshots.py` + Compressor Web GUI verify. |

**Shared-file protocol:** Never two agents edit the same path in the same wave. `Devices/udts.json` parallel OK only via whole-type-object StrReplace (Pump vs Valve etc.). If merge conflict, A-merge / B4 wins and re-applies.

**Discretion locks (implementers — do not reopen):**
- Evaporator `Status`: keep current HMI simplified enum; document PLC `Sts_State` 0–10 → HMI map in Controls comments/SUMMARY (research Option B).
- Pump `Temp` → rename `Flow` (engUnit `gpm`); ExhaustFan `Temp` → `Airflow` (`cfm`); update Overview/AnalogValue paths.
- Valve: **delete** bogus `Temp` (°F).
- Sensor: single UDT; promote PV to `_Root/Analog`; add Hi/Lo digitals + limit SPs.
- Mode UX: `OPER`/`MAINT`/`PROG` bools like Compressor (not nested P_Mode).
- `deviceType` strings: `Pump`, `ExhaustFan`, `Valve`, `Tank`, `Sensor`, `Evaporator`, `CoolingTower`, `Compressor`. SolenoidValve / SolenoidValve3Way openers pass `deviceType='Valve'`.
- Out of scope: live PLC OPC for every leaf; non-compressor Web GUI.

---

<tasks>

<!-- ========== WAVE A — UDT + instance prep (parallel) ========== -->

<task type="auto" wave="A" agent="A1">
  <name>A1: Devices/Pump + ExhaustFan UDT expand</name>
  <files>gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json, gateways/standard/data/config/resources/core/ignition/tag-definition/default/Pumps/udts.json, gateways/standard/data/config/resources/core/ignition/tag-definition/default/ExhaustFans/udts.json, sim/build_plant_sim.py</files>
  <read_first>
    - CONTEXT.md locked goals
    - RESEARCH-plc-devices-map.md §1 Pump, §5 ExhaustFan, §0 Compressor pattern, §8 folders
    - Devices/udts.json Compressor + Pump + ExhaustFan type blocks
    - sim/build_plant_sim.py COMP_FACEPLATE_DEFAULTS / Pumps profiles
  </read_first>
  <action>
  Per D-02 / D-08 and PLC map: expand **Devices/Pump** and **Devices/ExhaustFan** to Compressor-depth motor pattern (`P_Motor`).

  1. **Pump type:** Rename `Temp` → `Flow` (`_Root/Analog`, engUnit `gpm`). Keep `Status` Multistate; document Val_Sts states in metadata/shortDescription: 0=UNK, 1=STOPPED, 2=RUNNING, 7=STOPPING, 8=STARTING, 33=DISABLED. Add Boolean `OPER`/`MAINT`/`PROG`, `Cmd_Start`/`Cmd_Stop`/`Cmd_Auto`/`Cmd_Manual`/`Cmd_Reset`, digitals `Failed`/`Alm`/`Started`/`Comm` (`_Root/Digital` or Boolean matching Compressor), KPI `RuntimeHours` (engUnit `h`), `MotorStarts` (Int4), config writables `AutoEN`, `Fail_Timer_PRE`. Copy Compressor-shaped `Interlock/` folder (Sts_*, Cfg_Bypassable, OCmd_Reset, Rdy_Reset, Cfg_CondTxt00–15, MSet_Bypass00–15). Keep `SummaryInstances`, `_Alarms`.

  2. **ExhaustFan type:** Same as Pump but KPI rename `Temp` → `Airflow` (engUnit `cfm`). Do not share members incorrectly across types — duplicate the motor pattern into each type block.

  3. **Instances:** Pumps PMP-*, ExhaustFans EFAN-* inherit; fix any instance overrides still pointing at `/Temp` → `/Flow` or `/Airflow`. Seed demo mode/cmd defaults on *-01 if useful.

  4. **Sim helper only:** In `build_plant_sim.py` add/replace `# --- PUMP ---` and `# --- EXHAUSTFAN ---` profile blocks (Status wall + Controls defaults mirroring COMP_FACEPLATE_DEFAULTS subset). Do **not** change global FOLDERS or regenerate CSV (A-merge owns that).

  5. Do not touch Valve/Tank/Sensor/Evaporator/CoolingTower/Compressor type blocks except if a shared helper forces a read — leave them alone.
  </action>
  <verify>
    <automated>python -c "import json; from pathlib import Path
p=Path('gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json')
types={t['name']:t for t in json.loads(p.read_text(encoding='utf-8'))}
def names(t):
  s=set()
  def w(tags, pref=''):
    for x in tags or []:
      n=x.get('name',''); s.add(pref+n); w(x.get('tags'), pref+n+'/')
  w(t.get('tags')); return s
for typ, flow in [('Pump','Flow'),('ExhaustFan','Airflow')]:
  n=names(types[typ])
  for req in [flow,'Status','OPER','MAINT','PROG','Cmd_Start','Cmd_Stop','RuntimeHours','MotorStarts','Interlock','Interlock/Cfg_CondTxt00']:
    assert any(req==x or x.endswith('/'+req.split('/')[-1]) or req in x for x in n), (typ,req)
  assert 'Temp' not in n or flow in n
assert '# --- PUMP ---' in Path('sim/build_plant_sim.py').read_text(encoding='utf-8') or 'PUMP' in Path('sim/build_plant_sim.py').read_text(encoding='utf-8')
print('A1-ok')" </automated>
  </verify>
  <done>Pump and ExhaustFan Devices UDTs have motor Controls/Interlock leaves, renamed Flow/Airflow KPIs, and sim profile markers ready for A-merge.</done>
</task>

<task type="auto" wave="A" agent="A2">
  <name>A2: Devices/Valve UDT + Overview tagPaths</name>
  <files>gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json, gateways/standard/data/config/resources/core/ignition/tag-definition/default/Valves/udts.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Valves/Overview/view.json, sim/build_plant_sim.py</files>
  <read_first>
    - RESEARCH-plc-devices-map.md §2 Valve / P_ValveSO
    - RESEARCH-sim-overviews.md §2 Valves wall (SV-* broken), §1 real instances
    - Devices/Valve + Compressor Interlock pattern
  </read_first>
  <action>
  Per D-02 / D-04 / D-06:

  1. **Devices/Valve:** Delete bogus `Temp` (°F). Keep/fix `Status` Multistate for Val_Sts: CLOSED=1, OPEN=2, CLOSING=5, OPENING=6, DISABLED=33. Add `Cmd_Open`/`Cmd_Close`/`Cmd_Reset`, `OPER`/`MAINT`/`PROG`, digitals `OpenLS`/`ClosedLS`/`Failed`/`Comm`, optional Analog `TravelTime` (engUnit `s`), full `Interlock/` mirror, `SummaryInstances` if missing, keep `_Alarms`.

  2. **Instances:** Ensure HPRL-ISO, LTR-SV, MAIN-LIQ-SV, HTR-SV inherit new members (memory/sim OK).

  3. **Overview:** Retarget Valves Overview wall tagPaths from non-existent SV-*/SV3-* to the four live Valves instances (and SolenoidValve / SolenoidValve3Way components as appropriate). faceplate param may stay SolenoidValve* — openers in Wave B map to deviceType Valve.

  4. **Sim helper:** `# --- VALVE ---` profiles in build_plant_sim.py (Status Open/Closed/Fault demos + Cmd/Interlock defaults). No full CSV regen.
  </action>
  <verify>
    <automated>python -c "import json,re; from pathlib import Path
types={t['name']:t for t in json.loads(Path('gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json').read_text(encoding='utf-8'))}
def names(t):
  s=set()
  def w(tags,p=''):
    for x in tags or []:
      n=x.get('name',''); s.add(p+n); w(x.get('tags'),p+n+'/')
  w(t.get('tags')); return s
n=names(types['Valve'])
assert 'Temp' not in n
for req in ['Status','Cmd_Open','Cmd_Close','OPER','OpenLS','ClosedLS','Interlock']:
  assert any(req in x for x in n), req
ov=Path('gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Valves/Overview/view.json').read_text(encoding='utf-8')
assert 'SV-01' not in ov and 'SNS-' not in ov
assert any(x in ov for x in ['HPRL-ISO','LTR-SV','MAIN-LIQ-SV','HTR-SV'])
print('A2-ok')" </automated>
  </verify>
  <done>Valve UDT is P_ValveSO-shaped without Temp; Overview points at live valve instances; sim Valve profiles marked.</done>
</task>

<task type="auto" wave="A" agent="A3">
  <name>A3: Devices/Tank UDT expand</name>
  <files>gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json, gateways/standard/data/config/resources/core/ignition/tag-definition/default/Tanks/udts.json, sim/build_plant_sim.py</files>
  <read_first>
    - RESEARCH-plc-devices-map.md §3 Tank / Recirculator / Accumulator
    - Devices/Tank current HH/H/L/LL folders
  </read_first>
  <action>
  Per D-02 / D-08:

  1. Normalize `Level` as `_Root/Analog` engUnit `%` with optional instance `SP` child pattern (Compressor DisP style — SP on instance/member override, never on `_Root/Analog` type). Document Status Multistate: 0=OK, 1=LOW, 2=HIGH, 3=LOLO, 4=HIHI, 5=FAULT (or READY/ALARM + bits — pick one and set metadata consistently).

  2. Normalize HH/H/L/LL to `_Root/Digital` Values (+ Float4/Analog SP siblings with engUnit `%`) matching research. Keep LSH/LSL Digital.

  3. Add optional `Pressure` Analog (`psi`/`psig`), `SummaryInstances` if missing, lightweight Interlock folder when recirculator COMP_INTERLOCK-style demo useful (at least Sts_IntlkOK + CondTxt00–03 so Interlocks tab can appear on one tank). Add any makeup/reseq cmds only if leaves are clearly demoable.

  4. Instance folders Tanks/* inherit; seed LTR-01 demo Level/alarms.

  5. `# --- TANK ---` sim profiles in build_plant_sim.py. No CSV regen.
  </action>
  <verify>
    <automated>python -c "import json; from pathlib import Path
types={t['name']:t for t in json.loads(Path('gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json').read_text(encoding='utf-8'))}
def names(t):
  s=set()
  def w(tags,p=''):
    for x in tags or []:
      n=x.get('name',''); s.add(p+n); w(x.get('tags'),p+n+'/')
  w(t.get('tags')); return s
n=names(types['Tank'])
for req in ['Status','Level','LSH','LSL']:
  assert any(req==x or x.endswith(req) for x in n), req
assert any('HH' in x or x=='HH' for x in n)
print('A3-ok')" </automated>
  </verify>
  <done>Tank UDT has normalized level/alarm digits, SummaryInstances, and Tank sim profile markers.</done>
</task>

<task type="auto" wave="A" agent="A4">
  <name>A4: Devices/Sensor UDT + Overview tagPaths</name>
  <files>gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json, gateways/standard/data/config/resources/core/ignition/tag-definition/default/Sensors/udts.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Sensors/Overview/view.json, sim/build_plant_sim.py</files>
  <read_first>
    - RESEARCH-plc-devices-map.md §4 Sensor / P_AIn
    - RESEARCH-sim-overviews.md Sensors SNS-* broken vs LSS-PT etc.
  </read_first>
  <action>
  Per D-02 / D-04 / D-08:

  1. Migrate Sensor `Value` from bare Float4 to `_Root/Analog` (name `Value` or `PV` — prefer `Value` for path stability). engUnit per instance (psig/°F). Status Multistate: 0=OK, 1=HI, 2=LO, 3=HIHI, 4=LOLO, 5=FAIL, 6=BAD.

  2. Add Digital HiHi/Hi/Lo/LoLo/Fail; Float4 limit SPs (or Analog.SP siblings) same engUnit as PV; `Cmd_Reset`; `SummaryInstances`; keep `_Alarms`.

  3. Instances LSS-PT, HSS-PT, HPR-PT, OIL-TT inherit; preserve engUnits.

  4. **Overview:** Retarget SNS-* wall paths to the four live Sensors instances.

  5. `# --- SENSOR ---` sim profiles. No CSV regen.
  </action>
  <verify>
    <automated>python -c "import json; from pathlib import Path
types={t['name']:t for t in json.loads(Path('gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json').read_text(encoding='utf-8'))}
sensor=next(t for t in json.loads(Path('gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json').read_text(encoding='utf-8')) if t.get('name')=='Sensor')
# Value should be typed Analog (typeId containing Analog) not bare atomic only
val=next(x for x in sensor.get('tags',[]) if x.get('name') in ('Value','PV'))
assert 'Analog' in str(val.get('typeId','')) or val.get('tagType')=='UdtInstance' or 'Analog' in json.dumps(val)
ov=Path('gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Sensors/Overview/view.json').read_text(encoding='utf-8')
assert 'SNS-01' not in ov
assert any(x in ov for x in ['LSS-PT','HSS-PT','HPR-PT','OIL-TT'])
print('A4-ok')" </automated>
  </verify>
  <done>Sensor PV is _Root/Analog with limits; Overview uses live sensor instances; sim Sensor profiles marked.</done>
</task>

<task type="auto" wave="A" agent="A5">
  <name>A5: Devices/Evaporator UDT expand</name>
  <files>gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json, gateways/standard/data/config/resources/core/ignition/tag-definition/default/Evaporators/udts.json, sim/build_plant_sim.py</files>
  <read_first>
    - RESEARCH-plc-devices-map.md §6 CG_RL_Evap
    - Devices/Evaporator + existing StatusIndicator enum usage
  </read_first>
  <action>
  Per D-02 / discretion Option B:

  1. Keep HMI Status simplified enum (0=STOP,1=CLG,2=DFT,3=FLT,5=IDLE) used by StatusIndicator; add shortDescription documenting PLC Sts_State 0–10 mapping.

  2. Ensure Temp (°F) + Pressure (psi) Analogs support instance SP (ZAT). Add Boolean/Digital: `HMIEnable`, `Cmd_StartDefrost`, `Cmd_StopDefrost`, `Cleanup`, `TooHot`, `TooCold`, `IntlkOK`, `PermOK`, `Off`; Analog `TimeLeft` (engUnit `min`). Add Interlock/ folder (at least usable CondTxt + Sts_IntlkOK). Config-relevant writables: defrost step times / DB as memory floats if Controls/Config need them (Cfg_* names OK as HMI mirrors).

  3. Keep Fan 1..3 VFD children. Instances EV-* inherit.

  4. `# --- EVAPORATOR ---` Controls-grade sim profile extensions (beyond Status/Temp/Pressure/Fans). No CSV regen.
  </action>
  <verify>
    <automated>python -c "import json; from pathlib import Path
types={t['name']:t for t in json.loads(Path('gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json').read_text(encoding='utf-8'))}
def names(t):
  s=set()
  def w(tags,p=''):
    for x in tags or []:
      n=x.get('name',''); s.add(p+n); w(x.get('tags'),p+n+'/')
  w(t.get('tags')); return s
n=names(types['Evaporator'])
for req in ['Status','Temp','Pressure','HMIEnable','Cmd_StartDefrost','Cmd_StopDefrost','TimeLeft','Interlock']:
  assert any(req in x for x in n), req
print('A5-ok')" </automated>
  </verify>
  <done>Evaporator UDT has defrost/enable/ZAT Controls leaves + Interlock; sim profile markers ready.</done>
</task>

<task type="auto" wave="A" agent="A6">
  <name>A6: Devices/CoolingTower UDT expand</name>
  <files>gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json, gateways/standard/data/config/resources/core/ignition/tag-definition/default/CoolingTowers/udts.json, sim/build_plant_sim.py</files>
  <read_first>
    - RESEARCH-sim-overviews.md CoolingTower lean members
    - Devices/CoolingTower + Pump motor pattern (A1)
    - Compressor Interlock folder
  </read_first>
  <action>
  Per D-02 (CONTEXT deliverable includes CT if present — it is):

  1. Expand CoolingTower toward motor/VFD hybrid: keep Status, Temp (or BasinTemp — keep name if Overview binds Temp), SPD_FBK. Add OPER/MAINT/PROG, Cmd_Start/Stop/Auto/Manual, Failed/Alm/Comm, RuntimeHours/MotorStarts, Interlock/ folder.

  2. Instances CT-01..04 inherit.

  3. `# --- COOLINGTOWER ---` sim Controls profiles. No CSV regen.
  </action>
  <verify>
    <automated>python -c "import json; from pathlib import Path
types={t['name']:t for t in json.loads(Path('gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json').read_text(encoding='utf-8'))}
def names(t):
  s=set()
  def w(tags,p=''):
    for x in tags or []:
      n=x.get('name',''); s.add(p+n); w(x.get('tags'),p+n+'/')
  w(t.get('tags')); return s
n=names(types['CoolingTower'])
for req in ['Status','Cmd_Start','OPER','Interlock','RuntimeHours']:
  assert any(req in x for x in n), req
print('A6-ok')" </automated>
  </verify>
  <done>CoolingTower UDT has Controls/Interlock leaves and sim profile markers.</done>
</task>

<!-- ========== WAVE A-merge ========== -->

<task type="auto" wave="A-merge" agent="A-merge" depends_on="A1,A2,A3,A4,A5,A6">
  <name>A-merge: Sim FOLDERS + CSV regen + Overview polish</name>
  <files>sim/build_plant_sim.py, sim/bh-plant-sim.csv, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Evaporators/Overview/view.json, gateways/standard/data/config/resources/core/ignition/tag-definition/default/Pumps/udts.json, gateways/standard/data/config/resources/core/ignition/tag-definition/default/ExhaustFans/udts.json</files>
  <read_first>
    - RESEARCH-sim-overviews.md §4 FOLDERS gap, §8 recommended order
    - All `# --- {FAMILY} ---` markers from A1–A6
    - Existing COMP_FACEPLATE_DEFAULTS pattern
  </read_first>
  <action>
  Per D-03 / D-06:

  1. Extend `FOLDERS` to include `Valves`, `Tanks`, `Sensors` (keep Evaporators/Compressors/Pumps/ExhaustFans/CoolingTowers).

  2. Wire each family’s profile/defaults so new Controls leaves get demo values (Status walls still intentional: Run/Idle/Fault/Off; Interlock text on *-01 where applicable).

  3. Regenerate `sim/bh-plant-sim.csv` via `python sim/build_plant_sim.py` (or repo’s documented regen entrypoint). Confirm CSV contains Valve/Tank/Sensor device paths and Pump Flow (not only Temp), ExhaustFan Airflow, Evap Cmd_*, etc.

  4. Evaporators Overview: add EV-17 to wall if trivial; fix any Overview AnalogValue paths still binding renamed Temp→Flow/Airflow on Pump/EFAN walls.

  5. Do not invent live OPC item paths — memory/`[Sim]` OK.
  </action>
  <verify>
    <automated>python -c "from pathlib import Path
src=Path('sim/build_plant_sim.py').read_text(encoding='utf-8')
assert 'Valves' in src and 'Tanks' in src and 'Sensors' in src
csv=Path('sim/bh-plant-sim.csv').read_text(encoding='utf-8')
for token in ['Valves/','Tanks/','Sensors/','Cmd_Start','Interlock']:
  assert token in csv, token
# Pump flow rename should appear if regen used new leaf names
assert 'Pumps/' in csv and 'ExhaustFans/' in csv
print('A-merge-ok')" </automated>
  </verify>
  <done>Plant sim includes all device families and Controls-grade leaves; Overview path renames reconciled.</done>
</task>

<!-- ========== WAVE B — Controls + wiring (parallel) ========== -->

<task type="auto" wave="B" agent="B1" depends_on="A-merge">
  <name>B1: Controls views — Pump, ExhaustFan, CoolingTower</name>
  <files>gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Pump/Controls/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Pump/Controls/resource.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls/resource.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/CoolingTower/Controls/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/CoolingTower/Controls/resource.json</files>
  <read_first>
    - RESEARCH-faceplate-controls-ext.md §3 Compressor Controls stack, §8.2 pattern A
    - _Assets/Compressor/Controls/view.json (copy structure)
    - perspective-ticket-logger.mdc
  </read_first>
  <action>
  Per D-05: create `_Assets/{Pump,ExhaustFan,CoolingTower}/Controls` (+ resource.json) cloning Compressor section stack **Mode → Status/commands → KPI**.

  - Mode chips OPER/MAINT/PROG (hide section if no Good quality).
  - StatusIndicator on `{tagPath}/Status`; Cmd_* buttons gated by `!session.custom.ReadOnly`.
  - KPI: RuntimeHours/MotorStarts + Flow (Pump) / Airflow (EFAN) / Temp+SPD_FBK (CT) via AnalogValue or KPI rows.
  - Reuse CSS classes `faceplate-section*`, `faceplate-mode-chip`, `faceplate-kpi-row`. No Web GUI in Controls body (D-01).
  - Ticket Logger on each root. Tab-indent scripts; `\n` only in JSON strings.
  - Do **not** edit Faceplate shell (B4 owns it).
  </action>
  <verify>
    <automated>python -c "from pathlib import Path
root=Path('gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets')
for d in ['Pump','ExhaustFan','CoolingTower']:
  v=root/d/'Controls'/'view.json'
  assert v.is_file(), d
  t=v.read_text(encoding='utf-8')
  assert 'ticketLog' in t or 'Ticket' in t or 'contextMenu' in t
  assert 'OPER' in t or 'Mode' in t
print('B1-ok')" </automated>
  </verify>
  <done>Three motor-like Controls assets exist with Mode→Status→KPI and Ticket Logger.</done>
</task>

<task type="auto" wave="B" agent="B2" depends_on="A-merge">
  <name>B2: Controls views — Valve + Tank</name>
  <files>gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Valve/Controls/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Valve/Controls/resource.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Tank/Controls/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Tank/Controls/resource.json</files>
  <read_first>
    - _Assets/Compressor/Controls/view.json
    - RESEARCH-plc-devices-map.md Valve/Tank recommended members
  </read_first>
  <action>
  Per D-05:

  **Valve Controls:** Mode (if tags exist) → Status + Open/Close/Reset commands → LS/KPI (OpenLS/ClosedLS text status; TravelTime if present). No Web GUI.

  **Tank Controls:** Mode optional/hide if absent → Status → Level AnalogValue (+ HH/H/L/LL indicators as text codes) → Pressure if present. Commands only if UDT has them.

  Ticket Logger; Advanced Stylesheet classes only; hide empty sections via quality/visibility.
  </action>
  <verify>
    <automated>python -c "from pathlib import Path
root=Path('gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets')
assert (root/'Valve'/'Controls'/'view.json').is_file()
assert (root/'Tank'/'Controls'/'view.json').is_file()
vt=(root/'Valve'/'Controls'/'view.json').read_text(encoding='utf-8')
assert 'Cmd_Open' in vt or 'Open' in vt
tk=(root/'Tank'/'Controls'/'view.json').read_text(encoding='utf-8')
assert 'Level' in tk
print('B2-ok')" </automated>
  </verify>
  <done>Valve and Tank Controls assets ship Mode→Status→KPI appropriate to each family.</done>
</task>

<task type="auto" wave="B" agent="B3" depends_on="A-merge">
  <name>B3: Controls views — Sensor + Evaporator</name>
  <files>gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Sensor/Controls/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Sensor/Controls/resource.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Evaporator/Controls/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Evaporator/Controls/resource.json</files>
  <read_first>
    - _Assets/Compressor/Controls/view.json
    - RESEARCH-plc-devices-map.md Sensor + Evaporator
  </read_first>
  <action>
  Per D-05:

  **Sensor Controls:** Status → PV AnalogValue → limit/fault digitals as status codes; Reset cmd if present. No motor Mode required (hide Mode if OPER tags absent).

  **Evaporator Controls:** Enable / Start–Stop Defrost / Cleanup commands → StatusIndicator → Temp/Pressure/TimeLeft KPIs; TooHot/TooCold text. Document Sts_State map in view custom or SUMMARY only — do not break simplified Status enum.

  Ticket Logger; no Web GUI in body.
  </action>
  <verify>
    <automated>python -c "from pathlib import Path
root=Path('gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets')
assert (root/'Sensor'/'Controls'/'view.json').is_file()
assert (root/'Evaporator'/'Controls'/'view.json').is_file()
ev=(root/'Evaporator'/'Controls'/'view.json').read_text(encoding='utf-8')
assert 'Defrost' in ev or 'Cmd_StartDefrost' in ev
print('B3-ok')" </automated>
  </verify>
  <done>Sensor and Evaporator Controls assets exist with family-appropriate stacks.</done>
</task>

<task type="auto" wave="B" agent="B4" depends_on="A-merge">
  <name>B4: Faceplate shell + openers + Web GUI verify</name>
  <files>gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Faceplate/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Pump/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/ExhaustFan/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/CoolingTower/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Evaporator/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Tank/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Sensor/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/SolenoidValve/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/SolenoidValve3Way/view.json, gateways/standard/data/projects/BH/ignition/script-python/shared/Alerts/code.py</files>
  <read_first>
    - RESEARCH-faceplate-controls-ext.md §2.2–2.4, §5 openers, §8.3 checklist
    - Compressor device graphic openFaceplate branch
    - Faceplate tagFlags hasControlsAsset + Controls case()
  </read_first>
  <action>
  Per D-01 / D-05:

  1. **Faceplate shell:** Expand `hasControlsAsset` allow-list to include Pump, ExhaustFan, Valve, Tank, Sensor, Evaporator, CoolingTower (and empty-string/Compressor as today). Expand Controls `case(deviceType, …)` arms to `_Assets/{Device}/Controls` for each; fallback remains Compressor only when deviceType unknown — prefer explicit arms for all eight.

  2. **Web GUI verify (D-01):** Confirm header WebGui visibility expression is still `deviceType = 'Compressor' && len(coalesce(webGuiUrl,'')) > 0`. Confirm Controls body has no Web GUI section. Do not add Web GUI for other types.

  3. **Device openers:** Migrate Pump, ExhaustFan, CoolingTower, Evaporator (+Dual/Triple if present), Tank, Sensor, SolenoidValve, SolenoidValve3Way click handlers to unified Faceplate via `shared.Alerts.showFaceplate(tagPath, deviceType=…)` or Compressor-equivalent `Navigation.Faceplate.openFaceplate` with params `{tagPath, deviceType, showControls/Configuration/Interlocks/Trend/…=True}`. SolenoidValve* → `deviceType='Valve'`. Popup geometry prefer 560×640.

  4. **Nav:** Prefer thin wrappers `01_Popups/00_Faceplates/{Device}` embedding Faceplate with hardcoded deviceType (Compressor pattern), **or** extend nav payloads — ensure opening from docked nav does not default non-compressors to Compressor Controls. At minimum, Overview wall clicks must work.

  5. Shared Config/Interlocks already browse-based — no rewrite; they appear when UDT leaves exist (D-05). Empty tabs remain hidden via tagFlags.

  6. After view edits: `python scripts/repair-resource-signatures.py` and `--check`; POST scan/projects (and scan/config if tags changed).
  </action>
  <verify>
    <automated>python -c "from pathlib import Path
fp=Path('gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Faceplate/view.json').read_text(encoding='utf-8')
for dt in ['Pump','ExhaustFan','Valve','Tank','Sensor','Evaporator','CoolingTower']:
  assert dt in fp, dt
assert \"deviceType = 'Compressor'\" in fp or 'deviceType = \\'Compressor\\'' in fp
# openers mention showFaceplate or Faceplate + deviceType
pump=Path('gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Pump/view.json').read_text(encoding='utf-8')
assert 'deviceType' in pump and ('showFaceplate' in pump or 'Faceplate' in pump)
print('B4-ok')" </automated>
  </verify>
  <done>Faceplate routes all deviceTypes to Controls assets; device clicks open unified shell; Web GUI remains compressor header-only; signatures clean.</done>
</task>

<!-- ========== WAVE C — proof ========== -->

<task type="auto" wave="C" agent="C1" depends_on="B1,B2,B3,B4">
  <name>C1: Playwright Controls screenshots + Pushover all types</name>
  <files>scripts/pushover_nav_screenshots.py, docs/handoff/fp-controls-Compressor.png, docs/handoff/fp-controls-Pump.png, docs/handoff/fp-controls-Valve.png, docs/handoff/fp-controls-Tank.png, docs/handoff/fp-controls-Sensor.png, docs/handoff/fp-controls-ExhaustFan.png, docs/handoff/fp-controls-Evaporator.png, docs/handoff/fp-controls-CoolingTower.png</files>
  <read_first>
    - RESEARCH-faceplate-controls-ext.md §9 Pushover
    - scripts/pushover_nav_screenshots.py (load_env, pushover_with_image, shots list)
    - CONTEXT.md deliverable proof list
  </read_first>
  <action>
  Per D-07:

  1. Ensure gateway RUNNING (`StatusPing`). Capture Perspective client screenshots of Faceplate **Controls** tab for each deviceType using Playwright (`user-playwright` MCP or a small script). Suggested instances: COMP-01, PMP-01, MAIN-LIQ-SV (or HPRL-ISO), LTR-01, LSS-PT, EFAN-01, EV-02, CT-01. Save to `docs/handoff/fp-controls-{Device}.png`.

  2. Update `scripts/pushover_nav_screenshots.py` shots list to those PNGs (titles like `BH Faceplate Controls — Pump`) OR add a sibling script that reuses `load_env` + `pushover_with_image`. Run it with `.env` PUSHOVER_* set. Confirm multipart image send succeeds for each type.

  3. Spot-check Compressor: Web GUI header visible with demo URL; Controls has no duplicate Web GUI block (D-01).

  4. Write `.planning/quick/260730-mun-device-udt-faceplate-controls-sweep-pump/260730-mun-SUMMARY.md` with status, what shipped, PLC→HMI Status map for Evaporator, and Pushover send counts.
  </action>
  <verify>
    <automated>python -c "from pathlib import Path
hand=Path('docs/handoff')
needed=['Compressor','Pump','Valve','Tank','Sensor','ExhaustFan','Evaporator','CoolingTower']
missing=[d for d in needed if not (hand/f'fp-controls-{d}.png').is_file()]
assert not missing, missing
script=Path('scripts/pushover_nav_screenshots.py').read_text(encoding='utf-8')
assert 'fp-controls' in script or 'Controls' in script
print('C1-ok')" </automated>
  </verify>
  <done>Eight Controls PNGs on disk; Pushover notified; SUMMARY written; Web GUI compressor-only verified.</done>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| Operator session → tag writes | Faceplate Cmd_*/Mode/bypass writes gated by session.custom.ReadOnly |
| Browser → external Web GUI URL | openURL only for Compressor header when webGuiUrl set |
| Agent host → Pushover API | Token/user from .env; never commit secrets |

## STRIDE Threat Register

| Threat ID | Category | Component | Severity | Disposition | Mitigation Plan |
|-----------|----------|-----------|----------|-------------|-----------------|
| T-mun-01 | Tampering | Cmd_* / Mode / Interlock bypass writes | medium | mitigate | Gate all write actions with !session.custom.ReadOnly; one-shot bools not historized as process PV |
| T-mun-02 | Information Disclosure | Pushover screenshots | low | accept | Lab HMI only; no plant credentials in shots |
| T-mun-03 | Elevation | Web GUI openURL | medium | mitigate | Header visible only for deviceType Compressor + non-empty URL (D-01) |
| T-mun-04 | Tampering | Shared Devices/udts.json parallel edits | medium | mitigate | Whole-type StrReplace ownership; A-merge reconciles |
| T-mun-SC | Tampering | npm/pip installs | low | accept | No new package installs in this plan |
</threat_model>

<verification>
- Wave A verifies: each Devices type has Controls-grade members; Valves/Sensors Overviews lack SV-*/SNS-* ghosts.
- Wave A-merge: CSV contains Valves/Tanks/Sensors + Cmd_/Interlock paths.
- Wave B: `_Assets/*/Controls` exist; Faceplate case/hasControlsAsset lists all types; Pump opener passes deviceType.
- Wave C: eight `docs/handoff/fp-controls-*.png` files; Pushover script references them.
- Post-edit: `python scripts/repair-resource-signatures.py --check` exit 0; gateway scan OK.
</verification>

<success_criteria>
1. Devices UDTs for Pump, ExhaustFan, Valve, Tank, Sensor, Evaporator, CoolingTower expanded with _Root bases, states/engUnits, Interlock where actuated (D-02, D-08).
2. Sim demos all new leaves including previously missing Valves/Tanks/Sensors (D-03, D-06).
3. Overview walls for Valves/Sensors use live instances; other family Overviews still work (D-04).
4. Unified Faceplate Controls per deviceType; openFaceplate from device clicks; empty Config/Interlocks hide (D-05).
5. Web GUI header-only compressor verified (D-01).
6. Pushover Controls screenshots for all eight component types (D-07).
</success_criteria>

<output>
Create `.planning/quick/260730-mun-device-udt-faceplate-controls-sweep-pump/260730-mun-SUMMARY.md` when done (Wave C).
</output>

## Source coverage audit

| ID | Source | Item | Plan coverage |
|----|--------|------|---------------|
| GOAL | CONTEXT | Comprehensive UDT + Faceplate Controls sweep + Pushover proof | Entire plan |
| D-01 | CONTEXT | Web GUI header-only Compressors | B4 verify + C1 spot-check |
| D-02 | CONTEXT | Expand Devices UDTs (Pump…Evaporator; CT if present) | A1–A6 |
| D-03 | CONTEXT | Correlate CSV + PLC UDTs | A* + A-merge |
| D-04 | CONTEXT | Overview create/fix | A2, A4, A-merge |
| D-05 | CONTEXT | Faceplate Controls + Config/Interlocks | B1–B4 |
| D-06 | CONTEXT | Demo tags + metadata/states/engUnits | A* + A-merge |
| D-07 | CONTEXT | Pushover Controls screenshots each type | C1 |
| D-08 | CONTEXT | Thorough / parallel agents | Wave map A/B/C |
| REQ | RESEARCH-plc | Per-family leaf maps | A1–A6 actions |
| REQ | RESEARCH-sim | FOLDERS + SV/SNS fix | A2, A4, A-merge |
| REQ | RESEARCH-fp | Per-device Controls + hasControlsAsset + openers | B1–B4 |
| OUT | CONTEXT | Live PLC OPC every leaf | Explicitly excluded |
| OUT | CONTEXT | Non-compressor Web GUI | Explicitly excluded |
| DEFER | — | none listed beyond OUT | — |
