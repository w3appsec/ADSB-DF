path = "./gpsfifo"
fifo = open(path, "r")
for line in fifo:
	print(line)


