import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as ss

y = np.array([38,48,51,44,48,56,56,41,20,-3,-9,-1,6,5,6,17,24,38,56,57,52,52,48,37,39,51,51,40,37,34,27,25,23,21,25,37,43,45,53,
     57,60,71,73,67,58,51,40,40,53,72,88,89,88,92,88,81,92,117,124,119,123,140,144,140,147,150,154,152,140,131,122,122,
     133,148,162,169,171,162,146,135,139,154,162,154,145,150,164,166,156,140,134,150,168,156,123,107,112,107,103,103,109,
     128,136,130,115,96,86,100,124,131,100,64,56,76,105,128,118,93,66,48,44,48,53,53,48,33,33,41,56,70,72,69,69,86,96,80,
     67,67,69,60,53,52,53,54,54,54,61,70,68,68,71,72,69,70,77,76,66,60,71,68,48,19,19,50,67,58,49,39,34,42,67,80,70,59,55,
     38,24,37,59,70,54,26,16,11,19,33,41,41,34,27,25,34,32,5,-12,-1,29,41,27,9,4,7,8,-3,-11,-9,-2,-6,-22,-35,-34,-17,-7,-12,
     -12,2,10,4,5,10,18,16,12,24,26,21,20,20,25,28,25,21,10,-11,-37,-42,-34,-13,5,16,10,-2,-21,-34,-25,-4,4,-9,-29,-40,-35,
     -22,-14,-8,-2,0,-11,-22,-25,-38,-53,-54,-52,-52,-49,-38,-38,-41,-41,-37,-35,-36,-30,-29,-44,-52,-37,-17,-10,-23,-37,
     -35,-20,-6,2,4,7,19,22,21,21,9,-3,0,1,-4,-10,-11,-5,-2,2,10,18,18,11,17,21,7,-7,0,16,12,5,3,4,3,1,5,17,19,9,2,2,2,-2,
     -7,-17,-22,-27,-22,-13,-12,-13,-5,1,10,24,27,27,33,42,40,21,-1,-8,-4,1,-3,-21,-38,-43,-41,-35,-22,-8,-6,-6,4,18,34,56,
     71,70,67,69,69,60,48,38,39,44,38,18,6,20,42,54,81,98,84,53,37,43,49,22,43,80,97,102,114,120,113,98,85,89,107,114,108,
     102,86,83,100,117,121,116,102,76,64,67,67,65,68,82,96,100,90,84,96,108,109,99,81,59,45,38,23,6,-5,1,12,12,4,-17,-40,
     -51,-53,-62,-60,-53,-55,-73,-99,-119,-120,-99,-67,-55,-70,-71,-72,-68,-54,-50,-46,-37,-20,-3,0,-5,4,22,37,49,51,52,
     52,59,65,58,57,58,52,42,41,33,19,11,17,34,41,22,-1,-18,-36,-43,-35,-36,-61,-78,-76,-70,-66,-60,-62,-67,-60,-52,-52,
     -50,-33,-5,5,-2,-11,-13,-26,-43,-62,-87,-102,-93,-82,-87,-92,-84,-59,-43,-34,-29,-44,-54,-51,-54,-51,-40,-34,-33,-35,
     -35,-42,-51,-49,-35,-22,-21,-24,-18,-8,-4,-7,-12,-20,-35,-55,-71,-72,-65,-53,-42,-49,-54,-44,-24,-13,-35,-59,-70,-59,
     -42,-36,-17,-1,4,6,10,27,41,51,53,38,17,7,4,44,52,35,26,29,36,23,5,4,5,-1,-9,-8,3,13,17,18,25,48,70,69,57,58,59,54,
     55,57,54,44,42,64,82,91,90,75,53,38,50,59,53,52,59,60,57,61,69,75,88,112,132,144,148,149,151,147,137,131,133,139,139,
     129,115,105,72,55,57,67,68,57,45,40,40,38,33,37,44,52,68,74,69,54,38,40,52,58,58,45,44,65,86,92,104,116,119,114,103,
     103,117,137,134,104,72,54,58,73,88,83,57,44,56,85,103,102,90,82,85,91,86,76,60,43,53,70,66,56,65,85,88,86,80,60,49,
     33,23,37,61,81,80,66,59,64,64,56,52,51,48,33,11,0,-6,-7,-2,4,11,22,37,54,69,80,80,77,82,80,70,52,39,41,48,48,51,58,
     75,81,76,77,86,84,72,69,72,72,73,73,73,88,103,104,98,85,71,59,52,53,54,48,24,17,20,28,28,27,32,29,24,27,48,66,74,68,
     53,40,38,42,38,20,4,-1,3,4,1,3,7,13,27,37,35,26,22,23,23,26,35,42,52,57,49,35,36,38,40,48,51,40,36,51,71,86,96,92,
     86,86,97,90,89,80,72,92,117,124,123,133,144,136,130,119,117,119,112,92,77,68,64,66,66,64,65,68,74,67,60,74,88,83,67,
     59,68,64,41,19,5,8,13,7,2,1,8,11,12,17,19,21,19,12,9,4,4,8,16,24,35,25,20,38,61,72,75,69,52,38,40,52,65,76,82,66,40,
     20,16,19,21,16,-2,-17,-7,17,32,40,44,37,27,21,23,27,29,25,20,22,26,22,25,29,17,2,-6,-5,-2,-9,-11,-9,-4,4,17,29,33,28,
     28,35,40,58,82,96,92,92,103,118,136,146,145,134,117,105,91,72,66,69,76,77,67,50,32,13,10,17,20,32,43,38,32,32,38,41,
     49,58,64,55,49,52,60,67,60,65,74,75,72,73,88,89,75,65,65,70,70,58,43,41,56,75,87,72,50,42,52,60,69,71,60,51,45,52,64,
     75,84,83,81], dtype = int)

fig, ax = plt.subplots(2)
ax[0].plot(y)
#Wavelet Transform
w = 51
width = np.arange(1,w)

cwt_matrix = ss.cwt(y, ss.ricker, width)

plt.imshow(cwt_matrix, extent = [0,1024 ,1, w], cmap = 'hot', aspect = 'auto',
           vmax = abs(cwt_matrix).max(), vmin = -abs(cwt_matrix).max())

'''
#Fourier Transform
f = np.fft.fft(y) / len(y)
end = len(y)/3
f = f[:int(end)]

ax[1].plot(abs(f))
'''
plt.show()
