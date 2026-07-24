# Graph Report - C:\Users\dylan.jones\Documents\Bors  (2026-07-23)

## Corpus Check
- 0 files · ~0 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 111 nodes · 64 edges · 73 communities (6 shown, 67 thin omitted)
- Extraction: 83% EXTRACTED · 16% INFERRED · 2% AMBIGUOUS · INFERRED: 10 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- Docker Lab Stack
- Docker Lab Stack
- Docker Lab Stack
- Docker Lab Stack
- Nice to Have Priority
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- Docker Lab Stack
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- MCC OT Network Inventory
- Docker Lab Stack
- Docker Lab Stack

## God Nodes (most connected - your core abstractions)
1. `Subnet 10.80.31.0/24` - 23 edges
2. `RCP PLC 10.80.31.60 CompactLogix 1769` - 13 edges
3. `Quantum HD NH3 Compressors .61-.65` - 8 edges
4. `PowerFlex 525 Evaporator VFDs AU#` - 8 edges
5. `NH3 Pumps 1-2 IEC Starters .127-.128` - 5 edges
6. `Boars Head FactoryTalk to Ignition Migration` - 5 edges
7. `EX FAN PSR 440C-CR30 10.80.31.102` - 4 edges
8. `EX FAN #14/#15 IEC Starters .129-.130` - 4 edges
9. `Stratix Managed ENET Switches` - 3 edges
10. `Phase 2 Lab Route/VPN into 10.80.31.0/24` - 3 edges

## Surprising Connections (you probably didn't know these)
- `Confirm Lab Routing VPN to 10.80.31.0/24` --semantically_similar_to--> `Phase 2 Lab Route/VPN into 10.80.31.0/24`  [INFERRED] [semantically similar]
  .planning/STATE.md → docs/network-inventory.md
- `Validated MCC IP Inventory 10.80.31.0/24` --references--> `Subnet 10.80.31.0/24`  [EXTRACTED]
  .planning/PROJECT.md → docs/network-inventory.md
- `Pumped Liquid Overfeed NH3 System` --conceptually_related_to--> `NH3 Pumps 1-2 IEC Starters .127-.128`  [INFERRED]
  .planning/PROJECT.md → docs/network-inventory.md
- `Boars Head FactoryTalk to Ignition Migration` --references--> `Subnet 10.80.31.0/24`  [EXTRACTED]
  .planning/PROJECT.md → docs/network-inventory.md
- `Confirm Lab Routing VPN to 10.80.31.0/24` --references--> `Subnet 10.80.31.0/24`  [EXTRACTED]
  .planning/STATE.md → docs/network-inventory.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Critical Ignition Architecture Endpoints** — docs_network_inventory_rcp_plc, docs_network_inventory_quantum_hd_compressors, docs_network_inventory_ex_fan_psr_440c, docs_network_inventory_stratix_switches [EXTRACTED 1.00]
- **REFER MCC ENET Segment 10.80.31.0/24** — docs_network_inventory_subnet_10_80_31_0_24, docs_network_inventory_rcp_plc, docs_network_inventory_refer_enet_sw_1, docs_network_inventory_refer_enet_sw_2, docs_network_inventory_powerflex_evaporators, docs_network_inventory_condenser_fans, docs_network_inventory_nh3_pumps, docs_network_inventory_ex_fans [EXTRACTED 1.00]
- **Phase 2 Connectivity and Tracker Scope Links** — _planning_project_tracker_id_10, _planning_project_tracker_id_28, _planning_project_tracker_id_34, _planning_project_tracker_id_37, _planning_project_tracker_id_26, docs_network_inventory_rcp_plc, _planning_state_phase2_prep [INFERRED 0.85]

## Communities (73 total, 67 thin omitted)

### Community 0 - "MCC OT Network Inventory"
Cohesion: 0.18
Nodes (13): Tracker ID 26 PLC NIC Gateway Redundancy LAN, Confirm Lab Routing VPN to 10.80.31.0/24, MCC IP Inventory Ingest Complete, COND 1A FAN MCC 10.80.31.120, Condenser H2O Pumps IEC Starters .124-.126, Condenser Fan PowerFlex VFDs COND 1A/1B/2A/2B, Phase 2 Lab Route/VPN into 10.80.31.0/24, REFER ENET SW 1 Stratix 10.80.31.100 (+5 more)

