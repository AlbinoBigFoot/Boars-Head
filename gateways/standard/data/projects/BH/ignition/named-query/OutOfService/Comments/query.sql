-- Comment / status thread of a record, oldest first (flex repeater instances: keys = CommentEntry params).
SELECT
    c.id,
    c.display_name,
    c.username,
    CONVERT(VARCHAR(16), c.created_at, 120) AS created_text,
    COALESCE(c.status, N'') AS status,
    c.comment
FROM dbo.oos_comment c
WHERE :allowed = 1
  AND :refresh >= 0
  AND c.record_id = :id
ORDER BY c.created_at, c.id
