SELECT id, form_type, form_date, submitted_by, submitted_name, submitted_at, shift_status, summary, data
FROM dbo.ops_form_submission
WHERE id = :id
  AND (:viewAll = 1 OR (submitted_by = :username AND :username <> ''))
