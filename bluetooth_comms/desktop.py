import socket
import keyboard
import time
from functools import partial
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import time
import librosa
from os.path import exists
from playsound import playsound

#Global variables
l0_1 = None
l90_1 = None
l0_2 = None
l90_2 = None
fullyCalibrate = False
Pi_1_connected = False
Pi_2_connected = False
from_server_d1 = None
from_server_d2 = None
normLen1 = 0
normLen2 = 0
bpmObtained = False
timePeriod = -1
timer = 0
path = "../music/playlists/90-100_bpm/Lynyrd Skynyrd - Sweet Home Alabama.wav"


#Set up graphing stuff
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xs = []
ys = []
xstemp = []
ystemp = []

fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)
xs2 = []
ys2 = []
xs2temp = []
ys2temp = []


#Formula derived from own calculations, obtain the length
def lengthVsVoltage(x):
    try:
        float(x)
        return (float(x) + 0.0729) / 0.0329
    except (ValueError, TypeError) as e:
        return None
    

#Formula calculated from research paper to convert length to angle
def normalLen(x, l0, l90):
    try:
        res = ((x - l0) / (l90 - l0) )*90
        return res
    except ZeroDivisionError:
        print("Recalibrate, division by 0!")
 
#Establish the bluetooth sockets and timeout
blue_pi_1 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
blue_pi_2 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

#Hardcode the Pi bluetooth addresses
port = 4
pi_1_addr = 'B8:27:EB:03:EB:6D'
pi_2_addr = 'B8:27:EB:55:97:DE'

#Knee sensor calibration function
def calibrate():
    global l0_1, l0_2, l90_1, l90_2, fullyCalibrate

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

#Function to test just one sensor
def testCalibrate(num_sensor):
    global l0_1, l0_2, l90_1, l90_2, fullyCalibrate

    #Check if sensor is already calibrated
    if not fullyCalibrate:
        #First Calibrate 0 degrees
        if num_sensor == 1:
            if not l0_1:
                l0_1 = lengthVsVoltage(from_server_d1)
                print('Calibrated at 0 degrees')
            else:  
                l90_1 = lengthVsVoltage(from_server_d1)
                fullyCalibrate = True
        else:
            if not l0_2:  
                l0_2 = lengthVsVoltage(from_server_d2)
                print('Calibrated at 0 degrees')
            else:
                l90_2 = lengthVsVoltage(from_server_d2)
                fullyCalibrate = True
    else:
        #Tell user sensor is calibrated
        print('Sensors are already calibrated!')

#Function to set calibrated to false and reset sensors values
def recalibrate():
    global l0_1, l0_2, l90_1, l90_2, fullyCalibrate
    fullyCalibrate = False
    l0_1 = None
    l0_2 = None
    l90_1 = None
    l90_2 = None

#Sets up 'interupt' to calibrate using space key
keyboard.add_hotkey('space', calibrate)

#Alternative calibrate for single sensor
#keyboard.add_hotkey('space', partial(testCalibrate, 2))

#Set up 'interrupt' to recalibrate
keyboard.add_hotkey('r', recalibrate)


