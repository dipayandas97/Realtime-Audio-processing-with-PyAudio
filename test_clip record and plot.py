import pyaudio
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 4096 
RATE = 44100 
FORMAT = pyaudio.paInt16
CHANNELS = 1

p=pyaudio.PyAudio()

stream=p.open(format=FORMAT,
              channels=CHANNELS,
              rate=RATE,
              input=True,
              frames_per_buffer=CHUNK)

fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(CHUNK))
ax.set_ylim(-32768,32767)

clip = np.zeros((1,1), dtype = np.int16)

while True:
    try:
        data = stream.read(CHUNK)
        data_int = np.fromstring(data,dtype=np.int16)
        clip = np.concatenate((clip, data_int), axis = None)

        line.set_ydata(data_int)
        fig.show()
        fig.canvas.flush_events()
    except Exception:
        print(len(clip))
        break
    
stream.stop_stream()
stream.close()
p.terminate()

ft = np.fft.fft(clip) #fourier transform of recorded clip

fig2,ax2 = plt.subplots(2)
ax2[0].set_title('Time Domain')
ax2[0].plot(clip)

ax2[1].set_title('Frequency Domain')
#ax2[1].set_xlim(0,RATE/2)
ax2[1].semilogx(abs(ft)/RATE)

plt.show()
 


    

