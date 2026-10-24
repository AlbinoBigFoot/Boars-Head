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
