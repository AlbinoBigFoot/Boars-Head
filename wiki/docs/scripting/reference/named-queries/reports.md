---
title: "Named Queries: Reports"
sidebar_label: "Reports"
description: "Named queries under Reports/: SQL, parameters and callers."
generated: true
custom_edit_url: null
---

:::note

:::

Designer: **Project Browser > Data > Named Queries > Reports**. Files: `gateways/standard/data/projects/BH/ignition/named-query/Reports/<Query>/query.sql + resource.json`.

| Query | Type | Parameters | Callers |
|---|---|---|---|
| [`Reports/Alarms/Events`](#reports-alarms-events) | `Query` | `start, end, areas, devices, priorities, shifts, n` | 1 |
| [`Reports/Alarms/Facts`](#reports-alarms-facts) | `Query` | `start, end, areas, devices, priorities, shifts, grain, groupBy` | 1 |
| [`Reports/Alarms/Options`](#reports-alarms-options) | `Query` | `start, end, areas, devices, priorities, shifts` | 1 |
| [`Reports/Alarms/Top`](#reports-alarms-top) | `Query` | `start, end, areas, devices, priorities, shifts, dim, orderBy, n` | 1 |
| [`Reports/Forms/Submissions`](#reports-forms-submissions) | `Query` | `start, end, username, viewAll` | 1 |
| [`Reports/History/Coverage`](#reports-history-coverage) | `Query` | `paths` | 1 |
| [`Reports/History/FirstSample`](#reports-history-firstsample) | `Query` | `paths` | 1 |
| [`Reports/OOS/Options`](#reports-oos-options) | `Query` | | 1 |
| [`Reports/OOS/Records`](#reports-oos-records) | `Query` | `start, end` | 1 |
| [`Reports/Runs/Get`](#reports-runs-get) | `Query` | `id, username` | 1 |
| [`Reports/Runs/Insert`](#reports-runs-insert) | `UpdateQuery` | `username, source, title, definition, format, now` | 1 |
| [`Reports/Runs/LastByTitle`](#reports-runs-lastbytitle) | `Query` | `username` | 1 |
| [`Reports/Runs/List`](#reports-runs-list) | `Query` | `username, viewAll` | 1 |
| [`Reports/Runs/Recent`](#reports-runs-recent) | `Query` | `username` | 1 |
| [`Reports/Templates/Delete`](#reports-templates-delete) | `UpdateQuery` | `id, username, manage` | 1 |
| [`Reports/Templates/Get`](#reports-templates-get) | `Query` | `id, username` | 1 |
| [`Reports/Templates/Insert`](#reports-templates-insert) | `UpdateQuery` | `name, source, definition, username, ownerName, isShared, now` | 1 |
| [`Reports/Templates/List`](#reports-templates-list) | `Query` | `username` | 1 |
| [`Reports/Templates/NameTaken`](#reports-templates-nametaken) | `Query` | `username, name, id` | 1 |
| [`Reports/Templates/Update`](#reports-templates-update) | `UpdateQuery` | `id, name, source, definition, isShared, now, username, manage` | 1 |

## Reports/Alarms/Events {#reports-alarms-events}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Alarms/Events` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:start` | Parameter | `String` |
| `:end` | Parameter | `String` |
| `:areas` | Parameter | `String` |
| `:devices` | Parameter | `String` |
| `:priorities` | Parameter | `String` |
| `:shifts` | Parameter | `String` |
| `:n` | Parameter | `Int4` |

```sql
WITH ev AS (
    SELECT e.eventid,
           MIN(CASE WHEN e.eventtype = 0 THEN e.eventtime END) AS act,
           MIN(CASE WHEN e.eventtype = 1 THEN e.eventtime END) AS clr,
           MIN(CASE WHEN e.eventtype = 2 THEN e.eventtime END) AS ack,
           MAX(e.priority) AS priority,
           MIN(e.source) AS source
    FROM dbo.alarm_events e
    WHERE e.eventtime >= CAST(:start AS datetime2) AND e.eventtime < DATEADD(day, 3, CAST(:end AS datetime2))
    GROUP BY e.eventid
), p AS (
    SELECT ev.*, SUBSTRING(ev.source, CHARINDEX(':/tag:', ev.source) + 6, 4000) AS path,
           SUBSTRING(ev.source, CHARINDEX(':/alm:', ev.source) + 6, 255) AS alarm,
           DATEPART(hour, ev.act) AS hr
    FROM ev
    WHERE ev.act >= CAST(:start AS datetime2) AND ev.act < CAST(:end AS datetime2)
), s AS (
    SELECT p.*, i2, i3, i4, CHARINDEX('/', p.path, i4 + 1) AS i5
    FROM p
    CROSS APPLY (SELECT CHARINDEX('/', p.path) AS i1) a1
    CROSS APPLY (SELECT CHARINDEX('/', p.path, i1 + 1) AS i2) a2
    CROSS APPLY (SELECT CHARINDEX('/', p.path, i2 + 1) AS i3) a3
    CROSS APPLY (SELECT CHARINDEX('/', p.path, i3 + 1) AS i4) a4
), a AS (
    SELECT act, clr, ack, priority, alarm, hr,
           CASE WHEN path LIKE 'Boars[_]Head/%' AND i3 > i2 THEN SUBSTRING(path, i2 + 1, i3 - i2 - 1)
                ELSE N'Other' END AS area,
           CASE WHEN path LIKE 'Boars[_]Head/%' AND i5 > i4 THEN SUBSTRING(path, i4 + 1, i5 - i4 - 1)
                WHEN path LIKE 'Boars[_]Head/%' AND i4 > i3 THEN SUBSTRING(path, i3 + 1, i4 - i3 - 1)
                ELSE N'Other' END AS device,
           CASE WHEN hr >= 7 AND hr < 15 THEN 'A' WHEN hr >= 15 AND hr < 23 THEN 'B' ELSE 'C' END AS shift
    FROM s
), f AS (
    SELECT * FROM a
    WHERE (:areas = N'' OR area IN (SELECT LTRIM(value) FROM STRING_SPLIT(:areas, '|')))
      AND (:devices = N'' OR area + N'/' + device IN (SELECT LTRIM(value) FROM STRING_SPLIT(:devices, '|')))
      AND (:priorities = N'' OR CAST(priority AS nvarchar(2)) IN (SELECT value FROM STRING_SPLIT(:priorities, ',')))
      AND (:shifts = N'' OR shift IN (SELECT value FROM STRING_SPLIT(:shifts, ',')))
)

-- Event List section of the Alarms source: the latest activations in the window (one row per activation)
SELECT TOP (:n) CONVERT(varchar(19), act, 120) AS act, alarm, area, device, priority,
       CASE WHEN ack IS NOT NULL THEN DATEDIFF_BIG(millisecond, act, ack) / 60000.0 END AS ack_min,
       CASE WHEN clr IS NOT NULL THEN DATEDIFF_BIG(millisecond, act, clr) / 60000.0 END AS clr_min
FROM f
ORDER BY act DESC
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports._almRecords` | script | |

## Reports/Alarms/Facts {#reports-alarms-facts}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Alarms/Facts` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:start` | Parameter | `String` |
| `:end` | Parameter | `String` |
| `:areas` | Parameter | `String` |
| `:devices` | Parameter | `String` |
| `:priorities` | Parameter | `String` |
| `:shifts` | Parameter | `String` |
| `:grain` | Parameter | `String` |
| `:groupBy` | Parameter | `String` |

```sql
WITH ev AS (
    SELECT e.eventid,
           MIN(CASE WHEN e.eventtype = 0 THEN e.eventtime END) AS act,
           MIN(CASE WHEN e.eventtype = 1 THEN e.eventtime END) AS clr,
           MIN(CASE WHEN e.eventtype = 2 THEN e.eventtime END) AS ack,
           MAX(e.priority) AS priority,
           MIN(e.source) AS source
    FROM dbo.alarm_events e
    WHERE e.eventtime >= CAST(:start AS datetime2) AND e.eventtime < DATEADD(day, 3, CAST(:end AS datetime2))
    GROUP BY e.eventid
), p AS (
    SELECT ev.*, SUBSTRING(ev.source, CHARINDEX(':/tag:', ev.source) + 6, 4000) AS path,
           SUBSTRING(ev.source, CHARINDEX(':/alm:', ev.source) + 6, 255) AS alarm,
           DATEPART(hour, ev.act) AS hr
    FROM ev
    WHERE ev.act >= CAST(:start AS datetime2) AND ev.act < CAST(:end AS datetime2)
), s AS (
    SELECT p.*, i2, i3, i4, CHARINDEX('/', p.path, i4 + 1) AS i5
    FROM p
    CROSS APPLY (SELECT CHARINDEX('/', p.path) AS i1) a1
    CROSS APPLY (SELECT CHARINDEX('/', p.path, i1 + 1) AS i2) a2
    CROSS APPLY (SELECT CHARINDEX('/', p.path, i2 + 1) AS i3) a3
    CROSS APPLY (SELECT CHARINDEX('/', p.path, i3 + 1) AS i4) a4
), a AS (
    SELECT act, clr, ack, priority, alarm, hr,
           CASE WHEN path LIKE 'Boars[_]Head/%' AND i3 > i2 THEN SUBSTRING(path, i2 + 1, i3 - i2 - 1)
                ELSE N'Other' END AS area,
           CASE WHEN path LIKE 'Boars[_]Head/%' AND i5 > i4 THEN SUBSTRING(path, i4 + 1, i5 - i4 - 1)
                WHEN path LIKE 'Boars[_]Head/%' AND i4 > i3 THEN SUBSTRING(path, i3 + 1, i4 - i3 - 1)
                ELSE N'Other' END AS device,
           CASE WHEN hr >= 7 AND hr < 15 THEN 'A' WHEN hr >= 15 AND hr < 23 THEN 'B' ELSE 'C' END AS shift
    FROM s
), f AS (
    SELECT * FROM a
    WHERE (:areas = N'' OR area IN (SELECT LTRIM(value) FROM STRING_SPLIT(:areas, '|')))
      AND (:devices = N'' OR area + N'/' + device IN (SELECT LTRIM(value) FROM STRING_SPLIT(:devices, '|')))
      AND (:priorities = N'' OR CAST(priority AS nvarchar(2)) IN (SELECT value FROM STRING_SPLIT(:priorities, ',')))
      AND (:shifts = N'' OR shift IN (SELECT value FROM STRING_SPLIT(:shifts, ',')))
)
, g AS (
    SELECT f.*, CASE :grain
        WHEN 'hour' THEN DATEADD(hour, DATEDIFF(hour, 0, act), 0)
        WHEN 'day' THEN CAST(CAST(act AS date) AS datetime2)
        WHEN 'week' THEN DATEADD(day, -((DATEPART(weekday, act) + @@DATEFIRST - 2) % 7), CAST(CAST(act AS date) AS datetime2))
        WHEN 'shift' THEN CASE WHEN hr < 7 THEN DATEADD(hour, -1, CAST(CAST(act AS date) AS datetime2))
                               ELSE DATEADD(hour, CASE WHEN hr < 15 THEN 7 WHEN hr < 23 THEN 15 ELSE 23 END,
                                            CAST(CAST(act AS date) AS datetime2)) END
        ELSE CAST(:start AS datetime2) END AS bucket, CASE :groupBy WHEN 'area' THEN area WHEN 'device' THEN area + N'/' + device
        WHEN 'shift' THEN shift ELSE N'' END AS grp FROM f
)
-- one row per time bucket x group (area | device | shift | all): counts and summed response times (seconds)
SELECT CONVERT(varchar(19), bucket, 120) AS bucket, grp,
       COUNT(*) AS activations,
       SUM(CASE WHEN priority >= 3 THEN 1 ELSE 0 END) AS high_cnt,
       SUM(CASE WHEN ack IS NOT NULL THEN 1 ELSE 0 END) AS acked,
       SUM(CASE WHEN ack IS NOT NULL THEN DATEDIFF_BIG(millisecond, act, ack) ELSE 0 END) / 1000.0 AS ack_sec,
       SUM(CASE WHEN clr IS NOT NULL THEN 1 ELSE 0 END) AS cleared,
       SUM(CASE WHEN clr IS NOT NULL THEN DATEDIFF_BIG(millisecond, act, clr) ELSE 0 END) / 1000.0 AS clr_sec,
       MAX(CASE WHEN clr IS NOT NULL THEN DATEDIFF_BIG(millisecond, act, clr) ELSE 0 END) / 1000.0 AS clr_max
FROM g
GROUP BY bucket, grp
ORDER BY bucket, grp
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports._almFacts` | script | |

## Reports/Alarms/Options {#reports-alarms-options}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Alarms/Options` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:start` | Parameter | `String` |
| `:end` | Parameter | `String` |
| `:areas` | Parameter | `String` |
| `:devices` | Parameter | `String` |
| `:priorities` | Parameter | `String` |
| `:shifts` | Parameter | `String` |

```sql
WITH ev AS (
    SELECT e.eventid,
           MIN(CASE WHEN e.eventtype = 0 THEN e.eventtime END) AS act,
           MIN(CASE WHEN e.eventtype = 1 THEN e.eventtime END) AS clr,
           MIN(CASE WHEN e.eventtype = 2 THEN e.eventtime END) AS ack,
           MAX(e.priority) AS priority,
           MIN(e.source) AS source
    FROM dbo.alarm_events e
    WHERE e.eventtime >= CAST(:start AS datetime2) AND e.eventtime < DATEADD(day, 3, CAST(:end AS datetime2))
    GROUP BY e.eventid
), p AS (
    SELECT ev.*, SUBSTRING(ev.source, CHARINDEX(':/tag:', ev.source) + 6, 4000) AS path,
           SUBSTRING(ev.source, CHARINDEX(':/alm:', ev.source) + 6, 255) AS alarm,
           DATEPART(hour, ev.act) AS hr
    FROM ev
    WHERE ev.act >= CAST(:start AS datetime2) AND ev.act < CAST(:end AS datetime2)
), s AS (
    SELECT p.*, i2, i3, i4, CHARINDEX('/', p.path, i4 + 1) AS i5
    FROM p
    CROSS APPLY (SELECT CHARINDEX('/', p.path) AS i1) a1
    CROSS APPLY (SELECT CHARINDEX('/', p.path, i1 + 1) AS i2) a2
    CROSS APPLY (SELECT CHARINDEX('/', p.path, i2 + 1) AS i3) a3
    CROSS APPLY (SELECT CHARINDEX('/', p.path, i3 + 1) AS i4) a4
), a AS (
    SELECT act, clr, ack, priority, alarm, hr,
           CASE WHEN path LIKE 'Boars[_]Head/%' AND i3 > i2 THEN SUBSTRING(path, i2 + 1, i3 - i2 - 1)
                ELSE N'Other' END AS area,
           CASE WHEN path LIKE 'Boars[_]Head/%' AND i5 > i4 THEN SUBSTRING(path, i4 + 1, i5 - i4 - 1)
                WHEN path LIKE 'Boars[_]Head/%' AND i4 > i3 THEN SUBSTRING(path, i3 + 1, i4 - i3 - 1)
                ELSE N'Other' END AS device,
           CASE WHEN hr >= 7 AND hr < 15 THEN 'A' WHEN hr >= 15 AND hr < 23 THEN 'B' ELSE 'C' END AS shift
    FROM s
), f AS (
    SELECT * FROM a
    WHERE (:areas = N'' OR area IN (SELECT LTRIM(value) FROM STRING_SPLIT(:areas, '|')))
      AND (:devices = N'' OR area + N'/' + device IN (SELECT LTRIM(value) FROM STRING_SPLIT(:devices, '|')))
      AND (:priorities = N'' OR CAST(priority AS nvarchar(2)) IN (SELECT value FROM STRING_SPLIT(:priorities, ',')))
      AND (:shifts = N'' OR shift IN (SELECT value FROM STRING_SPLIT(:shifts, ',')))
)

-- Area / Device pairs that raised alarms in the window (Scope picker of the Alarms source)
SELECT area, device, COUNT(*) AS cnt FROM f GROUP BY area, device ORDER BY area, device
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports._almOptions` | script | |

## Reports/Alarms/Top {#reports-alarms-top}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Alarms/Top` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:start` | Parameter | `String` |
| `:end` | Parameter | `String` |
| `:areas` | Parameter | `String` |
| `:devices` | Parameter | `String` |
| `:priorities` | Parameter | `String` |
| `:shifts` | Parameter | `String` |
| `:dim` | Parameter | `String` |
| `:orderBy` | Parameter | `String` |
| `:n` | Parameter | `Int4` |

```sql
WITH ev AS (
    SELECT e.eventid,
           MIN(CASE WHEN e.eventtype = 0 THEN e.eventtime END) AS act,
           MIN(CASE WHEN e.eventtype = 1 THEN e.eventtime END) AS clr,
           MIN(CASE WHEN e.eventtype = 2 THEN e.eventtime END) AS ack,
           MAX(e.priority) AS priority,
           MIN(e.source) AS source
    FROM dbo.alarm_events e
    WHERE e.eventtime >= CAST(:start AS datetime2) AND e.eventtime < DATEADD(day, 3, CAST(:end AS datetime2))
    GROUP BY e.eventid
), p AS (
    SELECT ev.*, SUBSTRING(ev.source, CHARINDEX(':/tag:', ev.source) + 6, 4000) AS path,
           SUBSTRING(ev.source, CHARINDEX(':/alm:', ev.source) + 6, 255) AS alarm,
           DATEPART(hour, ev.act) AS hr
    FROM ev
    WHERE ev.act >= CAST(:start AS datetime2) AND ev.act < CAST(:end AS datetime2)
), s AS (
    SELECT p.*, i2, i3, i4, CHARINDEX('/', p.path, i4 + 1) AS i5
    FROM p
    CROSS APPLY (SELECT CHARINDEX('/', p.path) AS i1) a1
    CROSS APPLY (SELECT CHARINDEX('/', p.path, i1 + 1) AS i2) a2
    CROSS APPLY (SELECT CHARINDEX('/', p.path, i2 + 1) AS i3) a3
    CROSS APPLY (SELECT CHARINDEX('/', p.path, i3 + 1) AS i4) a4
), a AS (
    SELECT act, clr, ack, priority, alarm, hr,
           CASE WHEN path LIKE 'Boars[_]Head/%' AND i3 > i2 THEN SUBSTRING(path, i2 + 1, i3 - i2 - 1)
                ELSE N'Other' END AS area,
           CASE WHEN path LIKE 'Boars[_]Head/%' AND i5 > i4 THEN SUBSTRING(path, i4 + 1, i5 - i4 - 1)
                WHEN path LIKE 'Boars[_]Head/%' AND i4 > i3 THEN SUBSTRING(path, i3 + 1, i4 - i3 - 1)
                ELSE N'Other' END AS device,
           CASE WHEN hr >= 7 AND hr < 15 THEN 'A' WHEN hr >= 15 AND hr < 23 THEN 'B' ELSE 'C' END AS shift
    FROM s
), f AS (
    SELECT * FROM a
    WHERE (:areas = N'' OR area IN (SELECT LTRIM(value) FROM STRING_SPLIT(:areas, '|')))
      AND (:devices = N'' OR area + N'/' + device IN (SELECT LTRIM(value) FROM STRING_SPLIT(:devices, '|')))
      AND (:priorities = N'' OR CAST(priority AS nvarchar(2)) IN (SELECT value FROM STRING_SPLIT(:priorities, ',')))
      AND (:shifts = N'' OR shift IN (SELECT value FROM STRING_SPLIT(:shifts, ',')))
)
, k AS (
    SELECT f.*, CASE WHEN :dim IN ('alarms', 'devices') THEN device ELSE N'' END AS k_device,
           CASE WHEN :dim = 'alarms' THEN alarm ELSE N'' END AS k_alarm,
           CASE WHEN ack IS NOT NULL THEN DATEDIFF_BIG(millisecond, act, ack) / 60000.0 END AS ack_min,
           CASE WHEN clr IS NOT NULL THEN DATEDIFF_BIG(millisecond, act, clr) / 60000.0 END AS clr_min
    FROM f
), t AS (
    SELECT area, k_device AS device, k_alarm AS alarm, COUNT(*) AS cnt, MAX(priority) AS max_priority,
           COUNT(ack_min) AS acked, AVG(ack_min) AS avg_ack_min, AVG(clr_min) AS avg_clr_min,
           ISNULL(SUM(clr_min), 0) AS total_min
    FROM k
    GROUP BY area, k_device, k_alarm
)
-- Top N alarms / devices / areas by count, total active time or average time to acknowledge
SELECT TOP (:n) area, device, alarm, cnt, max_priority, acked, avg_ack_min, avg_clr_min, total_min
FROM t
ORDER BY CASE :orderBy WHEN 'duration' THEN total_min WHEN 'ack' THEN ISNULL(avg_ack_min, 0) ELSE cnt END DESC,
         cnt DESC, area, device, alarm
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports._almTopN` | script | |

## Reports/Forms/Submissions {#reports-forms-submissions}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Forms/Submissions` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:start` | Parameter | `String` |
| `:end` | Parameter | `String` |
| `:username` | Parameter | `String` |
| `:viewAll` | Parameter | `Boolean` |

```sql
-- Operations Forms source: submissions in the window. Same visibility as Form History - Forms/ViewAll sees every
-- user, otherwise only the session user's own rows (viewAll and username come from shared.Reports on the gateway)
SELECT id, form_type, CONVERT(varchar(10), form_date, 120) AS form_date, submitted_by, submitted_name,
       CONVERT(varchar(19), submitted_at, 120) AS submitted_at, shift_status, is_abnormal, release_logged, open_items,
       summary
FROM dbo.ops_form_submission
WHERE (:viewAll = 1 OR submitted_by = :username)
  AND :username <> ''
  AND submitted_at >= CAST(:start AS datetime2) AND submitted_at < CAST(:end AS datetime2)
ORDER BY submitted_at DESC
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports._formRows` | script | |

## Reports/History/Coverage {#reports-history-coverage}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/History/Coverage` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:paths` | Parameter | `String` |

```sql
-- First history sample per tag (SQL historian 'historian', sqlth_te.created = epoch ms); paths lower-case, '|'-joined
SELECT tagpath, MIN(created) AS first_ms
FROM dbo.sqlth_te
WHERE tagpath IN (SELECT value FROM STRING_SPLIT(:paths, '|'))
GROUP BY tagpath
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports._historian` | script | |

## Reports/History/FirstSample {#reports-history-firstsample}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/History/FirstSample` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:paths` | Parameter | `String` |

```sql
-- History start of the live (non-retired) history row per tag (sqlth_te.created, epoch ms): the report ignores the
-- hours before it (the historian returns 0 for them). Paths lower-case, '|'-joined.
SELECT tagpath, MIN(created) AS first_ms
FROM dbo.sqlth_te
WHERE retired IS NULL AND tagpath IN (SELECT value FROM STRING_SPLIT(:paths, '|'))
GROUP BY tagpath
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports._histData` | script | |

## Reports/OOS/Options {#reports-oos-options}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/OOS/Options` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

```sql
-- Area / Device pairs that have ever been out of service (Scope picker of the Out Of Service source)
SELECT area, device_name AS device, COUNT(*) AS cnt FROM dbo.oos_record
WHERE COALESCE(area, N'') <> N'' GROUP BY area, device_name ORDER BY area, device_name
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports._oosOptions` | script | |

## Reports/OOS/Records {#reports-oos-records}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/OOS/Records` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:start` | Parameter | `String` |
| `:end` | Parameter | `String` |

```sql
-- Records that overlap the report window (an open record runs to now); shared.Reports aggregates them per bucket
SELECT r.id, r.device_name, r.device_type, r.area, r.reason, r.taken_name, r.taken_by,
       CONVERT(varchar(19), r.taken_at, 120) AS taken_at,
       CONVERT(varchar(19), r.returned_at, 120) AS returned_at,
       r.returned_name, r.status, r.is_backfill,
       LEFT(REPLACE(REPLACE(COALESCE(r.memo, N''), CHAR(13), N' '), CHAR(10), N' '), 200) AS memo
FROM dbo.oos_record r
WHERE r.taken_at < CAST(:end AS datetime2)
  AND (r.returned_at IS NULL OR r.returned_at >= CAST(:start AS datetime2))
ORDER BY r.taken_at DESC
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports._oosRows` | script | |

## Reports/Runs/Get {#reports-runs-get}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Runs/Get` |
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
| `:username` | Parameter | `String` |

```sql
SELECT id, source, title, definition, format, run_at FROM dbo.report_run
WHERE id = :id AND username = :username AND :username <> ''
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports.loadSaved` | script | |

## Reports/Runs/Insert {#reports-runs-insert}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Runs/Insert` |
| Type | `UpdateQuery` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:username` | Parameter | `String` |
| `:source` | Parameter | `String` |
| `:title` | Parameter | `String` |
| `:definition` | Parameter | `String` |
| `:format` | Parameter | `String` |
| `:now` | Parameter | `DateTime` |

```sql
INSERT INTO dbo.report_run (username, source, title, definition, format, run_at)
VALUES (:username, :source, :title, :definition, :format, :now)
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports.logRun` | script | |

## Reports/Runs/LastByTitle {#reports-runs-lastbytitle}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Runs/LastByTitle` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:username` | Parameter | `String` |

```sql
-- Saved Reports > Last Run: the session user's newest download per report title
SELECT source, title, MAX(run_at) AS last_run
FROM dbo.report_run
WHERE username = :username AND :username <> ''
GROUP BY source, title
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports._lastRuns` | script | |

## Reports/Runs/List {#reports-runs-list}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Runs/List` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:username` | Parameter | `String` |
| `:viewAll` | Parameter | `Boolean` |

```sql
-- Saved Reports > Recent Runs: the session user's downloads, or everyone's with Reports/ManageTemplates (viewAll = 1)
SELECT TOP (200) id, username, source, title, definition, format, run_at
FROM dbo.report_run
WHERE :username <> '' AND (username = :username OR :viewAll = 1)
ORDER BY run_at DESC, id DESC
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports._runList` | script | |

## Reports/Runs/Recent {#reports-runs-recent}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Runs/Recent` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:username` | Parameter | `String` |

```sql
-- The session user's latest downloads (newest first); shared.Reports keeps the newest per title
SELECT TOP (40) id, source, title, definition, format, run_at
FROM dbo.report_run
WHERE username = :username AND :username <> ''
ORDER BY run_at DESC, id DESC
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports._runRows` | script | |

## Reports/Templates/Delete {#reports-templates-delete}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Templates/Delete` |
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
| `:username` | Parameter | `String` |
| `:manage` | Parameter | `Boolean` |

```sql
DELETE FROM dbo.report_template
WHERE id = :id AND :username <> '' AND (owner_username = :username OR (:manage = 1 AND is_shared = 1))
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports.deleteTemplate` | script | |

## Reports/Templates/Get {#reports-templates-get}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Templates/Get` |
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
| `:username` | Parameter | `String` |

```sql
SELECT id, name, source, owner_username, owner_name, is_shared, definition, created_at, updated_at, updated_by
FROM dbo.report_template
WHERE id = :id AND :username <> '' AND (owner_username = :username OR is_shared = 1)
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports.loadTemplate` | script | |

## Reports/Templates/Insert {#reports-templates-insert}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Templates/Insert` |
| Type | `UpdateQuery` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:name` | Parameter | `String` |
| `:source` | Parameter | `String` |
| `:definition` | Parameter | `String` |
| `:username` | Parameter | `String` |
| `:ownerName` | Parameter | `String` |
| `:isShared` | Parameter | `Boolean` |
| `:now` | Parameter | `DateTime` |

```sql
INSERT INTO dbo.report_template (name, source, definition, owner_username, owner_name, is_shared, created_at,
                                 updated_at, updated_by)
VALUES (:name, :source, :definition, :username, :ownerName, :isShared, :now, :now, :username)
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports.saveTemplate` | script | |

## Reports/Templates/List {#reports-templates-list}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Templates/List` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:username` | Parameter | `String` |

```sql
-- Own templates + every shared template (shared.Reports.templates)
SELECT id, name, source, definition, owner_username, owner_name, is_shared, created_at, updated_at, updated_by
FROM dbo.report_template
WHERE :username <> '' AND (owner_username = :username OR is_shared = 1)
ORDER BY is_shared, name
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports.templates` | script | |

## Reports/Templates/NameTaken {#reports-templates-nametaken}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Templates/NameTaken` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:username` | Parameter | `String` |
| `:name` | Parameter | `String` |
| `:id` | Parameter | `Int4` |

```sql
SELECT COUNT(*) AS n FROM dbo.report_template WHERE owner_username = :username AND name = :name AND id <> :id
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports.saveTemplate` | script | |

## Reports/Templates/Update {#reports-templates-update}

| Setting | Value |
|---|---|
| Path (what callers pass) | `Reports/Templates/Update` |
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
| `:name` | Parameter | `String` |
| `:source` | Parameter | `String` |
| `:definition` | Parameter | `String` |
| `:isShared` | Parameter | `Boolean` |
| `:now` | Parameter | `DateTime` |
| `:username` | Parameter | `String` |
| `:manage` | Parameter | `Boolean` |

```sql
-- Owner, or Reports/ManageTemplates (manage = 1) for someone else's shared template
UPDATE dbo.report_template
SET name = :name, source = :source, definition = :definition, is_shared = :isShared, updated_at = :now,
    updated_by = :username
WHERE id = :id AND :username <> '' AND (owner_username = :username OR (:manage = 1 AND is_shared = 1))
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Reports.saveTemplate` | script | |
