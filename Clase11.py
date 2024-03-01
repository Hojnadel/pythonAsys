#%%

# Para Colab
# from google.colab import files
# files.upload()
# files.upload()

# Para PC
import sys
sys.path.append("../toolbox_python")

from AsysToolbox import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint as ode


dt = 0.001
t = np.arange(-5, 3, dt)
T0 = 3;
w0 = 2*PI/T0

x = abs(5*np.cos(w0*t)) + 5*np.cos(w0*t)
plt.plot(t,x), plt.grid()

t1p = np.arange(-T0/2, T0/2, dt)
x1p = 10*np.cos(w0*t1p) * (u(t1p+T0/4) - u(t1p-T0/4))
plt.plot(t1p, x1p)

N = 5
[an, bn] = STF(t, x, N, T0)


#%% Reconstruccion

tr = np.arange(-6, 6, dt)
xr = ISTF(tr, an, bn, T0)

x_an = 10/PI \
        + 5 * np.cos(2*PI/3*t) \
        + 20/3/PI * np.cos(4*PI/3*t) \
        - 4/3/PI * np.cos(8*PI/3*t)
        

plt.plot(t, x, ".-", tr, xr, "--y", t, x_an, "--r", linewidth=3)
plt.grid()
plt.legend(["x", "xr", "x_an"], loc="upper right")
plt.show()

#%% Expectro

# an[0] = a0

plt.subplot(211)
plt.stem(np.arange(0, N+1) * 1/T0, an)
plt.grid()
plt.subplot(212)
plt.stem(np.arange(0, N+1) * 1/T0, bn)
plt.grid()


#%%

dt = 0.001
t = np.arange(-2, 2, dt)
x = abs(t)
T0 = 4
[an, bn] = STF(t, x, 10, T0)

tr = np.arange(-6, 6, dt)
xsyn = ISTF(tr, an, bn, T0)
plt.plot(t,x, tr, xsyn), plt.grid()
