import math

def ns_ew (ns, ew):
	if (not ns == "") and (not ew == ""):
		ns_i = int(ns)
		ew_i = int(ew)
		kts = math.sqrt((ns_i**2) + (ew_i**2))
		mph = int(kts*1.15)
		if ((ns_i != 0) and (ew_i != 0)):
			course = math.atan2(ew_i,ns_i) 
		else:
			course = 0
		course_deg = int(course*57.3)
		if course_deg < 0:
			course_deg = course_deg + 360
		return str(mph).rjust(4," ")+" "+str(course_deg).rjust(3," ")
	else: 
		return str("        ")

def dist_brng (lat_s, lon_s, my_lat, my_lon):
	if lat_s != "" and lon_s != "":
		lat = float(lat_s)
		lon = float(lon_s)
		delta_lat = lat - my_lat
		delta_lon = lon - my_lon
		y_nm = delta_lat * 60
		x_nm = delta_lon * 60 * math.cos(my_lat / 57.3)
		dist_nm = math.sqrt((y_nm**2) + (x_nm**2)) 
		brng = int (math.atan2(x_nm, y_nm) * 57.3)
		if brng < 0:
			brng = brng + 360  
		return str(int(dist_nm*1.15)).rjust(3," "), str(int(brng)).rjust(3," ")
	else:
		return "   ", "   "


