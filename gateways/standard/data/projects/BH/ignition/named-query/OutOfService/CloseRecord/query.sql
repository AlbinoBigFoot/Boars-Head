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
