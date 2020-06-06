import numpy as np

def generar_senal_cuadrada(T, lim_izq, lim_der, fs):
    duracion = lim_der - lim_izq
    n_muestras = duracion * fs
    eje_t = np.linspace(lim_izq, lim_der, n_muestras, endpoint=None)
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