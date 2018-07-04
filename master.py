import time
import display
#import batmonitor
import gpshandler

speed = 0

while (True):
    global speed
    speed = gpshandler.getSpeed()
    display.updateDisplay(speed)
    time.sleep(1)