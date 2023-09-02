import my_utils as mutls
mutls.clc()
mutls.clearAll()

import my_utils as mutls
import numpy as np
import matplotlib.pyplot as plt

#%% Consigna A

msg = "Hello world!"

# Vector aleatorio entre -10 y 10
vA = (np.random.rand(1,100)-0.5)*20;


print("max", np.max(vA),
      "\nmin: ", np.min(vA),
      "\nmevn: ", np.mean(vA),
      "\nsize: ", np.size(vA),
      "\nshape: ", np.shape(vA))

vB = vA[vA > 3]


#%%

def CALC(x1, x2):
    s = x1 + x2
    r = x1 - x2
    return s,r

plt.close('all')
PI = np.pi

t = np.arange(0, 2*PI, 0.01)
Sa = np.sin(2*t)
Sb = np.cos(4*t)

suma, resta = CALC(Sa, Sb)

print("max: ", np.max(Sa), "\nmin: ", np.min(Sa))

plt.plot(t,Sa,'b',t,Sb,'r')
plt.plot(t, suma, 'g.', t, resta, 'm--')
plt.xlabel("Tiempo [s]")
plt.ylabel("Señales")
plt.grid()
plt.legend(["Sa", "Sb", "Suma", "Resta"], loc="lower left")
plt.title("Mi gráfico")
plt.axis([0, 2*PI, -3, 3])
# plt.tight_layout()


#%%
# fig, axs = plt.subplots(2,2);
# fig.suptitle("Title")
# axs[0][0].plot(t, Sa)
# axs[0][0].set(xlabel="time", ylabel="ylabel")
# axs[0][1].plot(t, Sb)
# axs[1][0].plot(t, suma)
# axs[1][1].plot(t, resta)
# axs[1][1].set(xlabel="time", ylabel="ylabel")

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2);
fig.suptitle("Title")
ax1.plot(t, Sa)
ax1.set(xlabel="time", ylabel="ylabel")
ax2.plot(t, Sb)
ax3.plot(t, suma)
ax4.plot(t, resta)
ax4.set(xlabel="time", ylabel="ylabel")
