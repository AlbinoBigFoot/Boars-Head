def doPut(request, session):
	data = request['data']
	system.tag.writeBlocking(['[default]_Config/MapMarkerGeoJson'], [data])
	return {'ok': True}
