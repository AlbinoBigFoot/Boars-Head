# Scout Faceplate Configuration & Interlocks — research brief (BH redesign)

**Source (Scout):** `C:\Program Files\Inductive Automation\Perspective-8-3-Scout\data\projects\ScoutMotors`  
**Source (FT / PLC):** `Displays/(RA-BAS) P_Intlk-Faceplate.xml`, `BoarsHead.L5K`, `PLC/Screw_Compressor`, `PLC/P_Intlk`  
**Date:** 2026-07-30  
**Scope:** Configuration tab patterns + Interlocks (Scout gap / FT pattern) + shell tab visibility. Alarm Configuration paths already known — not re-covered in depth.

**Related:** `.planning/quick/_scout-faceplate-trend-research.md` (Trend / shell browse flags), `.planning/quick/260730-m0m-faceplate-controls-config-interlocks-red/CONTEXT.md`

---

## Verdict (read this first)

| Topic | Scout reality | BH implication |
|--------|---------------|----------------|
| **Configuration tab** | Generic **browse** of writable, non-alarmed leaf tags under `tagPath` → FlexRepeater rows | Prefer Scout browse pattern (or hybrid) over forever-hardcoded FLA/SVP/DisP; compressor Devices tree has few writable leaves today |
| **Interlocks tab** | **Does not exist** in Scout Faceplate | BH decision to add Interlocks is **FT/RA-BAS-driven**, not a Scout port |
| **Permissives / bypasses in Config** | Not a special Config subsection — only appear if they are ordinary writable tags under the device | Compressor interlock bypasses belong on a **dedicated Interlocks** tab (P_Intlk), not Scout Config |
| **Hide empty tabs** | Shell script sets `showConfiguration` / etc. from tag tree contents | BH today uses **caller params** (`showConfiguration: True` always) — should adopt Scout auto-detect (+ new `showInterlocks`) |

---

## 1. Scout view paths

| Role | Path (under `ScoutMotors` Perspective views) |
|------|-----------------------------------------------|
| Unified shell | `01_Popups/00_Faceplates/Faceplate` |
| **Configuration tab** | `01_Popups/00_Faceplates/Configuration/Configuration` |
| Configuration row | `01_Popups/00_Faceplates/_Assets/Configuration/ConfigurationRow` |
| SP / numeric editor | `03_Elements/00_Control/AnalogInput` |
| Bool / Int4 editor | `03_Elements/00_Control/MultiStateInput` |
| Alarm Configuration (known) | `01_Popups/00_Faceplates/Alarm Configuration/AlarmConfiguration` |
| Device-specific Config (AHU/VAV only) | `01_Popups/00_Faceplates/Configuration/{AHU1&2,AHU3,AHU4&5,VAV,RH_VAV}` |

**Shell → Config wiring** (`Faceplate` EmbeddedView path case):

```
"Configuration" → "01_Popups/00_Faceplates/Configuration/Configuration"
```

Params into Config: `tagPath`, `hiddenTags` ← `params.hiddenFromConfiguration`.

**No** Scout path named Interlocks / Intlk / Permissive under `01_Popups/00_Faceplates/`.

Device-specific AHU/VAV Configuration views are **hardcoded** AnalogInput stacks (plant-specific). The **unified Faceplate** uses only the generic browse Configuration — that is the pattern to port.

---

## 2. Configuration tab — structure & row generation

### 2.1 Container (`Configuration/Configuration`)

**Params:** `tagPath`, `hiddenTags` (comma/semicolon list).

**Flow:**

1. `custom.tags` ← expr-struct binding on `{tagPath, hiddenTags}` + **script transform**.
2. Script:
   - `system.tag.browse(tagPath, recursive=True)`
   - Keep `tagType == 'AtomicTag'`, exclude `hiddenTags` (full path or provider-stripped)
   - Batch-read `.readOnly`, `.AlarmEvalEnabled`, `.Enabled`
   - Keep tag if **Enabled** and **not readOnly** and **AlarmEvalEnabled != True**
3. Comment in Scout: alarmed tags belong on **Alarm Configuration**, not Config.
4. `ia.display.flex-repeater` instances ← one per path; each instance gets `tagPath` + alternating `highlightRow`.
5. Repeater element path: `.../_Assets/Configuration/ConfigurationRow`.

**Example Scout instance payload under a pump** (illustrative): writable VFD leaves such as `.../VFD/MAN_DSBL`, `RT`, `STRT_NUM`, `YAR_RST` — i.e. enable/disable and counters appear **because they are writable AtomicTags**, not because of a deviceType table.

There is **no** Scout Config logic that specially discovers “feedback timers”, “permissives”, or “bypasses”. Those show up only if present as writable leaves (or are handled on other screens).

### 2.2 Row (`ConfigurationRow`)

