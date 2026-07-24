# Boars Head — FactoryTalk → Ignition Migration

## What This Is

Conversion of an existing FactoryTalk View SE / FactoryTalk SE Suite HMI into Ignition for a Boar's Head refrigeration / ammonia (NH3) plant (RCP ↔ BH topology). One Shot (contractor) builds Ignition deliverables; FBCO owns process, PSM, licensing, and many control-logic decisions. Shared scope covers screens, alarms, security, PLC connectivity, tag model, historian/trending, and digitized forms.

## Core Value

A safe, operator-usable Ignition platform that preserves critical NH3 alarming and control visibility at cutover — without losing PSM-traceable history or shared single-login chaos.

## Business Context

- **Customer**: FBCO / Boar's Head site (refrigeration operations)
- **Delivery model**: Contractor (One Shot) + client (FBCO) split ownership per migration tracker
- **Success metric**: Cutover-ready Ignition with parity for Needs in the Wants & Needs tracker; operators trained; rollback plan documented
- **Strategy notes**: `.planning/PRIORITIES.md` · tracker Excel · `Refrigeration MCC IPs.xlsx` / `docs/network-inventory.md`

## Requirements

### Validated

- [x] Refrigeration system type confirmed as pumped liquid overfeed NH3 (tracker ID 46)
- [x] Refrigeration MCC IP inventory received (`10.80.31.0/24`; RCP PLC `10.80.31.60`)

### Active

- [x] Docker lab: Standard GW 8.1.43 + Edge GW 8.3.7 + MSSQL; host-mounted gateway volumes for Git
- [ ] Gateway Network / project mirror Standard → Edge
- [ ] Plant-wide tag naming + UDTs (ID 28) — seed from MCC device names / AU# IDs
- [ ] PLC/OPC connectivity strategy (ID 10) — primary target CompactLogix `10.80.31.60`
- [ ] Screen templates + recreate graphics with cleanup (ID 2, 11)
- [ ] Alarm migration + rationalization coordination (ID 3, 20, 30)
- [ ] AD/IdP multi-user RBAC (ID 7)
- [ ] Historian strategy + trending UX (ID 4, 22)
- [ ] Digitize rounds/forms/PSM logs (ID 13)
- [ ] Project Git version control (ID 50)

### Out of Scope

- Replacing FactoryTalk licensing purchase decisions — FBCO (ID 1)
- Field hardware probe replacement — FBCO (ID 12)
- After-hours / on-call alarm notification (Emergency 24 vs Ignition) — FBCO (ID 44)
- Redefining safety relay (440-C-CR30) architecture without PSM — FBCO (ID 34)
- Corporate fire & gas mustering redesign unless scoped — Pending (ID 40)
- Production RCP/BH redundant hardware install — later phase after lab architecture proven

## Context

- Source of truth for scope: `FactoryTalk to Ignition Migration Tracker V6.xlsx`
- OT addressing: `Refrigeration MCC IPs.xlsx` → `docs/network-inventory.md` (RCP PLC, Quantum compressors, PowerFlex evaporators/condensers, NH3 pumps, 440C-CR30)
- Prioritization: `.planning/PRIORITIES.md`
- Lab topology (current decision): Standard Ignition `8.1.43` (may move to 8.3 later), Edge `8.3.7` mirroring standard project, MSSQL latest for DB-backed features
- Cross-version Gateway Network (8.1 ↔ 8.3) may require `GATEWAY_NETWORK_ALLOWJAVASERIALIZATION=true` temporarily
- Graphify knowledge graph under `graphify-out/` for tracker ↔ planning relationships

## Constraints

- **Tech**: Ignition Docker official images; MSSQL; Git on host-mounted gateway `data` (or project export paths)
- **Safety/PSM**: Alarm disregard, ESD, NH3 inventory need documented justification before Ignition changes
- **Ownership**: Do not unilaterally change FBCO-only control logic without operator/engineer sign-off
- **Version mix**: 8.1 standard + 8.3 edge is intentional for now; plan for eventual 8.3 consolidation

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Standard GW 8.1.43 + Edge 8.3.7 | Client/lab versions specified; Edge represents local mirror | — Pending validate EAM/GN mirror |
| MSSQL (latest available image) | TBD production DB; MSSQL is default assumption | — Pending confirm prod DB |
| MSSQL Docker volume internal | DB not needed in Git | ✓ |
| Gateway volumes bind-mounted on host | Enable Git revision control of projects | ✓ |
| GSD + Graphify for workflow | Structured phases + queryable scope graph | ✓ |
| RCP PLC at 10.80.31.60 | From MCC IP sheet; CompactLogix 1769 | ✓ Good |
| Compressors on Quantum HD .61–.65 | Matches tracker SICK Quantum sequencing note | ✓ |

---
*Last updated: 2026-07-23 after MCC IP inventory ingest*
