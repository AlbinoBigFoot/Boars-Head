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
