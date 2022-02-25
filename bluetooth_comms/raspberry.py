# for the pi, connect with any adress that pairs using hciconfig or bluetooth ctl show
# have the pi host the connection

import socket
#global variables
pi_addr= '?' # we can get from hciconfig
port = 3 
backlog = 1
size = 1024

#set up bluetooth socket server
blue_pi = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
blue_pi.bind((pi_addr,port))
blue_pi.listen(backlog)
print("Blue_Pi listening at "+pi_addr+":"+port)

#handle socket communication
try:
    client, address = blue_pi.accept()
    print("Connected to "+client)
    while 1:
        data = client.recv(size)
        if data:
            print("Recieved "+data +" from "+client)
            client.send(data)
except:	
    print("Closing socket")	
    client.close()
    blue_pi.close()

