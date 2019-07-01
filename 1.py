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

while True:
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    line.set_ydata(data)
    try:
        fig.show()
        fig.canvas.flush_events()
    except Exception as e: # PRINTS if any error occurs during matplot functioning
        print(e)

    

