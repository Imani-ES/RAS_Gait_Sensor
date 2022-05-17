import sys
import os
from os.path import exists
import wave

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.QtMultimedia import QAudioOutput, QAudioFormat, QAudioDeviceInfo
from PyQt5.QtCore import QFile, QIODevice, QObject, pyqtProperty

def startApp():
    app = QGuiApplication(sys.argv)

    qmlRegisterType(Calibration, 'Signal', 1, 0, 'Calibration')

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('./main.qml')

    #set up music
    '''
    Temporary...
    path is the filepath to the song
    soundFilePath just checks if the path exists
    '''
    path = "./music/playlists/105-110_bpm/Pirates of the Caribbean Theme.wav"
    soundFilePath = exists(path)
    #print(soundFilePath)

    if soundFilePath:
        #Create the file to be read
        soundFile = QFile()
        soundFile.setFilecmdline(path)
        soundFile.open(QIODevice.ReadOnly)

        #Obtain the sample rate, sample width, and channel count
        sampleRate = 0
        sampleWidth = 0
        channelCount = 0
        with wave.open(path, "rb") as wav_file:
            sampleRate = wav_file.getframerate()
            sampleWidth = wav_file.getsampwidth()*8
            channelCount = wav_file.getnchannels()

        '''
        Song debug commands
        print("Sample Rate: ", sampleRate)
        print("Sample Size: ", sampleWidth)
        print("Channel Count: ", channelCount)
        '''

        #Create the settings to playback the audio
        format = QAudioFormat()
        format.setSampleRate(sampleRate)
        format.setChannelCount(channelCount)
        format.setSampleSize(sampleWidth)
        format.setCodec("audio/pcm")
        format.setByteOrder(QAudioFormat.LittleEndian)
        format.setSampleType(QAudioFormat.UnSignedInt)

        #Not sure, I think this checks if there is a default output device
        info = QAudioDeviceInfo(QAudioDeviceInfo.defaultOutputDevice())
        if not info.isFormatSupported(format):
            print("Raw audio format not supported, cannot play.")

        #Output the audio and play it
        output = QAudioOutput(format)
        output.start(soundFile)


    sys.exit(app.exec())

class Calibration(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialise the value of the properties.
        self._cmdline = ''

    # Define the setter of the 'name' property.
    @pyqtProperty('QString')
    def cmdline(cmdline):
        os.system("python ./bluetooth_comms/desktop.py")

if __name__ == "__main__":
    startApp()
