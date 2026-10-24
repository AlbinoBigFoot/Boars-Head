def doDelete(request, session):
	# read-only resource: GET only
	return shared.WebAuth.deny(request, 405, 'method not allowed')
