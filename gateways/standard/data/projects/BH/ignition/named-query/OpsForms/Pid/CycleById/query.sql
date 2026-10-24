SELECT id, cycle_year, drawing_revision, performed_by, reviewed_by, status, created_by, created_at, completed_by,
       completed_at
FROM dbo.ops_pid_cycle
WHERE id = :id
