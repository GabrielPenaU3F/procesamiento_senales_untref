import numpy as np

# s(t)= A * cos(2 pi t)
def generar_senoide(t_inicial, t_final, A, f, phi_0, fs):
    cantidad_muestras = int((t_final - t_inicial) * fs)
    eje_t = np.linspace(t_inicial, t_final, cantidad_muestras, endpoint=False)
    senoide = []
    for k in range(len(eje_t)):
        senoide.append(A * np.cos(2 * np.pi * f * eje_t[k] + phi_0))
    return eje_t, np.array(senoide)

def calcular_energia(senal, fs):
    energia = 0
    for k in range(len(senal)):
        energia += (np.abs(senal[k])**2)
    return energia / fs

def calcular_potencia(senal, fs):
    energia = calcular_energia(senal, fs)
    duracion = len(senal) / fs
    potencia = energia / duracion
    return potencia
