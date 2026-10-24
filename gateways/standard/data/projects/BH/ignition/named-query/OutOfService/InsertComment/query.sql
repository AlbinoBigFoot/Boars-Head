-- Comment / status update on a record, open or returned (shared.OutOfService.addComment).
INSERT INTO dbo.oos_comment (record_id, username, display_name, created_at, status, comment)
VALUES (:recordId, :username, :displayName, :createdAt, :status, :comment)
