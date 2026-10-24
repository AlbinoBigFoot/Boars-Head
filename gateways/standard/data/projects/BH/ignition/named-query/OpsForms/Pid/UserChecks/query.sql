SELECT COUNT(*) AS n FROM dbo.ops_pid_check_log WHERE cycle_id = :cycleId AND updated_by = :username
