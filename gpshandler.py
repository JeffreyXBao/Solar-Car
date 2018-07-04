import gpsd
import time
import thread

gpsd.connect()
packet = gpsd.get_current()
#print(packet.movement()['speed'])
#speed = packet.movement()['speed']
speed = 0

def updatePacket():
    global packet
    global speed
    packet = gpsd.get_current()

    while (True):
        try:
            packet = gpsd.get_current()
            speed = packet.movement()['speed']
	    #print "speed updated"
        except Exception as e:
            print e
        time.sleep(.1)
try:
   thread.start_new_thread(updatePacket,())
except Exception as err:
	print "Error: unable to start gps updater thread"
	print err
def getSpeed():
    global speed
    #print speed
    return speed
