def country_lu(hex24):
	with open('icao.txt') as fp:
		icao = int(hex24, 16)
		for line in fp:
			a = line.split()
			lo = a[0].strip()
			hi = a[1].strip()
			lo_int = int(lo, 16)
			hi_int = int(hi, 16)
			if lo_int < icao and hi_int > icao:
				return(a[2]) 
	return ("blah")

#cc = country_lu (0xaa4464)
#print(cc)