**Params:** `tagPath`, `highlightRow`.

**Type routing (expressions on `.DataType`):**

| Condition | Control shown |
|-----------|----------------|
| not Boolean and not Int4 | `03_Elements/00_Control/AnalogInput` |
| Boolean **or** Int4 | `03_Elements/00_Control/MultiStateInput` |

Both children get `props.params.tagPath` from the row; `permission: true` default. Row background toggles `--neutral-50` / `--neutral-40` via `highlightRow`.

### 2.3 Editors (what “SP / enable” means in Scout)

| Control | Role |
|---------|------|
| **AnalogInput** | Numeric live value + eng unit + format from tag; click-to-edit when `permission`; uses tag `.Metadata`, `.FormatString`, `.EngUnit` |
| **MultiStateInput** | Boolean / Int4 multi-state edit (enable/disable, mode ints, etc.) |

BH today already uses `03_Elements/00_Control/AnalogValue` in `_Assets/Compressor/Configuration` for FLA/SVP/DisP SPs — close cousin, not a FlexRepeater browse.

### 2.4 BH Configuration today (gap vs Scout)

| | Scout | BH now |
|--|-------|--------|
| Discovery | Browse writable non-alarm leaves | Hardcoded `FLA/SP`, `SVP/SP`, `DisP/SP` |
| Path | Generic `Configuration/Configuration` | `_Assets/Compressor/Configuration` via `deviceType` case |
| Empty tab | Hidden when no writable leaves | Always shown (`showConfiguration: true` from device open) |

**Compressor Devices UDT writable Config candidates today:** essentially the three `*/SP` tags (and any future writable non-alarm leaves). Process setpoints like `Load_Setpoint`, `Min_Runtime_Set`, timers, etc. live on **PLC/`Screw_Compressor`**, not on **Devices/Compressor**.

---

## 3. Interlocks — Scout vs FT (BH needs FT)

### 3.1 Scout

- No Interlocks tab, no Interlock faceplate assets, no shell flag `showInterlocks`.
- CONTEXT assumption “interlock permissives and bypasses where they belong in Scout Config” → **Scout does not place them in Config**. Treat Interlocks as a **BH + PlantPAx FT** feature.

### 3.2 FT source of truth

| Artifact | Role |
|----------|------|
| `Displays/(RA-BAS) P_Intlk-Faceplate.xml` | Full interlock faceplate (16 channels) |
| `Displays/(RA-BAS) P_IntlkPerm-Help.xml` | Help / legend (OK, bypassed, NB OK, first-out, etc.) |
| `Displays/(RA-BAS) P_Perm-Faceplate.xml` | Permissive twin (same channel pattern) |
| `Displays/(STELLAR)MachineRoom.xml` | `GO_P_Intlk*` → `{[RCP1]COMP[n].Interlock}` for comps 1,4,5,6,7 |

**Machine Room indicator** (graphic, not faceplate list):

```
if (NOT {#102.Sts_NBIntlkOK}) or (Not ({#102.Sts_IntlkOK} or {#102.Sts_BypActive})) then 3
else if ( Not {#102.Sts_IntlkOK} ) then 2
else {#102.Sts_BypActive}
```

### 3.3 How the FT interlock list is built

**Fixed 16 rows** (channels `0..15`), not a browse. Each row `#102 = N` binds:

| UI need | FT tag expression | Notes |
|---------|-------------------|--------|
| Label | `{#1.Cfg_CondTxt[#102]}` | `STRING_20[16]` AOI local / HMI text |
| Latched / OK status bit | `{#1.Sts_Intlk.#102}` | `Sts_Intlk` is INT bitfield |
| Bypass checkbox | `{#1.MSet_Bypass#N}` / `MSet_Bypass` | Maint bypass per channel |
| Bypass allowed | `{#1.Cfg_Bypassable.#102}` | INT bitfield; write gated by FT security code `H` |
| Row “in use” visibility | `{#1.Sts_Intlk.#102} or ({#1.Cfg_CondTxt[#102]} > " ")` | Hide empty unused channels |
| Optional nav-to-tag | `Cfg_HasNav.#N`, `Cfg_NavTag[N]` | Config UI inside faceplate |
| Header / reset | `Sts_IntlkOK`, `Sts_NBIntlkOK`, `Sts_BypActive`, `Sts_FirstOut`, `OCmd_Reset`, `Rdy_Reset` | Aggregate status + reset |

L5K AOI `P_Intlk` (v3.1) confirms `Cfg_CondTxt : STRING_20[16]`, `Cfg_NavTag : STRING_20[16]`, bitfield INTs for `Cfg_Bypassable` / `Cfg_HasNav` / `Cfg_Latched` / `Cfg_OKState` / `Sts_Intlk`.

### 3.4 PLC wiring for compressors

