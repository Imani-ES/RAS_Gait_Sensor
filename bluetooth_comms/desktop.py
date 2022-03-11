# for the desktop app, might need two 
# not sure how to allow any device to pair without initial IP address though
#have the desktop connect to two different hosts (Won't need multiple threads, have two pis)
#

import socket
import keyboard

#Global variables for calibration
l0 = None
l90 = None
fullyCalibrate = False

def lengthVsVoltage(x):
    return (x + 0.0729) / 0.0329

def normalLen(x):
    return ((x - l0) / (l90-l0) )*90

# get addresses
port = 4
pi_1_addr = 'B8:27:EB:03:EB:6D'#need to find with hconfig i believe
blue_pi_2 = '?'#need to find with hconfig i believe

#establish bluetooth sockets 
blue_pi_1 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
blue_pi_1.connect((pi_1_addr,port))
blue_pi_1.send(bytes('greetings from app','UTF-8'))

def calibrate():
    global l0, l90, fullyCalibrate
    #Check if sensor is already calibrated
    if not fullyCalibrate:
        #First Calibrate 0 degrees
        if not l0:
            l0 = lengthVsVoltage(float(blue_pi_1.recv(4096).decode()))
            print('Calibrated at 0 degrees: ', l0)
        #Upon second space press calibrate 90 degrees
        else:
            l90 = lengthVsVoltage(float(blue_pi_1.recv(4096).decode()))
            print('Calibrated at 90 degrees: ', l90)
            
            #Flag that sensor is calibrated
            fullyCalibrate = True
            print('Sensor is calibrated!')
    else:
        #Tell user sensor is calibrated
        print('Sensor is already calibrated!')


keyboard.add_hotkey('space', calibrate)

while 1:

    from_server = blue_pi_1.recv(4096)
    from_server_d = from_server.decode()

    estLen = lengthVsVoltage(float(from_server_d))

    #Check if user pressed enter
    

    if not fullyCalibrate:
        print ('Voltage: ' + from_server_d + ' V | Estimated Length: ' + (str(estLen))) 
        print ('Calibrated l0, l90: (', l0, ', ', l90, ')')
        print ('----------------------------------------')
    # + ' | Estimated Angle: ' + (str(normalLen(estLen))))
    else:
        print(normalLen(estLen))

     
blue_pi_1.close()

def angle_converter(input):
    return 0
