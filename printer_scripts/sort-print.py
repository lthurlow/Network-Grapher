#!/usr/bin/python

import urllib, httplib
import urllib2
import os, sys

def print_serve(web_addr):
  printdict = {}
  hp_laserjet = "/set_config_networkPassword.html?tab=Networking&menu=NetPasswd"
  #"/password.html" for other models
  printdict["hplj"] = hp_laserjet
  #if reachable, check for Admin Password: <Set>

  hp_jetdirect = "/hp/jetdirect"
  printdict["hjjd"] = hp_jetdirect
  #if login is not there, not accessed

  ricoh = "/web/guest/en/websys/webArch/authForm.cgi"
  printdict["ricoh"] = ricoh
  #default username = supervisor, no password

  dell = "/security/set_password.htm"
  #/ews/setting/setews.htm for older model
  printdict["dell"] = dell
  ## read and check name="GSI_OLD_USER_PASSWORD" and disabled=""
  ## if so, old password is diabled, meaning set first one.

  cannon = "_top.html"
  #_devmgr.html, default password = "", others set.
  printdict["cannon"] = cannon

  xerox = "/securitysettings.html"
  printdict["xerox"] = xerox

  brother = "http://128.114.79.185/admin/administrator_settings.html"
  # defaults admin:access
  
  for key in printdict:
    print web_addr +  printdict[key], key
  """
    try:
      url = web_addr+type
      page = urllib2.urlopen(url, None, 5) # set timeout for each attempt
      ## if we can open the webpage with no error values we are in!
      if key == "hjjd":
        if "Login" in page.read():
          # authorized access, we lose, break
          #strip off http
          addr = web_addr[7:]
          #add comments
          comm = addr + ": " + key + ": Protected"
          w_prot.write(comm)
          break
        else:
          #no login means no deafult password set.
          #strip off http
          addr = web_addr[7:]
          #add comments
          comm = addr + ": " + key + ": No Password"
          w_unprot.write(comm)
          break
      if key == "hplj":
        #if we could reach this page, we win, no encryption by default
          #strip off http
          addr = web_addr[7:]
          #add comments
          comm = addr + ": " + key + ": No Password"
          w_unprot.write(comm)
          break
      if key == "ricoh":
        #we need to try and login with default credentials
        call_ricoh(web_addr)
        
        

    except urllib2.URLError as e:
      try:
        if e.code == 401:
          # authorized access, we lose, break
          #strip off http
          addr = web_addr[7:]
          #add comments
          comm = addr + ": " + key + ": Protected"
          w_prot.write(comm)
          break
        else if e.code = 500:
          #Server Error, not running, so quit.
          break
        #else
          # 404, we continue as it may not be our selected value
      except AttributeError as c:
    except httplib.BadStatusLine as e:
      # bad status line, not correct response from server
      # drop server
      break
  """

f = open("printer-web.txt","r")
w_unprotect = open("unprotected.txt", "w")
w_prot = open("protected.txt","w")

for l in f:
  addr = "http://" + str(l).strip()
  print_serve(addr)