`PLC/Screw_Compressor` includes:

```
Interlock → UdtInstance typeId PLC/P_Intlk
```

Also related (not the P_Intlk list, but compressor logic): `Permissive`, `LU_Permissive`, `LU_Permissive_Timer`, `Run_Permissive_Timer`, `Fail_Timer`, `AuxIntlk` (P_DOut), setpoints (`Load_Setpoint`, `Min_Runtime_Set`, …).

**Devices/Compressor has no `Interlock` (or P_Intlk) member** — HMI Devices layer cannot drive an Interlocks tab until tags are added or the tab binds a separate PLC path.

---

## 4. Shell: `showConfiguration` / hide empty tabs

### 4.1 Scout Faceplate `custom.tagFlags` script

Browse/enumerate leaves under `tagPath`, then `system.tag.getConfiguration(leaf)` per leaf:

| Flag | Qualifies when |
|------|----------------|
| `showTrend` | `historyEnabled` and analog datatype; not in `hiddenFromTrend` |
| **`showConfiguration`** | **not `readOnly`**, **no alarms**, non-empty datatype; not in `hiddenFromConfiguration` |
| `showAlarmConfiguration` | has alarms; not in `hiddenFromAlarmConfiguration` |
| `showAlarms` | has alarms; not in `hiddenFromAlarms` |

Tab button width / flex / opacity collapse to `0` / `none` when flag false. `defaultTab` prefers Trend → Configuration → Alarm Configuration → Alarms.

**Caller overrides:** `hiddenFromConfiguration` (and siblings) suppress specific paths without removing tags.

### 4.2 BH Faceplate today

- Params: `showControls`, `showConfiguration`, `showTrend`, `showAlarmConfiguration`, `showAlarms` — **manual booleans**.
- Compressor device open sets **all True**.
- No `showInterlocks`.
- Embedded paths: Controls/Configuration under `_Assets/Compressor/*`; Trend / Alarm Config / Alarms under `_Assets/*`.

### 4.3 Recommended BH shell behavior (Config + Interlocks)

| Tab | Show when |
|-----|-----------|
| Configuration | Scout rule: any writable non-alarm leaf under Devices `tagPath` (after `hiddenFromConfiguration`) **or** (optional) known device Config allow-list if browse would be empty but PLC mirror SPs exist |
| **Interlocks** | Devices (or resolved PLC) path has usable P_Intlk: e.g. child `Interlock` / `Sts_IntlkOK` quality good **or** `deviceType=='Compressor'` once Interlock tags exist |
| Controls | Keep BH-specific (Scout shell has no Controls tab) |
| Trend / Alarm Config / Alarms | Same Scout browse rules as Trend research brief |

Hide tab chrome when flag false (match Scout width/`display` pattern). Do not show Interlocks on devices with no P_Intlk.

---

## 5. Recommended BH tag gaps — `Devices/Compressor` (+ `PLC/P_Intlk`)

### 5.1 Must-have for Interlocks tab

Add under **Devices/Compressor** (HMI layer), sourced from PLC `COMP[*].Interlock` / sim equivalent:

| Member | Purpose |
|--------|---------|
| `Interlock` (folder or UDT instance) | Faceplate `tagPath + '/Interlock'` |
| `Sts_IntlkOK`, `Sts_NBIntlkOK`, `Sts_BypActive`, `Sts_FirstOut`, `Sts_Intlk` | Header / row status |
| `Inp_Intlk00` … `Inp_Intlk15` **or** rely on `Sts_Intlk` bits | Per-channel OK (FT uses `Sts_Intlk.n` for display) |
| `MSet_Bypass00` … `MSet_Bypass15` | Operator/maint bypass writes |
| `Cfg_Bypassable` (Int / bitfield) | Enable bypass UI per channel |
| **`Cfg_CondTxt[0..15]` (String)** | Row labels — **missing from Ignition `PLC/P_Intlk` UDT today** |
| `OCmd_Reset`, `Rdy_Reset` | Reset latched interlocks |
| Optional: `Cfg_HasNav`, `Cfg_NavTag[]`, `Cfg_Latched`, `Cfg_OKState` | FT parity / advanced config |

**Also fix `PLC/P_Intlk` type definition** so OPC/UDT instances expose:

- `Cfg_CondTxt` (String array ×16) — required for labels  
- `Cfg_NavTag` (String array ×16) — optional  
- `Cfg_Label`, `Cfg_Desc`, `Cfg_Tag`, `Inf_Type`, `Inf_Lib` — header/meta if desired  

Ignition already has per-bool `Inp_Intlk00..15` / `MSet_Bypass00..15` and Int2 bitfields for `Sts_Intlk` / `Cfg_Bypassable` / etc. Prefer **bit expressions** on Int2 (`getBit`) or document OPC bit path convention to match FT `.#N`.

