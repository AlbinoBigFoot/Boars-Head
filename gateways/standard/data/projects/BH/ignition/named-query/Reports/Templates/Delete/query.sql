DELETE FROM dbo.report_template
WHERE id = :id AND :username <> '' AND (owner_username = :username OR (:manage = 1 AND is_shared = 1))
