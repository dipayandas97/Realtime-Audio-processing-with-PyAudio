import pyaudio
import numpy as np
import matplotlib.pyplot as plt
#import scipy.fftpack as fft

CHUNK = 2048
RATE = 44100 
FORMAT = pyaudio.paInt16
CHANNELS = 1

p=pyaudio.PyAudio()

stream=p.open(format=FORMAT,
              channels=CHANNELS,
              rate=RATE,
              input=True,
              frames_per_buffer=CHUNK)

fig, (ax1, ax2) = plt.subplots(2)

x1 = np.arange(0,CHUNK)
line, = ax1.plot(x1, np.random.rand(CHUNK),'-')
ax1.set_ylim(-32768,32767)

x_fft = np.linspace(0, RATE, CHUNK) # f = 0 to 44.1kHz, len = CHUNK samples
line_fft, = ax2.semilogx(x_fft, np.random.rand(CHUNK),'-')
ax2.set_xlim(20, RATE/2)
ax2.set_ylim(0,6000)


while True:
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    line.set_ydata(data)
    
    y_fft = (np.fft.fft(data)/CHUNK)
    line_fft.set_ydata(np.abs(y_fft))
    
    fig.show()
    fig.canvas.flush_events()


    

