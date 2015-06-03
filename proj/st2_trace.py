#!/usr/bin/python

import os, sys 

if (len(sys.argv) <= 2 or len(sys.argv) > 4): 
  print "invalid usage: command inputfile outfile"
  exit(1)

trace_in = open(sys.argv[1], "rb")
trace_out = open(sys.argv[2], "w")

## Read file in
## Run trace on each input
for line in trace_in:
  dest = str(str(line.split("(")[1]).split(")")[0])
  cmd_args = "-a -e -P ICMP -p 80 " + dest
  #x = os.popen("traceroute","cmd_args")
  cmd = "traceroute " + cmd_args + " >> " + str(sys.argv[2])
  print cmd
  ##os.system(cmd)
  ## Output to new file
