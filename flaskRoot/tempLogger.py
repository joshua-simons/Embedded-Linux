#Import Libraries we will be using
from flask import Flask, render_template, jsonify, Response
import time
import os
import sqlite3 as sqlite
import smtplib
import json
import threading

#SMTP eMail Variables
eFROM = "kd2egt@gmail.com"
eTO = "8453094409@msg.fi.google.com"
Subject = "Alert!"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

#Connect to the database
con = sqlite.connect('../log/templog.db')
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

#Set up Flask server to serve out the web page and return a json of the database when '/sqlData' is called
def flask_thread():
	con1 = sqlite.connect('../log/templog.db', check_same_thread=False)
	cur1 = con1.cursor()
	app = Flask(__name__)

	@app.route("/")
	def index():
		return render_template('index.html')

	@app.route("/sqlData")
	def chartData():
		con1.row_factory = sqlite.Row
		cur1.execute("SELECT * FROM templog")
		dataset = cur1.fetchall()
		chartData = []
		for row in dataset:
			chartData.append({"Date": row[0], "Temperature": float(row[1])})
		return Response(json.dumps(chartData), mimetype='application/json')

	if __name__ == "__main__":
		app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False)


webApp_thread = threading.Thread(target = flask_thread)
webApp_thread.daemon = True
webApp_thread.start()

try:
	while True:
	#Send text message alert if temperature is out of range
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
