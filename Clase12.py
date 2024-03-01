#%%
ENTORNO = "PC"

if (ENTORNO == "COLAB"):
    # Para Colab
    from google.colab import files
    files.upload()
    files.upload()
else:
    # Para PC
    import sys
    sys.path.append("../toolbox_python")

from AsysToolbox import *
import numpy as np
import matplotlib.pyplot as plt

#%%

dt = 0.001
t = np.arange(-5, 3, dt)
T0 = 3;
w0 = 2*PI/T0

x = abs(5*np.cos(w0*t)) + 5*np.cos(w0*t)
plt.plot(t,x), plt.grid()

t1p = np.arange(-T0/2, T0/2, dt)
x1p = 10*np.cos(w0*t1p) * (u(t1p+T0/4) - u(t1p-T0/4))
plt.plot(t1p, x1p)

N = 10
[an, bn] = STF(t, x, N, T0)

Pot_t = POTENCIA(x, T0, dt)
Pot_f = POTENCIA_STF(an, bn, 2)

print(f'Potencia: {Pot_t}')
print(f'Potencia: {Pot_f}')
print(f'%: {Pot_f/Pot_t}')


#%%

dt = 0.001
t = np.arange(-2, 2, dt)
T0 = 4;
w0 = 2*PI/T0

x = np.exp(t)
plt.plot(t,x), plt.grid()


N = 10
[an, bn] = STF(t, x, N, T0)

Pot_t = POTENCIA(x, T0, dt)
Pot_f = POTENCIA_STF(an, bn, 5)

print(f'Potencia: {Pot_t}')
print(f'Potencia: {Pot_f}')
print(f'%: {Pot_f/Pot_t}')