UPDATE dbo.ops_pid_cycle
SET drawing_revision = NULLIF(:revision, ''), performed_by = NULLIF(:performedBy, ''), reviewed_by = NULLIF(:reviewedBy, '')
WHERE id = :id AND status = N'Open'
