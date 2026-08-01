# Handoff — RCP1 Simulate mode

**Branch:** `feat/rcp1-simulate` (pushed to `origin`)  
**Commits:**
- `0ce707c` — `feat: RCP1 Simulate toggle — OPC vs memory via tagChange`
- `095efef` — `docs: RCP1 Simulate handoff commit hash + branch pointer`

**Base:** `main` (branched while main was ahead of `origin/main`)  
**Primary doc:** [`docs/rcp1-simulate.md`](../rcp1-simulate.md)

## Status

Implemented and verified on gateway `bh-ignition-standard`:

- Tag Change `rcp1Simulate` watches `[default]RCP1/Simulate`
- `shared.Rcp1Simulate` flips **503** AtomicTags OPC ↔ Memory (Simulate excluded)
- Header dock left toggle bound bidirectionally to Simulate
- Gateway logs: `listRcp1AtomicTags found 503` then `memory=503` / `opc=503`

## Remote agent — start here

```text
git fetch origin
git checkout feat/rcp1-simulate
git pull
```

Read `docs/rcp1-simulate.md` for behavior, path stash (`#OPC:` in documentation), test steps.

## Screenshots (Pushover)

| File | State |
|------|--------|
| `docs/handoff/rcp1-sim-off.png` | SIM off (OPC) — Machine Room |
| `docs/handoff/rcp1-sim-on.png` | SIM ON (Memory) — Machine Room |

Pushover attachments sent successfully (HTTP 200) for both shots.

## Changed files (feature)

- `gateways/.../BH/ignition/script-python/shared/Rcp1Simulate/`
- `gateways/.../BH/ignition/tag-change/rcp1Simulate/`
- `gateways/.../BH/.../00_Docked/Header/view.json` (+ resource signature)
- `gateways/.../BH/.../stylesheet/stylesheet.css` (+ resource signature)
- `gateways/.../tag-definition/default/RCP1/tags.json` — Simulate boolean
- `docs/rcp1-simulate.md`, `docs/rcp1-opc-tags.md` (pointer), this handoff

## Notes

- Plant Programmable Device Simulator (`Sim` / `bh-plant-sim.csv`) is **not** used for RCP1; Memory tags are the demo path.
- Runtime `system.tag.configure` may temporarily rewrite folder layout on disk; committed tree keeps nested Folders inside `udts.json` + root `Simulate` Memory tag.
- After pull: POST scan/projects (and scan/config if tags changed).
