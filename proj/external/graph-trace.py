#!/usr/bin/env python

import os, sys
import re
import networkx, pygraphviz
import matplotlib.pyplot as plt

#from pygrphviz import *

ex_file = open("ex_trace.txt","r")
in_file = open("in_trace.txt","r")

scan_list = []
current = []
past = []
unique = {}
dest = "" # Compare, if dest != lest, unreachable addr
last = ""
for line in ex_file:
  #print line.strip()
  ## Get our destination address
  if ("traceroute" in line): # On line 1 of output, get ip addr
    dest = str(str(line.strip().split("(")[1]).split(")")[0])
    #out_file.write("###\n")
    continue
  ## Dont worry about lines that are not found.
  if re.search('^[0-9]+\s+\*\s\*', line.strip()):
    past = ["","firewall",""]
    continue
  if ("#####" in line):
    last = past[2]
    if (last != dest):
      print "Unreachable: ", dest
    else:
      singleline = ""
      count = 0
      for x in scan_list:
        singleline += ', '.join(x)
        if (count % 1 == 0):
          unique[singleline] = 0
          count = 0
          singleline = ""
        count+=1

    scan_list = []
    continue

  ## Find the first traceroute line
  if re.search('^1\s',line.strip()):
    #print line.strip()
    AS = re.search('AS[0-9]+', line.strip()).group(0)
    name = re.search('\s[a-zA-Z0-9._-]+\s',line.strip()).group()
    IP = re.search('\([0-9.]+\)',line.strip()).group(0)
    IP = IP[1:-1] #remove parens
    #print AS, name, IP
    current = [AS, name, IP]
    past = ["","",""]
  else:
    AS = re.search('AS[0-9]+', line.strip()).group(0)
    name = re.search('\s[a-zA-Z0-9._-]+\s',line.strip()).group()
    IP = re.search('\([0-9.]+\)',line.strip()).group(0)
    IP = IP[1:-1] #remove parens
    current = [AS.strip(), name.strip(), IP.strip()]
      
    ## Add link to past
  #print current, past
  both = current + past
  scan_list.append(both)
  past = current


G = networkx.Graph()
for k in unique:
  if "comcast" not in k or "cenic" not in k or "router.belkin" not in k \
    or "###" not in k:
    out_file.write(k+"\n")
    G.add_node(k.split(',')[1])
for k in unique:
  print k
  if "comcast" not in k or "cenic" not in k or "router.belkin" not in k \
    or "###" not in k:
    G.add_edge(k.split(',')[1], k.split(',')[4])

networkx.write_dot(G,"data.dot")
os.system("sfdp -x -Goverlap=prism -Tpng data.dot > data.png")


#run grapher
pdf_file = "FULL_OUT"
run = "./grapher " + str(out_file) + " " + str(pdf_file)
print run
