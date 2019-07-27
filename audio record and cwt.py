import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

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

#close the matplot window to break the loop

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


#CWT
fig3 = plt.subplots()
w_max = 151
width = np.arange(1,w_max)
cwt_matrix = signal.cwt(clip, signal.ricker, width)

plt.imshow(cwt_matrix, extent = [0,len(clip)/CHUNK,1,w_max], cmap = 'hot', aspect = 'auto',
           vmax = abs(cwt_matrix).max(), vmin = -abs(cwt_matrix).max())

plt.show()
 


    

