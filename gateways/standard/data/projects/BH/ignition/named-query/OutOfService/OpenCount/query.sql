-- Devices currently out of service (header notes icon badge). refresh only re-runs it.
SELECT COUNT(*) AS open_count
FROM dbo.oos_record
WHERE :allowed = 1
  AND :refresh >= 0
  AND returned_at IS NULL
