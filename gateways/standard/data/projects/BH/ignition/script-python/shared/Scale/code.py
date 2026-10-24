# Coordinate-container view scaling (Scout-style).
# PROP_CENTER_V2: always center X and Y.
# Bind root/Canvas props.style.transform via expr-struct + script:
#   return shared.Scale.cssTransform(value)
#
# value keys:
#   scale / Scale          — truthy enables; falsy returns "none"
#   primaryViewWidth/Height — page.props.dimensions.primaryView.*
#   defaultViewWidth/Height — view.props.defaultSize.*


def _truthy(v):
	if v in (True, 1, "1", "true", "True"):
		return True
	if v in (False, 0, "0", "false", "False", None, ""):
		return False
	try:
		return bool(v)
	except:
		return False


def _num(v):
	try:
		if v is None or v == "":
			return None
		return float(v)
	except:
		return None


def _get(value, *keys):
	for key in keys:
		try:
			if hasattr(value, "get"):
				if key in value:
					return value[key]
			else:
				return value[key]
		except:
			continue
	return None


def transformParams(value):
	"""
	Return scale factor and pre-scale translate for cssTransform(), or None when scaling is off.
	Matches: scale(s) translate(tx, ty) with transform-origin top left.
	"""
	enabled = _get(value, "scale", "Scale")
	if not _truthy(enabled):
		return None

	pw = _num(_get(value, "primaryViewWidth"))
	ph = _num(_get(value, "primaryViewHeight"))
	dw = _num(_get(value, "defaultViewWidth"))
	dh = _num(_get(value, "defaultViewHeight"))
	if pw is None or ph is None or dw is None or dh is None:
		return None
	if pw <= 0 or ph <= 0 or dw <= 0 or dh <= 0:
		return None

	# Optional content box: fit just the drawn area (plus margin) instead of the whole defaultSize, for views whose
	# canvas has empty space (e.g. Machine Room). Omitted = the full defaultSize.
	cx = _num(_get(value, "contentX"))
	cy = _num(_get(value, "contentY"))
	cw = _num(_get(value, "contentWidth"))
	ch = _num(_get(value, "contentHeight"))
	if cx is None or cy is None or not cw or not ch or cw <= 0 or ch <= 0:
		cx, cy, cw, ch = 0.0, 0.0, dw, dh

	s = min(pw / cw, ph / ch)
	if s <= 0:
		return None

	tx = ((pw - cw * s) / 2.0) / s - cx
	ty = ((ph - ch * s) / 2.0) / s - cy
	return {"s": s, "tx": tx, "ty": ty}


def cssTransform(value):
	"""
	Return CSS transform string: scale(...) translate(...px, ...px).
	Fits defaultSize into primaryView and keeps it centered (both axes).
	"""
	params = transformParams(value)
	if params is None:
		return "none"
	return "scale(%s) translate(%spx, %spx)" % (params["s"], params["tx"], params["ty"])
