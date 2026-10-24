UPDATE dbo.ops_pid_cycle
SET status = N'Complete', completed_by = :user, completed_at = :now
WHERE id = :id AND status = N'Open'
