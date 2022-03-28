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

#Formula derived from own calculations, obtain the length
def lengthVsVoltage(x):
    return (x + 0.0729) / 0.0329

#Formula calculated from research paper to convert length to angle
def normalLen(x):
    return ((x - l0) / (l90-l0) )*90

#Hardcode the Pi bluetooth addresses
port = 4
pi_1_addr = 'B8:27:EB:03:EB:6D'
pi_2_addr = 'B8:27:EB:55:97:DE'

#Establish the bluetooth sockets and timeout
blue_pi_1 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    
blue_pi_2 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

#Knee sensor calibration function
def calibrate():
    global l0_1, l0_2, l90_1, l90_2, fullyCalibrate
    #Check if sensor is already calibrated
    if not fullyCalibrate:
        #First Calibrate 0 degrees
        if not l0_1 or l0_2:
            l0_1 = lengthVsVoltage(float(blue_pi_1.recv(4096).decode()))
            l0_2 = lengthVsVoltage(float(blue_pi_2.recv(4096).decode()))
            print('Calibrated at 0 degrees')
        #Upon second space press calibrate 90 degrees
        else:
            l90_1 = lengthVsVoltage(float(blue_pi_1.recv(4096).decode()))
            l90_2 = lengthVsVoltage(float(blue_pi_2.recv(4096).decode()))
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
    #Check connection to Pi 2
    try:
        print("Trying to connect to Pi 2")
        blue_pi_2.connect((pi_2_addr, port))
    except:
        print("Lost connection to Pi 2, reconnect!")
        fullyCalibrate = False
        time.sleep(5)
        continue
    else:
        print("Pi 2 is connected!")

    #Check connection to Pi 1
    try:
        print("Trying to connect to Pi 1")
        blue_pi_1.connect((pi_1_addr, port))
    except:
        print("Lost connection to Pi 1, reconnect!")
        fullyCalibrate = False
        time.sleep(10)
        continue
    else:
        print("Pi 1 connected!")    

    #Receive data from pis, decode the data
    from_server_1 = blue_pi_1.recv(4096)
    from_server_d1 = from_server_1.decode()

    from_server_2 = blue_pi_2.recv(4096)
    from_server_d2 = from_server_2.decode()

    #Convert the voltage to length
    estLen_1 = lengthVsVoltage(float(from_server_d1))
    estLen_2 = lengthVsVoltage(float(from_server_d2))    

    #Check if both sensors are calibrated
    if not fullyCalibrate:
        print('temp')
    else:
        print(normalLen(estLen_1))
        print(normalLen(estLen_2))

     
blue_pi_1.close()

def angle_converter(input):
    return 0