### Community 1 - "MCC OT Network Inventory"
Cohesion: 0.36
Nodes (8): Boars Head FactoryTalk to Ignition Migration, Validated MCC IP Inventory 10.80.31.0/24, Decision RCP PLC at 10.80.31.60 CompactLogix 1769, Tracker ID 10 PLC/OPC Connectivity, Tracker ID 28 Plant-wide Tag Naming UDTs, Phase 2 Prep Connectivity and Tag UDT Naming, RCP PLC 10.80.31.60 CompactLogix 1769, Refrigeration MCC IPs.xlsx Source Sheet

### Community 2 - "MCC OT Network Inventory"
Cohesion: 0.25
Nodes (8): Decision Compressors Quantum HD .61-.65, Tracker ID 37 SICK Quantum Compressor Sequencing, NH3 Compressor 1 Quantum HD 10.80.31.61, NH3 Compressor 4 Quantum HD 10.80.31.62, NH3 Compressor 5 Quantum HD 10.80.31.63, NH3 Compressor 6 Quantum HD 10.80.31.64, NH3 Compressor 7 Quantum HD 10.80.31.65, Quantum HD NH3 Compressors .61-.65

### Community 3 - "MCC OT Network Inventory"
Cohesion: 0.33
Nodes (6): AU#201-B1 EVAP MCC 10.80.31.104, AU#301-C1 EVAP MCC 10.80.31.105, AU#401-D1 EVAP MCC 10.80.31.106, AU#501-E1 EVAP MCC 10.80.31.107, AU#705-G5 EVAP MCC 10.80.31.119, PowerFlex 525 Evaporator VFDs AU#

### Community 4 - "MCC OT Network Inventory"
Cohesion: 0.40
Nodes (5): Tracker ID 34 440C-CR30 Safety Relay Architecture, EX FAN #14 MCC 10.80.31.129, EX FAN #15 MCC 10.80.31.130, EX FAN PSR 440C-CR30 10.80.31.102, EX FAN #14/#15 IEC Starters .129-.130

### Community 5 - "MCC OT Network Inventory"
Cohesion: 0.50
Nodes (4): Pumped Liquid Overfeed NH3 System, NH3 PUMP 1 MCC 10.80.31.127, NH3 PUMP 2 MCC 10.80.31.128, NH3 Pumps 1-2 IEC Starters .127-.128

## Ambiguous Edges - Review These
- `RCP PLC 10.80.31.60 CompactLogix 1769` → `Quantum HD NH3 Compressors .61-.65`  [AMBIGUOUS]
  docs/network-inventory.md · relation: shares_data_with

## Knowledge Gaps
- **82 isolated node(s):** `Priorities vs Needs & Wants`, `Boars Head FactoryTalk to Ignition Migration`, `Requirements — Boars Head Ignition Migration`, `Roadmap — Boars Head Ignition Migration`, `Project State` (+77 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **67 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `RCP PLC 10.80.31.60 CompactLogix 1769` and `Quantum HD NH3 Compressors .61-.65`?**
  _Edge tagged AMBIGUOUS (relation: shares_data_with) - confidence is low._
- **Why does `Subnet 10.80.31.0/24` connect `MCC OT Network Inventory` to `MCC OT Network Inventory`, `MCC OT Network Inventory`, `MCC OT Network Inventory`, `MCC OT Network Inventory`, `MCC OT Network Inventory`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **Why does `RCP PLC 10.80.31.60 CompactLogix 1769` connect `MCC OT Network Inventory` to `MCC OT Network Inventory`, `MCC OT Network Inventory`, `MCC OT Network Inventory`, `MCC OT Network Inventory`, `MCC OT Network Inventory`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Why does `PowerFlex 525 Evaporator VFDs AU#` connect `MCC OT Network Inventory` to `MCC OT Network Inventory`, `MCC OT Network Inventory`?**
  _High betweenness centrality (0.036) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `RCP PLC 10.80.31.60 CompactLogix 1769` (e.g. with `EX FAN PSR 440C-CR30 10.80.31.102` and `NH3 Pumps 1-2 IEC Starters .127-.128`) actually correct?**
  _`RCP PLC 10.80.31.60 CompactLogix 1769` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `NH3 Pumps 1-2 IEC Starters .127-.128` (e.g. with `Pumped Liquid Overfeed NH3 System` and `RCP PLC 10.80.31.60 CompactLogix 1769`) actually correct?**
  _`NH3 Pumps 1-2 IEC Starters .127-.128` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Priorities vs Needs & Wants`, `Boars Head FactoryTalk to Ignition Migration`, `Requirements — Boars Head Ignition Migration` to the rest of the system?**
  _86 weakly-connected nodes found - possible documentation gaps or missing edges._