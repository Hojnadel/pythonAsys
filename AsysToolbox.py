#my_utils.py
import numpy as np

def ENERGIA(x, dt=1):
    '''
    x: signal
    dt: time-step used to define the signal x. 
        Default value: dt = 1
    '''
    return np.sum(np.abs(x)**2)*dt

def POTENCIA(x, T0, dt=1):
    '''
    x: signal
    T0: signal period; N0 in case of discrete signal
    dt: time-step used to define the signal x.
        For discrete time signals, this must be 1 or can be ommited.
        Default value: dt = 1
    '''
    i_T0 = int(round(T0/dt))        # index where is 1 period
    x_T0 = x[0:i_T0]                # one period of the signal
    if (i_T0 > len(x)):
        print("ERROR: signal length is less than 1 period")
        return None
    else:
        return 1/T0 * np.sum(np.abs(x_T0)**2)*dt

#Definición de la función IMPULSO UNITARIO APROXIMADO delta(t)
delta = lambda t,Ts: np.piecewise(t, t==0, [1/Ts,0])

#Definición de la función ESCALÓN UNITARIO u(t)
u = lambda t: np.piecewise(t, t>=0, [1,0])

#Definición de la función RAMPA UNITARIA rho(t)
rho = lambda t: t*u(t)