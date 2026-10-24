---
title: "Named Queries: OutOfService"
sidebar_label: "OutOfService"
description: "Named queries under OutOfService/: SQL, parameters and callers."
generated: true
custom_edit_url: null
---

:::note

:::

Designer: **Project Browser > Data > Named Queries > OutOfService**. Files: `gateways/standard/data/projects/BH/ignition/named-query/OutOfService/<Query>/query.sql + resource.json`.

| Query | Type | Parameters | Callers |
|---|---|---|---|
| [`OutOfService/CloseRecord`](#outofservice-closerecord) | `UpdateQuery` | `id, status, returnedBy, returnedName, returnedAt, returnMemo` | 1 |
| [`OutOfService/Comments`](#outofservice-comments) | `Query` | `allowed, id, refresh` | 1 |
| [`OutOfService/InsertComment`](#outofservice-insertcomment) | `UpdateQuery` | `recordId, username, displayName, createdAt, status, comment` | 1 |
| [`OutOfService/InsertRecord`](#outofservice-insertrecord) | `Query` | `tagPath, deviceName, deviceType, site, area, takenBy, takenName, takenAt, reason, memo, status, isBackfill` | 1 |
| [`OutOfService/OpenCount`](#outofservice-opencount) | `Query` | `allowed, refresh` | 1 |
| [`OutOfService/OpenRecordId`](#outofservice-openrecordid) | `Query` | `tagPath` | 1 |
| [`OutOfService/Record`](#outofservice-record) | `Query` | `allowed, id, now, refresh` | 2 |
| [`OutOfService/Records`](#outofservice-records) | `Query` | `allowed, filter, search, now, refresh, device, startDate, endDate` | 1 |
| [`OutOfService/SetStatus`](#outofservice-setstatus) | `UpdateQuery` | `id, status` | 1 |

## OutOfService/CloseRecord {#outofservice-closerecord}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OutOfService/CloseRecord` |
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
| `:status` | Parameter | `String` |
| `:returnedBy` | Parameter | `String` |
| `:returnedName` | Parameter | `String` |
| `:returnedAt` | Parameter | `DateTime` |
| `:returnMemo` | Parameter | `String` |

```sql
-- Return To Service closes the open record (shared.OutOfService.setOutOfService).
UPDATE dbo.oos_record
SET status = :status,
    returned_by = :returnedBy,
    returned_name = :returnedName,
    returned_at = :returnedAt,
    return_memo = :returnMemo,
    updated_at = :returnedAt
WHERE id = :id
  AND returned_at IS NULL
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.OutOfService._closeRecord` | script | |

## OutOfService/Comments {#outofservice-comments}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OutOfService/Comments` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:allowed` | Parameter | `Int4` |
| `:id` | Parameter | `Int4` |
| `:refresh` | Parameter | `Int4` |

```sql
-- Comment / status thread of a record, oldest first (flex repeater instances: keys = CommentEntry params).
SELECT
    c.id,
    c.display_name,
    c.username,
    CONVERT(VARCHAR(16), c.created_at, 120) AS created_text,
    COALESCE(c.status, N'') AS status,
    c.comment
FROM dbo.oos_comment c
WHERE :allowed = 1
  AND :refresh >= 0
  AND c.record_id = :id
ORDER BY c.created_at, c.id
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog` | view | `binding custom.comments` |

## OutOfService/InsertComment {#outofservice-insertcomment}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OutOfService/InsertComment` |
| Type | `UpdateQuery` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:recordId` | Parameter | `Int4` |
| `:username` | Parameter | `String` |
| `:displayName` | Parameter | `String` |
| `:createdAt` | Parameter | `DateTime` |
| `:status` | Parameter | `String` |
| `:comment` | Parameter | `String` |

```sql
-- Comment / status update on a record, open or returned (shared.OutOfService.addComment).
INSERT INTO dbo.oos_comment (record_id, username, display_name, created_at, status, comment)
VALUES (:recordId, :username, :displayName, :createdAt, :status, :comment)
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.OutOfService.addComment` | script | |

## OutOfService/InsertRecord {#outofservice-insertrecord}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OutOfService/InsertRecord` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:tagPath` | Parameter | `String` |
| `:deviceName` | Parameter | `String` |
| `:deviceType` | Parameter | `String` |
| `:site` | Parameter | `String` |
| `:area` | Parameter | `String` |
| `:takenBy` | Parameter | `String` |
| `:takenName` | Parameter | `String` |
| `:takenAt` | Parameter | `DateTime` |
| `:reason` | Parameter | `String` |
| `:memo` | Parameter | `String` |
| `:status` | Parameter | `String` |
| `:isBackfill` | Parameter | `Int4` |

```sql
-- New Out Of Service record (shared.OutOfService.setOutOfService, inside its transaction); returns the id.
INSERT INTO dbo.oos_record
    (tag_path, device_name, device_type, site, area, taken_by, taken_name, taken_at, reason, memo, status, is_backfill,
     updated_at)
OUTPUT INSERTED.id
VALUES
    (:tagPath, :deviceName, :deviceType, :site, :area, :takenBy, :takenName, :takenAt, :reason, :memo, :status,
     :isBackfill, :takenAt)
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.OutOfService._insertRecord` | script | |

## OutOfService/OpenCount {#outofservice-opencount}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OutOfService/OpenCount` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:allowed` | Parameter | `Int4` |
| `:refresh` | Parameter | `Int8` |

```sql
-- Devices currently out of service (header notes icon badge). refresh only re-runs it.
SELECT COUNT(*) AS open_count
FROM dbo.oos_record
WHERE :allowed = 1
  AND :refresh >= 0
  AND returned_at IS NULL
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/00_Docked/_Assets/OosNotification` | view | `binding custom.count` |

## OutOfService/OpenRecordId {#outofservice-openrecordid}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OutOfService/OpenRecordId` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:tagPath` | Parameter | `String` |

```sql
-- Open record of a device (shared.OutOfService, server side only).
SELECT id
FROM dbo.oos_record
WHERE tag_path = :tagPath
  AND returned_at IS NULL
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.OutOfService._openRecordId` | script | |

## OutOfService/Record {#outofservice-record}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OutOfService/Record` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:allowed` | Parameter | `Int4` |
| `:id` | Parameter | `Int4` |
| `:now` | Parameter | `DateTime` |
| `:refresh` | Parameter | `Int4` |

```sql
-- One Out Of Service record with display text (OutOfServiceLog detail pane, shared.OutOfService.addComment).
SELECT
    r.id,
    r.tag_path,
    r.device_name,
    r.device_type,
    r.site,
    r.area,
    r.taken_by,
    r.taken_name,
    CONVERT(VARCHAR(16), r.taken_at, 120) AS taken_at_text,
    r.reason,
    r.memo,
    CASE WHEN r.is_backfill = 1 AND r.returned_at IS NULL THEN N'Out Of Service (No Record)' ELSE r.status END AS status,
    COALESCE(r.returned_by, N'') AS returned_by,
    COALESCE(r.returned_name, N'') AS returned_name,
    r.returned_at,
    COALESCE(CONVERT(VARCHAR(16), r.returned_at, 120), '') AS returned_at_text,
    COALESCE(r.return_memo, N'') AS return_memo,
    r.is_backfill,
    CASE
        WHEN d.m < 60 THEN CONCAT(d.m, 'm')
        WHEN d.m < 1440 THEN CONCAT(d.m / 60, 'h ', d.m % 60, 'm')
        ELSE CONCAT(d.m / 1440, 'd ', (d.m % 1440) / 60, 'h')
    END AS duration
FROM dbo.oos_record r
CROSS APPLY (SELECT CASE WHEN DATEDIFF(MINUTE, r.taken_at, COALESCE(r.returned_at, :now)) < 0 THEN 0
                    ELSE DATEDIFF(MINUTE, r.taken_at, COALESCE(r.returned_at, :now)) END AS m) d
WHERE :allowed = 1
  AND :refresh >= 0
  AND r.id = :id
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog` | view | `binding custom.record` |
| `shared.OutOfService.addComment` | script | |

## OutOfService/Records {#outofservice-records}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OutOfService/Records` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:allowed` | Parameter | `Int4` |
| `:filter` | Parameter | `String` |
| `:search` | Parameter | `String` |
| `:now` | Parameter | `DateTime` |
| `:refresh` | Parameter | `Int4` |
| `:device` | Parameter | `String` |
| `:startDate` | Parameter | `DateTime` |
| `:endDate` | Parameter | `DateTime` |

```sql
-- Out Of Service log / history list (OutOfServiceLog page). filter = open, returned or all; device = one tag path
-- or empty; records overlapping the start / end dates (open ones run to now); refresh only re-runs it.
-- (No colon-prefixed names in comments: Ignition turns them into JDBC placeholders.)
SELECT
    r.id,
    r.device_name,
    r.device_type,
    r.area,
    CASE WHEN r.is_backfill = 1 AND r.returned_at IS NULL THEN N'Out Of Service (No Record)' ELSE r.status END AS status,
    r.taken_name,
    r.taken_at,
    r.reason,
    LEFT(REPLACE(REPLACE(r.memo, CHAR(13), N' '), CHAR(10), N' '), 300) AS memo_excerpt,
    CONCAT(r.device_name, N';;', r.area, CASE WHEN r.device_type <> N'' THEN N' · ' + r.device_type ELSE N'' END)
        AS device_cell,
    CONCAT(CASE WHEN r.is_backfill = 1 AND r.returned_at IS NULL THEN N'Out Of Service (No Record)' ELSE r.status END, N';;', COALESCE(r.reason, N'')) AS status_cell,
    CONCAT(r.taken_name, N';;', FORMAT(r.taken_at, 'yyyy-MM-dd HH:mm')) AS taken_cell,
    CASE
        WHEN d.m < 60 THEN CONCAT(d.m, 'm')
        WHEN d.m < 1440 THEN CONCAT(d.m / 60, 'h ', d.m % 60, 'm')
        ELSE CONCAT(d.m / 1440, 'd ', (d.m % 1440) / 60, 'h')
    END AS duration,
    r.tag_path,
    r.returned_at
FROM dbo.oos_record r
CROSS APPLY (SELECT CASE WHEN DATEDIFF(MINUTE, r.taken_at, COALESCE(r.returned_at, :now)) < 0 THEN 0
                    ELSE DATEDIFF(MINUTE, r.taken_at, COALESCE(r.returned_at, :now)) END AS m) d
WHERE :allowed = 1
  AND :refresh >= 0
  AND (COALESCE(:device, '') = '' OR r.tag_path = :device)
  AND r.taken_at <= :endDate
  AND COALESCE(r.returned_at, :now) >= :startDate
  AND (
        :filter = 'all'
        OR (:filter = 'returned' AND r.returned_at IS NOT NULL)
        OR (:filter NOT IN ('all', 'returned') AND r.returned_at IS NULL)
      )
  AND (
        COALESCE(:search, '') = ''
        OR r.device_name LIKE :search
        OR r.tag_path LIKE :search
        OR r.area LIKE :search
        OR r.device_type LIKE :search
        OR r.reason LIKE :search
      )
ORDER BY CASE WHEN r.returned_at IS NULL THEN 0 ELSE 1 END, r.taken_at DESC, r.id DESC
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog` | view | `binding custom.records` |

## OutOfService/SetStatus {#outofservice-setstatus}

| Setting | Value |
|---|---|
| Path (what callers pass) | `OutOfService/SetStatus` |
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
| `:status` | Parameter | `String` |

```sql
-- Status change carried by a comment (shared.OutOfService.addComment); only while the record is open.
UPDATE dbo.oos_record
SET status = :status,
    updated_at = SYSDATETIME()
WHERE id = :id
  AND returned_at IS NULL
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.OutOfService.addComment` | script | |
