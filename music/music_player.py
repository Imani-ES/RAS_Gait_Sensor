import sys
from os.path import exists
import wave
import os
import random
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtMultimedia import QAudioOutput, QAudio, QAudioFormat, QAudioDeviceInfo
from PyQt5.QtCore import QFile, QIODevice

def play_song(song_path):

    if(exists(song_path)):

        with wave.open(song_path, "rb") as wav_file:
            #Create the file to be read
            soundFile = QFile()
            soundFile.setFileName(song_path)
            soundFile.open(QIODevice.ReadOnly)

            #Create the settings to playback the audio
            format = QAudioFormat()
            format.setSampleRate(wav_file.getframerate())
            format.setChannelCount(wav_file.getnchannels())
            format.setSampleSize(wav_file.getsampwidth()*8)
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
    return 0
    #loop song