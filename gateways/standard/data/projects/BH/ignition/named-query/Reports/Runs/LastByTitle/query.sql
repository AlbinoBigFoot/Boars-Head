-- Saved Reports > Last Run: the session user's newest download per report title
SELECT source, title, MAX(run_at) AS last_run
FROM dbo.report_run
WHERE username = :username AND :username <> ''
GROUP BY source, title
