# Samson DeVol webclient for cs372 project 2
# 9-26-2022

import socket, sys

# parse inputs
server_name = sys.argv[1]
if len(sys.argv)>2: 
  port_number = int(sys.argv[2])
else:
  port_number=80;

# ask OS for a socket
s = socket.socket()

# perform DNS lookup
#connect the socket
s.connect((server_name,port_number))

# send data
s.sendall("GET / HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n".format(server_name).encode())

# recieve data
while 1: 
  d = s.recv(4096)  # Receive up to 4096 bytes
  print(d)
  if len(d)==0:
    break

# close
s.close()
print(d)
