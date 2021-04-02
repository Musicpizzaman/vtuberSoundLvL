###py -m pip install sounddevice

### ANIMATION POSITIONS NEEDED 
'''
Small mouth open 
Large mouth open
Idle animation
Randon Animation
'''

import subprocess
import sounddevice
import numpy
import pymkv

IDLE = 25
SMALLTALK = 25
BIGSPEAK = 50

soundlvl = 0

def print_sound(indata, outdata, frames, time, status):
    volume_norm = numpy.linalg.norm(indata)*10
    print(int(volume_norm))
    soundlvl = int(volume_norm)

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

def device_sound():
    stream = sounddevice.Stream(callback=print_sound)
    with stream:
        print(soundlvl)


print(process_exists('TwitchStudio.exe'))

while (process_exists('TwitchStudio.exe') == True):
    device_sound()
'''
    stream = sounddevice.Stream(callback=print_sound)
    with stream:
        print("pinecone")
        ## I want to be able to 
        ## I need to figure out to place the video clips here to play 
'''    
