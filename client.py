#ANKITKUMAR CHAUDHARY
#100887553
#TPRG 2
#the client

import socket
import json

s = socket.socket()
host = '192.168.2.107'
port = 5000
s.connect((host, port))
print(s.recv(1024).decode('utf-8'))
s.close()
