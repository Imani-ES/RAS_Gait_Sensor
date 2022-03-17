#pip3 install pydub
#pip3 install soundfile
#pip3 install pyrubberband
#pip3 install numpy
#pip3 install AudioSegment
#pip install playsound
#https://medium.com/prog-ramming-solutions/python-music-playback-speed-1x-2x-3x-change-without-chipmunk-effect-890eb10826c1
from playsound import playsound

from pydub import AudioSegment
import os

audio = AudioSegment.from_mp3("./playlists/100-105_bpm/Black Mountain - Stay Free.mp3")
audio.export("audio.wav",format="wav")
