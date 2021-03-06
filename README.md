# RAS_Gait_Sensor

People who suffer from diseases that affect their walking, like Parkinson’s disease, require rehabilitation to help them regain their ability to walk safely. Systems that use Rhythmic Auditory Stimulation (RAS) have been shown to help patients more quickly regain their walking ability, compared to traditional rehabilitation methods. We will develop a knee sensor to obtain useful data about the patient’s walking patterns. This data and sensor will be used in conjunction with a RAS desktop application.

## Use Cases
Rehabilitation for people with Parkinson’s gait disease, other neurodegenerative diseases which negatively affect their walking ability, stroke victims, etc. 
Possible general use for athletes, at-home diagnostics, personal use, etc.

## Features
A wearable knee sensor that can accurately measure a user’s knee angle within ± 5°
The sensor is wireless and transmits data without physical connections
The battery powered sensor is adjustable, ensuring a wide range of users can wear it comfortably
Users can hear music that is equivalent to the BPM they want to walk to

This code contains the components of the accompanying Music App that will be used with the Knee Sensor

## Getting Started

### Bluetooth Communication
- Power the Raspberry Pi, the bluetooth communcation script should run on start up
- Navigate to /bluetooth_comms/
- Run the desktop portion of the bluetooth communication with the command ``` python ./desktop.py ```
- Press the space bar to calibrate the sensor at 0&deg; knee angle
- Press the space bar again to calibrate at 90&deg; knee angle
- You should now see the sensor data being recieved in your console

## Collaborators:
Imani Muhammad-Graham, Kexin Chen, Seongjae Shin, Andrew Talamo

## Resources
https://github.com/pyqt/examples
https://blog.kevindoran.co/bluetooth-programming-with-python-3/
https://codezup.com/socket-server-with-multiple-clients-model-multithreading-python/
