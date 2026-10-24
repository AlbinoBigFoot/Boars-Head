-- Ticket Logger outbox row (shared.TicketLogger._outbox: Oracle stub / dry run); returns the id.
INSERT INTO dbo.ticket_outbox
    (destination, status, ticket_type, priority, area, title, reporter, username, view_name, route, payload,
     external_id)
OUTPUT INSERTED.id
VALUES
    (:destination, :status, :ticketType, :priority, :area, :title, :reporter, :username, :viewName, :route, :payload,
     NULLIF(:externalId, ''))
