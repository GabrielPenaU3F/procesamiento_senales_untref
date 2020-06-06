import numpy as np
from matplotlib import pyplot as plt

from ejemplos.practica_4.funciones import generar_senal_cuadrada
from ejemplos.practica_5.ejercicio_1 import calcular_transformada

fs = 500
lim_izq = -10
lim_der = 10
duracion = lim_der - lim_izq
T = 1

t, x = generar_senal_cuadrada(T, lim_izq, lim_der, fs)

X_w = calcular_transformada(x)
mod_X = np.abs(X_w)[0:int(len(X_w)/2)]/(len(X_w)/2)

f = np.linspace(0, fs, duracion*fs, endpoint=None)[0:int(len(X_w)/2)]

fig, axes = plt.subplots(1, 2)

axes[0].plot(t, x)
axes[1].set_xlabel("t (seg)")

axes[1].plot(f, mod_X)
axes[1].set_xlabel("f (Hz)")

plt.show()
