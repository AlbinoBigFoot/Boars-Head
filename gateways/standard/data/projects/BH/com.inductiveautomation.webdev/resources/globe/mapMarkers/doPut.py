def doPut(request, session):
	# Gateway-wide marker write: admin login first (shared.Globe.adminWriter, docs/globe-hover.md#security).
	status, user = shared.Globe.adminWriter(request)
	if status != 200:
		try:
			request['servletResponse'].setStatus(status)
		except:
			pass
		return {'json': {'ok': False, 'reason': 'login required' if status == 401 else 'admin role required'}}
	data = request['data']
	system.tag.writeBlocking(['[default]_Config/MapMarkerGeoJson'], [data])
	return {'json': {'ok': True}}
