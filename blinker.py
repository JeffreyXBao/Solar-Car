import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)

#GPIO.add_event_detect(4, GPIO.BOTH)

leftBool = 0

#def updateLeft(var):
#	leftBool=GPIO.input(4)
#	GPIO.output(25,leftBool)
#	print GPIO.input(4)
#	print leftBool
#GPIO.add_event_callback(4,updateLeft)

a = True
while a:
	time.sleep(.1)
	if (GPIO.input(4) == GPIO.HIGH):
	#if leftBool == 1:
		GPIO.output(25, 1)
		print "on"
		time.sleep(.25)
		GPIO.output(25, 0)
		print "off"
		time.sleep(.25)

#except KeyboardInterrupt:
#	GPIO.cleanup()
#GPIO.cleanup()
