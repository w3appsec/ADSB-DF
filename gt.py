import time
import threading
from threading import Thread

from gnssobj import GNSSobj

gnss = GNSSobj()

gps_th = Thread(target=gnss.rx_thread)
gps_th.start()

while True:
	gnss.process()
	lat, lon = gnss.lat_lon()
	print(lat)
	print(lon)

	time.sleep(1)
