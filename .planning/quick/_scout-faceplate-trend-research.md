# Scout Faceplate Trend — research brief (port → BH)

**Source:** `C:\Program Files\Inductive Automation\Perspective-8-3-Scout\data\projects\ScoutMotors`  
**Date:** 2026-07-30  
**Scope:** Unified Faceplate Trend tab + Alarm Status table type fix

---

## 1. View paths (relative to project `ScoutMotors`)

| Role | Path |
|------|------|
| Unified shell | `01_Popups/00_Faceplates/Faceplate` |
| **Trend tab content** | `01_Popups/00_Faceplates/_Assets/Main` |
| Alarms tab | `01_Popups/00_Faceplates/Alarm/Alarms` |
| Config tab | `01_Popups/00_Faceplates/Configuration/Configuration` |
| Alarm Config tab | `01_Popups/00_Faceplates/Alarm Configuration/AlarmConfiguration` |
| Separate RealTime / widget trend (not the unified tab) | `01_Popups/00_Faceplates/Trend/RealTime` |

**Shell → Trend wiring:** Faceplate embeds `ia.display.view` with:

```
case(selected,
  "Trend", "01_Popups/00_Faceplates/_Assets/Main",
  ...)
```

Params passed into Trend: `tagPath`, `hiddenTags` ← `params.hiddenFromTrend`.

**BH today:** shell already targets `01_Popups/00_Faceplates/_Assets/Trend` (stub). Port Scout `_Assets/Main` → BH `_Assets/Trend` (name stays BH’s).

Device-specific shells (Utility/Pumps, HotWater/PumpFaceplate, etc.) either use the same unified Faceplate or a parallel Utility/HotWater Main that **duplicates the same browse + ApexChart pattern**.

---

## 2. How pens are auto-loaded

**Not** `params.pens`, **not** a deviceType lookup table, **not** a fixed UDT field list.

**Mechanism:** script transform on `custom.sensors` (expr-struct of `tagPath` + `hiddenTags`):

1. `system.tag.browse(tagPath, recursive=True)` — collect leaf tags (skip Folder / UdtType / UdtInstance / Property; skip `tag.Value`-style meta dots).
2. Apply `hiddenTags` allow-list exclusions (comma/semicolon; full path or provider-stripped).
3. Batch-read `.Enabled`, `.HistoryEnabled`, `.DataType` via `system.tag.readBlocking`.
4. Keep tags where **Enabled** and **HistoryEnabled** and datatype is **numeric** (exclude string / date / bool).
5. Build `[{path, alias, aggregate: "Average"}, ...]` under `sensors.analog`.  
   Alias = parent folder name if leaf is `VALUE`, else leaf name.

**History fetch:** second transform on `custom.chartDataAnalog` calls `system.tag.queryTagHistory` (Wide, Average, returnSize=100, window from hours dropdown).

**Tab visibility (shell):** separate browse/`getConfiguration` script sets `showTrend` if any leaf has `historyEnabled` + analog datatype (and not in `hiddenFromTrend`). Same idea for Config / Alarm Config / Alarms.

---

## 3. Chart component

| | |
|--|--|
| **Type** | `kyvislabs.display.apexchart` (Kyvis ApexCharts module) |
| **Not** | Power Chart / Time Series Chart |
| **Series** | Script transform: history dataset → Apex `series` `[{name, data: filteredDataset}, ...]` |
| **UI** | Hours dropdown (`ia.input.dropdown`: 2/4/8/24) + line chart, datetime x-axis |

BH already has `com.kyvislabs.apexcharts` and uses the same component in AdhocTrend — reuse that pattern.

`Trend/RealTime` is a different design: `params.tags` + Perspective **tag-history** binding → ApexChart (explicit pens, not browse).

---

## 4. Compressor vs pump — what selects tags?

**UDT instance contents + history flags**, not device type.

- Faceplate opens with `tagPath` = device instance root (e.g. compressor UDT vs pump UDT).
- Browse discovers whatever analog, history-enabled children exist under that path.
- Compressor and pump differ because their tag trees differ (and which tags have History enabled), not because of a Faceplate `deviceType` switch.

Optional caller overrides: `hiddenFromTrend` / `hiddenTags` to suppress specific paths.

**Contrast with BH stub:** `_Assets/Trend` hardcodes compressor pens (`FLA/SVP/DisP/Amps`) and opens AdhocTrend — Scout shows an **inline** chart with dynamic pens instead.

---

## 5. Minimal copy set for BH `01_Popups/00_Faceplates/_Assets/Trend`

| File | Action |
|------|--------|
| Scout `_Assets/Main/view.json` | Replace BH `_Assets/Trend/view.json` (keep BH path name) |
| Scout `_Assets/Main/resource.json` | Template for `resource.json` (`files: view.json[, thumbnail.png]`); **re-sign** after edit |
| Faceplate shell | Already points at `_Assets/Trend`; ensure embedded params pass `tagPath` + `hiddenTags` (or `hiddenFromTrend`) like Scout |
| Ticket logger | Add BH-required root `contextMenu` + `ticketLog` handler (Scout Main may lack it) |
| CSS | Prefer stylesheet classes over Scout’s Designer `Fonts/Label` class paths |

**Do not need for inline Trend tab:** `Trend/RealTime`, AdhocTrend Pen assets, deviceType tables.

**JSON shape (Trend view):**

```text
params: { tagPath, hiddenTags }
custom: { sensors: { analog: [] }, chartDataAnalog }
propConfig:
  custom.sensors     → expr-struct + browse/filter script
  custom.chartDataAnalog → expr-struct + queryTagHistory script
root flex column:
  Dropdown (hours)
  AnalogChart → type: kyvislabs.display.apexchart
    props.series ← dataset→series script
```

**Shell params (reference):** `tagPath`, `hiddenFromTrend`, `hiddenFromConfiguration`, `hiddenFromAlarmConfiguration`, `hiddenFromAlarms`.

---

## Alarm Status table — BH fix

| | Type string |
|--|-------------|
| **Scout (correct)** | `ia.display.alarmstatustable` |
| **BH broken** | `ia.display.alarm-status-table` ← causes “not found” |

**Scout references:**

- Faceplate tab: `01_Popups/00_Faceplates/Alarm/Alarms` → direct `ia.display.alarmstatustable`
- Wrapped asset: `01_Popups/Assets/Alarm_Elements/AlarmStatusTable` / `00_Pages/Alarms/_Assets/AlarmStatusTable` (same component type inside)

**BH fix:** in `_Assets/Alarms/view.json`, change type to `ia.display.alarmstatustable` (no hyphens). Filter pattern Scout uses:

`prov:<provider>:/tag:<path>*` from `tagPath`.

---

## Port decisions (short)

1. Copy Scout `_Assets/Main` → BH `_Assets/Trend`; keep ApexChart + browse auto-pens.
2. Drop BH’s hardcoded compressor pen list for the inline tab (AdhocTrend “Open” can remain optional).
3. Pump/compressor/evap get correct pens automatically if tags are history-enabled under `tagPath`.
4. Fix Alarms component type to `ia.display.alarmstatustable`.
5. Run `repair-resource-signatures.py` + project scan after edits.
