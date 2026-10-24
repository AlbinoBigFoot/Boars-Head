-- Forms/ViewAll sees every user; otherwise only the session user own rows (shared.Forms.history)
SELECT id, form_type, form_date, submitted_by, submitted_name, submitted_at, shift_status, is_abnormal,
       release_logged, open_items, summary
FROM dbo.ops_form_submission
WHERE (:viewAll = 1 OR submitted_by = :username)
  AND :username <> ''
  AND (:formType = '' OR form_type = :formType)
  AND form_date BETWEEN CAST(:startDate AS DATE) AND CAST(:endDate AS DATE)
  AND (:userFilter = '' OR submitted_by = :userFilter)
ORDER BY form_date DESC, id DESC
