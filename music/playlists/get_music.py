#pip3 install pytube
#pip install os_sys
#https://jog.fm/workout-songs/at/100/bpm.100?order=desc&sort=popularity
from pytube import YouTube
import os
  
# url input from user
yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))
  
# extract only audio
video = yt.streams.filter(only_audio=True).first()

# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

# download the file
out_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
  
# result of success
print(yt.title + " has been successfully downloaded.")

print("Converting to wav")
from os import path
from pydub import AudioSegment

# files                                                                         
src = destination+"/"+yt.title+".mp3"
dst = destination+"/"+yt.title+".mp3"+"/"+"test.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
print("Successfully converted from mp3 to wav")