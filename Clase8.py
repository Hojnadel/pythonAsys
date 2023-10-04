#%%
import sys
sys.path.append("../toolbox_python")

from AsysToolbox import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint as ode

dt = 0.001
t = np.arange(-1, 5, dt)
x = rho(t) - rho(t-1) - u(t-2)
h = np.exp(-2*t) * u(t)

# By convolution
y = np.convolve(x, h) * dt
t2 = np.arange(-2, 10-dt, dt)

# By definition
y_an = (t/2 - 1/4 + 1/4*np.exp(-2*t)) * (u(t) - u(t-1)) \
        + (1/2 + (1/4 - np.exp(2)/4)*np.exp(-2*t)) * (u(t-1) - u(t-2)) \
        + (1/4 + np.exp(4)/2 - np.exp(2)/4) * np.exp(-2*t) * u(t-2)

y_prop = (t/2 - 1/4 + 1/4*np.exp(-2*t)) * u(t) \
        - ((t-1)/2 - 1/4 + 1/4*np.exp(-2*(t-1))) * u(t-1) \
        - np.gradient(((t-2)/2 - 1/4 + 1/4*np.exp(-2*(t-2))) * u(t-2)) / dt

plt.plot(t2, y,
        t, y_an, '-.r',
        t, y_prop, '--y',
        linewidth=5), 
plt.grid()
plt.legend(["y_convolve", "y_an", "y_prop"])
plt.xlabel("Tiempo [s]"), plt.ylabel("y(t)")



