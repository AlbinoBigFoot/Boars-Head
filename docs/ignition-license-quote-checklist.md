# Ignition Addon Modules — Cost Estimate Checklist

For distributor / Inductive Automation quote.  
Scope basis: Migration Tracker V6 + One Shot / shared (Both) work.  
**Excludes FBCO-only items** (e.g. ID 44 after-hours SMS/voice).

Architecture to license:

| Role | Version (current plan) | Purpose |
|------|------------------------|---------|
| Standard Gateway | 8.3.7 | Primary development / central gateway |
| Edge Gateway | 8.3.7 | Local mirror of Standard project |
| Database | MSSQL (lab now; prod TBD) | Historian / forms / audit storage |

> SKUs and what counts as “included vs addon” change between 8.1 and 8.3 and by edition. Ask the quote to itemize **platform** vs **modules** separately for Standard and Edge.

---

## 1. Platform (not modules — still needed on the quote)

| Line item | Why | Tracker |
|-----------|-----|---------|
| **Ignition Standard — Unlimited** (or equivalent scale tier) | Unlimited clients/tags called out as Need | ID 1 (FBCO buys; One Shot confirms tag count) |
| **Ignition Edge** (correct Edge SKU for Perspective + EAM agent sync) | Local mirrored gateway | ID 26, 50 |
| **2nd Standard license?** (prod redundancy / RCP↔BH) | Tracker wants redundant gateways | ID 26 — confirm if redundancy pack vs two Standards |
| **Dev/sandbox gateway license?** | Training + parallel run | ID 9 (FBCO) — may reuse trial or spare |

---

## 2. Addon modules — **quote these (recommended Must)**

These are the addons that match One Shot / Both go-live Needs.

| Module | Gateway(s) | Why needed | Tracker IDs |
|--------|------------|------------|-------------|
| **Perspective** | Standard + Edge | Operator HMI, mobile/remote web clients, forms UI | 2, 7, 11, 13 |
| **Enterprise Administration (EAM)** | Standard (controller) + Edge (agent) | Project / config mirror Standard → Edge | 26, 50 |
| **Tag Historian** | Standard (and Edge if local history required) | Going-forward history + trending UI | 4 (Want), **22 (Need)** |
| **Alarm Notification** | Standard (Edge only if local pipelines needed) | Email (and pipeline) alarm notifications on-site; **not** for after-hours SMS (that’s FBCO ID 44) | 3, 30 |

### Drivers (usually platform-included — confirm, don’t assume free)

| Driver / connectivity | Why | Tracker |
|-----------------------|-----|---------|
| **Logix / Allen-Bradley EtherNet/IP** | CompactLogix RCP PLC `10.80.31.60` | 10 |
| OPC UA (platform) | Fallback / vendor devices if not via PLC | 10, 37 |

If distributor lists drivers as separate SKUs, add Logix to the quote.

---

## 3. Addon modules — **quote as Options (Want / nice)**

| Module | Why | Tracker | Recommendation |
|--------|-----|---------|----------------|
| **Reporting** | Shift/production KPI reports | 6 (Want) | Option line — not go-live blocker |
| **Vision** | Tracker allows “Perspective and/or Vision”; only if client insists on Vision clients | 2 | Option — prefer Perspective-only unless FBCO requires Vision |
| **SQL Bridge** (Transaction Groups) | Digitized rounds/forms → MSSQL without heavy scripting | 13 | Option — strong fit for forms/logs |
| **Symbol Factory** | Faster HMI symbol library for graphics rebuild | 2, 11 | Option |
| **Web Developer** | Custom HTTP/APIs or non-Perspective pages | 13, 42 | Option — only if scope needs it |

---

## 4. Do **not** put on One Shot estimate (unless FBCO requests)

| Module | Reason |
|--------|--------|
| **SMS Notification** | ID 44 is FBCO-only (Emergency 24 vs Ignition) |
| **Voice Notification** | Same as above |
| Sepasoft / other MES | Forms planned in Perspective + DB, not MES suite |
| Cirrus Link MQTT | Not in current architecture |
| Third-party Quantum/Frick driver | Assume compressor data via PLC unless FBCO proves otherwise (ID 37) |

---

## 5. Suggested quote packages (for the salesperson)

### Package A — Go-live minimum (One Shot Needs)

1. Standard Unlimited platform  
2. Edge (sync-capable SKU)  
3. Perspective (Std + Edge as required by Edge edition)  
4. EAM  
5. Tag Historian  
6. Alarm Notification (email pipelines)  
7. Confirm Logix driver included  

### Package B — Package A + likely forms/history extras

Everything in A, plus:

8. SQL Bridge  
9. Reporting (if FBCO funds Want ID 6 now)  
10. Symbol Factory (graphics productivity)

### Package C — Only if FBCO decides later

11. Vision  
12. SMS Notification / Voice Notification (ID 44)  
13. Extra Standard license for redundancy pair  

---

## 6. Open questions that change the quote

1. **Perspective-only vs Vision too?** (ID 2)  
2. **Historian on Edge as well as Standard?** (store-and-forward vs central only)  
3. **Prod redundancy = 2× Standard licenses?** (ID 26)  
4. **Stay on 8.1 Standard or move both to 8.3?** (affects SKUs / upgrade path)  
5. **Will Quantum compressors ever be polled outside the PLC?** (could add OPC/third-party later)

---

## 7. One-page ask for the distributor

Please quote **Package A** and **Package B** as separate totals, with line-item module prices, for:

- 1× Ignition Standard (Unlimited), version **8.1.x** (and optional price delta to **8.3.x**)  
- 1× Ignition Edge **8.3.x** suitable for EAM project sync + Perspective  
- Modules listed in §2 (Must) and §3 (Options as alternates)  
- Annual support/renewal for each line  

Site context: ammonia refrigeration HMI migration; primary PLC Allen-Bradley CompactLogix; MSSQL for DB-backed features.

---

*Generated for cost estimating — not a binding BOM. Confirm final SKUs with authorized Inductive Automation distributor.*