Without `Cfg_CondTxt`, BH can temporarily fall back to `"Interlock " + n` or documentation strings — not FT-faithful.

### 5.2 Config tab — compressor fields N/A on Devices today

CONTEXT: compressors show only applicable Config fields. Devices today → SPs only.

If Config should expose more Screw_Compressor settings later, promote selectively onto Devices (writable, **no** Ignition alarms on those leaves so Scout browse keeps them on Config):

| PLC `Screw_Compressor` | Typical HMI use |
|------------------------|-----------------|
| `Load_Setpoint`, `UBL_Setpoint`, `LBL_Setpoint`, `Bkl_Set` | Capacity / balance SPs |
| `Min_Runtime_Set`, `AntiR_*` | Runtime / anti-recycle |
| `AutoTarget`, `AutoEN` | Auto control |
| `Fail_Timer`, `Run_Permissive_Timer`, `LU_Permissive_Timer` | Feedback / permissive **timers** (TIMER UDT — expose `.PRE` / editable preset as AtomicTags if operators edit them) |
| `Clear_Failures` | Command (bool) — may fit Controls more than Config |

Do **not** put P_Intlk bypasses on the Configuration tab if Interlocks tab exists.

### 5.3 Pump later

Devices/Pump is thin (`Status`, `Temp/SP`). Scout-style Config will stay empty until writable leaves (VFD disable, feedback delay, etc.) are added — same browse shell still works.

---

## 6. BH implementation sketch (Config + Interlocks only)

### Configuration

1. Port Scout `Configuration/Configuration` + `ConfigurationRow` under BH  
   `01_Popups/00_Faceplates/_Assets/Configuration/` (shared, not compressor-only).
2. Point Faceplate Configuration case at that generic view (all `deviceType`s).
3. Reuse BH `AnalogValue` **or** port Scout `AnalogInput` / `MultiStateInput` (BH currently only has `AnalogValue` under `03_Elements/00_Control`).
4. Keep compressor hardcoded SP view only as fallback if browse empty during transition.
5. Pass `hiddenFromConfiguration` for tags that must not appear (e.g. internal writes).

### Interlocks

1. New tab content e.g. `_Assets/Interlocks` (or `Interlocks/Interlocks`) — **FlexRepeater 0..15** or static 16 rows mirroring FT bindings.
2. Params: `tagPath` = device root; resolve `interlockPath = tagPath + '/Interlock'` (or explicit param).
3. Row visibility: `Sts_Intlk` bit **or** non-blank `Cfg_CondTxt[n]` (FT rule).
4. Bypass write → `MSet_BypassNN`; gate on `Cfg_Bypassable` bit + session permission (map FT code `H` to BH roles).
5. Shell: `showInterlocks` + hide empty; open from Machine Room graphic can deep-link `selected: 'Interlocks'`.

### Shell flags

Replace always-true params with Scout-like `tagFlags` script; extend with Interlocks detection. Compressor open script should stop forcing all tabs visible.

---

## 7. Path cheat-sheet

### Scout

```
01_Popups/00_Faceplates/Faceplate
01_Popups/00_Faceplates/Configuration/Configuration
01_Popups/00_Faceplates/_Assets/Configuration/ConfigurationRow
01_Popups/00_Faceplates/Alarm Configuration/AlarmConfiguration   (known)
03_Elements/00_Control/AnalogInput
03_Elements/00_Control/MultiStateInput
```

### BH (current)

```
01_Popups/00_Faceplates/Faceplate
01_Popups/00_Faceplates/_Assets/Compressor/Configuration   (hardcoded SPs)
01_Popups/00_Faceplates/_Assets/Compressor/Controls
01_Popups/00_Faceplates/_Assets/AlarmConfiguration         (known)
03_Elements/00_Control/AnalogValue
```

### FT / PLC

```
Displays/(RA-BAS) P_Intlk-Faceplate.xml
Displays/(STELLAR)MachineRoom.xml          → COMP[n].Interlock
PLC/Screw_Compressor.Interlock             → PLC/P_Intlk
Devices/Compressor                         → no Interlock yet
```

---

## 8. Assumptions confirmed / rejected

| Assumption (CONTEXT) | Result |
|----------------------|--------|
| Scout detects “tab has data” for show/hide | **Yes** — browse + `getConfiguration` / property reads |
| Interlock permissives/bypasses live in Scout Config | **No** — Scout Config is generic writable tags only; FT owns Interlocks faceplate |
| Compressor interlock tag sources | **PLC `Screw_Compressor.Interlock` (P_Intlk)** + FT faceplate; **Devices UDT gap** |
| Compressors: many Config fields N/A | **Yes** on Devices today — only SPs; richer PLC members need promotion if Config should show them |
