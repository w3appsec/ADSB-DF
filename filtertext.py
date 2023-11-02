import re

def filt_float (l):
	return re.sub('[^.\-0123456789]', '', l)

def filt_hex (l):
	return re.sub('[^0123456789ABCDEF]', '', l)

def str_n(s, n):
	if len(s) > n:
		return s[:n]
	if len(s) < n:
		return s.rjust(n," ")
	return s


