# Priorities vs Needs & Wants

Source: `FactoryTalk to Ignition Migration Tracker V6.xlsx`  
Roles: **FBCO** (client) · **One Shot** (you / Ignition contractor) · **Both**

Legend (from tracker): **Need** = go-live blocker · **Want** = important, not a blocker · **Nice to Have** = bonus

---

## Priority stack (execution order)

| Tier | Focus | Why first |
|------|--------|-----------|
| **P0** | Dev platform: Standard GW 8.1.43 + Edge GW 8.3.7 + MSSQL + Git-backed volumes | Unblocks all Ignition work |
| **P1** | Architecture foundation: tags/UDTs, PLC drivers, screen standards, alarms, security | Everything else hangs on these |
| **P2** | Historian/trending, digitized forms/PSM logs, project version control | Operator daily use + compliance path |
| **P3** | Wants & deferred FBCO-only control/process items | After P1/P2 baselines exist |
| **P4** | Pending-input items | Blocked on operator/PSM/IT answers |

---

## Needs (Must ship for go-live)

### One Shot primary / Both (your build surface)

| ID | Item | Owner | Priority tier |
|----|------|-------|---------------|
| 26* | Gateway topology, environments, redundancy (dev stack now; prod later) | FBCO (+ One Shot builds) | **P0** |
| 50 | Ignition project version control (Git) | Both | **P0** (platform) |
| 28 | Tag naming, hierarchy, equipment UDTs | Both | **P1** |
| 10 | PLC/OPC connectivity strategy | Both | **P1** |
| 2 | Recreate operator graphics (w/ templates) | Both | **P1** |
| 11 | Equipment/tag relabeling & graphics cleanup | Both | **P1** |
| 3 | Migrate alarm config & history | Both | **P1** |
| 7 | AD/IdP multi-user RBAC + remote access | Both | **P1** |
| 22 | Improved trending interface | Both | **P2** |
| 13 | Digitize manual logs / forms / PSM into Ignition | Both | **P2** |

\*ID 26 is FBCO-owned in tracker; Docker lab implements the **dev** half now.

### FBCO-led Needs (One Shot supports / implements when specified)

| ID | Item | Notes |
|----|------|-------|
| 1 | Unlimited tag/client licensing | Purchase / tier confirmation |
| 9 | Training, sandbox, cutover/rollback | Sandbox can reuse this Docker stack |
| 18, 19, 25, 37, 38, 39, 45 | Refrigeration control/HMI functions | PLC + HMI; FBCO process ownership |
| 20, 30 | Alarm disregard + rationalization / PSM instructions | Needs PSM input |
| 31, 32, 33 | Audit trail, change mgmt, FAT/SAT | Process + Ignition features |
| 34, 35, 46, 47 | Safety arch, NH3 inventory, system type, P&ID validation | Site/PSM |
| 44 | After-hours alarm notification | **FBCO only** — out of One Shot scope (Emergency 24 vs Ignition is their call) |
| 48 | OT endpoint protection / patching | Corporate IT/OT |

### Needs still Pending Input (do not schedule deep work yet)

| ID | Item | Waiting on |
|----|------|------------|
| 20 | Alarm disregard / management standard | PSM review |
| 39 | Pump-out / liquid-level | Operator walkthrough |
| 40 | Fire & gas beyond PPM | Local + corporate |
| 44 | On-call notification path | **FBCO only** — Greg Rogers / Emergency 24; do not plan Ignition SMS/Voice unless FBCO requests it |
| 45 | Head pressure / condenser control | Operator |
| 48 | OT security policy | Corporate IT/OT |

---

## Wants (Important, not go-live blockers)

| ID | Item | Owner | Suggested tier |
|----|------|-------|----------------|
| 4 | Historian retention / migrate-vs-archive | Both | **P2** (decide early; implement after tags) |
| 6 | Shift/production reports | Both | **P3** |
| 12 | Replace ICTD temperature probes | FBCO | **P3** (hardware) |
| 14 | Evaporator fan start timer bypass | FBCO | **P3** |
| 42 | Third-party integrations (CMMS, etc.) | FBCO | **P3** |
| 49 | NTP across gateways | FBCO | **P2** (cheap; do with architecture) |
| 50 | Project Git version control | Both | **P0** (already in platform) |

---

## One Shot near-term ToDo (actionable)

1. **P0** — Stand up Docker Compose: Standard `8.1.43`, Edge `8.3.7`, MSSQL (internal volume), host-mounted gateway data for Git.
2. **P0** — Document Gateway Network / EAM mirror path Standard → Edge (note 8.1↔8.3 Java serialization flag).
3. **P0** — GSD roadmap + Graphify knowledge graph from tracker + planning docs.
4. **P1** — Draft tag naming / UDT standard from P&IDs (ID 28) with FBCO.
5. **P1** — Lock PLC driver vs OPC hosting decision (ID 10).
6. **P1** — Screen template + navigation standard before mass display rebuild (ID 2).
7. **P1** — Alarm migration plan coordinated with rationalization (ID 3 ↔ 30).
8. **P1** — IdP/AD role model design (ID 7).
9. **P2** — Historian strategy decision (migrate vs archive) (ID 4) + trending UX (ID 22).
10. **P2** — Forms/logs inventory for Ignition digitization (ID 13).
11. **P3+** — Pull Wants and Pending Input only after P1 baselines and FBCO answers land.

---

## Explicitly out of One Shot solo ownership

Hardware probe replacement (12), compressor sequencing source-of-truth on SICK panels (37), safety relay architecture (34), licensing purchase (1), and most PSM policy decisions remain **FBCO-led**. One Shot implements Ignition-side deliverables once FBCO defines process/safety constraints.
