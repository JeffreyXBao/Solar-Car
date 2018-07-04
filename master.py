import time
import display
#import batmonitor
import gpshandler

speed = 0
voltageAux = 0

while (True):
    global speed
    #voltageAux = batmonitor.getAuxV()
    speed = gpshandler.getSpeed()
    mph = speed*0.621371

    text = str(mph) + "mph\nAux:" + str(voltageAux) + "V"
    display.updateDisplay(text)
    time.sleep(.3)
