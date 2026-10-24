-- Operations Forms source: submissions in the window. Same visibility as Form History - Forms/ViewAll sees every
-- user, otherwise only the session user's own rows (viewAll and username come from shared.Reports on the gateway)
SELECT id, form_type, CONVERT(varchar(10), form_date, 120) AS form_date, submitted_by, submitted_name,
       CONVERT(varchar(19), submitted_at, 120) AS submitted_at, shift_status, is_abnormal, release_logged, open_items,
       summary
FROM dbo.ops_form_submission
WHERE (:viewAll = 1 OR submitted_by = :username)
  AND :username <> ''
  AND submitted_at >= CAST(:start AS datetime2) AND submitted_at < CAST(:end AS datetime2)
ORDER BY submitted_at DESC
