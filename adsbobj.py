import time
from queue import Queue
import re

import sqlite3 as lite
import dbapi
import filtertext
import nav
import collision

class ADSBobj(object):
	def __init__(self):
		self.lat = 37.374621 
		self.lon = -121.920155 
		self.q = Queue()
		self.mode = ""
		self.ac = {}
		self.icao = ""

		self.con = lite.connect(":memory:")
		self.cur = self.con.cursor()
		dbapi.aircraft_table(self.cur)
		dbapi.master_table(self.cur)

	def lat_lon(self):
		return self.lat, self.lon

	def set_lat_lon(self, lat_in, lon_in):
		self.lat = lat_in
		self.lon = lon_in

	def trim(self):
		now = int(time.time())
		tag_delete = []
		for k in list(self.ac):
			delta_t = now - self.ac[k]["ts"]
			if delta_t > 60:
				tag_delete.append(k)
		for i in tag_delete:
			del self.ac[i]

	def display(self):
		update = 0
		now = int(time.time())
		for k in list(self.ac):
			update = 1
			delta_t = now - self.ac[k]["ts"]
			if  ("db" in self.ac[k]):
				db_s = str(self.ac[k]["db"])
			else:
				db_s = "DB" 
			ns_s = self.ac[k]["ns"]
			ew_s = self.ac[k]["ew"]
			kts = nav.ns_ew(ns_s, ew_s)
			lat_s = self.ac[k]["lat"] 
			lon_s = self.ac[k]["lon"]
			alt_s = self.ac[k]["alt"].rjust (5, " ")
			dist_s, brng_s = nav.dist_brng(lat_s, lon_s, self.lat, self.lon)
			out_str = k+" "+str(delta_t).rjust(2, " ")+" "+db_s+" "+alt_s+" "+kts+" "+dist_s+" "+brng_s
			print(out_str)
		if update == 1:
			print("\n")

	def process(self):
		while not self.q.empty():
			a = self.q.get()
			if "DF 17" in a:
				self.mode = "DF 17"
			if "*" in a:
				self.mode = ""
			if self.mode == "DF 17":
				if "ICAO" in a:
					self.icao = filtertext.filt_hex(a[-7:-1].strip().upper())
					if len(self.icao) == 6 and not self.icao in self.ac:
						self.ac[self.icao] = {}
						dbi = dbapi.get_ac(self.cur, self.icao)
						self.ac[self.icao]["db"] = dbi 
						self.ac[self.icao]["lat"] = ""
						self.ac[self.icao]["lon"] = ""
						self.ac[self.icao]["alt"] = ""
						self.ac[self.icao]["ns"] = ""
						self.ac[self.icao]["ew"] = ""

				if self.icao != "" and self.icao in self.ac:
					if "Latitude : " in a:
						if not "not decoded" in a:
							lat = filtertext.filt_float(a)
							if  (not lat == "") and len(lat) > 7 :
								self.ac[self.icao]["lat"] = lat
					if "Longitude:" in a:
						if not "not decoded" in a:
							lon = filtertext.filt_float (a) 
							self.ac[self.icao]["lon"] = lon
					if "Altitude" in a:
						alt = re.sub('[^0123456789]', '', a)
						if not alt == "":
							self.ac[self.icao]["alt"] = alt
					if "NS" in a:
						ns = filtertext.filt_float(a)
						if not ns == "":
							self.ac[self.icao]["ns"] = ns
					self.ac[self.icao]["ts"] = int(time.time())
					if "EW" in a:
						ew = filtertext.filt_float(a)
						if not ew =="":
							self.ac[self.icao]["ew"] = ew
		i1 = 0
		i2 = 0
		for k in list(self.ac):
			for k2 in list(self.ac):
				if (i2 > i1):
					#print(k + " " + k2)
					if collision.detect(self.ac[k], self.ac[k2]):
						print(k + " " + k2)
				i2 += 1
			i2 = 0		
			i1 += 1

	def rx_thread(self):
		path = "./adsbfifo"
		fifo = open(path, "r")
		for line in fifo:
			self.q.put(line)
		fifo.close()

