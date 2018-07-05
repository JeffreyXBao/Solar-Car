import os
import gpsd
import time
import thread

#start gpsd service (web server)
os.system('sudo systemctl stop gpsd.socket')
os.system('sudo systemctl disable gpsd.socket')
os.system('sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock')

#declare global vars
connectSuccess = False
packet = None
speed = 0
errCount = 0

#function that trys and catches connect attempts to the gps service
#used only by the connectLoop() function
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

 #restarts gpsd service
def restartGPS():
    os.system('sudo killall gpsd')
    time.sleep(.1)
    os.system('sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock')
    print "gps service restarted"

#contiuously tries to connect to gpsd service
def connectLoop():
    global connectSuccess

    connectSuccess = False
    counter = 0

    while not connectSuccess:
        #restarts gpsd service is it fails over 100 times
        if counter > 100:
            counter = 0
            restartGPS()
            time.sleep(.5)

        #tries to connect
        connectAttempt()
        counter += 1
        time.sleep(.1)

#initializes seperate GPS thread
def gpsThread():
    connectLoop()
    updatePacket()

#function to restart gpsd service and reconnect to it
def reconnect():
    restartGPS()
    time.sleep(.5)
    connectLoop()

#updates information from gpsd service
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
                reconnect()
                errCount = 0
        time.sleep(.1)

#initializes gps thread
try:
    thread.start_new_thread(gpsThread,())
except Exception as err:
    print "Error: unable to start gps thread"
    print err

#returns current speed from gpsd reading
def getSpeed():
    global speed
    return speed
