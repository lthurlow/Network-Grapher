#!/usr/bin/python

import os,sys,time

ipaddr = "128.114."
x = 0
y = 0

for i in xrange(255,0,-1):
  for j in xrange(255,1,-1):
    print "scanning: " + ipaddr + str(x) + "." + str(y)
    Z = "host " + ipaddr + str(x) + "." + str(y) + " >> hosts.txt"
    os.system(Z)
    y += 1
  x+= 1
  y = 1
