def doTrace(request, session):
	return shared.WebAuth.deny(request, 405)
