import numpy as np

# s(t)= A * cos(2 pi t)
def generar_senoide(t_inicial, t_final, A, f, phi_0, fs):
    cantidad_muestras = (t_final - t_inicial) * fs
    eje_t = np.linspace(t_inicial, t_final, cantidad_muestras, endpoint=False)
    senoide = []
    for k in range(len(eje_t)):
        senoide.append(A * np.cos(2 * np.pi * f * eje_t[k] + phi_0))
    return eje_t, np.array(senoide)

def calcular_energia(senoide, fs):
    energia = 0
    ts = 1/fs
    for k in range(len(senoide)):
        energia += (np.abs(senoide[k])**2)
    return energia * ts