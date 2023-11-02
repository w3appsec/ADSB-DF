import time
import threading
from threading import Thread

from adsbobj import ADSBobj
from gnssobj import GNSSobj

adsb = ADSBobj()
gnss = GNSSobj()

adsb_th = Thread(target=adsb.rx_thread)
adsb_th.start()

gps_th = Thread(target=gnss.rx_thread)
gps_th.start()

while True:
	gnss.process()
	lat, lon = gnss.lat_lon()
	print(lat)
	print(lon)

	adsb.process()
	adsb.trim()
	adsb.set_lat_lon(lat, lon)
	adsb.display()

	time.sleep(1)
