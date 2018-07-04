import time
import display
#import batmonitor
import gpshandler

speed = 0

while (True):
    global speed
    speed = gpshandler.getSpeed()
    mph = speed*0.621371
    text = str(mph) + "mph"
    display.updateDisplay()
    time.sleep(.3)
