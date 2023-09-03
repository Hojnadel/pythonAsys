#%% Primer orden
# import toolbox_python.AsysToolbox as tbx
import sys
sys.path.append("../toolbox_python")
import AsysToolbox as tbx
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint as ode

# Defino funcion de mi edo: 3y' + 5y = 2t
def fun_orden1(y, t):
    ft = 2/3*t
    dy = -5/3*y + ft
    return dy

dt = 0.001
t = np.arange(0, 2, dt)

CI = 0
y_ode = ode(fun_orden1, CI, t)                  # Numérica
y_an = 6/25*np.exp(-5/3*t) + 2/5*t - 6/25       # Analitica


plt.plot(t, y_ode, t, y_an, 'y--', linewidth=3)
plt.grid(), 
plt.legend(["Ode", "Analítca"], loc="upper left")

#%% Segundo orden

import sys
sys.path.append("../toolbox_python")
import AsysToolbox as tbx
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint as ode

# Defino funcion de mi edo: 5y'' - 3y' + 6y = cos(t)
def fun_orden2(y, t):
    ft = np.cos(t)
    dy = (y[1], 
         3/5*y[1] - 6/5*y[0] + ft/5)
    return dy

dt = 0.001
t = np.arange(0, 10, dt)
CI = [20, 0]
y = ode(fun_orden2, CI, t)
plt.plot(t,y), plt.grid()
plt.legend(["y", "y'"])


