import socket
from turtle import update
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
import sys
from tkinter import *


#Global variables
#Knee Calibration values
l0_1 = None
l90_1 = None
l0_2 = None
l90_2 = None
fullyCalibrate = False

#Pi connection variables
Pi_1_connected = False
Pi_2_connected = False
from_server_d1 = None
from_server_d2 = None

#Angle variables
normLen1 = 0
normLen2 = 0

#BPM and music variables
bpmObtained = False
timePeriod = -1
timer = 0
path = "music/playlists/90-100_bpm/Lynyrd Skynyrd - Sweet Home Alabama.wav"



#Set up graphing stuff, xs(2) and ys(2) should be able to export to csv if need be
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

#This is to make two subplots into one screen, with a common x and y axis
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

ax.set_xlabel('Time Period (sesconds)')
ax.set_ylabel('Knee Angle (degrees)')

ax1.set_title('Left Knee Angle')
ax2.set_title('Right Knee Angle')

#These variables store the data from the sensor, xs(2) stores the current times within the step period and ys(2) stores the associated knee angle
xs = []
ys = []
xstemp = []
ystemp = []

xs2 = []
ys2 = []
xs2temp = []
ys2temp = []


#Formula derived from own calculations, return the string length given voltage
def lengthVsVoltage(x):
    try:
        float(x)
        return (float(x) + 0.0729) / 0.0329
    #Return nothing if a number could not be obtained
    except (ValueError, TypeError) as e:
        return None
    

#Formula calculated from research paper to convert length to angle
def normalLen(x, l0, l90):
    try:
        res = ((x - l0) / (l90 - l0) )*90
        return res
    #If any sensors have 0 length, something is probably not right
    except ZeroDivisionError:
        print("Recalibrate, division by 0!")
 
#Establish the bluetooth sockets
blue_pi_1 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
blue_pi_2 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

#Hardcode the Pi bluetooth addresses, obtained from the Pis
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

#Function to test just one sensor if needed, pass in 1 for left knee, anything else for right knee
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
                #print("test")
            else:
                blue_pi_1.sendall("1".encode())
        except socket.error:
            #Attempt to reconnect to left knee sensor
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
            #Attempt to reconnect to right knee sensor
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
            #Convert the lengths to angles
            normLen1 = normalLen(estLen_1, l0_1, l90_1)
            normLen2 = normalLen(estLen_2, l0_2, l90_2)
           
            #print(normLen1)
            #print(normLen2)
            #print('--------------------')

def animate(i, xs, ys):
    #Obtain knee sensor reading if calibrated
    global fullyCalibrate, normLen1, normLen2, timer, timePeriod, ax1, ax2
    
    #If the timer exceeds the timeperiod, reset the timer
    if time.time() - timer > timePeriod:
        timer = time.time()
    
    if fullyCalibrate:
        angle = normLen1
        angle2 = normLen2

        #Add knee data over realtime
        xs.append(time.time() - timer)
        ys.append(angle)

        xs2.append(time.time() - timer)
        ys2.append(angle2)

        #Calculate the number of elements needed to plot, denominator is animation rate in seconds
        num_elem = round(timePeriod[0]/0.025)

        #Plot only elements in the current step (not really accurate)
        xstemp = xs[-num_elem:]
        ystemp = ys[-num_elem:]

        xs2temp = xs2[-num_elem:]
        ys2temp = ys2[-num_elem:]

        #Create the scatter dots
        ax1.clear()
        ax1.scatter(xstemp, ystemp)

        ax2.clear()
        ax2.scatter(xs2temp, ys2temp)

        #Set x and y axis limit
        ax1.set_ylim([0, 90])
        ax1.set_xlim([0, timePeriod])

        ax2.set_ylim([0, 90])
        ax2.set_xlim([0, timePeriod])

def runAnimation():
    global fig, ax1, ax2, xs, ys, xs2, ys2, bpmObtained, timePeriod, timer, path, fullyCalibrate

    #Check if the song's bpm was already obtained
    if not bpmObtained:
        #Check if song path exists
        soundFilePath = exists(path)
        #print(soundFilePath)
        if soundFilePath:
            #BPM Calculation, not the most accurate, sometimes may use double the bpm
            y, sr = librosa.load(path=path)
            onset_env = librosa.onset.onset_strength(y=y,sr=sr)
            tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
            print(tempo)

            bpmObtained = True

            #Multiply by two for full step
            timePeriod = 2*(60/tempo)
            print(timePeriod)

            #Call the function again to run the animation part
            runAnimation()
        else:
            #Exit program if song doesn't exist
            print("Song path does not exist!")
            sys.exit()
    else:
        #Debug variable to set calibrate to true
        #fullyCalibrate = True
        #Wait until sensors are calibrated
        while not fullyCalibrate:
            continue
        if fullyCalibrate:
            #Play song in another thread to prevent blocking, could prob use a different library
            thread2 = threading.Thread(target=playSong)
            thread2.daemon = True
            thread2.start()

            #Start another thread to display the knee angles
            thread3 = threading.Thread(target=displayAngles)
            thread3.daemon = True
            thread3.start()

            #Start the timer and the animation
            timer = time.time()
            ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=25)
            fig.tight_layout()
            plt.show()

#Function to play the hardcoded song
def playSong():
    global path
    playsound(path)

#Function to show the knee angles
def displayAngles():
    global normLen1, normLen2
    #Tkinter stuff to display text within a separate window from the graph
    window = Tk()

    #Set window GUI and size
    window.title('Knee Angles')
    window.geometry('600x300+100+100')

    #Left knee title and angle
    left = Label(window, text=round(normLen1), fg='Black', font=("Helvetica", 60))
    leftText = Label(window, text="Left Angle", fg='Black', font=("Helvetica", 16))
    left.place(x=120, y=150)
    leftText.place(x=120, y=50)

    #Right knee title and angle
    right = Label(window, text=round(normLen2), fg='Black', font=("Helvetica", 60))
    rightText = Label(window, text="Right Angle", fg='Black', font=("Helvetica", 16))
    right.place(x=380, y=150)
    rightText.place(x=380, y=50)

    #Update the window's text every 1 ms
    window.after(1, updateAngles, window, left, right)

    window.mainloop()

#Helper function to update the knee angles
def updateAngles(window, left, right):
    global normLen1, normLen2
    left.config(text=round(normLen1))
    right.config(text=round(normLen2))
    window.after(1, updateAngles, window, left, right)

#Create the thread to run the animation    
if __name__ == "__main__":
    thread1 = threading.Thread(target=main)
    thread1.daemon = True
    thread1.start()
    runAnimation()
