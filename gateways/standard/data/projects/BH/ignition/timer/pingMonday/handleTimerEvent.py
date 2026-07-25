def handleTimerEvent():
	# Detect connectivity between Ignition and Monday.com for Ticket Logger access gate.
	from shared import TicketLogger

	reads = system.tag.readBlocking([
		"[default]_Config/Monday/Enabled",
		"[default]_Config/Monday/API Token",
		"[default]_Config/Monday/Board Id",
	])

	connected = False
	enabled = False
	token = None
	boardId = None

	if reads[0] is not None:
		try:
			if reads[0].quality.isGood():
				enabled = bool(reads[0].value)
		except:
			enabled = bool(reads[0].value)

	if reads[1] is not None:
		try:
			if reads[1].quality.isGood():
				token = reads[1].value
		except:
			token = reads[1].value

	if reads[2] is not None:
		try:
			if reads[2].quality.isGood():
				boardId = reads[2].value
		except:
			boardId = reads[2].value

	if enabled and token and boardId:
		connected = TicketLogger.ping()

	system.tag.writeBlocking(["[default]_Config/Monday/Connected"], [connected])
