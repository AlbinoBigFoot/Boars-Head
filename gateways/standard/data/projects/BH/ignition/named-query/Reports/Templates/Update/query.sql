-- Owner, or Reports/ManageTemplates (manage = 1) for someone else's shared template
UPDATE dbo.report_template
SET name = :name, source = :source, definition = :definition, is_shared = :isShared, updated_at = :now,
    updated_by = :username
WHERE id = :id AND :username <> '' AND (owner_username = :username OR (:manage = 1 AND is_shared = 1))
