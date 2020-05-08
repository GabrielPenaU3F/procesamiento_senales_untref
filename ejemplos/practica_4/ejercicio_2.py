import numpy as np
from matplotlib import pyplot as plt

lim_izq = -10
lim_der = 10
duracion_senal = lim_der - lim_izq
T = 1

def generar_senal_cuadrada(fs):
    n_muestras = duracion_senal * fs + 1
    eje_t = np.linspace(lim_izq, lim_der, n_muestras)
    senal = [0 for x in range(n_muestras)]
    for indice, t in enumerate(eje_t):
        # 0 < t < T/2 -> tiene que valer 1
        # T/2 < t < T -> tiene que valer -1
        for k in range(lim_izq, lim_der):
            if k <= t <= k + T/2:
                senal[indice] = 1
            elif k + T/2 < t <= k + T:
                senal[indice] = -1

    return eje_t, senal

def generar_seno(frecuencia, fase_inicial, fs):
    n_muestras = duracion_senal * fs + 1
    eje_t = np.linspace(lim_izq, lim_der, n_muestras)
    seno = [np.sin(frecuencia * t + fase_inicial) for t in eje_t]
    return eje_t, np.array(seno)

fs = 2000
eje_t_1, senal = generar_senal_cuadrada(fs)
eje_t_2, seno = generar_seno(1, 0, fs)

N = 48
n_muestras = duracion_senal * fs + 1
suma_parcial_fourier = [0 for x in range(n_muestras)]

for n in range(1, N + 1):
    seno = generar_seno((2*n - 1) * 2 * np.pi / T, 0, fs)
    coef = 1 / (2*n - 1)
    suma_parcial_fourier += coef * seno[1]
suma_parcial_fourier *= (4/np.pi)

plt.plot(eje_t_1, suma_parcial_fourier)
plt.show()
