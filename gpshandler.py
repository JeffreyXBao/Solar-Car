import gpsd
import time
import thread

connectSuccess = False
packet = None
speed = 0

def connectAttempt():
    try:
        gpsd.connect()
        connectSuccess = True
    except Exception as e:
        print e

def gpsThread():
    while not connectSuccess:
        connectAttempt()
    updatePacket()

def updatePacket():
    global packet
    global speed
    packet = gpsd.get_current()

    while (True):
        try:
            packet = gpsd.get_current()
            speed = packet.movement()['speed']
        except Exception as err:
            print err
        time.sleep(.1)

try:
    thread.start_new_thread(gpsThread,())
except Exception as err:
    print "Error: unable to start gps thread"
    print err

def getSpeed():
    global speed
    return speed
