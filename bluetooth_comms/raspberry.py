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
    print("Connected to "+ str(client))
    while 1:
        data = client.recv(size)
        if data:
            print("Recieved "+ str(data) +" from "+ str(client))
            client.send(data)
except:	
    print("Closing socket")	
    client.close()
    blue_pi.close()

'''
This code is outdated, but it was supposed to be the code within the Pis. The more current code
is on the two Pis, and should be located in ~/CSE 450/blue_pi.py, or something similar.

Below is the code just in case:

import socket
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#pi_addr is the bluetooth address of the Pi, can be found from hciconfig
pi_addr = ''
port = 4
backlog = 1
size = 1024

blue_pi = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
blue_pi.bind((pi_addr,port))
blue_pi.listen(backlog)

#Set up I2C
i2c = busio.I2C(board.SCL, board.SDA)

#Set up the ADC, the ADC's data_rate can be adjusted, there is documentation somewhere on it, we thought 8 would be enough
ads = ADS.ADS1115(i2c)
ads.data_rate = 8

chan = AnalogIn(ads, ADS.P0, ADS.P1)

#Variable to keep track if the desktop app is connected
clientConnected = False

while True:
    try:
        if not clientConnected:
            print("Trying to find desktop")
            conn, addr = blue_pi.accept()
        else:
            checker = conn.recv(4096)
            if not checker:
                #Client lost connection
                raise socket.error
    except socket.error:
        print("Couldn't find desktop!")
        clientConnected = False
        continue
    except KeyboardInterrupt:
        print("Force closing server!")
        blue_pi.shutdown(socket.SHUT_RDWR)
        blue_pi.close()
        exit()
    else:
        #Send over the sensor data
        clientConnected = True
        conn.send((str(chan.voltage)).encode())


'''

