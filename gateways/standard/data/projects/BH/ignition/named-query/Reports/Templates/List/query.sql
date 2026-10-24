-- Own templates + every shared template (shared.Reports.templates)
SELECT id, name, source, definition, owner_username, owner_name, is_shared, created_at, updated_at, updated_by
FROM dbo.report_template
WHERE :username <> '' AND (owner_username = :username OR is_shared = 1)
ORDER BY is_shared, name
