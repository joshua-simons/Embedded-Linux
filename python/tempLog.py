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
buttonPin = 26

#Temp and Humidity Sensor
tempSensor = Adafruit_DHT.DHT22
#LED Variables-----------------------------------------------------------------------------------------
#Duration of each Blink
blinkDur = .1
#Number of times to Blink the LED
blinkTime = 7
#-----------------------------------------------------------------------------------------------------

#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def oneBlink(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDur)
	GPIO.output(pin,False)
	time.sleep(blinkDur)

def stayLit(pin):
	GPIO.output(pin,True)

def ledOff(pin):
	GPIO.output(pin,False)

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

#Use the blinkonce function in a loopity-loop when the button is pressed
try:

	with open("../log/templog.csv", "a") as log:

		while True:
			input_state = GPIO.input(buttonPin)
			if input_state == False:
				for i in range (blinkTime):
					oneBlink(redPin)
				time.sleep(.2)
				data1 = readF(tempPin)
				data2 = readH(tempPin)
				print ('The Temperature is '+data1+'*F')
				print ('The Humidity is '+data2+'%')
				log.write("{0},{1},{2}\n".format(time.strftime('new Date(%Y,%m,%d,%H,%M,%S)'),data1,data2))
				log.flush()
				os.fsync(log)

except KeyboardInterrupt:
#	os.system('clear')
	print('Thanks for Blinking and Thinking!')
	GPIO.cleanup()

