---
title: "Named Queries: OpsForms"
sidebar_label: "OpsForms"
description: "Named queries under OpsForms/: SQL, parameters and callers."
generated: true
custom_edit_url: null
---

:::note

:::

Designer: **Project Browser > Data > Named Queries > OpsForms**. Files: `gateways/standard/data/projects/BH/ignition/named-query/OpsForms/<Query>/query.sql + resource.json`.

| Query | Type | Parameters | Callers |
|---|---|---|---|
| [`OpsForms/Pid/Check`](#opsforms-pid-check) | `Query` | `cycleId, valvePk` | 1 |
| [`OpsForms/Pid/CompleteCycle`](#opsforms-pid-completecycle) | `UpdateQuery` | `id, user, now` | 1 |
| [`OpsForms/Pid/CreateCycle`](#opsforms-pid-createcycle) | `UpdateQuery` | `year, revision, performedBy, reviewedBy, user, now` | 1 |
| [`OpsForms/Pid/CycleById`](#opsforms-pid-cyclebyid) | `Query` | `id` | 1 |
| [`OpsForms/Pid/Cycles`](#opsforms-pid-cycles) | `Query` | `viewAll, username` | 1 |
| [`OpsForms/Pid/OpenCycle`](#opsforms-pid-opencycle) | `Query` | | 2 |
| [`OpsForms/Pid/Rows`](#opsforms-pid-rows) | `Query` | `cycleId, category, unit, search, show` | 2 |
| [`OpsForms/Pid/SaveCheck`](#opsforms-pid-savecheck) | `UpdateQuery` | `cycleId, valvePk, verified, verifiedBy, verifiedDate, notes, user, now` | 1 |
| [`OpsForms/Pid/Summary`](#opsforms-pid-summary) | `Query` | `cycleId` | 2 |
| [`OpsForms/Pid/Units`](#opsforms-pid-units) | `Query` | `category` | 1 |
| [`OpsForms/Pid/UpdateCycleHeader`](#opsforms-pid-updatecycleheader) | `UpdateQuery` | `id, revision, performedBy, reviewedBy` | 1 |
| [`OpsForms/Pid/UserChecks`](#opsforms-pid-userchecks) | `Query` | `cycleId, username` | 1 |
| [`OpsForms/Submission/Get`](#opsforms-submission-get) | `Query` | `id, viewAll, username` | 2 |
| [`OpsForms/Submission/Insert`](#opsforms-submission-insert) | `UpdateQuery` | `formType, formDate, submittedBy, submittedName, submittedAt, shiftStatus, isAbnormal, releaseLogged, openItems, summary, data` | 1 |
| [`OpsForms/Submission/List`](#opsforms-submission-list) | `Query` | `formType, startDate, endDate, viewAll, username, userFilter` | 1 |
| [`OpsForms/Submission/Users`](#opsforms-submission-users) | `Query` | `viewAll` | 1 |

## OpsForms/Pid/Check {#opsforms-pid-check}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Pid/Check` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:cycleId` | Parameter | `Int4` |
| `:valvePk` | Parameter | `Int4` |

```sql
SELECT v.valve_pk, v.category, v.pid, v.unit_id, v.unit_desc, v.valve_id, v.size, v.valve_type, v.position,
       v.function_service, CAST(COALESCE(c.verified, 0) AS BIT) AS verified, c.verified_by, c.verified_date, c.notes,
       c.updated_by, c.updated_at
FROM dbo.ops_pid_valve v
LEFT JOIN dbo.ops_pid_check c ON c.valve_pk = v.valve_pk AND c.cycle_id = :cycleId
WHERE v.valve_pk = :valvePk
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms.pidCheck` | script | |

## OpsForms/Pid/CompleteCycle {#opsforms-pid-completecycle}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Pid/CompleteCycle` |
| Type | `UpdateQuery` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:id` | Parameter | `Int4` |
| `:user` | Parameter | `String` |
| `:now` | Parameter | `DateTime` |

```sql
UPDATE dbo.ops_pid_cycle
SET status = N'Complete', completed_by = :user, completed_at = :now
WHERE id = :id AND status = N'Open'
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms.pidComplete` | script | |

## OpsForms/Pid/CreateCycle {#opsforms-pid-createcycle}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Pid/CreateCycle` |
| Type | `UpdateQuery` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:year` | Parameter | `Int4` |
| `:revision` | Parameter | `String` |
| `:performedBy` | Parameter | `String` |
| `:reviewedBy` | Parameter | `String` |
| `:user` | Parameter | `String` |
| `:now` | Parameter | `DateTime` |

```sql
INSERT INTO dbo.ops_pid_cycle (cycle_year, drawing_revision, performed_by, reviewed_by, status, created_by, created_at)
VALUES (:year, NULLIF(:revision, ''), NULLIF(:performedBy, ''), NULLIF(:reviewedBy, ''), N'Open', :user, :now)
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms.pidStartCycle` | script | |

## OpsForms/Pid/CycleById {#opsforms-pid-cyclebyid}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Pid/CycleById` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:id` | Parameter | `Int4` |

```sql
SELECT id, cycle_year, drawing_revision, performed_by, reviewed_by, status, created_by, created_at, completed_by,
       completed_at
FROM dbo.ops_pid_cycle
WHERE id = :id
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms._pidCycle` | script | |

## OpsForms/Pid/Cycles {#opsforms-pid-cycles}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Pid/Cycles` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:viewAll` | Parameter | `Boolean` |
| `:username` | Parameter | `String` |

```sql
-- open cycles: every Forms user; completed: Forms/ViewAll, or cycles the session user recorded checks in
SELECT cy.id, cy.cycle_year, cy.status, cy.drawing_revision, cy.performed_by, cy.reviewed_by, cy.created_by,
       cy.created_at, cy.completed_by, cy.completed_at,
       (SELECT COUNT(*) FROM dbo.ops_pid_valve) AS total,
       (SELECT COUNT(*) FROM dbo.ops_pid_check c WHERE c.cycle_id = cy.id AND c.verified = 1) AS verified,
       (SELECT COUNT(*) FROM dbo.ops_pid_check c WHERE c.cycle_id = cy.id AND COALESCE(c.notes, '') <> '') AS disc
FROM dbo.ops_pid_cycle cy
WHERE :username <> ''
  AND (cy.status = N'Open' OR :viewAll = 1
       OR EXISTS (SELECT 1 FROM dbo.ops_pid_check_log l WHERE l.cycle_id = cy.id AND l.updated_by = :username))
ORDER BY cy.cycle_year DESC, cy.id DESC
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms.pidCycles` | script | |

## OpsForms/Pid/OpenCycle {#opsforms-pid-opencycle}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Pid/OpenCycle` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

```sql
SELECT TOP 1 id, cycle_year, drawing_revision, performed_by, reviewed_by, status, created_by, created_at,
       completed_by, completed_at
FROM dbo.ops_pid_cycle
WHERE status = N'Open'
ORDER BY id DESC
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms.pidOpenCycle` | script | |
| `shared.Forms.pidStartCycle` | script | |

## OpsForms/Pid/Rows {#opsforms-pid-rows}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Pid/Rows` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:cycleId` | Parameter | `Int4` |
| `:category` | Parameter | `String` |
| `:unit` | Parameter | `String` |
| `:search` | Parameter | `String` |
| `:show` | Parameter | `String` |

```sql
SELECT v.valve_pk, v.category, v.pid, v.unit_id, v.unit_desc, v.valve_id, v.size, v.valve_type, v.position,
       v.function_service, CAST(COALESCE(c.verified, 0) AS BIT) AS verified, c.verified_by, c.verified_date, c.notes,
       c.updated_by, c.updated_at
FROM dbo.ops_pid_valve v
LEFT JOIN dbo.ops_pid_check c ON c.valve_pk = v.valve_pk AND c.cycle_id = :cycleId
WHERE (:category = '' OR v.category = :category)
  AND (:unit = '' OR v.unit_id = :unit)
  AND (:search = ''
       OR v.valve_id LIKE '%' + :search + '%' OR v.unit_id LIKE '%' + :search + '%'
       OR v.function_service LIKE '%' + :search + '%' OR v.size LIKE '%' + :search + '%'
       OR v.valve_type LIKE '%' + :search + '%' OR c.notes LIKE '%' + :search + '%'
       OR c.verified_by LIKE '%' + :search + '%')
  AND (:show = 'All'
       OR (:show = 'Remaining' AND COALESCE(c.verified, 0) = 0)
       OR (:show = 'Verified' AND c.verified = 1)
       OR (:show = 'Discrepancies' AND COALESCE(c.notes, '') <> '')
       OR (:show = 'Incomplete' AND c.verified = 1 AND COALESCE(c.verified_by, '') = ''))
ORDER BY v.sort_order
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms._pidReportData` | script | |
| `shared.Forms.pidRows` | script | |

## OpsForms/Pid/SaveCheck {#opsforms-pid-savecheck}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Pid/SaveCheck` |
| Type | `UpdateQuery` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:cycleId` | Parameter | `Int4` |
| `:valvePk` | Parameter | `Int4` |
| `:verified` | Parameter | `Boolean` |
| `:verifiedBy` | Parameter | `String` |
| `:verifiedDate` | Parameter | `String` |
| `:notes` | Parameter | `String` |
| `:user` | Parameter | `String` |
| `:now` | Parameter | `DateTime` |

```sql
-- upsert the check of this cycle + append the audit row; only while the cycle is open
IF EXISTS (SELECT 1 FROM dbo.ops_pid_cycle WHERE id = :cycleId AND status = N'Open')
BEGIN
    MERGE dbo.ops_pid_check AS t
    USING (SELECT :cycleId AS cycle_id, :valvePk AS valve_pk) AS s
        ON t.cycle_id = s.cycle_id AND t.valve_pk = s.valve_pk
    WHEN MATCHED THEN UPDATE SET
        verified = :verified, verified_by = NULLIF(:verifiedBy, ''),
        verified_date = TRY_CAST(NULLIF(:verifiedDate, '') AS DATE), notes = NULLIF(:notes, ''),
        updated_by = :user, updated_at = :now
    WHEN NOT MATCHED THEN INSERT (cycle_id, valve_pk, verified, verified_by, verified_date, notes, updated_by, updated_at)
        VALUES (:cycleId, :valvePk, :verified, NULLIF(:verifiedBy, ''), TRY_CAST(NULLIF(:verifiedDate, '') AS DATE),
                NULLIF(:notes, ''), :user, :now);
    INSERT INTO dbo.ops_pid_check_log (cycle_id, valve_pk, verified, verified_by, verified_date, notes, updated_by, updated_at)
    VALUES (:cycleId, :valvePk, :verified, NULLIF(:verifiedBy, ''), TRY_CAST(NULLIF(:verifiedDate, '') AS DATE),
            NULLIF(:notes, ''), :user, :now);
END
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms.pidSaveCheck` | script | |

## OpsForms/Pid/Summary {#opsforms-pid-summary}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Pid/Summary` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:cycleId` | Parameter | `Int4` |

```sql
SELECT v.category, MIN(v.category_order) AS category_order, COUNT(*) AS total,
       SUM(CASE WHEN c.verified = 1 THEN 1 ELSE 0 END) AS verified,
       SUM(CASE WHEN COALESCE(c.notes, '') <> '' THEN 1 ELSE 0 END) AS disc,
       SUM(CASE WHEN c.verified = 1 AND COALESCE(c.verified_by, '') = '' THEN 1 ELSE 0 END) AS incomplete
FROM dbo.ops_pid_valve v
LEFT JOIN dbo.ops_pid_check c ON c.valve_pk = v.valve_pk AND c.cycle_id = :cycleId
GROUP BY v.category
ORDER BY MIN(v.category_order)
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms._pidReportData` | script | |
| `shared.Forms.pidSummary` | script | |

## OpsForms/Pid/Units {#opsforms-pid-units}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Pid/Units` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:category` | Parameter | `String` |

```sql
SELECT unit_id, MAX(unit_desc) AS unit_desc, COUNT(*) AS n
FROM dbo.ops_pid_valve
WHERE (:category = '' OR category = :category)
GROUP BY unit_id
ORDER BY MIN(sort_order)
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms.pidSummary` | script | |

## OpsForms/Pid/UpdateCycleHeader {#opsforms-pid-updatecycleheader}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Pid/UpdateCycleHeader` |
| Type | `UpdateQuery` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:id` | Parameter | `Int4` |
| `:revision` | Parameter | `String` |
| `:performedBy` | Parameter | `String` |
| `:reviewedBy` | Parameter | `String` |

```sql
UPDATE dbo.ops_pid_cycle
SET drawing_revision = NULLIF(:revision, ''), performed_by = NULLIF(:performedBy, ''), reviewed_by = NULLIF(:reviewedBy, '')
WHERE id = :id AND status = N'Open'
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms.pidSaveHeader` | script | |

## OpsForms/Pid/UserChecks {#opsforms-pid-userchecks}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Pid/UserChecks` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:cycleId` | Parameter | `Int4` |
| `:username` | Parameter | `String` |

```sql
SELECT COUNT(*) AS n FROM dbo.ops_pid_check_log WHERE cycle_id = :cycleId AND updated_by = :username
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms.pidCanView` | script | |

## OpsForms/Submission/Get {#opsforms-submission-get}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Submission/Get` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:id` | Parameter | `Int4` |
| `:viewAll` | Parameter | `Boolean` |
| `:username` | Parameter | `String` |

```sql
SELECT id, form_type, form_date, submitted_by, submitted_name, submitted_at, shift_status, summary, data
FROM dbo.ops_form_submission
WHERE id = :id
  AND (:viewAll = 1 OR (submitted_by = :username AND :username <> ''))
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms.getSubmission` | script | |
| `shared.Forms.reportData` | script | |

## OpsForms/Submission/Insert {#opsforms-submission-insert}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Submission/Insert` |
| Type | `UpdateQuery` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:formType` | Parameter | `String` |
| `:formDate` | Parameter | `String` |
| `:submittedBy` | Parameter | `String` |
| `:submittedName` | Parameter | `String` |
| `:submittedAt` | Parameter | `DateTime` |
| `:shiftStatus` | Parameter | `String` |
| `:isAbnormal` | Parameter | `Boolean` |
| `:releaseLogged` | Parameter | `Boolean` |
| `:openItems` | Parameter | `Boolean` |
| `:summary` | Parameter | `String` |
| `:data` | Parameter | `String` |

```sql
INSERT INTO dbo.ops_form_submission
    (form_type, form_date, submitted_by, submitted_name, submitted_at, shift_status, is_abnormal, release_logged,
     open_items, summary, data)
VALUES
    (:formType, CAST(:formDate AS DATE), :submittedBy, :submittedName, :submittedAt, NULLIF(:shiftStatus, ''),
     :isAbnormal, :releaseLogged, :openItems, :summary, :data)
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms.submit` | script | |

## OpsForms/Submission/List {#opsforms-submission-list}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Submission/List` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:formType` | Parameter | `String` |
| `:startDate` | Parameter | `String` |
| `:endDate` | Parameter | `String` |
| `:viewAll` | Parameter | `Boolean` |
| `:username` | Parameter | `String` |
| `:userFilter` | Parameter | `String` |

```sql
-- Forms/ViewAll sees every user; otherwise only the session user own rows (shared.Forms.history)
SELECT id, form_type, form_date, submitted_by, submitted_name, submitted_at, shift_status, is_abnormal,
       release_logged, open_items, summary
FROM dbo.ops_form_submission
WHERE (:viewAll = 1 OR submitted_by = :username)
  AND :username <> ''
  AND (:formType = '' OR form_type = :formType)
  AND form_date BETWEEN CAST(:startDate AS DATE) AND CAST(:endDate AS DATE)
  AND (:userFilter = '' OR submitted_by = :userFilter)
ORDER BY form_date DESC, id DESC
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms.history` | script | |

## OpsForms/Submission/Users {#opsforms-submission-users}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OpsForms/Submission/Users` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:viewAll` | Parameter | `Boolean` |

```sql
SELECT submitted_by, MAX(submitted_name) AS submitted_name
FROM dbo.ops_form_submission
WHERE :viewAll = 1
GROUP BY submitted_by
ORDER BY submitted_by
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Forms.historyUsers` | script | |
