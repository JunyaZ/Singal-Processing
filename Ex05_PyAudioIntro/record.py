'''
https://www.swharden.com/wp/2016-07-19-realtime-audio-visualization-in-python/#comments
'''
import pyaudio
import numpy as np

CHUNK = 4096  #Number of samples to read at a time
RATE = 44100  #Sampling rate

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
                frames_per_buffer=CHUNK) #uses default input device

#Create a numpy array holding a single read of audio data
for i in range(10):  #Do it 10 times to check things out
    data = np.fromstring(stream.read(CHUNK), dtype = np.int16)
    print(data)
#Close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()
