import sys
from os.path import exists

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
    path = "./music/playlists/95-100_bpm/Lynyrd Skynyrd - Sweet Home Alabama.wav"
    soundFilePath = exists(path)
    #print(soundFilePath)

    if soundFilePath:
        #Create the file to be read
        soundFile = QFile()
        soundFile.setFileName(path)
        soundFile.open(QIODevice.ReadOnly)

        #Create the settings to playback the audio
        format = QAudioFormat()
        format.setSampleRate(44100)
        format.setChannelCount(1)
        format.setSampleSize(32)
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
