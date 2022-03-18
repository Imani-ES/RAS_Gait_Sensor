import sys
from os.path import exists
import wave

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtMultimedia import QAudioOutput, QAudio, QAudioFormat, QAudioDeviceInfo
from PyQt5.QtCore import QFile, QIODevice


def startApp():
    app = QGuiApplication(sys.argv)

    #set up blue tooth  - threadsfor each raspberry?

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
        soundFile.setFileName(path)
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

if __name__ == "__main__":
    startApp()
