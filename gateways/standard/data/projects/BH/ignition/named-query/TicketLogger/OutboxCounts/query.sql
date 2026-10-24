-- Ticket Logger outbox counts per destination / status (Ticket Logger > Settings).
SELECT destination, status, COUNT(*) AS n
FROM dbo.ticket_outbox
GROUP BY destination, status
