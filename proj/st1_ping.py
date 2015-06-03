#!/usr/bin/python

import os,sys,time

ipaddr = "128.114."
x = 0
y = 0
ipaddrs = 65025

for i in xrange(255,1,-1):
  for j in xrange(255,1,-1):
    print "scanning: " +ipaddr + str(x) + "." + str(y) + " (" + str(ipaddrs-(i+j)) + ")"
    Z = "/usr/local/sbin/fping -a -A " + ipaddr + str(x) + "." + str(y) + " >> pings.txt"
    #print Z
    os.system(Z)
    y += 1
  x+= 1
  y = 1
