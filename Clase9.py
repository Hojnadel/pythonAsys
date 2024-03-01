#%%
import sys
sys.path.append("../toolbox_python")
from AsysToolbox import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint as ode

n = np.arange(-2, 10)
h = (1/2)**n*u(n)
x = u(n)
y = np.convolve(x,h)
n2 = np.arange(-4, 19)
plt.stem(n,x), plt.show()
plt.stem(n,h), plt.show()
plt.stem(n2, y), plt.show()