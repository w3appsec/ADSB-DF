import signal
import time

def handler(signum, frame):
	print("mowb")

signal.signal(signal.SIGINT, handler)

time.sleep(10)

