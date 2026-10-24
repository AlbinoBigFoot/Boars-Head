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
