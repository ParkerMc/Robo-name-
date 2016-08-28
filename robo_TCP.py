# Echo client program
import socket
import struct
import nxt.locator
from nxt.motor import *
print "looking for robot"
b = nxt.locator.find_one_brick()
print "robot Found!!"
HOST = raw_input("Host: ")
PORT = 5660           # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
m_x = Motor(b, PORT_B)
m_y = Motor(b, PORT_C)
speed = 75
yspeed = 35
xspeed = 35
yval = 0
xval = 0
add = float(0.8)
while (True):
    try:
        ox = xval
        oy = yval
        data = s.recvfrom(1024)[0].split(",")
        xval = data[0]
        yval = data[1]
        print (xval, yval)
        xval = float(xval)
        yval = float(yval)
        #print xval
        if xval == 0 and ox != 0: m_x.idle()
        elif xval > 0:
            try:
                m_x.run(-xspeed*(abs(xval)+add))
            except nxt.motor.BlockedException:
                m_x.turn(speed, dataX)
        elif xval < 0:
            try:
                m_x.run(xspeed*(abs(xval)+add))
            except nxt.motor.BlockedException:
                m_x.turn(-speed, dataX)
        if yval == 0 and oy !=0: m_y.idle()
        elif yval < 0:
            try:
                m_y.run(yspeed*(abs(yval)+add))
            except nxt.motor.BlockedException:
                m_y.turn(-speed, dataX)
        elif yval > 0:
            try:
                m_y.run(-yspeed*(abs(yval)+add))
            except nxt.motor.BlockedException:
                m_y.turn(speed, dataX)

    except Exception, e: #KeyboardInterrupt:
    	print data
    	#print xval
    	#print yval
        #s.close()
        #m_x.idle()
        #m_y.idle()
        raise e
