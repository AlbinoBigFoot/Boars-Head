SELECT id, name, source, owner_username, owner_name, is_shared, definition, created_at, updated_at, updated_by
FROM dbo.report_template
WHERE id = :id AND :username <> '' AND (owner_username = :username OR is_shared = 1)
