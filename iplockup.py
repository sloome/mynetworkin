import os 
from geoip import geolite2
os.system ("clear")
print ("""
______________
ip~of~target :
--------------
""")
ip = input()
locktor = geolite2.lookup(ip)
print ("locktor")
