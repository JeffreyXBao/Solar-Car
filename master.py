import time
import display
import batmonitor
import gpshandler

while (True):
    global speedM
    #voltageAux = batmonitor.getAuxV()
    speedM = gpshandler.getSpeed()
    auxV = batmonitor.getAuxV()
    mph = speedM*0.621371

    
    text = str(mph) + "mph\nAux:" + str(auxV) + "V"
    display.updateDisplay(text)
    time.sleep(.5)
