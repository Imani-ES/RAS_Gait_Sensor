# for the pi, connect with any adress that pairs using hciconfig or bluetooth ctl show
# not sure how to allow any device to pair without initial IP address though

import socket

# get addresses
port = 3
desk_addr = '?'#need to find with hconfig i believe

#establish bluetooth socket 
blue_desk = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
blue_desk.connect((desk_addr,port))
blue_desk.send(bytes('greetings from app'),'UFT-8')
while 1:
    #input = data sent over socket
    text = input()

    if text == "greeting":
        print("Greeting from raspberry")

    elif text == "disconnect":
        break
    blue_desk.send(bytes(text, 'UTF-8'))

blue_desk.close()

def angle_converter(input):
    return 0
