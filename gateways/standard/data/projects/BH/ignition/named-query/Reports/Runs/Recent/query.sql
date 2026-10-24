-- The session user's latest downloads (newest first); shared.Reports keeps the newest per title
SELECT TOP (40) id, source, title, definition, format, run_at
FROM dbo.report_run
WHERE username = :username AND :username <> ''
ORDER BY run_at DESC, id DESC
