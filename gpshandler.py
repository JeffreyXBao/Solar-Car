import gpsd
import time

gpsd.connect()
packet = gpsd.get_current()
#print(packet.movement()['speed'])
speed = packet.movement()['speed']

def updatePacket(interval):
    global packet
    packet = gpsd.get_current()

    try:
        speed = packet.movement()['speed']
    except Exception as e:
        print e

    time.sleep(interval)
try:
   thread.start_new_thread(updatePacket,(.1))
except:
   print "Error: unable to start thread"

def getSpeed():
    global speed
    return speed
