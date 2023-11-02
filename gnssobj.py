from queue import Queue

class GNSSobj(object):
	def __init__(self):
		self.lat = 0.0
		self.lon = 0.0
		self.q = Queue()

	def lat_lon(self):
		return self.lat, self.lon

	def set_lat_lon(self, lat_in, lon_in):
		self.lat = lat_in
		self.lon = lon_in

	def process(self):
		print("Qinit")
		while not self.q.empty():
			print("Q")
			g = self.q.get()
			print(g)
			lat_s = g.split(' ')[0]
			lon_s = g.split(' ')[1]
			self.lat = float(lat_s) 
			self.lon = float(lon_s) 

	def rx_thread(self):
		path = "./gpsfifo"
		fifo = open(path, "r")
		for line in fifo:
			#print(line)
			self.nmea(line)
		fifo.close()

	def nmea(self, msg):
		if msg.startswith("$GPGGA") and ((",N," in msg) or (",S," in msg) or (",E," in msg) or (",W," in msg)):
			x = msg.split(',')
			lat_l = float(x[2]) / 100
			lon_l = float(x[4]) / 100
			if ",W," in msg:
				lon_l = -lon_l
			if ",S," in msg:
				lat_l = -lat_l
			self.q.put(str(lat_l)+" "+str(lon_l))

