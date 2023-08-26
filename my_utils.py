#my_utils.py
from IPython import get_ipython
import numpy as np

def clc():
    print("\014")
    
def clearAll():
    get_ipython().magic('reset -sf')

def ENERGIA(x, dt=1):
    '''
    x: signal
    dt: time-step used to define the signal x. 
        Default value: dt = 1
    '''
    return np.sum(np.abs(x)**2)*dt

def POTENCIA(x, T0, dt=1):
    '''
    x: a period (ONLY ONE) of the signal
    T0: signal period
    dt: time-step used to define the signal x.
        Default value: dt = 1
    '''
    return 1/T0 * np.sum(np.abs(x)**2)*dt

#Definición de la función IMPULSO UNITARIO APROXIMADO delta(t)
delta = lambda t,Ts: np.piecewise(t, t==0, [1/Ts,0])

#Definición de la función ESCALÓN UNITARIO u(t)
u = lambda t: np.piecewise(t, t>=0, [1,0])

#Definición de la función RAMPA UNITARIA rho(t)
rho = lambda t: t*u(t)