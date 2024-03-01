#%%

ENVIRONMENT = "PC"

if (ENVIRONMENT == "COLAB"):
    # For Colab
    from google.colab import files
    files.upload()      # Upload AsysToobox.py
else:
    # For PC
    import sys
    sys.path.append("../toolbox_python")        # Tooblox path

from AsysToolbox import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint as ode

#%% A)

# Primer intento: uy/ux != 0,5

dt = 1e-3
TF = 5
t = np.arange(0, TF, dt)

x = np.random.normal(0, 1, len(t))
h = np.exp(-2*t) * u(t)
y = np.convolve(x, h) *dt

t2 = np.arange(0, 2*TF-dt, dt)

plt.subplot(311)
plt.plot(t, x), plt.grid()
plt.subplot(312)
plt.plot(t, h), plt.grid()
plt.subplot(313)
plt.plot(t2, y), plt.grid()

print(f"uy/ux: {np.mean(y)/np.mean(x)}")

#%% Segundo intento
dt = 1e-3
TF = 50
t = np.arange(0, TF, dt)

x = np.random.normal(0, 1, len(t))
h = np.exp(-2*t) * u(t)
y = np.convolve(x, h) * dt

indexHalf = int( (len(y)+1) / 2)
y = y[:indexHalf]

plt.subplot(311)
plt.plot(t, x), plt.grid()
plt.subplot(312)
plt.plot(t, h), plt.grid()
plt.subplot(313)
plt.plot(t, y), plt.grid()

print(f"uy/ux: {np.mean(y)/np.mean(x)}")



#%% B - FAC Ryy
import scipy.signal as ss

dt = 1e-3
TF = 50
t = np.arange(0, TF, dt)

x = np.random.normal(0, 1, len(t))
h = np.exp(-2*t) * u(t)
y = np.convolve(x, h) *dt

Rxx = ss.correlate(x, x) * dt
tau_x = ss.correlation_lags(len(x), len(x)) * dt
Rhh = ss.correlate(h, h) * dt
tau_h = ss.correlation_lags(len(h), len(h)) * dt
Ryy = ss.correlate(y, y) * dt
tau_y = ss.correlation_lags(len(y), len(y)) * dt

Ryy_2 = np.convolve(Rxx, Rhh) * dt

plt.plot(tau_x, Rxx), plt.grid(),
plt.show()
plt.plot(tau_h, Rhh), plt.grid(),
plt.show()
plt.plot(tau_y, Ryy, linewidth=2), plt.grid(),
plt.plot(tau_y, Ryy_2, "--")
plt.xlim([-TF, TF])
plt.show()

G0 = max(Rxx) * dt
Ryy0_an = G0/4
print(f"ENERGIA Y\n \
      Ryy:      {max(Ryy)}\n \
      ENERGIA:  {ENERGIA(y, dt)}\n \
      VAR:      {np.var(y) * len(y) * dt}\n \
      Ryy0_an:  {Ryy0_an}")

