import RPi.GPIO as GPIO 
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

n = 100
while n > 0:
	n -= 1
	GPIO.output(22, True)
	time.sleep(1)
	GPIO.output(22, False)
	time.sleep(1)
print ("OK")
GPIO.cleanup()

