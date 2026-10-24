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