def main():
    global Pi_1_connected, Pi_2_connected, from_server_d1, from_server_d2, fullyCalibrate, normLen1, normLen2, blue_pi_1, blue_pi_2
    
    while 1:
        #Check connection to Pi 1
        try:
            if not Pi_1_connected:
                print("Trying to connect to Pi 1")
                blue_pi_1.connect((pi_1_addr, port))
                print("test")
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
            #print("Pi 1 connected!")
            Pi_1_connected = True

            #Receive data from pi 1, decode the data
            #print("Trying to read from Pi 1...")
            from_server_1 = blue_pi_1.recv(4096)
            from_server_d1 = from_server_1.decode()

            #print("Data received!")
            #Did you want to have a message processing thread so the listener doesnt stall?
            #Convert the voltage to length
            estLen_1 = lengthVsVoltage(from_server_d1)

            #call update motion from gait_converter file

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
            #print("Pi 2 connected!")
            Pi_2_connected = True

            #Receive data from pi 2, decode the data
            #print("Trying to read from Pi 2...")
            from_server_2 = blue_pi_2.recv(4096)
            from_server_d2 = from_server_2.decode()   

            #print("Data received! from 2")

            #Convert the voltage to length
            estLen_2 = lengthVsVoltage(from_server_d2)

        #Check if both sensors are calibrated
        if not fullyCalibrate:
            print('Calibrate the sensors !')
        else:
            #print('--------------------')
            normLen1 = normalLen(estLen_1, l0_1, l90_1)
            normLen2 = normalLen(estLen_2, l0_2, l90_2)
           
            print(normLen1)
            print(normLen2)
            #print('--------------------')

def animate(i, xs, ys):
    #Obtain knee sensor reading if calibrated
    global fullyCalibrate, normLen1, timer, timePeriod
    
    #If the timer exceeds the timeperiod, reset the timer
    if time.time() - timer > timePeriod:
        timer = time.time()
    
    if fullyCalibrate:
        angle = normLen1

        #Add knee data over realtime
        xs.append(time.time() - timer)
        ys.append(angle)

        #Calculate the number of elements needed to plot, denominator is animation rate
        num_elem = round(timePeriod[0]/0.025)

        #Plot only elements in the current step
        xstemp = xs[-num_elem:]
        ystemp = ys[-num_elem:]

        #Draw x and y lists
        ax.clear()
        ax.scatter(xstemp, ystemp)

        #Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.3)
        plt.title('Knee Angle Over Time')
        plt.ylabel('Knee Angle (degrees)')
        plt.ylim([0,80])
        plt.xlim([0, timePeriod])

def animate2(i, xs, ys):
    #Obtain knee sensor reading if calibrated
    global fullyCalibrate, normLen1, timer, timePeriod
    
    #If the timer exceeds the timeperiod, reset the timer
    if time.time() - timer > timePeriod:
        timer = time.time()
    
    if fullyCalibrate:
        angle = normLen1

        #Add knee data over realtime
        xs.append(time.time() - timer)
        ys.append(angle)

        #Calculate the number of elements needed to plot, denominator is animation rate
        num_elem = round(timePeriod[0]/0.025)

        #Plot only elements in the current step
        xstemp = xs[-num_elem:]
        ystemp = ys[-num_elem:]

        #Draw x and y lists
        ax.clear()
        ax.scatter(xstemp, ystemp)

        #Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.3)
        plt.title('Knee Angle Over Time')
        plt.ylabel('Knee Angle (degrees)')
        plt.ylim([0,80])
        plt.xlim([0, timePeriod])

def runAnimation():
    global fig, ax, xs, ys, bpmObtained, timePeriod, timer, path

    #set up music
    '''
    Temporary...
    path is the filepath to the song
    soundFilePath just checks if the path exists
    '''
    if not bpmObtained:
        soundFilePath = exists(path)
        print(soundFilePath)
        if soundFilePath:
            y, sr = librosa.load(path=path)
            onset_env = librosa.onset.onset_strength(y=y,sr=sr)
            tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
            print(tempo)

            bpmObtained = True

            #Multiply by two for full step
            timePeriod = 2*(60/tempo)
            print(timePeriod)
            runAnimation()
        else:
            print("File not found!")
    else:
        while not fullyCalibrate:
            continue
        if fullyCalibrate:
            #Play song in another thread to prevent blocking
            thread2 = threading.Thread(target=playSong)
            thread2.daemon = True
            thread2.start()

            timer = time.time()
            ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=25)
            plt.show()

def playSong():
    global path
    playsound(path)

if __name__ == "__main__":
    thread1 = threading.Thread(target=main)
    thread1.daemon = True
    thread1.start()
    runAnimation()