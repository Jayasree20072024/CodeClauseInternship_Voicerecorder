####################################################
#Open cmd
#Install Required Module
#py -m pip install wavio
#py -m pip install scipy
#py -m pip install sounddevice --user

#Save the below code using Notepad with filename.py
#cd path
#py filename.py
######################################################

# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
 
# Sampling frequency
freq = 44100
 
# Recording duration
duration = 5
 
# Start recorder with the given values 
# of duration and sample frequency
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)
 
# Record audio for the given number of seconds
sd.wait()
 
# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)
 
# Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)