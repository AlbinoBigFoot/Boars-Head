# Handoff — RCP1 Simulate mode

**Branch:** `cursor/rcp1-simulate-fix-eb66` (PR #7)

## SIM ON polish (verified)

- Device labels = instance names (`COMP 1`, `HTLR-Pump 1`, `HTR`, …)
- Pumps: `Val_Sts` 2=RUN / 1=STOP (no UNK)
- Tanks: Status 0=OK; RUN text color green (`#228B22`)
- Stub Compressor Amps/FLA/SVP/DisP Hi/Lo@0 disabled (was blanket medium alarms)
- Varied bank: COMP 6 STOP; COMP 7 Alm only; others RUN with different FLA

## Scan order

1. `POST /scan/config`  2. `POST /scan/projects`
