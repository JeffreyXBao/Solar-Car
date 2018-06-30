import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leftSigPin = 4
rightSigPin = 5
hazSigPin = 6

leftOutPin = 25
rightOutPin = 24

GPIO.setup(leftSigPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(rightSigPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(hazSigPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(leftOutPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(rightOutPin, GPIO.OUT, initial=GPIO.LOW)

leftBool = GPIO.input(leftSigPin)
rightBool = GPIO.input(righSigPin)
hazBool = GPIO.input(hazSigPin)

a = True
while a:
	time.sleep(.1)

	leftBool = GPIO.input(leftSigPin)
	rightBool = GPIO.input(rightSigPin)
	hazBool = GPIO.input(hazSigPin)

	if (leftBool == GPIO.HIGH || rightBool == GPIO.HIGH || hazBool == GPIO.HIGH):
		if (leftBool == GPIO.HIGH || hazBool == GPIO.HIGH):
			GPIO.output(leftOutPin, 1)
		if (rightBool == GPIO.HIGH || hazBool == GPIO.HIGH):
			GPIO.output(rightOutPin, 1)
		time.sleep(.25)
		if (leftBool == GPIO.HIGH || hazBool == GPIO.HIGH):
			GPIO.output(leftOutPin, 0)
		if (rightBool == GPIO.HIGH || hazBool == GPIO.HIGH):
			GPIO.output(rightOutPin, 0)
		time.sleep(.15)

#except KeyboardInterrupt:
#	GPIO.cleanup()
#GPIO.cleanup()
