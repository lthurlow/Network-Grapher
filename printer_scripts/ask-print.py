#!/usr/bin/python

import urllib, httplib
import urllib2
import os

f = open("printer-list.txt","r")
w = open("printer-web2.txt","w")

for l in f:
  addr = "http://" + str(l)
  try:
    page = urllib2.urlopen(addr, None, 5)
    w.write(l)
    #print "read " + l
    #pgtxt = page.read()
    #print pgtxt
  except (urllib2.URLError, httplib.BadStatusLine) as e:
    print "could not read " + l.strip() + ": " + str(e)
