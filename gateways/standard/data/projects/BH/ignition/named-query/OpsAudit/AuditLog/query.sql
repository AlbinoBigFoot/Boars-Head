-- OPS Audit Log page (.cursor/tasks/ops-audit-log/build.py): OpsAudit events in the start / end range, newest
-- first, with display columns (action / target / change / source text), tooltip and detail columns. search = LIKE
-- pattern over the text columns (empty = all). refresh only re-runs it. At most 5000 rows (the page says so).
-- Target = the tag path from originating_system without provider, site / area / type folders and a trailing
-- Value member; folders joined with a chevron, the UDT member after a middle dot.
-- (No colon-prefixed names in comments: Ignition turns them into JDBC placeholders.)
SELECT TOP (5000)
    e.audit_events_id AS id,
    e.event_timestamp,
    FORMAT(e.event_timestamp, 'yyyy-MM-dd HH:mm:ss') AS time_text,
    COALESCE(e.actor, N'') AS actor,
    COALESCE(e.actor_host, N'') AS actor_host,
    COALESCE(e.action, N'') AS action,
    COALESCE(a.action_text, N'') AS action_text,
    COALESCE(e.action_target, N'') AS action_target,
    t.target_text,
    CASE WHEN p.tag_path <> N'' THEN p.tag_path ELSE COALESCE(e.action_target, N'') END AS target_tip,
    COALESCE(r.area, N'') AS area,
    p.tag_path,
    COALESCE(e.action_value, N'') AS action_value,
    REPLACE(COALESCE(e.action_value, N''), N' -> ', N' ' + NCHAR(8594) + N' ') AS change_text,
    REPLACE(REPLACE(COALESCE(e.action_value, N''), N' -> ', N' ' + NCHAR(8594) + N' '), N' | ', NCHAR(10))
        AS change_full,
    CASE WHEN p.view_path = N'' THEN CASE WHEN o.os LIKE N'script%' THEN N'Script' ELSE N'Gateway' END
         WHEN p.view_path LIKE N'%/01_Devices/%' THEN v.view_leaf + N' Device'
         WHEN p.view_path LIKE N'%Faceplate%' THEN N'Faceplate'
         WHEN p.view_path LIKE N'%OutOfServiceLog' THEN N'Out Of Service Log'
         WHEN p.view_path LIKE N'%UserManagement%' THEN N'User Management'
         WHEN p.view_path LIKE N'%RolesPermissions%' THEN N'Roles & Permissions'
         ELSE v.view_leaf END AS source_text,
    p.view_path,
    CONCAT(p.view_path, CASE WHEN p.view_path <> N'' AND COALESCE(e.actor_host, N'') <> N'' THEN N' ' + NCHAR(183) + N' '
           ELSE N'' END, COALESCE(e.actor_host, N'')) AS source_tip,
    COALESCE(e.status_code, 0) AS status_code
FROM dbo.ops_audit_events e
CROSS APPLY (SELECT COALESCE(e.originating_system, N'') AS os) o
CROSS APPLY (SELECT CHARINDEX(N'tagPath:', o.os) AS tp_at, CHARINDEX(N'/view:', o.os) AS v_at,
                    o.os + N':/' AS os2) k
CROSS APPLY (SELECT
    CASE WHEN k.tp_at > 0 THEN SUBSTRING(k.os2, k.tp_at + 8, CHARINDEX(N':/', k.os2, k.tp_at + 8) - k.tp_at - 8)
         ELSE N'' END AS tag_path,
    CASE WHEN k.v_at > 0 THEN SUBSTRING(k.os2, k.v_at + 6, CHARINDEX(N':/', k.os2, k.v_at + 6) - k.v_at - 6)
         ELSE N'' END AS view_path) p
CROSS APPLY (SELECT CASE WHEN CHARINDEX(N'/', p.view_path) > 0
    THEN RIGHT(p.view_path, CHARINDEX(N'/', REVERSE(p.view_path)) - 1) ELSE p.view_path END AS view_leaf,
    SUBSTRING(p.tag_path, CHARINDEX(N']', p.tag_path) + 1, 4000) AS p0) v
CROSS APPLY (SELECT CASE WHEN v.p0 LIKE N'Boars[_]Head/%' THEN 4 WHEN v.p0 LIKE N'Plant/%' THEN 3 ELSE 0 END AS skip) d
OUTER APPLY (SELECT MAX(CASE WHEN g.ordinal = g.skip - 1 THEN g.value END) AS area,
                    STRING_AGG(CASE WHEN g.ordinal > g.skip AND g.value <> N'Value' THEN g.value END,
                               N' ' + NCHAR(8250) + N' ') WITHIN GROUP (ORDER BY g.ordinal) AS rest
             FROM (SELECT x.value, x.ordinal, d.skip FROM STRING_SPLIT(v.p0, N'/', 1) x) g) r
CROSS APPLY (SELECT CASE WHEN COALESCE(r.rest, N'') = N'' THEN COALESCE(e.action_target, N'')
    ELSE REPLACE(r.rest, N'.', N' ' + NCHAR(183) + N' ') END AS path_text) t0
CROSS APPLY (SELECT CASE WHEN e.action = N'alarm config' AND CHARINDEX(N' Value ', e.action_target) > 0
    THEN t0.path_text + N' ' + NCHAR(183) + N' ' + SUBSTRING(e.action_target, CHARINDEX(N' Value ', e.action_target) + 7, 400)
    ELSE t0.path_text END AS target_text) t
OUTER APPLY (SELECT REPLACE(STRING_AGG(UPPER(LEFT(w.value, 1)) + SUBSTRING(w.value, 2, 400), N' ')
                 WITHIN GROUP (ORDER BY w.ordinal), N'/ ', N'/') AS action_text
             FROM STRING_SPLIT(REPLACE(COALESCE(e.action, N''), N'/', N'/ '), N' ', 1) w) a
WHERE :allowed = 1
  AND :refresh >= 0
  AND e.event_timestamp BETWEEN :startDate AND :endDate
  AND (
        COALESCE(:search, '') = ''
        OR e.actor LIKE :search
        OR e.actor_host LIKE :search
        OR e.action LIKE :search
        OR e.action_target LIKE :search
        OR e.action_value LIKE :search
        OR e.originating_system LIKE :search
      )
ORDER BY e.audit_events_id DESC
