INSERT INTO dbo.ops_pid_cycle (cycle_year, drawing_revision, performed_by, reviewed_by, status, created_by, created_at)
VALUES (:year, NULLIF(:revision, ''), NULLIF(:performedBy, ''), NULLIF(:reviewedBy, ''), N'Open', :user, :now)
