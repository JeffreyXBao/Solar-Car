import gpsd
import time
import thread

connectSuccess = False
packet = None
speed = 0

def connectAttempt():
    global connectSuccess
    try:
        gpsd.connect()
        connectSuccess = True
        print "successfully connected to gps service"
    except Exception as e:
        print e

def gpsThread():
    counter = 0
    while not connectSuccess:
        if counter > 10:
            counter = 0
            os.system('sudo killall gpsd')
            os.system('sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock')
        connectAttempt()
        counter += 1
        time.sleep(.1)
    updatePacket()

def updatePacket():
    global packet
    global speed
    packet = gpsd.get_current()

    while (True):
        lastErr = None
        try:
            packet = gpsd.get_current()
            speed = packet.movement()['speed']
            print "speed updated"
        except Exception as err:
            if err != lastErr:
                print err
            lastErr = err
        time.sleep(.1)

try:
    thread.start_new_thread(gpsThread,())
except Exception as err:
    print "Error: unable to start gps thread"
    print err

def getSpeed():
    global speed
    return speed
