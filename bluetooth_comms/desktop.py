# for the desktop app, might need two 
# not sure how to allow any device to pair without initial IP address though
#have the desktop connect to two different hosts (Won't need multiple threads, have two pis)
#

import socket

def lengthVsVoltage(x):
    return (x + 0.0729) / 0.0329

def normalLen(x):
    l0 = 8.26
    l90 = 10.88
    return ((x - l0) / (l90-l0) )*90

# get addresses
port = 4
pi_1_addr = 'B8:27:EB:03:EB:6D'#need to find with hconfig i believe
blue_pi_2 = '?'#need to find with hconfig i believe

#establish bluetooth sockets 
blue_pi_1 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
blue_pi_1.connect((pi_1_addr,port))
blue_pi_1.send(bytes('greetings from app','UTF-8'))

while 1:

    from_server = blue_pi_1.recv(4096)
    from_server_d = from_server.decode()


    estLen = lengthVsVoltage(float(from_server_d))
    print ('Voltage: ' + from_server_d + ' V | Estimated Length: ' + (str(estLen)) + ' | Estimated Angle: ' + (str(normalLen(estLen))))

blue_pi_1.close()

def angle_converter(input):
    return 0
