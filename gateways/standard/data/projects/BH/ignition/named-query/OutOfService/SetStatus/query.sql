-- Status change carried by a comment (shared.OutOfService.addComment); only while the record is open.
UPDATE dbo.oos_record
SET status = :status,
    updated_at = SYSDATETIME()
WHERE id = :id
  AND returned_at IS NULL
