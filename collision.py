def detect(ac1, ac2):
	lat1 = ac1["lat"]
	lon1 = ac1["lon"]
	ns1  = ac1["ns"]
	ew1  = ac1["ew"]
	lat2 = ac2["lat"]
	lon2 = ac2["lon"]
	ns2  = ac2["ns"]
	ew2  = ac2["ew"]

	if ((lat1) and (lon1) and (ns1) and (ew1) and (lat2) and (lon2) and (ns2) and (ew2)): 
		return True
		#print(ac1["lat"])
		#print(ac2["lat"])
	else:
		return False

