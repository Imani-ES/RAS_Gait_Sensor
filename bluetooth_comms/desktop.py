# for the desktop app, might need two 
# not sure how to allow any device to pair without initial IP address though
#have the desktop connect to two different hosts (Won't need multiple threads, have two pis)
#

import socket

# get addresses
port = 3
pi_1_addr = '?'#need to find with hconfig i believe
blue_pi_2 = '?'#need to find with hconfig i believe

#establish bluetooth sockets 
blue_pi_1 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
blue_pi_1.connect((pi_1_addr,port))
blue_pi_1.send(bytes('greetings from app'),'UFT-8')
while 1:
    #input = data sent over socket
    text = input()

    if text == "greeting":
        print("Greeting from raspberry")

    elif text == "disconnect":
        break
    blue_pi_1.send(bytes(text, 'UTF-8'))

blue_pi_1.close()

def angle_converter(input):
    return 0
