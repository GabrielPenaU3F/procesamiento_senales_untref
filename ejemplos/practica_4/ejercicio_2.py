import numpy as np
from matplotlib import pyplot as plt

from ejemplos.practica_2.funciones import generar_senoide
from ejemplos.practica_4.funciones import generar_senal_cuadrada

lim_izq = -10
lim_der = 10
duracion_senal = lim_der - lim_izq
T = 1


fs = 2000
eje_t_1, senal = generar_senal_cuadrada(T, lim_izq, lim_der, fs)
eje_t_2, seno = generar_senoide(lim_izq, lim_der, 1, 1, 0, fs)

N = 48
n_muestras = duracion_senal * fs + 1
suma_parcial_fourier = [0 for x in range(n_muestras)]

for n in range(1, N + 1):
    seno = generar_senoide(lim_izq, lim_der, 1, (2*n - 1) * 2 * np.pi / T, 0, fs)
    coef = 1 / (2*n - 1)
    suma_parcial_fourier += coef * seno[1]
suma_parcial_fourier *= (4/np.pi)

plt.plot(eje_t_1, suma_parcial_fourier)
plt.show()

