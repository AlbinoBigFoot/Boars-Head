# Requirements — Boars Head Ignition Migration

Derived from migration tracker V6 + platform decisions (2026-07-23).

## User Stories

1. As an operator, I can run the plant from Ignition screens that match current FactoryTalk capability (optimized where practical).
2. As an engineer, I can develop on a Standard gateway and have the project mirrored to a local Edge gateway.
3. As an admin, I can assign named users/roles via IdP/AD instead of one shared login.
4. As PSM/compliance, I can retain alarm/historian/audit evidence required for retention rules.
5. As One Shot, I can version Ignition project files in Git via host-mounted gateway volumes.

## Acceptance Criteria

### Platform (Phase 1)

- [ ] `docker compose up` starts Standard `8.1.43`, Edge `8.3.7`, and MSSQL
- [ ] Gateway data directories live on host under `gateways/` and are Git-trackable (with secrets excluded)
- [ ] MSSQL data uses a named Docker volume (not host-mounted)
- [ ] Both gateways reachable on documented HTTP(S) ports; admin login works from `.env`
- [ ] Documented path for Standard → Edge project mirror (Gateway Network / EAM)

### Foundation (Phase 2+)

- [ ] Tag naming + UDT standard drafted and reviewed with FBCO (ID 28)
- [ ] PLC driver vs OPC hosting decision recorded (ID 10)
- [ ] Screen template + navigation standard exists before mass screen rebuild (ID 2)
- [ ] Alarm migration approach defined; rationalization touchpoints noted (ID 3, 30)
- [ ] IdP/AD role matrix drafted (ID 7)

## Definition of Done (milestone)

Go-live Needs from `.planning/PRIORITIES.md` marked Complete or explicitly deferred with FBCO sign-off; training/cutover plan (ID 9) executed; rollback tested.

## Traceability

| Req theme | Tracker IDs |
|-----------|-------------|
| Licensing | 1 |
| Screens/HMI | 2, 11 |
| Alarming | 3, 20, 30 |
| After-hours notify (FBCO-only) | 44 |
| Historian | 4, 22 |
| Reporting | 6 |
| Security | 7 |
| Training/cutover | 9 |
| PLC/OPC | 10 |
| Forms/PSM digitization | 13 |
| Architecture | 26, 48, 49, 50 |
| Tag/UDT model | 28, 46, 47 |
| Audit/MOC/change/test | 31, 32, 33 |
| Safety / NH3 process | 18, 19, 25, 34, 35, 37–40, 45 |
