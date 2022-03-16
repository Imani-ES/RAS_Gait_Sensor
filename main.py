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
    path = "./music/playlists/95-100_bpm/Lynyrd Skynyrd - Sweet Home Alabama.wav"
    soundFilePath = exists(path)
    #print(soundFilePath)

    if soundFilePath:
        soundFile = QFile()
        soundFile.setFileName(path)
        soundFile.open(QIODevice.OpenModeFlag.ReadOnly)

        format = QAudioFormat()
        format.setSampleRate(8000)
        format.setChannelCount(1)
        format.setSampleSize(8)
        format.setCodec("audio/pcm")
        format.setByteOrder(QAudioFormat.Endian.LittleEndian)
        format.setSampleType(QAudioFormat.SampleType.UnSignedInt)

        info = QAudioDeviceInfo(QAudioDeviceInfo.defaultOutputDevice())
        if not info.isFormatSupported(format):
            print("Raw audio format not supported, cannot play.")

        output = QAudioOutput(format)
        output.start(soundFile)
        

    sys.exit(app.exec())

if __name__ == "__main__":
    startApp()
