SELECT id, source, title, definition, format, run_at FROM dbo.report_run
WHERE id = :id AND username = :username AND :username <> ''
