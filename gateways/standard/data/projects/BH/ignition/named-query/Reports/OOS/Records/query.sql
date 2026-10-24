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
