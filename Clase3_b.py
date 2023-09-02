#%%
import my_utils as utl
utl.clc()
utl.clearAll()

#%% A: x(t) = exp(-abs(t))
import my_utils as utl
import numpy as np
import matplotlib.pyplot as plt
#%%

dt = 0.001
t = np.arange(-20, 20, dt)
x = np.exp(-np.abs(t))

plt.plot(t,x)

E = utl.ENERGIA(x, dt)
print("energia: ", E)


#%% B: x(t) = sin(2*pi*5*t) + cos(2*pi*10*t)
PI = np.pi
dt = 0.001
To = 0.2

t = np.arange(0, 5*To, dt)
x = np.sin(2*PI*5*t) + np.cos(2*PI*10*t)

plt.plot(t, x)

pot = utl.POTENCIA(x, To, dt)
print("Potenica: ", pot)

#%% C: x[n] = 2*(-5/8)^n * u[n]

n = np.arange(0, 15)
x = 2*(-5/8)**n * utl.u(n)

plt.stem(n,x)
energia = utl.ENERGIA(x)
print("Energia: {:.2f}".format(energia))

#%% C*: x[n] = 2*(-5/8)^n * u[n-1]

n = np.arange(0, 15)
x = 2*(-5/8)**n * utl.u(n-1)

plt.stem(n,x)
energia = utl.ENERGIA(x)
print("Energia: ", energia)
# %%
