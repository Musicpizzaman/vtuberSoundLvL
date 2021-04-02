###Install pyaudio : py -m pip install C:\Users\user\Downloads\PyAudio-0.2.11-cp39-cp39-win_amd64.whl
###https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
###https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14

### ANIMATION POSITIONS NEEDED 
'''
Small mouth open 
Large mouth open
Idle animation
Randon Animation
'''
from sys import byteorder
from array import array
from struct import pack

import wave
import pyaudio
import subprocess


## Adjust these values based on your set up and mic 
## Threshold is to eliminate white noise 
## the other two are the thresholds for the different animation triggers 
SILENT = (array('h', [0, 0, 0, 1, 0, 0, 1, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, -1, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, -1, 0, 1, 0, 0, 1, 0, 0, -1, 0, -1, 0, 0, 0, -1, 0, 1, -1, 0, 0, 0, 0, -1, 0, 1, 0, -1, 1, 1, 0, 1, -1, 0, 0, 1, 0, 0, -1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1, -1, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, 1, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, -1, 1, 0, -1, -1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, -1, 0, -1, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, -1, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, -1, 1, 0, -1, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 1, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 1, 0, -1, 0, 0, -1, -1, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 1, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 1, 1, 0, 0, 0, 0, -1, 0, 1, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1, -1, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 1, 1, -1, 0, 0, -1, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 1, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 1, 1]))
THRESHOLD = 100
SMALLTALK = 10000
BIGSPEAK = 50000
#################################

CHUNK = 1024
WIDTH = 2
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("* recording")

def is_silent(data):
    "Returns 'True' if below the 'silent' threshold"
    print("IDLE")
    return max(data) < THRESHOLD

def is_audio(data):
    "Returns 'True' if below the 'silent' threshold"
    print("Moving")
    return max(data) > THRESHOLD


def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

def bytes_to_int(data):
    result = 0
    for b in data:
        result = result * 256 + int(b) 
    return result

while (process_exists('TwitchStudio.exe') == True):
    ##data = stream.read(CHUNK)
    data = array('h', stream.read(CHUNK))
    if byteorder == 'big':
            data.byteswap()
    ##print(data)

    if (data) == SILENT:        
        print("silent")
    ##elif max(data) < THRESHOLD:
    ##    print("Moving")   

    ##stream.write(data, CHUNK) 

print("* done")

print(process_exists('TwitchStudio.exe'))
stream.stop_stream()
stream.close()
