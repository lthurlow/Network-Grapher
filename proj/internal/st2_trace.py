#!/usr/bin/python

import os, sys, subprocess

if (len(sys.argv) <= 2 or len(sys.argv) > 4): 
  print "invalid usage: command inputfile outfile"
  exit(1)

trace_in = open(sys.argv[1], "rb")
trace_out = open(sys.argv[2], "w")

## Read file in
## Run trace on each input
## store ip's in list for later
ip_set = []
for line in trace_in:
  if ( (len(line.split('.')) == 6) and ("report" in line) ) :
    ip_set.append(str(str(line.split("(")[1]).split(")")[0]))

ip_set = set(ip_set)
total = len(ip_set)
numtogo = len(ip_set)
for l in ip_set:
  dest = str(l)
  cmd_args = "-a -e -I -q 2 -m 18 " + dest
  cmd = "traceroute " + cmd_args
  print cmd, " ( ", numtogo, " of ", total, " )"
  proc = subprocess.Popen(['traceroute','-a','-e','-q','2','-I', '-m', '18', dest], \
              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  while(True):
    output = proc.stdout.readline()
    if not output:
      break
    print output.strip()
    trace_out.write(str(output))
  trace_out.write("#####\n")
  numtogo -= 1
