#Import Libraries we will be using
import RPi.GPIO as GPIO
import time
import os
import sqlite3 as logdb
import sys

#Read the i2c sensor and convert to Fahrenheit
def readF():
	tempfile_path = "/sys/bus/w1/devices/28-031689e53aff/w1_slave"
	if not os.path.exists(tempfile_path):
		print("Error: Sensor Not Connected")
		return False
	tempfile = open(tempfile_path)
	tempfile_text = tempfile.read()
	tempfile.close()
	tempC = float(tempfile_text.split("\n")[1].split("t=")[1]) / 1000
	tempF = '{0:0.1f}'.format(tempC * 9.0 / 5.0 + 32.0)
	return tempF

#Dummy time for first itteration of the loop
oldTime = 60

try:
	#Connect to the database
	con = logdb.connect('../log/templog.db')
	cur = con.cursor()

	while True:
		#if loop set for every 60 seconds
		if time.time() - oldTime > 59:
			data = readF()
			if not data:
				sleep(20)
				continue
			#Defines and executes the sql query (templog is the table name in the .db)
			query = "INSERT INTO templog (Date, Temperature) VALUES ('{}', '{}');"
			query = query.format(time.strftime("%Y-%m-%d %H:%M:%S"), data + "*F")
			cur.execute(query)
			con.commit()
			#Clear the console, and query the database. Prints the results to the console
			os.system('clear')
			print("Date, Temperature")
			for row in cur.execute('SELECT * FROM templog;'):
				print("{}, {}".format(row[0], row[1]))
			#Resets the oldTime to begin the countdown again
			oldTime = time.time()

#Spits an error if the database queries do not work as intended
except logdb.Error as e:
	print("Eroor %s:" % e.args[0])
	sys.exit(1)

#Accepts crtl+C as a keyboard interupt and exits cleanly
except KeyboardInterrupt:
	os.system('clear')
	print('Temerature Logger Exited Cleanly')

#Closes the database connection upon exiting in case it closes mid-write
finally:
	if con:
		con.close()
