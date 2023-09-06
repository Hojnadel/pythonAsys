#%%
import sys
sys.path.append("../toolbox_python")
import numpy as np
import matplotlib.pyplot as plt
from AsysToolbox import *

import numpy as np
import matplotlib.pyplot as plt
from AsysToolbox import *

## Sistema B - Aditividad

def sistema_b (x, t):
  return 2*np.exp(-4*x(t+1))

t = np.arange(-5, 15, 0.01)
x1 = lambda t: np.sin(t)*u(t)             # Entrada 1
x2 = lambda t: -0.5*u(t)                  # Entrada 2

plt.subplot(311)
plt.plot(t, x1(t), t, x2(t)),
plt.grid(), plt.title("Entradas")
plt.legend(["x1", "x2"])
plt.show(), 

## Calculo las salidas
y1 = sistema_b(x1, t)
y2 = sistema_b(x2, t)

plt.subplot(312)
plt.plot(t, y1, t, y2),
plt.grid(), plt.title("Salidas")
plt.legend(["y1", "y2"])
plt.show(), 

x3 = lambda t: x1(t) + x2(t)              # Defino la suma de entradas como lambda
y3 = sistema_b(x3, t)
plt.subplot(313)
plt.plot(t, y1+y2, "r", t, y3, "g"),
plt.grid(), plt.title("Aditividad")
plt.legend(["y1+y2", "y(x1+x2)"])
plt.show(), 

#%% Homogeneidad

def sistema_b (x, t):
  return 2*np.exp(-4*x(t+1))

x = lambda t: u(t)
A = 2
x1 = lambda t: A*x(t)                 # Escalo la entrada
plt.subplot(211)
plt.plot(t, x(t), t, x1(t))
plt.grid(), plt.title("Entradas")
plt.legend(["y1", "y2"], loc="upper right")
plt.show(), 

y1 = sistema_b(x1, t)                 # Salida con la entrada escalada
y2 = A*sistema_b(x, t)                # Escalo la salida

plt.subplot(212)
plt.plot(t, y1, t, y2)
plt.grid(), plt.title("Salidas")
plt.legend(["y1", "y2"], loc="upper right")
plt.show(), 


#%% Invarianza temporal - B

def sistema_b (x, t):
  return 2*np.exp(-4*x(t+1))

x = lambda t: u(t)
to = 3

x1 = lambda t: x(t-to)      # Entrada desplazada
y1 = sistema_b(x1, t)       # Salida para entrada desplazada

y2 = sistema_b(x, t-to)


plt.subplot(211)
plt.plot(t, x(t), t, x1(t), '--y'), plt.grid(), 
plt.legend(["x(t)", "x(t-to)"])
plt.title("Entradas")
plt.subplot(212)
plt.plot(t, y1, t, y2, '--y'), plt.grid(), 
plt.legend(["y(x(t-to))", "y(t-to)"])
plt.title("Salidas")
plt.show()


#%% Sistema lineal

def sistema_LTI(x, t):
    return 3*x + np.gradient(x)

x1 = rho(t)
x2 = np.sin(t)*u(t)

y1 = sistema_LTI(x1, t)
y2 = sistema_LTI(x2, t)
y3 = sistema_LTI(x1+x2, t)

plt.subplot(211)
plt.plot(t, y1+y2, t, y3, '--y', linewidth=5)
plt.grid(), plt.title("Aditividad")

A = 4
y1 = sistema_LTI(A*x1, t)
y2 = A*sistema_LTI(x1, t)
plt.subplot(212)
plt.plot(t, y1, t, y2, '--y', linewidth=5)
plt.grid(), plt.title("Homogeneidad")


#%% Sistema variante temporal

def sistema_VT(x, t):
   return x(3*t)

t = np.arange(-1, 2, 0.01)

x = lambda t: t + 1
y = sistema_VT(x, t)

plt.subplot(311)
plt.plot(t, x(t), t, y)
plt.grid(), plt.legend(["x(t)", "y(t)"])

# Desplazo la entrada
to = 2
x1 = lambda t: x(t-to)
y1 = sistema_VT(x1, t)

# Desplazo la salida
y2 = sistema_VT(x, t-to)

plt.subplot(312)
plt.plot(t, y1, t, y2)
plt.grid(), plt.legend(["y(x(t-to))", "y(t-to)"])


