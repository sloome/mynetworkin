import os
import socket
os.system ("clear")
print ("type link")
hos = input()
ip = socket.gethostbyname(hos)
print ("host:",hos,)
print ("ip is",ip,)
print ("done")
