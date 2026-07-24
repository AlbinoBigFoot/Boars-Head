# Roadmap — Boars Head Ignition Migration

Granularity: **standard** (5–8 phases). See `.planning/PRIORITIES.md` for Need/Want ranking.

## Phase 1 — Lab platform & Git foundation

**Goal:** Reproducible Docker stack (Standard + Edge + MSSQL) with host-backed gateway volumes and documented mirror path.

**Success criteria:**
- Compose stack healthy; gateways + DB reachable
- README covers ports, credentials pattern, volumes
- Standard → Edge mirror approach documented (cross-version notes)

**Primary tracker IDs:** 26 (dev), 50

## Phase 2 — Data model & connectivity

**Goal:** Plant tag hierarchy/UDTs and PLC/OPC strategy locked with FBCO.

**Success criteria:**
- Naming standard + UDT list for compressors, vessels, evaporators, NH3 sensors, fans
- Driver/OPC hosting decision + first live PLC browse in lab (or documented stub)

**Primary tracker IDs:** 28, 10, 46, 47

## Phase 3 — HMI standards & screen migration

**Goal:** Template/navigation standard; begin recreating/optimizing displays; cleanup decommissioned graphics.

**Success criteria:**
- Template project committed; pilot area screens reviewed with operators
- Relabeling plan aligned to P&IDs (ID 11)

**Primary tracker IDs:** 2, 11

## Phase 4 — Alarming, security, trending

**Goal:** Alarm migration path + IdP/AD roles + usable trending; coordinate PSM rationalization.

**Success criteria:**
- Alarm import/rebuild procedure; priority/message standards drafted
- Role matrix implemented against IdP (lab AD or mock)
- Trending UX accepted by sample operators

**Primary tracker IDs:** 3, 7, 20, 22, 30

## Phase 5 — Historian, forms, compliance features

**Goal:** Retention/migrate-vs-archive decision; digitize rounds/forms; audit/setpoint tracking design.

**Success criteria:**
- Historian strategy signed; Tag Historian configured for going-forward
- Priority forms live in Ignition (or phased backlog with FBCO)
- Audit trail approach for safety-critical setpoints documented

**Primary tracker IDs:** 4, 13, 31

## Phase 6 — Process control parity (FBCO-led)

**Goal:** Implement FBCO-specified refrigeration HMI/control improvements once logic is confirmed.

**Success criteria:**
- HOA, timers, PPM display, defrost visibility, sequencing docs implemented per FBCO specs

**Primary tracker IDs:** 18, 19, 25, 37, 38, 39, 45

## Phase 7 — Commissioning, training, cutover

**Goal:** FAT/SAT, training sandbox, cutover/rollback, notifications decision.

**Success criteria:**
- Test plan signed; operators trained; go/no-go checklist complete

**Primary tracker IDs:** 9, 32, 33

## Deferred / parking lot

Wants and pending-input items stay parked until their blockers clear: IDs 6, 12, 14, 40, 42, 48, 49 (NTP can pull forward cheaply in Phase 1). **ID 44 (after-hours notification) is FBCO-only — not One Shot scope.**
