#Import Libraries we will be using
import RPi.GPIO as GPIO
import time
import os

#Assign GPIO pins
redPin = 27
buttonPin = 26

#LED Variables--------------------------------------------------------
#Duration of each Blink
blinkDur = .1
#Number of times to Blink the LED
blinkTime = 7
#---------------------------------------------------------------------

#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Make the LED blink once
def oneBlink(pin):
    GPIO.output(pin, True)
    time.sleep(blinkDur)
    GPIO.output(pin, False)
    time.sleep(blinkDur)

#Read the temperature sensor from file
def readF():
    tempfile_path = "/sys/bus/w1/devices/28-031689e53aff/w1_slave"
    if not os.path.exists(tempfile_path):
        print("Error Reading Sensor")
        return False
    tempfile = open(tempfile_path)
    tempfile_text = tempfile.read()
    tempfile.close()
    tempCel = float(tempfile_text.split("\n")[1].split("t=")[1]) / 1000
    tempFahr = '{0:0.1f}°F'.format(tempCel * 9.0 / 5.0 + 32.0)
    return tempFahr

try:
    while True:
        input_state = GPIO.input(buttonPin)
        if input_state == False:
            for i in range (blinkTime):
                oneBlink(redPin)
            time.sleep(.2)
            data = readF()
            print(data)

except KeyboardInterrupt:
    os.system('clear')
    print('Thanks for Blinking and Thinking!')
    GPIO.cleanup()
