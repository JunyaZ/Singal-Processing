'''
https://www.swharden.com/wp/2016-07-19-realtime-audio-visualization-in-python/#comments
'''
import pyaudio
import numpy as np
import wave

CHUNK = 4096  #Number of samples to read at a time
RATE = 44100  #Sampling rate
RECORD_SECONDS = 5  #Number of seconds to record sound

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
                frames_per_buffer=CHUNK) #uses default input device
nchunks = int(RECORD_SECONDS * RATE / CHUNK)
frames = []  #Holds samples
#Create a numpy array holding a single read of audio data
print("Recording...")
for i in range(nchunks):  #Record one chunk at a time
    #data = np.fromstring(stream.read(CHUNK), dtype = np.int16)
    data = stream.read(CHUNK)
    frames.append(data)
    #print(data)
print("Done recording")
#Close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()

#Now save the audio in a file
wf = wave.open("audio.wav", "wb")
wf.setnchannels(1)  #This must match the number of channels used above
wf.setsampwidth(2)  #Must match the format used above
wf.setframerate(RATE)          #Sample (or frame) rate
wf.writeframes(b''.join(frames))
wf.close()
