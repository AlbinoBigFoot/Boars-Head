# PLC Rack / IO helpers (.cursor/tasks/plc-rack-io/build.py - generated; docs/plc-rack-io.md). UI only: nothing here
# reads or writes a PLC value.
POPUP_VIEW = "01_Popups/00_Faceplates/PlcRack/CardDetail"
WIDTH = 900
HEIGHT = {"AI": 238, "CTRL": 336}
DEFAULT_HEIGHT = 334


def openCard(sitePath, member, slot=0, kind="", title="", viewportW=0, viewportH=0):
	"""Pop one rack card (or the controller) out as its own faceplate. The popup id is per card, so several cards can be
	open side by side; each opens bottom-centred (over the detail panel, never over the rack) at a staggered offset,
	draggable and resizable, and is clamped on screen."""
	k = 0
	try:
		k = int(slot or 0) % 6
	except Exception:
		k = 0
	h = HEIGHT.get(str(kind or ""), DEFAULT_HEIGHT)
	vw = int(viewportW or 0) or 1366
	vh = int(viewportH or 0) or 768
	w = min(WIDTH, max(480, vw - 40))
	left = max(8, min(vw - w - 8, (vw - w) / 2 - 80 + k * 40))
	top = max(8, min(vh - h - 8, vh - h - 16 - k * 28))
	system.perspective.openPopup(
		id="plcRackCard-" + str(member or "Controller"),
		view=POPUP_VIEW,
		params={"sitePath": sitePath, "member": member},
		title=title or str(member),
		position={"left": left, "top": top, "width": w, "height": h},
		showCloseIcon=True,
		draggable=True,
		resizable=True,
		modal=False,
		overlayDismiss=False,
	)
	return True
