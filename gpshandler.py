import os
import gpsd
import time
import thread

os.system('sudo systemctl stop gpsd.socket')
os.system('sudo systemctl disable gpsd.socket')
os.system('sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock')

connectSuccess = False
packet = None
speed = 0
errCount = 0

def connectAttempt():
    global connectSuccess
    try:
        gpsd.connect()
        connectSuccess = True
        print "successfully connected to gps service"
    except Exception as e:
        print "failed to connect to gps service"
        connectSuccess = False
        print e

def restartGPS():
    os.system('sudo killall gpsd')
    os.system('sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock')
    print "gps service restarted"

def connectLoop():
    global connectSuccess

    connectSuccess = False
    counter = 0

    while not connectSuccess:
        if counter > 100:
            counter = 0
            restartGPS()
            time.sleep(.5)
        connectAttempt()
        counter += 1
        time.sleep(.1)

def gpsThread():
    connectLoop()
    updatePacket()

def reconnect():
    connectLoop

def updatePacket():
    global packet
    global speed
    global errCount

    while (True):
        try:
            packet = gpsd.get_current()
            speed = packet.movement()['speed']
        except Exception as err:
            print "error updating packet"
            print err
            errCount += 1
            if errCount > 100:
                restartGPS()
                time.sleep(.5)
                reconnect()
                errCount = 0
        time.sleep(.1)

try:
    thread.start_new_thread(gpsThread,())
except Exception as err:
    print "Error: unable to start gps thread"
    print err

def getSpeed():
    global speed
    return speed
