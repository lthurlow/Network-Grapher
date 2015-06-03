#!/usr/bin/python

nessus = "/opt/nessus/bin/nessus"
print nessus

in_file = open("EXTENDED","r")

ip_list = []

count = 0
fcount = 0
out_file = open("TESTX","w")
for line in in_file:
  if count % 31 == 0:
    out_file.close()
    filename = "IPS-"+str(fcount)
    out_file = open(filename,"w")
    fcount += 1
    count = 1
  else:
    k = (line.strip().split(',')[2]).strip()
    if (k[0:3] == "128"):
      #print k
      ip_list.append(k)
      out_file.write(k+"\n")
      count += 1
  
