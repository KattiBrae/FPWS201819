#!/usr/bin/python
# -*- coding: ascii -*-

import sys, serial, time, datetime
ser=serial.Serial('/dev/ttyUSB0', timeout=1)

try:
    ser.write('$012\r')
    data=''
    while not ('\r' in data):
      data+=ser.read(1)
    print 'Giving:',data

except:
    print 'Finished'

