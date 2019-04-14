#!/usr/bin/python
# -*- coding: ascii -*-
import serial, time, datetime
ser=serial.Serial('/dev/ttyUSB0', timeout=1)
while True:
    ser.write('%0101090680\r')
    data=''
    while not ('\r' in data):
      data+=ser.read(1)
    now=time.strftime("%Y%m%d%H%M%S",time.localtime())
    value=(now+","+str(float(data[1:])*20))
    print 'Giving:',now,value
print 'Finished'
