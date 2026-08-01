# RCP1 Simulate mode

Toggle **`[default]RCP1/Simulate`** to switch all Machine Room OPC AtomicTags under
`[default]RCP1/` between live **OPC UA** (PLC device `RCP1`) and writable **Memory**
tags for demo / faceplate testing.

There is no Programmable Device Simulator wiring for RCP1 leaves (the plant `Sim`
device + `sim/bh-plant-sim.csv` feed `[default]_Sim_/…`, not RCP1). Simulate mode
therefore uses **Memory** tags with type-default values (or last Good OPC value when
available). Faceplates can write Memory tags directly.

## Tag path

| Tag | Role |
|-----|------|
| `[default]RCP1/Simulate` | Boolean Memory control — **excluded** from reconfigure |
| `[default]RCP1/**` (other AtomicTags) | Flipped between `opc` and `memory` |

OPC server when not simulating: `Ignition OPC UA Server`  
Node id form: `ns=1;s=[RCP1]<PLC_TAG>.<member>` (see `docs/rcp1-opc-tags.md`)

## Behavior

| Simulate | Tag `valueSource` | Notes |
|----------|-------------------|--------|
| **False** (default) | `opc` | Restores `opcItemPath` / `opcServer` |
| **True** | `memory` | Clears OPC fields; tags writable for demo |

Nested folders (`Interlock/*`, `Fail_Timer/PRE`, etc.) are included via recursive
browse of AtomicTags. Structural Folder nodes are untouched.

## How OPC paths are preserved

1. **Before** flipping to Memory, the script reads each tag’s `opcItemPath` /
   `opcServer` via `system.tag.getConfiguration`.
2. Paths are stored in:
   - An in-process module cache (`shared.Rcp1Simulate._opcCache`)
   - The tag’s `documentation` field, prefixed with `#OPC:<opcItemPath>\n` so a
     gateway restart while Simulate is ON can still restore OPC later
3. **When** flipping back to OPC, paths are resolved from cache first, then from
   the `#OPC:` documentation stash, then from any remaining `opcItemPath` on the
   config. Clean documentation (without the marker) is restored.

## Gateway script (tagChange)

| Item | Path |
|------|------|
| Tag Change resource | `gateways/standard/data/projects/BH/ignition/tag-change/rcp1Simulate/` |
| Script file | `onTagChange.py` |
| Watched path | `[default]RCP1/Simulate` |
| Change types | `ValueChange` (including `initialChange` on gateway load) |
| Logic module | `gateways/standard/data/projects/BH/ignition/script-python/shared/Rcp1Simulate/code.py` |
| Call | `shared.Rcp1Simulate.applySimulate(simulate)` |

`applySimulate(True)` → `toMemory()`; `applySimulate(False)` → `toOpc()`.

## UI toggle

| Item | Detail |
|------|--------|
| Dock | Shared **top** dock → `00_Pages/00_Docked/Header` |
| Placement | **Left** of the header bar (before the flex spacer; user/settings stay right) |
| Binding | Bidirectional tag bind on `ia.input.toggle-switch` → `[default]RCP1/Simulate` |
| Label | `SIM` / `SIM ON` |
| CSS | `rcp1-sim-toggle`, `rcp1-sim-toggle-on`, `rcp1-sim-label`, `rcp1-sim-switch` in Advanced Stylesheet |

Page config: `com.inductiveautomation.perspective/page-config/config.json` →
`sharedDocks.top` → `viewPath: 00_Pages/00_Docked/Header`.

## How to test

1. Open Perspective client: `http://localhost:<STANDARD_HTTP_PORT>/data/perspective/client/BH`
2. Navigate to **Machine Room** (`/machine-room`).
3. Confirm header left shows **SIM** toggle (Simulate = False).
4. In Tag Browser / Designer, check a leaf e.g. `[default]RCP1/COMP 7/Alm` →
   `valueSource=opc`, `opcItemPath=ns=1;s=[RCP1]COMP[7].Alm`.
5. Flip **SIM** ON. Gateway logs (`shared.Rcp1Simulate`) should report
   `Simulate ON — memory=…`. Same leaf → `valueSource=memory`; documentation
   starts with `#OPC:ns=1;s=[RCP1]COMP[7].Alm`.
6. Write a Memory value from a faceplate / Tag Browser; UI should update.
7. Flip **SIM** OFF → leaf restored to OPC with original `opcItemPath`.

Gateway scripts: Status → Logs → filter `shared.Rcp1Simulate` or project tag-change
errors.

## Architecture constraints

- RCP1 remains **OPC AtomicTags only** when not simulating (no `_Root` under RCP1).
- Simulate itself stays a Memory AtomicTag at the RCP1 folder root.
- Plant Programmable Device Simulator (`Sim` / `bh-plant-sim.csv`) is unchanged.

## Related

- Branch: **`feat/rcp1-simulate`** (commit `0ce707c`)
- `docs/rcp1-opc-tags.md` — OPC tree inventory
- `docs/handoff/HANDOFF.md` — remote handoff pointer
- Screenshots: `docs/handoff/rcp1-sim-off.png`, `docs/handoff/rcp1-sim-on.png`
