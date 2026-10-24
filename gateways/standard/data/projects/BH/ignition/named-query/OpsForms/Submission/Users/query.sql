SELECT submitted_by, MAX(submitted_name) AS submitted_name
FROM dbo.ops_form_submission
WHERE :viewAll = 1
GROUP BY submitted_by
ORDER BY submitted_by
