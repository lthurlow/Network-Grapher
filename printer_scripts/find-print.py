#!/usr/bin/python

import sys, os

f = open("campus-print-scan.txt","r")
pname = ""
dict = {}
for line in f:
  if "Nmap scan report" in line and "[" not in line and "(" in line:
    #print line
    pname = str(str(line.split("(")[1]).split(")")[0])
  if "open  printer" in line:
    dict[pname] =1
    #print line, pname

for k in dict:
  print k
#print dict
