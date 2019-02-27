#Import Libraries we will be using
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import sys

#Assign GPIO pins
redPin = 27
greenPin = 22
tempPin = 17

#Temp and Humidity Sensor
tempSensor = Adafruit_DHT.DHT22
#LED Variables-----------------------------------------------------------------------------------------
#Duration of each Blink
blinkDur = .1
#Number of times to Blink the LED
blinkTime = 7
#------------------------------------------------------------------------------------------------------
#Time between sensor readings
sensorDelay = 60
#------------------------------------------------------------------------------------------------------

#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)

def redBlink(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDur)
	GPIO.output(pin,False)
	time.sleep(blinkDur)

def greenLight(pin):
	GPIO.output(redPin,False)
	GPIO.output(pin, True)

def readF(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}'.format(temperature)
	else:
		print('Error Reading Sensor')

	return tempFahr

def readH(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	if humidity is not None and temperature is not None:
		humid = '{1:0.1f}'.format(temperature, humidity)
	else:
		print('Error Reading Sensor')

	return humid

old_time = 60
data1 = readF(tempPin)

try:
	with open("../log/templog.csv", "a") as log:

		while True:
			if 68 <= float(data1) <= 78:
				greenLight(greenPin)
			else:
				GPIO.output(greenPin, False)
				redBlink(redPin)

			if time.time() - old_time > 59:
				data1 = readF(tempPin)
				data2 = readH(tempPin)
				print ('The Temperature is '+data1+'*F')
				print ('The Humidity is '+data2+'%')
				log.write("{0},{1},{2}\n".format(time.strftime('%Y,%m,%d,%H,%M,%S'),data1,data2))
				log.flush()
				os.fsync(log)
				time.sleep(.2)
				old_time = time.time()

except KeyboardInterrupt:
#	os.system('clear')
	print('Thanks for Blinking and Thinking!')
	GPIO.cleanup()

