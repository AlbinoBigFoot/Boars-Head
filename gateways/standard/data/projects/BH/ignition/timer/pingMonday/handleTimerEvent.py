def handleTimerEvent():
	# Connection status (Connected / Last Check / Last Error) for every [default]_Config/Integrations endpoint.
	# The Ticket Logger access gate reads Integrations/Monday/Connected.
	shared.Integrations.pingAll()
