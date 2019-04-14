#!/usr/bin/python
# -*- coding: ascii -*-
import sys, serial, time, datetime
ser=serial.Serial('/dev/ttyUSB0', timeout=1)
try:
  interval=int(sys.argv[1])
  filename=time.strftime("%Y%m%d%H%M%S",time.localtime())
  datafile=open(filename,'w')
  while True:
    ser.write('#014\r')
    data=''
    while not ('\r' in data):
      data+=ser.read(1)
    now=time.strftime("%Y%m%d%H%M%S",time.localtime())
    value=(now+","+str(float(data[1:])*10))
    print 'Giving:',now,value
    datafile.write(value+"\n")
    time.sleep(interval)
except:
    print 'Finished'
    datafile.close()
