def doGet(request, session):
	# HLCO Safety Relay 3D live state, READ ONLY (system.tag.readBlocking; no writes, no secrets). Logged-in BH Perspective
	# session only (shared.WebAuth). .cursor/tasks/safety-relay-3d/build.py - docs/safety-relay-3d.md
	if not shared.WebAuth.perspectiveUser(request):
		return shared.WebAuth.deny(request)
	shared.WebAuth.noStore(request)
	return {"json": shared.Relay3d.state(request)}
