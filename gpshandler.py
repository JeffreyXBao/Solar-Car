import gpsd
import time

gpsd.connect()
packet = gpsd.get_current()
#print(packet.movement()['speed'])

def updatePacket(interval):
    global packet
    packet = gpsd.get_current()
    time.sleep(interval)
try:
   thread.start_new_thread(updatePacket,(interval))
except:
   print "Error: unable to start thread"

def getSpeed():
    return packet.movement()['speed']