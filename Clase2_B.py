import my_utils as mutls
mutls.clc()
mutls.clearAll()

import my_utils as mutls
import numpy as np
import matplotlib.pyplot as plt

PI = np.pi

#%% Consigna B

# x1 = sin(2*PI*260*t) + 4*cos(2*pi*440*t)
# f1 = 260     f2 = 440
# T0 = mT1 = nT2 -- m/f1 = n/f2 -- f2/f1 = n/m = 440/260 = 22/13
T0 = 13/260
Fs = 8e3
dt = 1/Fs

t = np.arange(0, 1, dt)
# x1 = np.sin(2*PI*260*t) + 4*np.cos(2*PI*440*t)
# x1 = np.sin(2*PI*260*t)
# x1 = 4*np.cos(2*PI*440*t)
x1 = 0.5*np.sin(2*PI*260*t) + 0.5*np.cos(2*PI*440*t)

plt.plot(t, x1); plt.grid()

import sounddevice as sd
sd.play(x1,Fs)
