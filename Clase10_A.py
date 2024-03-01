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
from scipy.integrate import odeint as ode

#%%
file = np.genfromtxt("./files/MedTemp.txt")

print(file)

#%% Ensamble

d1 = file[1]
d2 = file[2]
d3 = file[3]
d4 = file[4]
d5 = file[5]


# Grafico del ensamble
dias = ["lun", "mar", "mie", "jue", "vie"]
horas = np.arange(8, 22+2, 2)

plt.subplot(5,1,1)
plt.title("Ensamble")
plt.stem(horas, d1), plt.grid(animated=True)
plt.subplot(5,1,2)
plt.stem(horas, d2), plt.grid()
plt.subplot(5,1,3)
plt.stem(horas, d3), plt.grid()
plt.subplot(5,1,4)
plt.stem(horas, d4), plt.grid()
plt.subplot(5,1,5)
plt.stem(horas, d5), plt.grid()
plt.xlabel("Horas")
plt.show()

#%% Estadísticos

# Media del ensamble
mediaEnsamble = np.mean(file[1:], 0)
print(f"Media del ensamble: {mediaEnsamble}")
plt.stem(horas, mediaEnsamble), plt.grid()
plt.title("Media del ensamble"),
plt.show()

# Media cuadrática
mediaCuadratica = np.mean((file[1:][:])**2, 0)
print(f"Media cuadrática: {mediaCuadratica}")
plt.stem(horas, mediaCuadratica), plt.grid()
plt.title("Media cuadratica"),
plt.show()

# Varianza
plt.title("Varianza del ensamble"),
varianza = np.var(file[1:], 0);
print(f"Varianza: {varianza}")
plt.stem(horas, varianza), plt.grid()
plt.show()

media_por_dia = np.mean(file[1:], 1)
print(f"Media de cada día: {media_por_dia}")
plt.stem(dias, media_por_dia), plt.grid()
plt.title("Media de cada día")
