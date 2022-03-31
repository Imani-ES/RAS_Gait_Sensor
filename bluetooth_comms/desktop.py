import socket
import keyboard
import time

#Global variables
l0_1 = None
l90_1 = None
l0_2 = None
l90_2 = None
fullyCalibrate = False
Pi_1_connected = False
Pi_2_connected = False
blue_pi_1 = None
blue_pi_2 = None
from_server_d1 = None
from_server_d2 = None

#Formula derived from own calculations, obtain the length
def lengthVsVoltage(x):
    try:
        float(x)
        return (float(x) + 0.0729) / 0.0329
    except (ValueError, TypeError) as e:
        return None
    

#Formula calculated from research paper to convert length to angle
def normalLen(x, l0, l90):
    return ((x - l0) / (l90 - l0) )*90
 
#Establish the bluetooth sockets and timeout
blue_pi_1 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
blue_pi_2 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

#Hardcode the Pi bluetooth addresses
port = 4
pi_1_addr = 'B8:27:EB:03:EB:6D'
pi_2_addr = 'B8:27:EB:55:97:DE'

#Knee sensor calibration function
def calibrate():
    global l0_1, l0_2, l90_1, l90_2, fullyCalibrate, estLen_1

    #Check if sensor is already calibrated
    if not fullyCalibrate:
        #First Calibrate 0 degrees
        if not l0_1 or not l0_2: 
            l0_1 = lengthVsVoltage(from_server_d1)
            l0_2 = lengthVsVoltage(from_server_d2)
            print('Calibrated at 0 degrees')
        #Upon second space press calibrate 90 degrees
        else:
            l90_1 = lengthVsVoltage(from_server_d1)
            l90_2 = lengthVsVoltage(from_server_d2)
            print('Calibrated at 90 degrees')
            
            #Flag that sensor is calibrated
            fullyCalibrate = True
            print('Sensors are calibrated!')
    else:
        #Tell user sensor is calibrated
        print('Sensors are already calibrated!')

#Sets up 'interupt' to calibrate using space key
keyboard.add_hotkey('space', calibrate)

while 1:
    estLen_1 = 0
    estLen_2 = 0

    #Check connection to Pi 1
    try:
        if not Pi_1_connected:
            print("Trying to connect to Pi 1")
            blue_pi_1.connect((pi_1_addr, port))
        else:
            blue_pi_1.sendall("1".encode())
    except socket.error:
        print("Lost connection to Pi 1, reconnect!")
        Pi_1_connected = False
        blue_pi_1.close()
        blue_pi_1 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        time.sleep(5)
        continue
    else:
        print("Pi 1 connected!")
        Pi_1_connected = True

        #Receive data from pi 1, decode the data
        print("Trying to read from Pi 1...")
        from_server_1 = blue_pi_1.recv(4096)
        from_server_d1 = from_server_1.decode()   

        print("Data received!")

        #Convert the voltage to length
        estLen_1 = lengthVsVoltage(from_server_d1)

   #Check connection to Pi 2
    try:
        if not Pi_2_connected:
            print("Trying to connect to Pi 2")
            blue_pi_2.connect((pi_2_addr, port))
        else:
            blue_pi_2.sendall("2".encode())
    except socket.error:
        print("Lost connection to Pi 2, reconnect!")
        Pi_2_connected = False
        blue_pi_2.close()
        blue_pi_2 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        time.sleep(5)
        continue
    else:
        print("Pi 2 connected!")
        Pi_2_connected = True

        #Receive data from pi 2, decode the data
        print("Trying to read from Pi 2...")
        from_server_2 = blue_pi_2.recv(4096)
        from_server_d2 = from_server_2.decode()   

        print("Data received! from 2")

        #Convert the voltage to length
        estLen_2 = lengthVsVoltage(from_server_d2)

    
    #estLen_2 = lengthVsVoltage(float(from_server_d2))    

    #Check if both sensors are calibrated
    if not fullyCalibrate:
        print('Calibrate the sensors !')
    else:
        print('--------------------')
        print(normalLen(estLen_1, l0_1, l90_1))
        print(normalLen(estLen_2, l0_2, l90_2))
        print('--------------------')

def angle_converter(input):
    return 0
