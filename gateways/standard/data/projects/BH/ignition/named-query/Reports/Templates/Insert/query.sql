INSERT INTO dbo.report_template (name, source, definition, owner_username, owner_name, is_shared, created_at,
                                 updated_at, updated_by)
VALUES (:name, :source, :definition, :username, :ownerName, :isShared, :now, :now, :username)
