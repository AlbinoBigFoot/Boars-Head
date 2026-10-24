def doGet(request, session):
	# PLC Rack 3D live state, READ ONLY (system.tag.readBlocking; no writes, no secrets). Logged-in BH Perspective session
	# only (shared.WebAuth). .cursor/tasks/plc-rack-3d/build.py - docs/plc-rack-3d.md
	if not shared.WebAuth.perspectiveUser(request):
		return shared.WebAuth.deny(request)
	shared.WebAuth.noStore(request)
	return {"json": shared.Rack3d.state(request)}
