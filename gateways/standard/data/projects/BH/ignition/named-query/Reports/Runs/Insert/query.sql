INSERT INTO dbo.report_run (username, source, title, definition, format, run_at)
VALUES (:username, :source, :title, :definition, :format, :now)
