def doOptions(request, session):
	return shared.WebAuth.deny(request, 405)
