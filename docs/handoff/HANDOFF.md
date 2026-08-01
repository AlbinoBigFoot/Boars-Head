# Handoff — RCP1 Simulate mode

**Branch:** `cursor/rcp1-simulate-fix-eb66` (PR #7)  
**Prior branch:** `feat/rcp1-simulate`  
**Primary doc:** [`docs/rcp1-simulate.md`](../rcp1-simulate.md)

## Status

**Fixed and verified** on gateway `bh-ignition-standard`:

- Root cause: `RCP1/unary-resource.json` had `"files": []` so `tags.json`
  (`[default]RCP1/Simulate`) never loaded — Header bound to null.
- Fix: `"files": ["tags.json"]`.
- Tag Change `rcp1Simulate` → `shared.Rcp1Simulate.applySimulate()`
- Verified: `listRcp1AtomicTags found 503` → `memory=503` / `opc=503`
- Sample after SIM ON: `COMP 7/Alm` + `Rung` → `valueSource=memory`, Good quality
- Units/Machine Room Values already `sourceTagPath` → `[default]RCP1/…`
- Plant instance tracked: `Plant/Machine Room/Overview` → `Units/Machine Room`

## Screenshots (Pushover HTTP 200)

| File | State |
|------|--------|
| `docs/handoff/rcp1-sim-off.png` | SIM off (OPC) — Machine Room |
| `docs/handoff/rcp1-sim-on.png` | SIM ON — Machine Room (sensors 0.0 psig) |
| `docs/handoff/rcp1-sim-gateway-proof.png` | Gateway log proof card |

## Notes

- Plant Programmable Device Simulator is **not** used for RCP1.
- Runtime `system.tag.configure` may rewrite folder layout (`udts.json` →
  nested `tags.json`); restore from git after local experiments if needed.
- Units Values stay `reference`; only RCP1 AtomicTags flip to `memory`.
- Device graphics may still show COMM LOSS if the Perspective client shows
  “No Connection to Gateway” even while tags are Good on the gateway.
