---
title: Audit Profiles
sidebar_position: 8
description: DevAudit (gateway and Designer changes) and OpsAudit (operator actions from the HMI), their tables and retention.
sources:
  - gateways/standard/data/config/resources/core/ignition/audit-profile/*/config.json
  - gateways/standard/data/config/resources/core/ignition/security-properties/config.json
last_verified: 2026-10-23
---

# Audit Profiles

**Where:** Platform > Security > Audit Profiles (`ignition/audit-profile/<name>/config.json`, tracked in git).

An **audit profile** is a destination for audit events (who did what, when, from where). Two exist:

| Profile | Purpose | Table | Columns Of Note | Retention |
|---|---|---|---|---|
| **`DevAudit`** | The **gateway's own** audit profile (Platform > Security > General Settings > Gateway Audit Profile): config changes, Designer saves, logins | `dev_audit_events` | `dev_action`, `dev_action_target`, `action_value`, `actor`, `actor_host`, `originating_system`, `originating_context`, `status_code`, `event_timestamp` | 90 days, pruned |
| **`OpsAudit`** | **Operator actions** written by the HMI scripts: setpoint and mode writes, commands, Out Of Service, acknowledgements | `ops_audit_events` | `action`, `action_target`, `action_value`, `actor`, `actor_host`, ... | 90 days, pruned |

Both are database profiles on the `ignition` connection with `autoCreate: true`, so the gateway creates the tables.
(`audit_events` in the database is an older, empty default table.)

## How OpsAudit Is Written

- Every HMI write that matters goes through `shared.Audit.writeTag` (or `shared.Alerts.confirmApplyWrite`, which calls
  it). It writes the tag, checks the result quality, and on success logs an OpsAudit event with
  `system.util.audit` (action, target tag, old and new value, user, host).
- A write refused by the PLC write lock or the OPC block returns bad quality and logs **no** event.
- `shared.OutOfService` and `shared.Forms` add their own entries.
- The profile is `OpsAudit` (Gateway web UI > Config > Security > Audit Profiles); the `shared.Audit` script writes to it.

**Read it:** Admin > **Audit Log** page in the HMI (named query `OpsAudit/AuditLog`, permission row `AuditLog/View`,
Engineering and up). The page was rebuilt on 2026-10-23; see
[Features](../features/index.md).

## Checks

- Row counts on 2026-10-23: `ops_audit_events` about 9,900, `dev_audit_events` about 1,800.
- A note from 2026-10-22 said OpsAudit had recorded nothing since 2026-10-02; rows exist now, but if the Audit Log page
  looks empty, check the profile's status on the Audit Profiles page and Store & Forward.
