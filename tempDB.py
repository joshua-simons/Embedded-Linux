#Import Libraries we will be using
import time
import os
import smtplib
import json
import sqlite3

old_time = 60

#Time between sensor readings
sensorDelay = 60
#------------------------------------------------------------------------------------------------------
#SMTP eMail Variables
eFROM = "kd2egt@gmail.com"
eTO = "8453094409@msg.fi.google.com"
Subject = "Danger: Impending Doom"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#------------------------------------------------------------------------------------------------------

#Connect to the database
con = sqlite3.connect('log/templog.db')
cur = con.cursor()

eChk = 0

def alert(data):
	global eChk
	if eChk == 0:
		Text = "The monitor now indicates that the temperature is now "+str(data)
		eMessage = 'Subject: {}\n\n{}'.format(Subject, Text)
		server.login("kd2egt@gmail.com", "ybihbernfcvynzju")
		server.sendmail(eFROM, eTO, eMessage)
		server.quit
		eChk = 1

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
#Read Temperature right off the bat
data = readF()

try:
	while True:
	#Send text message alert if temperature is out of range
		global eChk
		if 68 <= float(data) <= 78:
			eChk = 0
		else:
			alert(data)
		#if loop set for every 60 seconds
		if time.time() - oldTime > 59:
			data = readF()
			if not data:
				sleep(5)
				continue
			#Defines and executes the sql query (templog is the table name in the .db)
			query = "INSERT INTO templog (Date, Temperature) VALUES ('{}', '{}');"
			query = query.format(time.strftime("%Y-%m-%d %H:%M:%S"), data)
			cur.execute(query)
			con.commit()
			print(time.strftime("%Y-%m-%d %H:%M:%S")+" "+data)
			oldTime = time.time()

except KeyboardInterrupt:
	os.system('clear')
	con.close()
	print ("Temperature Logger and Web App Exited Cleanly")
	exit(0)

