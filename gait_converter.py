import threading
import time

last_right, last_left = 0
right_motion,leftmotion = 0
l_gait_track, r_gait_track = 0

def update_motion(angle, leg):
  global last_right, last_left, right_motion, leftmotion 
  
  if leg == "right":#check if right leg is changing direction
    if angle > last_right: 
      if right_motion != 1:#update gate when knee changes movement
        find_gait()
      right_motion = 1
    elif angle < last_right:
      if right_motion != -1:#update gate when knee changes movement
        find_gait()
      right_motion = -1
    else:
      right_motion = 0
    last_right = angle
    
  if leg == "left":#check if left leg is changing direction  
    if angle > last_left: 
      if left_motion != 1:#update gate when knee changes movement
        find_gait()
      left_motion = 1
    elif angle < last_left:
      if left_motion != -1:#update gate when knee changes movement
        find_gait()
      left_motion = -1
    else:
      lfet_motion = 0
    last_left = angle  
    
def find_gait():
  global l_gait_track, r_gait_track
  #find delta time by subtracting gait_track from current time 
  #send gait to front end
  #update gait track

