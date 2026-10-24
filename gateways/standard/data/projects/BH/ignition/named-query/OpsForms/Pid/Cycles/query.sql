-- open cycles: every Forms user; completed: Forms/ViewAll, or cycles the session user recorded checks in
SELECT cy.id, cy.cycle_year, cy.status, cy.drawing_revision, cy.performed_by, cy.reviewed_by, cy.created_by,
       cy.created_at, cy.completed_by, cy.completed_at,
       (SELECT COUNT(*) FROM dbo.ops_pid_valve) AS total,
       (SELECT COUNT(*) FROM dbo.ops_pid_check c WHERE c.cycle_id = cy.id AND c.verified = 1) AS verified,
       (SELECT COUNT(*) FROM dbo.ops_pid_check c WHERE c.cycle_id = cy.id AND COALESCE(c.notes, '') <> '') AS disc
FROM dbo.ops_pid_cycle cy
WHERE :username <> ''
  AND (cy.status = N'Open' OR :viewAll = 1
       OR EXISTS (SELECT 1 FROM dbo.ops_pid_check_log l WHERE l.cycle_id = cy.id AND l.updated_by = :username))
ORDER BY cy.cycle_year DESC, cy.id DESC
