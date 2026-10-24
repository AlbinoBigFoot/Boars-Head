---
title: Rollback
sidebar_position: 4
description: How to undo a production deployment - project, tags, gateway config, SQL - from the backups taken before it.
sources:
  - docs/plc-write-lock.md
last_verified: 2026-10-23
---

# Rollback

A rollback is only as good as the backups taken in step 0 of [Promote To Production](promote-to-production.md#0-prepare).
Decide **before** the deployment what "failed" means (for example: RCP1 not connected after 30 minutes, binding errors
on the Utility Overview, operators can't log in) and who decides to roll back.

## Fastest: Restore The Gateway Backup

1. Platform > System > Backup & Restore > **Restore** the `.gwbk` taken just before the deployment.
2. The gateway restarts with the previous project, tags and config. Everything since the backup is lost, including
   memory tag values changed by operators in between (forms and logs in SQL are unaffected).
3. Verify: RCP1 connected, `Locked = true`, OPC block state as before (ask the system integrator), logins.

## Targeted Rollbacks

| What Broke | Roll Back |
|---|---|
| Views / scripts only | Re-import the previous project export (Gateway web UI project import); restart if stale |
| A UDT change | Re-import the definition from the pre-deployment tag export (Overwrite). Instances follow their definition |
| Tag instances | Re-import the pre-deployment export of that folder |
| A tag group | Edit it back (Gateway web UI > Config > Tags > Tag Groups) to the previous mode and rate |
| Gateway setting | Re-enter the previous value (keep a screenshot/JSON of settings you change) |
| SQL schema | Restore the database backup, or run a reverse script prepared in advance |

## In Git

The lab follows the same rollback through git: `git revert <merge-commit>` on a branch, PR, review, redeploy. Don't
rewrite `main` history.

## After A Rollback

- Write down what happened in the PR / release notes.
- Fix forward in the lab, test, and schedule a new window.
