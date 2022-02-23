# for the desktop app, get address of pi and connect
# not sure how to allow any device to pair without initial IP address though
#have the desktop connect to two different hosts (Won't need multiple threads, have two pis)
#

import socket

pi_addr= '?' # we can get  
port = 3 
backlog = 1
size = 1024
blue_pi = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
blue_pi.bind((pi_addr,port))
blue_pi.listen(backlog)
try:
    client, address = blue_pi.accept()
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data)
except:	
    print("Closing socket")	
    client.close()
    blue_pi.close()
