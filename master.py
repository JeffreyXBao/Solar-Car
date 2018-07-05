import time
import display
#import batmonitor
import gpshandler

speedM = 0
voltageAux = 0

while (True):
    global speedM
    #voltageAux = batmonitor.getAuxV()
    speedM = gpshandler.getSpeed()
    mph = speedM*0.621371

    text = str(mph) + "mph\nAux:" + str(voltageAux) + "V"
    display.updateDisplay(text)
    time.sleep(.3)
