import sys, csv
import cclu

def get_ac (cur, hexin):
	info = get_ac_usa(cur, hexin)
	if info == "":
		info = cclu.country_lu(hexin).ljust(20," ")
	return info

def get_ac_usa (cur, hexin):
	cur.execute("SELECT * FROM mstr INNER JOIN acrft ON (mstr.mfg = acrft.code) WHERE hex24 = '" + hexin + "';")
	f1 = cur.fetchone()
	if (isinstance(f1, tuple)):
		return f1[2][:10].ljust(10," ")+" "+f1[6][:9].ljust(9," ")
	else:
		return ""

def master_table (cur):
	cur.execute("CREATE TABLE IF NOT EXISTS mstr (n text, mfg text, name text, hex24 text primary key, FOREIGN KEY(mfg) REFERENCES acrft (code));")
	f=open('./csv/MASTER.txt','r')
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		if row:
			print (row [33])
			cur.execute("INSERT INTO mstr VALUES (?,?,?,?)", (row[0],row[2],row[6],row[33].strip()))
	f.close ()
	return

def aircraft_table (cur):
	cur.execute("CREATE TABLE IF NOT EXISTS acrft (code text primary key, mfr text, model text);")

	f=open('csv/ACFTREF.txt','r')
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		if row:
			print(row [0])
			print(row [1])
			print(row [2])
			cur.execute("INSERT INTO acrft VALUES (?,?,?)",(row[0],row[1],row[2].strip()))
	f.close ()
	return
