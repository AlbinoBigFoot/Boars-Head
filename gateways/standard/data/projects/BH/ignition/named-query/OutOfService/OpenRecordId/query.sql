-- Open record of a device (shared.OutOfService, server side only).
SELECT id
FROM dbo.oos_record
WHERE tag_path = :tagPath
  AND returned_at IS NULL
