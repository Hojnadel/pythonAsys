#%%
import sys
sys.path.append("../toolbox_python")
from AsysToolbox import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint as ode

def mi_sistema_termico(y, t):
    Cth = 4
    Rth = 0.25
    Pin = 2*(rho(t) - rho(t-20))
    Tamb = 20

    dy = -1/(Cth*Rth) * y + Tamb/(Rth*Cth) + Pin/Cth
    return dy

dt = 0.01
t = np.arange(0, 40, dt)

CI = 20
y_ode = ode(mi_sistema_termico, CI, t)
y_an = (0.5*np.exp(-t) + t/2 + 19.5) * (u(t) - u(t-20)) \
        + (-0.5*np.exp(-(t-20)) + 30) * u(t-20)
y_lin = (0.5*np.exp(-t) + t/2 -0.5) * u(t) \
        - (0.5*np.exp(-(t-20)) + (t-20)/2 -0.5) * u(t-20) \
        + 20

plt.plot(t, y_an, \
        t, y_ode, '-.r', \
        t, y_lin, '--y', \
        linewidth=5)
plt.grid()
plt.legend(["$\\theta_{an}(t)$", \
            "$\\theta_{ode}(t)$", \
            "$\\theta_{lin}(t)$"])
plt.xlabel("Tiempo [s]"), plt.ylabel("Temperatura [°C]")

