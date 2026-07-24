# Refrigeration MCC / Controls Network Inventory

Source: `Refrigeration MCC IPs.xlsx`  
Subnet (observed): `10.80.31.0/24`  
Note from sheet: *Highlighted cells are subject to IP address changes.*

## Critical endpoints (Ignition / architecture)

| IP | Device | Type | Relevance |
|----|--------|------|-----------|
| 10.80.31.60 | RCP PLC | CompactLogix 1769 | Primary PLC target for Ignition EtherNet/IP (tracker ID 10) |
| 10.80.31.61–.65 | NH3 Compressors 1,4–7 | Quantum HD (Frick/JCI) | Compressor sequencing / SICK Quantum panels (ID 37) |
| 10.80.31.102 | EX FAN PSR 440C | 440C-CR30 safety relay | Safety interlock architecture (ID 34) |
| 10.80.31.100 / .101 | REFER ENET SW 1/2 | Stratix 20-port | OT switch fabric for MCC LAN |

## Full inventory

| IP | Device Name | Device Type | Manufacturer |
|----|-------------|-------------|--------------|
| 10.80.31.60 | RCP PLC | CompactLogix 1769 PLC | Rockwell/Allen-Bradley |
| 10.80.31.61 | NH3 Compressor 1 | Quantum HD Compressor Controller | Frick/Johnson Controls |
| 10.80.31.62 | NH3 Compressor 4 | Quantum HD Compressor Controller | Frick/Johnson Controls |
| 10.80.31.63 | NH3 Compressor 5 | Quantum HD Compressor Controller | Frick/Johnson Controls |
| 10.80.31.64 | NH3 Compressor 6 | Quantum HD Compressor Controller | Frick/Johnson Controls |
| 10.80.31.65 | NH3 Compressor 7 | Quantum HD Compressor Controller | Frick/Johnson Controls |
| 10.80.31.100 | REFER ENET SW 1 | Stratix managed ENET switch 20-port | Rockwell/Allen-Bradley |
| 10.80.31.101 | REFER ENET SW 2 | Stratix managed ENET switch 20-port | Rockwell/Allen-Bradley |
| 10.80.31.102 | EX FAN PSR 440C | A-B 440C-CR30 programmable safety relay | Rockwell/Allen-Bradley |
| 10.80.31.103 | REFER MCC DPM | Digital power meter MCC bucket | Rockwell/Allen-Bradley |
| 10.80.31.104 | AU#201-B1 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.105 | AU#301-C1 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.106 | AU#401-D1 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.107 | AU#501-E1 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.108 | AU#502-E2 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.109 | AU#503-E3 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.110 | AU#504-E4 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.111 | AU#601-F1 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.112 | AU#602-F2 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.113 | AU#603-F3 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.114 | AU#604-F4 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.115 | AU#701-G1 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.116 | AU#702-G2 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.117 | AU#703-G3 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.118 | AU#704-G4 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.119 | AU#705-G5 EVAP MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.120 | COND 1A FAN MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.121 | COND 1B FAN MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.122 | COND 2A FAN MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.123 | COND 2B FAN MCC | PowerFlex 525 VFD | Rockwell/Allen-Bradley |
| 10.80.31.124 | COND H2O PUMP 1 MCC | IEC motor starter | Rockwell/Allen-Bradley |
| 10.80.31.125 | COND H2O PUMP 2 MCC | IEC motor starter | Rockwell/Allen-Bradley |
| 10.80.31.126 | COND H2O PUMP 3 MCC | IEC motor starter | Rockwell/Allen-Bradley |
| 10.80.31.127 | NH3 PUMP 1 MCC | IEC motor starter | Rockwell/Allen-Bradley |
| 10.80.31.128 | NH3 PUMP 2 MCC | IEC motor starter | Rockwell/Allen-Bradley |
| 10.80.31.129 | EX FAN #14 MCC | IEC motor starter | Rockwell/Allen-Bradley |
| 10.80.31.130 | EX FAN #15 MCC | IEC motor starter | Rockwell/Allen-Bradley |

## Device counts (for UDT / driver planning)

| Class | Count | Typical Ignition approach |
|-------|------:|---------------------------|
| CompactLogix PLC | 1 | Native EtherNet/IP → Logix driver |
| Quantum HD compressors | 5 | Confirm protocol (often via PLC or vendor OPC) |
| Stratix switches | 2 | Monitor only / SNMP later |
| 440C-CR30 safety relay | 1 | Read status via PLC LAN if exposed |
| PowerFlex 525 VFDs | 20 | Usually via PLC tags; direct EIP optional |
| IEC motor starters | 7 | Via PLC |

## Implications for Phase 2 (connectivity + tags)

1. Lab gateways need a route/VPN/jump into `10.80.31.0/24` (or a mirrored PLC) before live browse of `10.80.31.60`.
2. Tag naming (ID 28) should align AU# evaporator IDs and compressor numbers already used on this sheet.
3. Tracker ID 26 note about adding a PLC NIC for gateway/redundancy LAN remains relevant — this list is the existing REFER MCC ENET segment.
