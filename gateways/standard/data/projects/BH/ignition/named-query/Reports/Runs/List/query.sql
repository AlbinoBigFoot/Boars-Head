-- Saved Reports > Recent Runs: the session user's downloads, or everyone's with Reports/ManageTemplates (viewAll = 1)
SELECT TOP (200) id, username, source, title, definition, format, run_at
FROM dbo.report_run
WHERE :username <> '' AND (username = :username OR :viewAll = 1)
ORDER BY run_at DESC, id DESC
