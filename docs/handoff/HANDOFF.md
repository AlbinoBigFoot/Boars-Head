# Handoff — RCP1 Simulate mode

**Branch:** `cursor/rcp1-simulate-fix-eb66` (PR #7)  
**Primary doc:** [`docs/rcp1-simulate.md`](../rcp1-simulate.md)

## Status

**Working on gateway** after config scan → projects scan:

- `[default]RCP1/Simulate` loads (`unary-resource` `files: ["tags.json"]`)
- SIM ON → 503 AtomicTags `valueSource=memory` + demo seeds (Rung=1, Amps=42, …)
- Plant devices live at **`[default]Plant/Machine Room/<device>`** with
  `Value` → `sourceTagPath=[default]RCP1/…` (`valueSource=reference`)
- Machine Room Overview view `params.tagPath` = `[default]Plant/Machine Room`
- UI: SIM ON shows compressors **RUN**, FLA **42**, SVP **55**, tanks **55%**

## Scan order (required)

1. `POST /data/api/v1/scan/config` — tags / UDT types  
2. `POST /data/api/v1/scan/projects` — views / scripts  

## Screenshots (Pushover)

| File | State |
|------|--------|
| `docs/handoff/rcp1-sim-off.png` | SIM off — empty values |
| `docs/handoff/rcp1-sim-on.png` | SIM ON — RUN / 42 / 55 |

## Root causes fixed

1. RCP1 `unary-resource.json` had `files: []` → Simulate tag missing  
2. Thin `Plant/.../Overview` UDT instance children were `Bad_NotFound` → always COMM LOSS  
