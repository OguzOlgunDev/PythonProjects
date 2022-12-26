import numpy as np
import wave
import pyaudio
from numpy.fft import fft, ifft


filename = 'file_example.wav'

p = pyaudio.PyAudio()



# Open the sound file
wf = wave.open(filename, 'rb')
# It is a stereo audio file
wf_channels = wf.getnchannels()
# 2 bytes for each sample
wf_sampwidth = wf.getsampwidth()
# Total frame number is 1306624
wf_totalframe = wf.getnframes()
# framerate number is 44100
wf_samplerate = wf.getframerate()


print(wf_channels,wf_sampwidth ,wf_samplerate,wf_totalframe)

# the duration of the audio file
audio_time = wf_totalframe/wf_samplerate

frames = wf.readframes(-1)
wf.close()


# It takes all the data a numpy array
frame_array = np.frombuffer(frames, dtype=np.int16)

# Crated a new array which consist of multiplied 2 coefficient
new_array = frame_array*2

# odd_frame_array is every odd sample in the audio
odd_frame = np.where(frame_array%2)
odd_frame_array = frame_array[odd_frame]


# I was trying to apply FFT
X = fft(frame_array)
N = len(X)
n = np.arange(N)
T = N/wf_samplerate
freq = n/T

Y = ifft(X)

# This part was my driver code to save files
filenew = wave.open("40.1k playback with IFFT array.wav ","wb")
filenew.setnchannels(wf_channels)
filenew.setsampwidth(wf_sampwidth)
filenew.setframerate(40100)
filenew.writeframes(Y)


filenew.close()






