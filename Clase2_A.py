import my_utils as mutls
mutls.clc()
mutls.clearAll()

import my_utils as mutls
import numpy as np
import matplotlib.pyplot as plt

PI = np.pi

#%% Consigna A
# T0 = 1ms; f0 = 1kHz; w0 = 2000pi
t1 = np.arange(0, 2e-3, 1e-6)
x1 = np.sin(2*PI*1000*t1+ PI/4)
plt.plot(t1,x1); plt.show()

# w0 = 2/3; T0 = 3pi; fo = 1/(3pi)
# t2 = np.arange(0, 3*PI, 1e-3)
# x2 = np.sin(2/3*t2 + PI/4)
# plt.plot(t2, x2); plt.show()

# W0 = 5pi/4; N0 = 8; k=5; F0 = 5/8
n3 = np.arange(0, 20)
x3 = np.cos(5*PI/4*n3 + PI/2)
stm = plt.stem(n3, x3); 
stm[1].set_linewidth(3)

t3 = np.arange(0, 20, 1e-3)
x3 = np.cos(5*PI/4*t3 + PI/2)
plt.plot(t3, x3, '--r')
plt.show()


# W0 = 3*pi/4; N0 = 8; k=3; F0 = 3/8
# x5 = np.cos(3*PI/4*n3 + PI/2)
# plt.stem(n3, x5, '--r'); plt.show()

# W0 = 4pi; N0 = 1
# n4 = np.arange(0, 12)
# x4 = np.sin(4*PI*n4)
# plt.stem(n4, x4); plt.grid()
# plt.ylim([-1, 1])
# plt.show()

#%% Complemento de la A

fig, (ax1, ax2) = plt.subplots(2, 1)

# W0 = 5pi/4; N0 = 8; k=5; F0 = 5/8
# t3 = np.arange(0, 20, 1e-3)
# x3 = np.cos(5*PI/4*t3 + PI/2)
# ax1.plot(t3, x3, '--m')
n3 = np.arange(0, 20)
x3 = np.cos(5*PI/4*n3 + PI/2)
ax1.stem(n3, x3); ax1.grid()

# W0 = pi/4; N0 = 8; k=3; F0 = 1/8
# x5 = np.cos(3*PI/4*t3 + PI/2)
# ax2.plot(t3, x5, '--m')
x5 = np.cos(PI/4*n3 + PI/2)
ax2.stem(n3, x5, '--r'); ax2.grid()


#%%

Fs = 8e3
dt = 1/Fs
f0 = 1e3
t = np.arange(0, 1, dt)
x = np.sin(2*PI*f0*t)

import sounddevice as sd
sd.play(x,Fs)

# from IPython.display import Audio
# Audio(x, rate=Fs)





























