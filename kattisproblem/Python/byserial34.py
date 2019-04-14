#!/usr/bin/python
# -*- coding: ascii -*-
import sys, serial, time, datetime
aprov=57.5
pprov=10.0


ser=serial.Serial('/dev/ttyUSB0', timeout=1)
try:
  interval=int(sys.argv[1])
  filename=time.strftime("%Y%m%d%H%M%S",time.localtime())
  datafile=open(filename,'w')
  while True:

    ser.write('#013\r')
    data=''
    while not ('\r' in data):
      data+=ser.read(1)
    area=data

    ser.write('#014\r')
    data=''
    while not ('\r' in data):
      data+=ser.read(1)
    pressure=data

    now=time.strftime("%Y%m%d%H%M%S",time.localtime())
    value=(now+" "+str(float(area[1:])*aprov)+' '+str(float(pressure[1:])*pprov))
    print 'Giving:',now,value
    datafile.write(value+"\n")
    time.sleep(interval)
except:
    raise 	
    print 'Finished'
    datafile.close()
