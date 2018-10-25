'''
https://www.swharden.com/wp/2016-07-19-realtime-audio-visualization-in-python/#comments
'''
import pyaudio
import numpy as np

CHUNK = 2**11  #Number of samples to read at a time
RATE = 44100  #Sampling rate

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
                frames_per_buffer=CHUNK) #uses default input device

for i in range(int(10*44100/1024)):  #Go for a few seconds
    data = np.fromstring(stream.read(CHUNK), dtype = np.int16)
    peak=np.average(np.abs(data))*2
    bars="#"*int(50*peak/2**16)
    print("%04d %05d %s"%(i,peak,bars))

#Close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()
