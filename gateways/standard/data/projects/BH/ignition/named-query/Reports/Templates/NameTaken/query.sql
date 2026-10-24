SELECT COUNT(*) AS n FROM dbo.report_template WHERE owner_username = :username AND name = :name AND id <> :id
